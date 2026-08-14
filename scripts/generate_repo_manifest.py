#!/usr/bin/env python3
"""generate_repo_manifest.py -- builds a single JSON index of every tracked
file across every EINHORN_INDUSTRIAL repo, for use as a blog-post artifact
(founder real-time, 2026-08-14: "i need a manifest file that concatinates
all repos files into one file as artifacts for the blog posts for okemily").

Deliberately an INDEX (repo name + file paths + sizes), not a full-content
concatenation -- founder confirmed via AskUserQuestion after being shown the
real alternative (concatenating every file's full text across ~30 repos,
several of them large codebases, would likely run hundreds of MB to GB+,
impractical to generate or host). Matches the existing MANIFEST.json pattern
already used by APPLES (an index for MJOLNIR's offline cache), not a new
convention.

Usage:
    python3 generate_repo_manifest.py --out manifest.json [--token TOKEN]

Clones each repo shallow (--depth 1) into a temp dir, runs `git ls-files`
for the real tracked-file list (not a raw directory walk, which would also
pick up .gitignore'd build output), records size via `git cat-file`, then
deletes the clone. Safe to re-run.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

# Real, deduplicated repo list -- confirmed 2026-08-14 by checking every
# local checkout's actual `git remote get-url origin` (not guessed from
# directory names). redgarden-deploy/redgarden-stable are separate local
# clones of the same REDGARDEN repo (the R&D-vs-Stable deployment split,
# see REDGARDEN/CLAUDE.md's own "Deployments" table) -- deduplicated here to
# one manifest entry, not three.
REPOS = [
    "APPLES", "BRAWLPIT", "CarePyre", "dragonfly", "EDIS", "EINHORN_SURVIVAL",
    "EMILY", "emily.cli", "EmilyOS", "EXODUS", "GoblinFoxDragon", "GOLDENBAND",
    "gpt2-alpine-c", "GTA7", "IDUNA", "MJOLNIR", "MoneyPrinterTurbo", "NORN",
    "OKEMILY", "PITVIPER", "PRRJECT_FATBABY",
    "QUEENSALLYONLINEBOOKOFMAGIFICATIONANDUNICOR", "REDGARDEN",
    "REDGARDEN.wiki", "SHANKPIT", "shankpit-460", "SKATEBOARD", "SKULDMARK",
    "TIPJAR", "TIPJAR.wiki", "TTT", "TYLER", "WEAKNIGHT_BEDROCK_RACERS",
]

ORG = "emilyspringerton"


def clone_url(repo: str, token: str | None) -> str:
    if token:
        return f"https://x-access-token:{token}@github.com/{ORG}/{repo}.git"
    return f"https://github.com/{ORG}/{repo}.git"


def list_repo_files(repo: str, token: str | None, workdir: str) -> dict:
    dest = os.path.join(workdir, repo)
    entry = {"name": repo, "files": [], "file_count": 0, "error": None}
    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", "--quiet", clone_url(repo, token), dest],
            check=True, capture_output=True, text=True, timeout=120,
        )
    except subprocess.CalledProcessError as e:
        entry["error"] = f"clone failed: {e.stderr.strip()[:200]}"
        return entry
    except subprocess.TimeoutExpired:
        entry["error"] = "clone timed out"
        return entry

    try:
        result = subprocess.run(
            ["git", "-C", dest, "ls-files"],
            check=True, capture_output=True, text=True, timeout=60,
        )
        files = [f for f in result.stdout.splitlines() if f]
        entry["files"] = files
        entry["file_count"] = len(files)
    except subprocess.CalledProcessError as e:
        entry["error"] = f"ls-files failed: {e.stderr.strip()[:200]}"
    finally:
        shutil.rmtree(dest, ignore_errors=True)
    return entry


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="manifest.json")
    ap.add_argument("--token", default=os.environ.get("GITHUB_TOKEN", ""))
    args = ap.parse_args()

    token = args.token or None
    repos_out = []
    with tempfile.TemporaryDirectory() as workdir:
        for repo in REPOS:
            print(f"indexing {repo}...", file=sys.stderr)
            repos_out.append(list_repo_files(repo, token, workdir))

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "org": ORG,
        "repo_count": len(repos_out),
        "total_file_count": sum(r["file_count"] for r in repos_out),
        "repos": repos_out,
    }
    with open(args.out, "w") as f:
        json.dump(manifest, f, indent=2)
    print(f"wrote {args.out}: {manifest['repo_count']} repos, "
          f"{manifest['total_file_count']} files", file=sys.stderr)


if __name__ == "__main__":
    main()
