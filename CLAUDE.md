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

Serving root is `/var/www/okemily/` (nginx, `www-data`), not this repo directory directly — `/home/
fatbaby` is `750` and nginx's `www-data` user can't traverse it. After editing `index.html` here:

```bash
sudo mkdir -p /var/www/okemily
sudo rsync -a --delete /home/fatbaby/OKEMILY/ /var/www/okemily/ --exclude='.git'
sudo chown -R www-data:www-data /var/www/okemily
```

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
