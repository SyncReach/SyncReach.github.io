#!/usr/bin/env python3
"""Build the ERG concept site.

Shared chrome (utility bar, header, CTA band, footer, credit) is defined once
here so it is byte-identical on every page. In the WordPress block theme these
become template parts and patterns; this script is the concept-build stand-in.
"""
import pathlib

OUT = pathlib.Path(__file__).parent

# Deployment root. Every canonical / og:url is absolute against this.
BASE = "https://syncreach.github.io/ERG_TEST"
OG_IMAGE = f"{BASE}/assets/img/og-card.png"
LOGO = "https://static.wixstatic.com/media/4f89bb_bcd4618cdfed4a4e90d2ae2a32650279~mv2.png"
EN_LOGO = "assets/img/express-network.png"
EN_ALT = "Express Network — a legal support network company"
PHONE = "(800) 555-0188"
TEL = "tel:+18005550188"

NAV = [
    ("index.html", "Home"),
    ("about.html", "About"),
    ("hire-legal-talent.html", "Employers"),
    ("find-a-position.html", "Candidates"),
    ("opportunities.html", "Positions"),
    ("contact.html", "Contact"),
]

GLOBE = ('<svg viewBox="0 0 100 100" fill="none" aria-hidden="true">'
         '<g stroke="currentColor" stroke-width="4" stroke-linecap="round">'
         '<circle cx="50" cy="50" r="44"/><line x1="50" y1="6" x2="50" y2="94"/>'
         '<ellipse cx="50" cy="50" rx="22" ry="44"/><line x1="6" y1="50" x2="94" y2="50"/>'
         '<line x1="11.34" y1="29" x2="88.66" y2="29"/><line x1="11.34" y1="71" x2="88.66" y2="71"/>'
         '<line x1="19.8" y1="18" x2="80.2" y2="18"/><line x1="19.8" y1="82" x2="80.2" y2="82"/>'
         '</g></svg>')
GLOBE_THIN = GLOBE.replace('stroke-width="4"', 'stroke-width="1.1"')


def header(active):
    def link(href, label):
        cur = ' aria-current="page"' if href == active else ""
        return f'<li><a href="{href}"{cur}>{label}</a></li>'
    links = "".join(link(h, l) for h, l in NAV)
    return f"""<div class="util">
  <div class="util__in">
    <span>Legal Recruiting Division of Express Network</span>
    <div class="util__right">
      <a class="util__phone" href="{TEL}">{PHONE}</a>
      <a href="contact.html">Book a Call</a>
      <a href="contact.html">Email Us</a>
    </div>
  </div>
</div>

<header class="site-header">
  <div class="site-header__in">
    <a class="logo" href="index.html"><img src="{LOGO}" alt="Express Recruiting Group, by Express Network"></a>
    <nav class="nav" id="primary-nav" aria-label="Primary"><ul>{links}</ul></nav>
    <div class="header__actions">
      <a class="header__phone" href="{TEL}">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.3 1.8.6 2.6a2 2 0 0 1-.4 2.1L8 9.8a16 16 0 0 0 6 6l1.4-1.4a2 2 0 0 1 2.1-.4c.8.3 1.7.5 2.6.6a2 2 0 0 1 1.7 2Z"/></svg>
        {PHONE}
      </a>
      <div class="header__ctas">
        <a class="btn btn--ghost" href="find-a-position.html">Find a Position</a>
        <a class="btn btn--primary" href="contact.html">Book a Call</a>
      </div>
    </div>
    <button class="nav-toggle" aria-label="Open menu" aria-controls="primary-nav"><span></span><span></span><span></span></button>
  </div>
</header>"""


CTA_BAND = f"""<section class="cta-band on-navy">
  <div class="wrap">
    <h2>Need Legal Talent?</h2>
    <p>Let's discuss your hiring needs &mdash; or find your next opportunity.</p>
    <div class="cta-band__row">
      <a class="btn btn--primary-navy" href="{TEL}">Call {PHONE}</a>
      <a class="btn btn--ghost-dark" href="contact.html">Email Us</a>
      <a class="btn btn--ghost-dark" href="contact.html">Book a Call</a>
      <a class="btn btn--ghost-dark" href="hire-legal-talent.html">Start Your Search</a>
    </div>
  </div>
</section>"""


FOOTER = f"""<footer class="site-footer">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-brand">
        <a class="foot-logo" href="index.html"><img src="{LOGO}" alt="Express Recruiting Group, by Express Network"></a>
        <p>The legal recruiting division of Express Network. Serving law firms nationwide since 1985, through eight offices and decades of legal industry experience.</p>
        <a class="phone" href="{TEL}">{PHONE}</a>
      </div>
      <div class="foot-col">
        <h2>Law Firms</h2>
        <ul>
          <li><a href="hire-legal-talent.html">Hire Legal Talent</a></li>
          <li><a href="contact.html">Book a Call</a></li>
          <li><a href="hire-legal-talent.html">Submit a Hiring Need</a></li>
        </ul>
      </div>
      <div class="foot-col">
        <h2>Candidates</h2>
        <ul>
          <li><a href="opportunities.html">Current Opportunities</a></li>
          <li><a href="find-a-position.html">Submit Your Resume</a></li>
          <li><a href="our-team.html">Connect With a Recruiter</a></li>
        </ul>
      </div>
      <div class="foot-col">
        <h2>Express Network</h2>
        <a class="en-plate" href="https://www.expressnetwork.com" rel="noopener"><img src="{EN_LOGO}" alt="{EN_ALT}"></a>
        <ul>
          <li><a href="https://www.expressnetwork.com" rel="noopener">Express Network</a></li>
          <li><a href="https://www.expressnetwork.com" rel="noopener">Express Deposition Services</a></li>
          <li><a href="https://www.expressnetwork.com/offices" rel="noopener">Office Locations</a></li>
          <li><a href="https://www.expressnetwork.com/about-us" rel="noopener">About Express Network</a></li>
        </ul>
      </div>
      <div class="foot-col">
        <h2>Connect</h2>
        <ul>
          <li><a href="our-team.html">Our Team</a></li>
          <li><a href="#" rel="noopener">LinkedIn</a></li>
          <li><a href="#" rel="noopener">Facebook</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>&copy; 2026 Express Recruiting Group, a division of Express Network. All rights reserved.</span>
      <span><a href="#">Terms</a> &middot; <a href="#">Privacy</a></span>
    </div>
  </div>
</footer>

<div class="disclaimer-band">Design concept only. Client names, video testimonials, team members and figures are placeholders pending confirmation and approval before publication.</div>"""


DOCK = f"""<nav class="dock" aria-label="Quick contact">
  <a href="{TEL}">Call</a>
  <a href="contact.html">Email</a>
  <a class="is-primary" href="contact.html">Book a Call</a>
</nav>"""


CREDIT = f"""<aside class="sr-credit" aria-label="Design credit">
  <div class="sr-ghost" aria-hidden="true">{GLOBE_THIN}</div>
  <div class="sr-in">
    <a class="sr-lock" href="https://syncreach.io/" target="_blank" rel="noopener">
      <span class="sr-mark">{GLOBE}</span>
      <span class="sr-wm"><b>SYNC</b><i>REACH</i></span>
    </a>
    <p class="sr-txt">Concept study designed and built by <strong>SyncReach</strong>. Digital growth systems for law firms: websites, client intake, search and AI visibility, automation. <a href="https://syncreach.io/" target="_blank" rel="noopener">syncreach.io</a></p>
  </div>
</aside>
<aside class="sr-badge-wrap" aria-label="SyncReach credit badge"><a class="sr-badge" href="https://syncreach.io/" target="_blank" rel="noopener">{GLOBE}<span>Concept by <b>SyncReach</b></span></a></aside>"""


ORG_LD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "@id": "%s/#organization",
  "name": "Express Recruiting Group",
  "alternateName": "The Legal Recruiting Division of Express Network",
  "url": "%s/",
  "logo": "%s/assets/img/og-card.png",
  "description": "The legal recruiting division of Express Network, connecting law firms with exceptional legal talent nationwide.",
  "foundingDate": "1985",
  "telephone": "+1-800-555-0188",
  "areaServed": "US",
  "parentOrganization": {
    "@type": "Organization",
    "name": "Express Network",
    "url": "https://www.expressnetwork.com",
    "description": "Nationwide provider of litigation, court, deposition and legal support services since 1985."
  },
  "knowsAbout": ["Legal recruiting","Attorney placement","Paralegal recruiting","Legal operations staffing"]
}
</script>
""" % (BASE, BASE, BASE)


def breadcrumb_ld(trail):
    """trail: list of (name, path-or-None). None means current page."""
    items = []
    for i, (name, path) in enumerate(trail, 1):
        item = f'"item": "{BASE}/{path}"' if path else ""
        sep = ", " + item if item else ""
        items.append('{"@type": "ListItem", "position": %d, "name": "%s"%s}' % (i, name, sep))
    return ('<script type="application/ld+json">\n'
            '{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [\n  '
            + ",\n  ".join(items) + '\n]}\n</script>\n')


SHELL = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{canonical}">

<!-- Concept build: kept out of every index. Deliberately NOT paired with a
     robots.txt Disallow — blocking the crawl would stop engines reading this
     tag, which is how a URL ends up listed as a bare link anyway. -->
<meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">
<meta name="googlebot" content="noindex, nofollow">
<meta name="bingbot" content="noindex, nofollow">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Express Recruiting Group">
<meta property="og:locale" content="en_US">
<meta property="og:title" content="{ogtitle}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{ogimage}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Express Recruiting Group — the legal recruiting division of Express Network">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{ogtitle}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ogimage}">

<meta name="theme-color" content="#193059">
<meta name="author" content="Express Network">
<link rel="icon" href="assets/img/favicon.png" type="image/png">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700;800&family=Inter:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;700&family=IBM+Plex+Serif:wght@400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/erg.css">
{jsonld}</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
{header}
<main id="main">
{body}
</main>
{cta}
{footer}
{dock}
{credit}
<script src="assets/erg.js"></script>
</body>
</html>
"""


def page_hero(crumb, h1, lede):
    return f"""  <section class="page-hero on-navy">
    <div class="wrap">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span>{crumb}</nav>
      <h1>{h1}</h1>
      <p>{lede}</p>
    </div>
  </section>"""


def build(slug, title, desc, body, active=None, cta=True, ogtitle=None, jsonld=""):
    canonical = f"{BASE}/" if slug == "index.html" else f"{BASE}/{slug}"
    html = SHELL.format(
        title=title,
        desc=desc,
        canonical=canonical,
        ogtitle=ogtitle or title,
        ogimage=OG_IMAGE,
        jsonld=ORG_LD + jsonld,
        header=header(active or slug),
        body=body,
        cta=CTA_BAND if cta else "",
        footer=FOOTER,
        dock=DOCK,
        credit=CREDIT,
    )
    (OUT / slug).write_text(html, encoding="utf-8")
    return slug


if __name__ == "__main__":
    import pages
    written = pages.render(build, page_hero, breadcrumb_ld, BASE)
    for name in written:
        print("wrote", name)
