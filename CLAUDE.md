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

## Mailchimp signup form (currently a placeholder)

`index.html`'s signup form has `YOUR_DC`/`YOUR_U`/`YOUR_ID`/`YOUR_HONEYPOT_NAME` placeholders. To
wire up a real audience:

1. Create a free Mailchimp account, create one Audience (e.g. "okemily waitlist").
2. Audience → Signup forms → Embedded form → copy the generated `<form>` action URL and the
   hidden honeypot input's `name` attribute.
3. Replace the four placeholders in `index.html` with the real values.
4. Redeploy (see above).

## Identity / content decisions (as of 2026-07-17)

- Founders are deliberately **not named** on this page — kept vague ("the founders and Emily") per
  explicit founder direction. Do not add a named bio without being told to.
- Copy emphasizes: three product pillars (capital markets intelligence / game worlds / recursive
  self-improvement), building in the open (GitHub, public domain release), operational
  seriousness as a value (ties to `EMILY/docs/THE_EMILY_WAY.md` Principle 15).

## CHANGELOG protocol

Append a dated bullet to `CHANGELOG.md` for any meaningful content or infra change, same as every
other repo in this monorepo.
