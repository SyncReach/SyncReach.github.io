# SyncReach — Production Landing Page

`index.html` is a self-contained, responsive landing page for SyncReach. No build step, no
framework — just open it or upload it. Fonts load from Google Fonts; everything else (styles,
SVG logo + globe motif, the animated growth system) is inline.

## What's here
- `index.html` — the full landing page.
- `favicon.svg` — browser tab icon (the SyncReach globe).

## Sections
Nav → Hero → "What we do" strip → Why we created SyncReach → **Growth System (animated:
Attract → Capture → Convert → Scale)** → What your firm gains → Services (8) → Built for modern
law firms → About (founders) → Book-a-consultation CTA → Footer.

## Pages
- `index.html` — landing.
- `services.html` — all 8 services.
- `about.html` — founders + story.
- `contact.html` — consultation form + contact details.
- `thanks.html` — post-submit confirmation (form redirects here).
- `favicon.svg`, `assets/site.css`, `assets/site.js` — shared chrome.

## Go live — checklist

1. **Add your real photos.** Search each page for `replace ... with <img>` comments. Each
   placeholder is a `<div class="photo …">`; swap the whole div for
   `<img class="photo hero__photo" src="https://yourhost.com/hero.jpg" alt="…">` (keep the same
   class so the frame/sizing carries over). Photo slots: hero, team/office, two founder headshots.
2. **Activate the contact form.** `contact.html` posts to **FormSubmit.co**, which emails every
   submission to **admin@syncreach.io** — no backend needed. The FIRST time the form is submitted
   from your live domain, FormSubmit sends a one-time confirmation email to admin@syncreach.io;
   click the link once and delivery is on for good. To switch providers (Formspree, your host's
   handler), change the `<form action="…">` in `contact.html`. The form redirects to `thanks.html`
   on success (the `_next` hidden field).
3. **Consultation buttons** across the site now point to `contact.html`. If you'd rather use a
   scheduler (e.g. Calendly), change those `href="contact.html"` links instead.
4. **Set the social preview image.** Add an `og-image.png` (1200×630) next to `index.html`
   (referenced in `<head>`), or update the `og:image` path.
5. **Upload** all `.html` files + `favicon.svg` + the `assets/` folder (+ your images +
   `og-image.png`) to your host's public/web root, keeping the structure.
6. **Point your domain.** Follow your host's DNS instructions to map your domain to the upload.
7. **Recommended before launch:** add Privacy Policy + Terms pages (the footer links are `#`),
   and a real Sign-in destination (currently `#`).

## Contact details (live)
- **Email:** admin@syncreach.io · **Phone:** +1 (289) 270-1009 (shown on `contact.html` + all footers).

## Editing copy
All text is plain HTML — edit it directly. The animated growth-system steps live in the
`<script>` at the bottom (the `STAGES` array) if you want to change those four labels/blurbs.

## Notes
- Fully responsive (desktop / tablet / phone) and keyboard-accessible; respects reduced-motion.
- Colors, type, and spacing come from the SyncReach design system (tokens inlined at the top of
  the file), so this page stays visually consistent with the rest of the brand.
- The nav links (Growth System / Services / About) scroll to sections on this one page. If you
  add separate pages later, update those `href`s.
