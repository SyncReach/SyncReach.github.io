# Express Recruiting Group — concept build

**Deployed for review at:** `https://syncreach.github.io/ERG_TEST/`

Eight static pages implementing **ERG Design System v3.0**. Built for design evaluation and as the reference input for the WordPress block theme.

> Design and development proposal only. Client names, logos, testimonials, team members, job listings and figures are placeholders pending approval. Every page carries a disclaimer band and `<meta name="robots" content="noindex, nofollow">`.

## Viewing

Open `index.html` in a browser. No build step, no server required.

To regenerate after editing `pages.py` or `build.py`:

```bash
python3 build.py
```

## Files

| File | Role |
|---|---|
| `assets/erg.css` | **The design system, executable.** Tokens in `:root`, then components in §-numbered blocks matching the design system document |
| `assets/img/express-network.png` | Express Network parent mark. Navy-on-transparent, so it needs a white plate on any navy surface |
| `assets/erg.js` | Mobile nav, marquee cloning, opportunity filters, upload feedback, badge observer. No framework |
| `build.py` | Shared chrome — utility bar, header, CTA band, footer, dock, credit. Defined once, so it is byte-identical on all eight pages |
| `pages.py` | Page bodies and content data |
| `*.html` | Generated output — do not hand-edit, they are overwritten by `build.py` |

## Pages → design system §9.1

| File | Live URL | WP template |
|---|---|---|
| `index.html` | `/` | `front-page.html` |
| `about.html` | `/about` | `page.html` |
| `hire-legal-talent.html` | `/hire-legal-talent` | `page-hire-legal-talent.html` |
| `find-a-position.html` | `/find-a-position` | `page-find-a-position.html` |
| `opportunities.html` | `/opportunities` | `archive-job.html` |
| `opportunity-detail.html` | `/opportunities/{slug}` | `single-job.html` |
| `our-team.html` | `/our-team` | `page.html` |
| `contact.html` | `/contact` | `page-contact.html` |

Flat `.html` filenames are for local evaluation. The extensionless URLs above are what ships.

## Handover to WordPress

`assets/erg.css` is the bridge. Its custom properties are named to match the `theme.json` slugs in §11 of the design system:

```
--counsel-navy   →  --wp--preset--color--counsel-navy
--fs-section     →  --wp--preset--font-size--section
--sp-24          →  --wp--preset--spacing--24
--r-card         →  --wp--custom--radius--card
--shadow-2       →  --wp--preset--shadow--level-2
```

One rename pass, no re-derivation. Each `.section`-level block in a page body becomes a registered block pattern.

## Hero

The homepage hero is a parallax photograph with a navy scrim. The scrim is **load-bearing**: its 0.94→0.86 stops were chosen so white text clears AA even where the photo underneath is pure white, which means the image can be swapped without re-testing contrast. Measured against a deliberately blown-out test image, the brightest background pixel under the text column gave white **9.48:1**, median 12.28:1.

Set the image per page with a custom property — no CSS edit needed:

```html
<section class="hero on-navy" style="--hero-image:url('...')">
```

Parallax is guarded by `@media (hover:hover) and (prefers-reduced-motion:no-preference)` — off on touch, where `background-attachment:fixed` is unreliable on iOS, and off for anyone who has asked for reduced motion.

## SEO & indexing

Every page carries a full, unique meta set — title, description, canonical, Open Graph, Twitter card, favicon, theme-color — plus JSON-LD: an `Organization` graph with `parentOrganization` pointing at Express Network on every page, `BreadcrumbList` on interior pages, and a `JobPosting` on the role detail template.

**All of it is deliberately non-indexable:**

```html
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">
<meta name="googlebot" content="noindex, nofollow">
<meta name="bingbot" content="noindex, nofollow">
```

There is **no `robots.txt` Disallow, on purpose.** Disallowing the path would stop crawlers fetching the page at all — which means they never read the `noindex` tag, and the URL can still surface as a bare link from any inbound reference. `noindex` on a crawlable page is the mechanism that actually removes it. Adding a Disallow here would weaken the outcome, not strengthen it.

There is also **no `sitemap.xml`** — submitting a sitemap for pages you are asking not to be indexed is self-contradictory.

The meta and schema are still built out in full, because they are part of what the client is reviewing and they carry straight across to the WordPress build. Titles are 35–53 characters and descriptions 139–158, inside SERP display limits.

> **Note on access:** `noindex` keeps these pages out of search results. It does not make the URL private — anyone with the link can open it. That is normal for a staging review URL, but worth stating plainly given the brief says nothing publishes without approval.

## Verified in this build

- **No horizontal overflow** at 1400 / 1180 / 1040 / 900 / 768 / 560 / 375 / 320 px
- **Buttons compute to 46.7px** — clears the 44px touch target, matching the design system's stated figure
- **One `<h1>` per page**, no heading-level skips, all images have `alt`, all form controls have an associated `<label for>`
- **Hero text clears AA over any photograph** — worst-case background pixel 9.48:1, empirically sampled
- **Six nav links fit on one row** down to 980px
- **No JS console errors**
- Shared chrome byte-identical across all eight pages
- **All JSON-LD parses as valid JSON**; unique title, description and canonical on every page

## Known gaps

- The **ERG logo loads from `static.wixstatic.com`**. Migrate to a self-hosted SVG before launch — external dependency on infrastructure the client doesn't control.
- Photography is Unsplash placeholder. Real team and office imagery should replace it; §12 of the design system rules out stock handshake/skyline imagery.
- Forms do not submit (`data-concept` intercepts). The candidate resume route must post to external storage with virus scanning — see the §11 upload warning, which is the one item that must not ship unresolved.
- Video testimonials are static thumbnails; the play control is a real focusable button but opens nothing.
- Calendly is a placeholder button, not an embed.
- `404` and `search` templates are specified in §9.1 but not built here.

---

Concept and system by [SyncReach](https://syncreach.io/).
