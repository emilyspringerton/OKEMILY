# OKEMILY — okemily.com landing page

## What this is

Static marketing/credibility landing page for `okemily.com`, EINHORN_INDUSTRIAL's public front
door. Plain HTML/CSS, no build step, no framework — deliberately minimal so it's fast, has near-zero
resource footprint, and is trivially administrable by Claude Code (edit → commit → deploy).

**Not the product funnel.** EDIS (WordPress, Ask Emily chat, signal widgets) is the eventual full
product front-end and is a separate, later effort — see `EDIS/CLAUDE.md`. This repo exists because
the immediate need (credibility for a Google Cloud for Startups application) is much narrower than
that: a real, on-brand page, not a full app.

## Deploy

Serving root is `/var/www/okemily/` (nginx reads it there, not this repo directory directly —
`/home/fatbaby` is `750` and nginx's `www-data` user can't traverse it). **Update, 2026-07-19:**
`/var/www/okemily/` is now `fatbaby:www-data` mode `2775` (group-writable, sgid) — deploying no
longer needs `sudo` at all; the `sudo mkdir`/`sudo chown` steps this doc used to list are stale
and would actually be a regression (chown-ing back to `www-data:www-data` removes the write
access that makes this work). After editing files here, run `~/okemily-deploy.sh` (no `sudo`) or:

```bash
mkdir -p /var/www/okemily
rsync -a --delete /home/fatbaby/OKEMILY/ /var/www/okemily/ --exclude='.git' --exclude='blog'
```

**`--exclude='blog'` is not optional.** `blog/` is rendered live by IDUNA's blog handler
(`IDUNA/internal/blog/render.go`) straight into `/var/www/okemily/blog` and is not part of this
git repo at all. A bare `--delete` sync without this exclusion wipes every published post —
happened for real 2026-07-19, recovered only because the SQLite source of truth
(`IDUNA/var/blog.db`) was untouched and could be re-rendered (`IDUNA/cmd/blog-rerender`).

nginx server block: `ops/nginx-okemily.conf` in this repo — copy to
`/etc/nginx/sites-available/okemily`, symlink into `sites-enabled/`, `sudo nginx -t && sudo
systemctl reload nginx`. Both the copy-into-`sites-available` step and the reload need `sudo`
(interactive password) — not something Claude Code can complete unattended in this environment.

**CRITICAL, learned the hard way (2026-07-18 outage):** certbot's `--nginx` plugin rewrites the
live file in place to add the SSL/443 server block, the HTTP→HTTPS redirect, and the HSTS header —
none of which exist in a plain edit of this repo's copy. Blindly `sudo cp`-ing this repo's file
over the live one (e.g. to add a new `location` block) **deletes all of that and takes HTTPS down
entirely** — this happened for real, causing a full outage, when a `/news/` proxy addition was
deployed this way without first re-syncing from live. **Before editing this file for a live
deploy: always `cat /etc/nginx/sites-available/okemily` first and diff against this repo's copy —
if they've diverged (they will, after any certbot run), copy the live file into the repo first,
then make your edit on top of that, never the other way around.**

## Blog posts (2026-07-28)

Blog content is **not in this git repo at all** — it lives in `IDUNA/var/blog.db` (SQLite) and
gets rendered live, on every publish, straight into `/var/www/okemily/blog/<slug>/` by IDUNA's
own blog handler (`IDUNA/internal/http/handlers/blog.go` + `internal/blog`). That's why
`~/okemily-deploy.sh`'s rsync excludes `blog/` (see Deploy section above) — this repo has nothing
to do with blog content, only the surrounding static page.

**Two ways to get a post live, pick based on the ask:**

1. **Draft-then-Fable-publishes** (the default for anything that should get a real editorial
   pass first — essays, anything long-form/literary). Write the full post as a pre-pass draft in
   `EMILY/docs/fable-prompts/okemily-blog-<slug>-DRAFT.md`, following the exact template the
   existing drafts in that directory use (status line, voice/format reference, publish path,
   numbered "facts to verify," then the full post body under its own heading — see
   `okemily-blog-clean-builds-first-DRAFT.md` for the canonical shape). Commit and push to
   `EMILY`. Fable's own pass does the line-edit and the actual publish (step 2 below).

2. **Publish it yourself, right now** (when the ask is "just get it live" — verified working
   2026-07-28, publishing "Mid-Piano Presents: The Squad"):
   ```bash
   # 1. Mint a short-lived (1h) bearer token for an agent with blog.write.
   #    Which agents have it: python3 -c "import json; d=json.load(open('/home/fatbaby/IDUNA/config/agents.json')); [print(a['name']) for a in d['agents'] if 'blog.write' in a.get('permissions', [])]"
   #    As of this writing, only EMILY-PRIME does.
   #    GOTCHA: the registered agent_name is HYPHENATED ("EMILY-PRIME"), not the underscored
   #    form CLAUDE.md's own env-var table uses elsewhere ("EMILY_PRIME") -- that mismatch is a
   #    real 401 the first time, not a typo to fix blindly. Confirm the exact string against
   #    IDUNA/config/agents.json, don't assume.
   source /home/fatbaby/IDUNA/var/agent-secrets.env   # provides IDUNA_SECRET_EMILY_PRIME
   TOKEN=$(curl -s -X POST http://localhost:8080/api/v1/auth/agent \
     -H "Content-Type: application/json" \
     -d "{\"agent_name\": \"EMILY-PRIME\", \"agent_secret\": \"$IDUNA_SECRET_EMILY_PRIME\"}" \
     | python3 -c "import json,sys; print(json.load(sys.stdin)['access_token'])")

   # 2. POST the post itself. slug must be lowercase-hyphenated; author defaults to
   #    EINHORN_INDUSTRIAL if omitted. Publishing is instant -- no build step, no deploy script,
   #    live the moment this returns 200.
   curl -s -X POST http://localhost:8080/api/v1/blog/posts \
     -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" \
     -d '{"slug": "my-post-slug", "title": "My Post", "author": "EINHORN_INDUSTRIAL", "body": "..."}'
   # -> {"status":"published","slug":"my-post-slug","url":"https://okemily.com/blog/my-post-slug/"}
   ```
   Verify with `curl -s http://localhost:8080/api/v1/blog/posts/<slug>` (public, no auth) or
   check `/var/www/okemily/blog/<slug>/index.html` exists directly.

**Voice/format reference for anything narrative** ("Mid-Piano Presents" episodes, hero-voiced
posts): the existing posts at `GET /api/v1/blog/posts` (public, lists every slug/title/author) are
the real corpus — read a couple of the closest-matching ones before writing, don't invent a new
voice from scratch. `TYLER/just_a_duck.md` is the original source material (the real "Jack's
Factory" short transcript) the entire hero roster, and the "Mid-Piano" show name itself (The
Ghost was mid-piano in the source clip), are grounded in.

## TYLER reading room (2026-08-06)

A dedicated reading experience for TYLER episode scripts, separate from the generic blog. Same
"not in this git repo, own SQLite, rendered live" shape as blog posts above, but a different
store/handler/template: `IDUNA/var/tyler.db` + `IDUNA/internal/tyler` + `IDUNA/internal/http/
handlers/tyler.go`, rendered straight into `/var/www/okemily/tyler/<slug>/`. `~/okemily-deploy.sh`
excludes `tyler/` for the exact same reason it excludes `blog/` — **do not remove that exclusion.**

Why a separate system instead of just using the blog: the blog's renderer only does "poor man's
markdown" (blank-line paragraph splitting, no real headers/bold/tables) — fine for prose posts,
but TYLER scripts have real headers, `**bold**` character tags, `- [x]` consistency checklists,
and pipe tables (e.g. hero ability comparisons) that would render as garbled literal text through
the blog's paragraph-only renderer. `internal/tyler`'s renderer is a real (if scoped)
markdown-to-HTML converter, styled on the IDUNA style guide (`IDUNA/styles.css`: cream/gold/serif,
not the blog's dark developer-blog theme) for an actual book-reading feel, plus the same
`speechSynthesis`-based "Listen" audio button the blog already has, restyled to match.

**Publishing** (requires `tyler.write` — as of this writing only EMILY-PRIME has it):
```bash
source /home/fatbaby/IDUNA/var/agent-secrets.env   # provides IDUNA_SECRET_EMILY_PRIME
TOKEN=$(curl -s -X POST http://localhost:8080/api/v1/auth/agent \
  -H "Content-Type: application/json" \
  -d "{\"agent_name\": \"EMILY-PRIME\", \"agent_secret\": \"$IDUNA_SECRET_EMILY_PRIME\"}" \
  | python3 -c "import json,sys; print(json.load(sys.stdin)['access_token'])")

curl -s -X POST http://localhost:8080/api/v1/tyler/episodes \
  -H "Content-Type: application/json" -H "Authorization: Bearer $TOKEN" \
  -d '{"slug": "my-episode", "title": "My Episode", "series": "SERIES X", "episode_tag": "INTERLUDE, UNNUMBERED", "build": "0134", "body": "..."}'
# -> {"status":"published","slug":"my-episode","url":"https://okemily.com/tyler/my-episode/"}
```
Strip the episode file's own leading `# .../## "Title"/### Build .../---` header block from
`body` before publishing — the reader page template already renders series/title/build in its own
styled header, so leaving that block in the body duplicates it. Everything after that leading
block (starting at `**SERIES:**...`) is the real body.

All 5 existing Series X interludes (`x00`–`x04`) are published as of 2026-08-06:
`okemily.com/tyler/the-custody-of-a-duck/`, `/the-long-quiet/`, `/recruitment-drive/`,
`/the-band-name/`, `/ask-the-frog-not-the-tree/`. The numbered season episodes
(`TYLER/episodes/s01e01_*.md` onward, ~80 files) are **not** backfilled — that's a real, separate
scope decision (bulk-publish everything vs. curate), not done here, flag it rather than assuming
either way if asked to expand this.

## Mailing-list signup (2026-07-18)

The signup form posts via JS `fetch()` to IDUNA's `/api/v1/mailing-list/subscribe`
(`https://iduna.farthq.com/api/v1/mailing-list/subscribe`), **not** a Mailchimp embedded form
directly. IDUNA is the system of record — it encrypts and stores the email itself (never at rest
unencrypted; see `IDUNA/internal/mailinglist` package doc for the full threat model), then
best-effort forwards to Mailchimp for actually sending email. Mailchimp is a downstream sync
target, not the source of truth.

Requires:
1. IDUNA env vars set: `MAILCHIMP_API_KEY`, `MAILCHIMP_LIST_ID` (from a real Mailchimp account —
   founder action, not something Claude Code can create).
2. **Double opt-in enabled on the Mailchimp audience** (account setting) — the code assumes this
   (`status_if_new: "pending"` in `IDUNA/internal/mailinglist/mailchimp.go`).
3. An nginx `/api/` proxy on `iduna.farthq.com` → `127.0.0.1:8080` — did not exist as of
   2026-07-18, tracked as a same-day follow-up in IDUNA's CHANGELOG.
4. The mailing-list vault must be unlocked after every IDUNA restart —
   `mailing-list-unlock` (interactive passphrase prompt, never a CLI arg). Until unlocked, the
   signup form fails closed with a friendly "try again shortly" message; nothing else in IDUNA is
   affected.

## Identity / content decisions

- **Update 2026-07-19: no longer anonymous.** Founder instruction: "time to come out of hiding" —
  the footer now names **Brian Danowski** ("Built by Brian Danowski and Emily"). This supersedes
  the earlier 2026-07-17 policy below; keeping the old note for context, not as current guidance.
- ~~Founders are deliberately not named on this page — kept vague ("the founders and Emily") per
  explicit founder direction. Do not add a named bio without being told to.~~ (2026-07-17, now
  reversed — see above.)
- Copy emphasizes: three product pillars (capital markets intelligence / game worlds / recursive
  self-improvement), building in the open (GitHub, public domain release), operational
  seriousness as a value (ties to `EMILY/docs/THE_EMILY_WAY.md` Principle 15).

## CHANGELOG protocol

Append a dated bullet to `CHANGELOG.md` for any meaningful content or infra change, same as every
other repo in this monorepo.

## Commit Protocol (standing instruction)

Always commit and push completed work immediately — don't wait to be asked. This is the default for every repo in this monorepo.
