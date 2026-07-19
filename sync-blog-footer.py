#!/usr/bin/env python3
"""Regenerates the footer-blog-links block in index.html from IDUNA's live
blog post list (GET /api/v1/blog/posts), so the footer never drifts out of
sync with what's actually published again. Run after every new post.
"""
import json
import re
import urllib.request

INDEX_HTML = "index.html"
API_URL = "http://127.0.0.1:8080/api/v1/blog/posts"

with urllib.request.urlopen(API_URL, timeout=10) as resp:
    posts = json.load(resp)["posts"]

# API returns newest-first; footer has always listed oldest-first historically,
# so reverse to match.
posts = list(reversed(posts))

links = " &middot;\n".join(
    f'      <a href="/blog/{p["slug"]}/">{p["title"]}</a>' for p in posts
)
block = f'    <div class="footer-blog-links">\n{links}\n    </div>'

with open(INDEX_HTML) as f:
    html = f.read()

new_html, n = re.subn(
    r'    <div class="footer-blog-links">.*?\n    </div>',
    block,
    html,
    flags=re.DOTALL,
)
if n != 1:
    raise SystemExit(f"expected exactly 1 footer-blog-links block, found {n} — not writing")

with open(INDEX_HTML, "w") as f:
    f.write(new_html)

print(f"synced {len(posts)} posts into footer")
