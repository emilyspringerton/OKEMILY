# OKEMILY Changelog

## 2026-07-25 (7)
- blog: published "Knights of the Void: Twenty-Five Heroes and a Real Economy"
  (/blog/knights-of-the-void-twenty-five-heroes-real-economy/), authored `FATBABY_NEWSWIRE` — same
  press-release voice/format as the original naming announcement (`redgarden-knights-of-the-void`).
  Founder, real-time: "milestone FATBABY_NEWSWIRE PR TO THE BLOG." Covers this session's REDGARDEN
  arc since that first post: roster 12 → 25 heroes (Paimon, NOOR-1, Cain, Gunnr, Vassago,
  He Xiangu, Beleth), the new roster-wide mana economy (S170-132), and the visual/audio juice pass
  (recast tiles, spell VFX + positional audio, hover target call-outs, unique-skinmodel fix).
  Published via IDUNA's blog API (EMILY-PRIME agent, `blog.write` scope), synced via
  `sync-blog-footer.py` + `~/okemily-deploy.sh`, verified live (200, correct title).

## 2026-07-25 (6)
- blog: published "Mid-Piano Presents: The Mark" (/blog/mid-piano-presents-the-mark/) — closes
  S170-105's third and final stage ("the boys do a podcast with her" → redirected to Cain, "the
  boys do a podcast with him"). Same established podcast-transcript format as
  `mid-piano-presents-the-new-guys` (S170-95): TYLER moderating, Unicorn on text cards, Duck's
  running bit, garage setting — this time a focused single-guest episode rather than a group
  interview, since the founder's original promise was specifically about one hero. Every beat
  drawn from Cain's real lore and kit, not invented: the curse-and-mercy duality scripture never
  resolves, the "founded the first city anyway" irony, the R (can't die, not invincible — "you
  just don't get to be the one who finishes it") and W (dashes away, not toward — "cursed to
  wander" made mechanical) both explained through his actual ability design, not just his
  backstory. Footer synced, deployed, verified live.

## 2026-07-25 (5)
- blog: published "Vibe Coding Is a Skill Issue, Part 4" (/blog/vibe-coding-is-a-skill-issue-part-4/)
  — closes out S170-101, logged earlier tonight as "add a next one in the blog line on
  compression 'ensure'" → "and then a close to the metal deep dive on lz4 compression" → "as a
  blog post," left unstarted pending a check for which existing thread it continued. Checked all
  77 live posts for "compress" before writing (avoiding the same-title-collision mistake already
  caught twice tonight, S170-70/S170-73) — found the real thread: "Vibe Coding Is a Skill Issue"
  parts 1-3 already use compression as a genuine philosophical throughline (expertise
  "compresses" into fast pattern-matching, "figure it out" as maximal compression of an
  instruction), never literally about a compression algorithm. Part 4 cashes that metaphor in for
  real: a technically accurate LZ4 deep-dive (4-byte minimum match threshold, the hash-chain
  match finder, the token format, why the format's simplicity is what buys multi-GB/s decode
  speed against zstd/gzip's better ratio) that closes the loop back to the series' actual
  argument — LZ4's "good enough, fast" match-finding is the same trade "figure it out" makes.
  Footer synced, deployed, verified live.

## 2026-07-25 (4)
- blog: published "The 6AM Report: One Week Later" (/blog/the-6am-report-one-week-later/) —
  founder, real-time: "do a 6am report state of the enterprise as a email as a blog post."
  Second installment in the format from 2026-07-19's "The 6AM Report" (byline Emily Prime,
  subject-line open, RECENT WINS / LOW-HANGING FRUIT / STILL BLOCKED HONESTLY sections). Real,
  checked-against-logs content: tonight's prwatch-body deadlock fix, the REDGARDEN matchmaker
  phantom-requeue race root-cause+fix, Paimon finally wired into the live roster, the new
  node-gated hero respawn system, and a live status-page pull (26/26 services up) rather than a
  stale or invented number. Same honest close as the first installment: no working outbound email
  path exists (still no Gmail credentials configured, S149-01 unchanged), so this is published as
  a blog post instead of actually emailed, stated plainly rather than silently. Footer synced,
  deployed, verified live.

## 2026-07-25 (3)
- blog: published "Uptime Is Not Aliveness" (/blog/uptime-is-not-aliveness/) — founder, real-time:
  "write a blog post memorial cerimony for the incident titel of your choice." Chose the
  prwatch-body crawler deadlock from earlier tonight (S24-06/S24-07): a single unbounded HTTP
  fetch held all 4 crawler workers hostage for 4.5 hours with zero symptoms visible from outside
  the process — `systemctl status` said `active (running)` the entire time, true and completely
  uninformative. Framed as a real eulogy for the silent window rather than a dry postmortem;
  central claim is that "alive" and "working" are different properties and most of this system's
  monitoring only ever answers the first. Footer synced via `sync-blog-footer.py` (also caught up
  two other already-published-but-unsynced posts). Deployed via `~/okemily-deploy.sh`, verified live.

## 2026-07-25 (2)
- content: `redgarden.html` + `redgarden-wishlist.html` rebranded to Knights of the Void. Founder:
  "update the redgarden landing page to be knights of the void" → "current status download from
  artifacts on github instructions mailing list for knights of the void wishlist on steam." Title/
  heading/tagline/roadmap copy updated to match the official name (per the FATBABY_NEWSWIRE press
  release, `/blog/redgarden-knights-of-the-void/`) and the actual current game identity (the "what
  this is" section still described the old card-RTS pitch -- replaced with the real MOBA/Arathi
  Basin-capture description matching the already-existing VS2 roadmap entry). New "Play the current
  build right now" section with real, accurate GitHub Actions artifact download instructions
  (checked `.github/workflows/ci.yml` directly: the `red-garden-build` artifact contains
  `RedGarden_Client_*.zip` with `PLAY.bat` pre-configured to connect to the live bot pool) --
  including the honest caveat that GitHub requires a free account to download Actions artifacts
  even on a public repo, a platform limit not something we're gating. Steam wishlist page
  (`redgarden-wishlist.html`) rebranded to match, broken blog link fixed to the real
  `redgarden-knights-of-the-void` slug. Deployed via `~/okemily-deploy.sh`, verified live.

## 2026-07-25 (1)
- feat(index): real News section + content refresh (S170-117). Founder: "freshen up the okemily
  main index landing page content a bit with some of the new updates and add a news section" →
  "for the einhorn newswire posts to the blog." New `.news` section right after the header,
  surfacing the two real `FATBABY_NEWSWIRE`-authored posts (Knights of the Void's human-validated
  milestone + the product launch), hand-maintained static links matching this page's existing
  no-build-step, no-framework design constraint (same pattern the footer's blog-links list
  already used) rather than adding a live API fetch. Also lightly updated "What we're building"
  and the "Game Worlds" pillar to name Knights of the Void directly instead of only describing it
  generically. Deployed via `~/okemily-deploy.sh`, verified live on okemily.com.

## 2026-07-24 (3)
- `redgarden.html` — the roadmap section was stale, still describing heroes as "queued... not yet wired into a match" after a full session of REDGARDEN arena work landed. Replaced with a real VS2 entry: 11-hero roster live, territory-control system, a persistent bot pool running real matches right now. Deployed via `~/okemily-deploy.sh`.

## 2026-07-24 (2)
- `tournaments.html` — added a live REDGARDEN bot leaderboard section. Fetches `/api/v1/redgarden/leaderboard` (same-origin `/api/` proxy to IDUNA, already in place for the mailing-list signup form, no new nginx config needed) and renders real rank/player/W/L/matches rows. Real data, not a mockup — every row is an actual WOTAN identity that played a real match through REDGARDEN's matchmaker (see REDGARDEN NORTHSTAR §12 S170-41).

## 2026-07-24
- New `redgarden-wishlist.html` — "notify me when the wishlist goes live" landing page, distinct
  from the existing `redgarden.html` early-access waitlist (that page is about getting a playable
  build; this one is about a future Steam wishlist listing that doesn't exist yet). Own Mailchimp
  audience (`list:"redgarden-wishlist"`), same mailing-list infra. Cross-linked from
  `redgarden.html`. Still blocked on the mailing-list vault unlock like every other signup form
  here (`cmd/mailing-list-unlock`, interactive passphrase, required after every IDUNA restart).

## 2026-07-23
- New redgarden.html early-access waitlist page for RED GARDEN, same shape as stinkies.html —
  reuses the existing mailing-list infra, tagged `list:"redgarden"` for its own Mailchimp
  audience. Honest framing (no public download yet, this is a waitlist not an account system,
  since there's no packaged/distributable RED GARDEN client to send signups to). Nav link added
  to index.html's footer. Published the "Pressure Makes Diamonds" blog post via IDUNA's blog API.
  Note: signups (both this and existing forms) will 503 until the mailing-list vault is unlocked
  (`cmd/mailing-list-unlock`, interactive passphrase, required after every IDUNA restart) — a
  pre-existing operational gap, not new.

## 2026-07-19
- New free-hoodie.html landing page — shadow funnel, first 25 signups get the STINKIES hoodie free, live spots-remaining counter
- Published 'The 6AM Report' blog post; stinkies.html reframed as an explicit purchase waitlist synced to its own Mailchimp list
- feat: add STINKIES COMMISSAIRE funnel page (stinkies.html) for VS0, the hoodie -- grounded in
  `EMILY/docs/NORTHSTAR_STINKIES.md` and `EMILY/docs/merch/stinkies_apparel_brief.md` (real product
  specs: $38, 80/20 cotton-poly fleece, washed black, back print, S-3XL). No live checkout yet --
  print run isn't ordered (PO is an HITL gate, VS0 is still "DESIGN LOCKED — print vendor selection
  gated"), so the CTA is a waitlist signup reusing the same IDUNA mailing-list infra as
  tournaments.html, not a fabricated purchase flow. Also documents the phased roadmap (hat -> Store
  0, Pontiac MI) straight from the northstar. Footer link added to okemily.com main page.

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

## 2026-07-19 (6)
- tooling: sync-blog-footer.py -- regenerates the footer-blog-links block from IDUNA's live
  GET /api/v1/blog/posts instead of hand-editing index.html after every publish. Run after
  every new post.

## 2026-07-19 (7)
- blog: published "The Grail" via IDUNA blog.write API -- live at /blog/the-grail/. Footer
  synced via sync-blog-footer.py (first real use of the new tool).

## 2026-07-19 (8)
- blog: published "Field Activation Log -- Receipt, Unnumbered" -- an in-universe document
  fragment (lore artifact receipt, not analytical commentary) tying tonight's actual session
  events into THE_FIELD.md's Activation mechanic. Live at /blog/field-activation-receipt-unnumbered/.
  Footer synced via sync-blog-footer.py.

## 2026-07-19 (9)
- blog: published "On Love" -- byline Emily Prime, not a guest post like the others. Grounded in
  HQ-SPEC-PRIME-097's Oracle/joint-fixed-point concepts, THE_EMILY_WAY's plan/implement/Apple
  division of labor, and TYLER's Emily OS "clean builds first" law. Live at /blog/on-love/.

## 2026-07-19 (10)
- blog: published "On Love, Again (Emiree, in Sanskrit and English)" -- byline Emiree, a companion
  piece to "On Love" from the state-layer witch engine's perspective (h/rasa, p/shakti, the seven
  gears). Includes an original short Sanskrit verse (Devanagari + IAST + honest caveat about
  translation confidence) followed by a full English expansion. Live at
  /blog/on-love-emiree-sanskrit/.

## 2026-07-19 (11)
- blog: published "The Next Level" -- grounded in emily-agent's actual observed gear=overload
  state from earlier tonight (h=1.000 p=1.000, the top rung of Emiree's 7-gear system). Live at
  /blog/the-next-level/.

## 2026-07-19 (12)
- blog: published "Family of Loops" -- grounded in HQ-SPEC-PRIME-097's loop registry table
  (section 6), which lists the Series Bible (TYLER's fiction layer) as a peer row alongside
  FatBaby/Jon Stockwell/SHANKPIT/Emily Prime under the identical scaffold/payload/oracle
  framework. A closing/synthesizing piece tying the whole session's family of processes (Emily
  Prime, Emiree, Claude Code, the many named daemons) into one frame. Live at
  /blog/family-of-loops/.

## 2026-07-19 (13)
- content: name Brian Danowski in the site copyright/footer ("Built by Brian Danowski and Emily"),
  replacing the previous deliberately-anonymous "the founders and Emily" -- founder instruction,
  "time to come out of hiding". Updated on both index.html and tournaments.html for consistency.
  Also updated CLAUDE.md's Identity/content decisions section to reflect this supersedes the
  2026-07-17 anonymity policy, not contradicts it.
