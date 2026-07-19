/**
 * Emily's Internet-Native Immune System — okemily.com consumption layer.
 *
 * The DIS collector (originally built for the WordPress/EDIS product) reads
 * this box's nginx access log, which is shared across every vhost on this
 * server — so it already sees okemily.com's traffic without any new
 * collector instance. This script is the read-only client side: on every
 * page load, ask IDUNA (which proxies the collector) what the current
 * posture is, and adapt the STINKIES ad block accordingly.
 *
 * The actual "pressure valve" logic here is specific to what okemily.com
 * costs to run: serving the static HTML is free either way, but every ad
 * click funnels into a mailing-list signup POST against IDUNA's API — the
 * one surface on this site that's actually expensive to abuse. So instead
 * of downgrading image quality (the WordPress version's job, since it's
 * paying for asset bandwidth), this version's job is: don't invite more
 * traffic into the signup endpoint while IDUNA is already under strain.
 *
 * Fail-open: any error here just leaves the ad block as originally
 * rendered. Never blocks the page, never throws where a caller would see it.
 */
(function () {
	'use strict';

	fetch('/api/v1/dis/admode')
		.then(function (res) { return res.ok ? res.text() : 'svg'; })
		.then(function (mode) {
			mode = mode.trim();
			var ads = document.querySelectorAll('.post-ad');
			ads.forEach(function (ad) {
				switch (mode) {
					case 'svg':
					case 'text':
						// Normal / elevated: leave the ad as rendered.
						break;
					case 'pow_captcha':
					case 'none':
					default:
						// Attack / degraded: don't invite more load onto the
						// signup API right now. The rest of the page (the
						// actual content) is untouched either way.
						ad.style.display = 'none';
						break;
				}
			});
		})
		.catch(function () {
			// Fail open — collector/IDUNA unreachable, leave ads as-is.
		});
})();
