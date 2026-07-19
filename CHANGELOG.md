# OKEMILY Changelog

## 2026-07-18 (3)
- docs: swapped the Fable guest post link in the footer -- founder feedback on the first draft ("The file that was waiting") was that it was too short, too hedged, and drew a conclusion they disagreed with. Rewritten from scratch with much fuller context (the full text of TYLER/THE_FIELD.md, explicit direction to perform the material in-voice rather than narrate about it from a safe distance) as "Activation #114" (/blog/activation-114/, IDUNA). Old post deleted (DB row + rendered static files), not just unlinked.

## 2026-07-18 (2)
- docs: added "The file that was waiting" (Fable guest post, /blog/the-file-that-was-waiting/) to the footer blog-links list.

## 2026-07-18
- feat: hidden TYLER teaser easter egg -- triple-click the copyright year in the footer to toggle a quiet, in-universe one-liner ('television as code...') crediting TIDES OF PARADOX s00e00, linking to the public TYLER repo. No visual hint, no modal -- deliberately minimal. Deployed + live-verified. OKEMILY 937641f.
- feat: add EINHORN Tournaments front door page (tournaments.html) -- honest landing page for IDUNA's declared VS2 social tournaments platform direction, names SHANKPIT-460 esports as the first real product with its NORTHSTAR linked, mailing-list signup CTA reusing existing infra verbatim. Footer link added to okemily.com main page. Deployed + live-verified. OKEMILY b2bc48d.
- feat: real signup flow — form now posts via JS fetch to IDUNA's `/api/v1/mailing-list/subscribe`
  (never-at-rest-unencrypted, vault-gated, see `IDUNA/internal/mailinglist`) instead of a direct
  Mailchimp embed. Added a required, unchecked-by-default consent checkbox (GDPR opt-in, not
  implied consent) and `privacy.html` (real policy text: what's collected, Mailchimp as processor,
  double opt-in, deletion-request contact). Consent version pinned to `okemily-v1-2026-07-17`,
  matching `CurrentConsentVersion` in the IDUNA handler.
- **Blocking follow-up, not yet done**: `iduna.farthq.com` has no nginx `/api/` proxy to IDUNA's
  `:8080` yet — the signup form will fail until that's added (falls through to WordPress's
  `location /` today). See IDUNA CHANGELOG same date.

## 2026-07-17
- feat: initial landing page (`index.html`) — static HTML/CSS, no build step. Mission/pillars/values
  copy (capital markets intelligence, game worlds, recursive self-improvement), founders
  deliberately unnamed per explicit direction, Mailchimp signup form scaffolded with placeholder
  IDs (not yet wired to a real audience). nginx server block at `ops/nginx-okemily.conf`, not yet
  deployed — `okemily.com` currently falls through to the `edis` vhost's catch-all and serves the
  wrong (IDUNA-branded) page; deploying this fixes that. Deploy needs sudo (root-owned
  `/etc/nginx/sites-available` and `/var/www`), see `CLAUDE.md`.

## 2026-07-19
- blog: published "Clean Builds First" (guest post by Claude) via IDUNA blog.write API —
  live at https://okemily.com/blog/clean-builds-first/, auto-listed in /blog/ index.
  Added footer link on index.html (needs deploy — see CLAUDE.md).

## 2026-07-19 (2)
- infra: add /admin/ same-origin nginx proxy to IDUNA (127.0.0.1:8080) in ops/nginx-okemily.conf,
  matching the existing /api/ pattern. Footer now links to /admin/login. Works over okemily.com's
  real HTTPS cert without depending on iduna.farthq.com's (still pending). Needs deploy — see
  sudo-queue/03-okemily-admin-proxy.sh.

## 2026-07-19 (3)
- content: add sub-sub-footer easter egg — "CLEAN BUILDS FIRST", styled with --subfooter, a
  new per-theme CSS variable computed (not eyeballed) to be the lightest grey that still clears
  WCAG AA 4.5:1 against --bg: #7a7a7a on dark (#0b0c10) = 4.554:1, #737373 on light (#fafafa) =
  4.543:1.

## 2026-07-19 (4)
- blog: published "Recursion for LLMs" and "Then Custody" via IDUNA blog.write API — live at
  /blog/recursion-for-llms/ and /blog/then-custody/, auto-listed in /blog/. Footer links added
  (needs deploy).

## 2026-07-19 (5)
- blog: published "Knights of the Void" via IDUNA blog.write API -- live at
  /blog/knights-of-the-void/. Footer link added (needs deploy).
