# OKEMILY Changelog

## 2026-07-17
- feat: initial landing page (`index.html`) — static HTML/CSS, no build step. Mission/pillars/values
  copy (capital markets intelligence, game worlds, recursive self-improvement), founders
  deliberately unnamed per explicit direction, Mailchimp signup form scaffolded with placeholder
  IDs (not yet wired to a real audience). nginx server block at `ops/nginx-okemily.conf`, not yet
  deployed — `okemily.com` currently falls through to the `edis` vhost's catch-all and serves the
  wrong (IDUNA-branded) page; deploying this fixes that. Deploy needs sudo (root-owned
  `/etc/nginx/sites-available` and `/var/www`), see `CLAUDE.md`.
