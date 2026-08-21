#!/usr/bin/env python3
"""Page bodies for the ERG concept build. Chrome lives in build.py."""

TEL = "tel:+18005550188"
PHONE = "(800) 555-0188"
PLAY = ('<svg width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true">'
        '<path d="M4 2.5L15 9L4 15.5V2.5Z" fill="#193059"/></svg>')
LOCK = ('<svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
        'stroke-width="2" stroke-linecap="round" aria-hidden="true">'
        '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>')

FIRMS = ["Morgan &amp; Morgan", "Sweet James", "Miller Barondess", "Barnes &amp; Thornburg",
         "Milbank", "Robert Sanders Law", "LADP"]

ATTORNEYS = ["Commercial Litigation Attorneys", "Employment Attorneys", "Personal Injury Attorneys",
             "Plaintiff-Side Attorneys", "Defense Attorneys", "Corporate Attorneys",
             "Other Legal Practice Areas"]
SUPPORT = ["Paralegals", "Legal Assistants", "Case Managers", "Intake Professionals",
           "Office Managers", "Directors of Operations", "HR Professionals",
           "Legal Billing Professionals", "Lien Negotiators", "Administrative &amp; Executive Support"]

WHY = [
    ("Legal Industry Specialization", "Every search is legal-focused, from attorneys through legal support and operations staff."),
    ("Part of Express Network", "Backed by an organization established in 1985, with the infrastructure and resources of a national platform."),
    ("Backed Since 1985", "Four decades of continuous service to the legal industry, not a recruiting desk opened last year."),
    ("Nationwide Reach", "Eight offices and established relationships within the legal community, coast to coast."),
    ("Established Relationships", "Decades of working relationships across national, regional, plaintiff-side and defense firms."),
    ("Attorneys Through Management", "One partner for attorney searches, legal support hires, and operations leadership."),
    ("Personalized Approach", "A concierge-style process focused on cultural fit, not just filling a vacancy."),
    ("Confidential Representation", "Candidate searches are handled with discretion from first contact through placement."),
    ("Operational Understanding", "We understand how law firms actually run, because Express Network has served them for decades."),
    ("Express Network Infrastructure", "Access to the systems, reach and resources of an established national legal-services platform."),
]

STORIES = [
    ("https://images.unsplash.com/photo-1573497019940-1c28c88b4f3e?auto=format&fit=crop&w=500&q=80",
     "Regional Litigation Firm", "Senior Associate Placed",
     "They found us a candidate who fit our culture, not just the job description.", "Filled in 19 days"),
    ("https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=500&q=80",
     "Plaintiff-Side Firm", "Director of Operations Placed",
     "The process was fast, confidential, and genuinely personalized.", None),
    ("https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=500&q=80",
     "Defense Firm", "Paralegal Team Placed",
     "Backed by Express Network's reach, they moved faster than any agency we'd used.", "4 hires, one quarter"),
]

ROLES = [
    ("Commercial Litigation Associate", "litigation", "Commercial Litigation", "Los Angeles, CA", "4–6 years", "2 days ago", True),
    ("Senior Employment Attorney", "employment", "Employment", "San Francisco, CA", "8+ years", "5 days ago", True),
    ("Personal Injury Case Manager", "support", "Legal Support", "Phoenix, AZ", "3+ years", "1 week ago", False),
    ("Director of Legal Operations", "support", "Operations", "Chicago, IL", "10+ years", "1 week ago", False),
    ("Corporate Counsel", "corporate", "Corporate", "New York, NY", "6–9 years", "2 weeks ago", False),
    ("Litigation Paralegal", "support", "Legal Support", "Dallas, TX", "2+ years", "2 weeks ago", False),
    ("Defense Trial Attorney", "litigation", "Defense", "Atlanta, GA", "7+ years", "3 weeks ago", False),
    ("Intake Team Lead", "support", "Legal Support", "Remote", "3+ years", "3 weeks ago", False),
]

TEAM = [
    ("https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=400&q=80",
     "Placeholder Name", "Director of Legal Recruiting", "Leads attorney search across commercial litigation and employment practices, with two decades inside the legal industry."),
    ("https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=400&q=80",
     "Placeholder Name", "Senior Recruiter, Attorneys", "Focuses on plaintiff-side and defense litigation placements for regional and national firms."),
    ("https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=400&q=80",
     "Placeholder Name", "Recruiter, Legal Support", "Places paralegals, case managers and intake professionals across all eight Express Network markets."),
    ("https://images.unsplash.com/photo-1560250097-0b93528c311a?auto=format&fit=crop&w=400&q=80",
     "Placeholder Name", "Manager, Client Partnerships", "Works with hiring partners and operations directors to scope roles before a search begins."),
]


def stories_html():
    out = []
    for img, firm, role, quote, metric in STORIES:
        m = f'<span class="metric">{metric}</span>' if metric else ""
        out.append(f"""        <article class="story">
          <div class="story__vid">
            <img src="{img}" alt="Video testimonial thumbnail" loading="lazy">
            <button class="play" type="button" aria-label="Play testimonial from {firm}"><span>{PLAY}</span></button>
          </div>
          <div class="story__body">
            <div class="story__firm">{firm}</div>
            <div class="story__role">{role}</div>
            <p class="story__quote">&ldquo;{quote}&rdquo;</p>
            {m}
          </div>
        </article>""")
    return "\n".join(out)


def why_html():
    return "\n".join(
        f'        <article class="why"><div class="why__n">{i}</div><h3>{t}</h3><p>{d}</p></article>'
        for i, (t, d) in enumerate(WHY, 1))


def practice_html():
    a = "".join(f"<li>{x}</li>" for x in ATTORNEYS)
    s = "".join(f"<li>{x}</li>" for x in SUPPORT)
    return f"""      <div class="practice">
        <div><h3>Attorneys</h3><ul>{a}</ul></div>
        <div><h3>Legal Support &amp; Management</h3><ul>{s}</ul></div>
      </div>"""


def marquee_html():
    spans = "".join(f"<span>{f}</span>" for f in FIRMS)
    return f"""  <section class="marquee-band">
    <div class="wrap">
      <div class="section-head">
        <span class="kicker">Who We Work With</span>
        <h2>Trusted by law firms nationwide</h2>
        <p>Placeholder names shown for design purposes. Final client logos to be confirmed and approved before publication.</p>
      </div>
    </div>
    <div class="marquee"><div class="marquee__track" aria-label="Client law firm names">{spans}</div></div>
    <p class="marquee-note">Placeholder client names for concept purposes only.</p>
  </section>"""


DOORS = """  <section class="doors">
    <div class="door door--employers on-navy">
      <span class="eyebrow">For Law Firms</span>
      <h3>Fast-Track Your Search for Legal Talent</h3>
      <p>Submit your hiring needs and let our recruiting team get to work &mdash; backed by Express Network's nationwide reach and legal industry relationships.</p>
      <ul><li>Submit a hiring need</li><li>Book a consultation</li><li>Contact our recruiting team</li></ul>
      <a class="btn btn--primary-navy" href="hire-legal-talent.html">Start Your Search</a>
    </div>
    <div class="door door--candidates on-navy">
      <span class="eyebrow">For Candidates</span>
      <h3>Looking for Your Next Legal Opportunity?</h3>
      <p>Your search stays private. Your next opportunity starts here &mdash; view current openings or submit your resume confidentially.</p>
      <ul><li>View current opportunities</li><li>Submit your resume confidentially</li><li>Connect with our recruiting team</li></ul>
      <a class="btn btn--secondary-navy" href="find-a-position.html">Submit Your Resume</a>
    </div>
  </section>"""


CONFIDENTIAL = f"""        <div class="confidential">
          <div class="confidential__head">{LOCK}<strong>Your search stays private.</strong></div>
          <ul>
            <li>We never contact your current employer, and never share your name without your explicit approval first.</li>
            <li>Your resume is stored outside this website and is only seen by the recruiter handling your search.</li>
            <li>You decide which firms see your materials, and when.</li>
          </ul>
        </div>"""


def render(build, page_hero, breadcrumb_ld=None, BASE=""):
    written = []

    JOB_LD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "JobPosting",
  "title": "Commercial Litigation Associate",
  "description": "<p>A well-established regional litigation practice is adding an associate to its commercial disputes team, with first-chair opportunities on smaller matters within the first year.</p><ul><li>4-6 years of commercial litigation experience</li><li>Substantive motion practice and deposition experience</li><li>California bar admission in good standing</li></ul>",
  "datePosted": "2026-08-14",
  "validThrough": "2026-11-14",
  "employmentType": "FULL_TIME",
  "hiringOrganization": {"@type": "Organization", "name": "Confidential regional litigation firm"},
  "jobLocation": {"@type": "Place", "address": {"@type": "PostalAddress", "addressLocality": "Los Angeles", "addressRegion": "CA", "addressCountry": "US"}},
  "occupationalCategory": "23-1011.00 Lawyers",
  "experienceRequirements": {"@type": "OccupationalExperienceRequirements", "monthsOfExperience": 48},
  "directApply": false,
  "disambiguatingDescription": "Placeholder listing published for design review only. Not a live vacancy."
}
</script>
"""


    # ---------------------------------------------------------------- HOME
    home = f"""  <section class="hero on-navy" style="--hero-image:url('https://images.unsplash.com/photo-1521737604893-d14cc237f11d?auto=format&fit=crop&w=1900&q=80')">
    <div class="hero__in">
      <div class="hero__col">
        <span class="eyebrow">Backed by Express Network &middot; Est. 1985</span>
        <h1>Legal Talent. <em>Delivered.</em></h1>
        <p class="hero__lede">Express Recruiting Group is the legal recruiting division of Express Network &mdash; connecting exceptional legal talent with leading law firms nationwide, backed by decades of infrastructure, relationships, and legal industry experience.</p>
        <div class="hero__ctas">
          <a class="btn btn--primary-navy" href="hire-legal-talent.html">Hire Legal Talent</a>
          <a class="btn btn--ghost-dark" href="find-a-position.html">Find a Position</a>
        </div>
        <div class="hero__trust">
          <div><span class="dot"></span>Placing across 8 nationwide offices</div>
          <div><span class="dot"></span>Serving law firms since 1985</div>
          <div><span class="dot"></span>Attorneys through legal support</div>
        </div>
      </div>
    </div>
  </section>

  <div class="parent-strip">
    <div class="wrap">
      <div class="parent-strip__in">
        <a class="en-mark" href="https://www.expressnetwork.com" rel="noopener"><img src="assets/img/express-network.png" alt="Express Network — a legal support network company"></a>
        <div class="en-divider" aria-hidden="true"></div>
        <p><strong>Express Recruiting Group</strong> operates as part of <strong>Express Network</strong>, a nationwide provider of litigation, court, deposition and legal support services since 1985 &mdash; bringing the same infrastructure and legal industry relationships to talent acquisition.</p>
      </div>
    </div>
  </div>

  <section class="section">
    <div class="wrap split-2">
      <div class="prose">
        <span class="eyebrow eyebrow--light">About Us</span>
        <h2>More than a recruiting agency. A division of Express Network.</h2>
        <p>Express Recruiting Group was created to bring Express Network's decades of legal industry experience to a new service: legal talent acquisition. We understand law firm operations because our parent organization has served law firms nationwide since 1985 &mdash; we're not an outside agency learning the industry, we're already part of it.</p>
        <p>We work with national, regional, plaintiff-side and defense law firms, recruiting everyone from attorneys to legal support and operations staff, with a personalized approach every step of the way.</p>
        <div class="stat-grid">
          <div class="stat"><div class="stat__n">1985</div><div class="stat__l">Express Network founded</div></div>
          <div class="stat"><div class="stat__n">8</div><div class="stat__l">Offices nationwide</div></div>
          <div class="stat"><div class="stat__n">~117</div><div class="stat__l">U.S.-based full-time employees &mdash; to be confirmed</div></div>
          <div class="stat"><div class="stat__n">40+</div><div class="stat__l">Years serving the legal industry</div></div>
        </div>
      </div>
      <div class="media"><img src="https://images.unsplash.com/photo-1552664730-d307ca884978?auto=format&fit=crop&w=800&q=80" alt="Legal recruiting professionals collaborating" loading="lazy"></div>
    </div>
  </section>

{marquee_html()}

  <section class="section section--powder">
    <div class="wrap">
      <div class="section-head">
        <span class="kicker">Client Success Stories</span>
        <h2>Trusted by law firms to deliver the right talent</h2>
        <p>Short video testimonials from firms we've helped fill critical positions. New stories can be added at any time without a layout change.</p>
      </div>
      <div class="grid-3">
{stories_html()}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="kicker">Legal Recruiting Positions</span>
        <h2>Who we recruit for</h2>
        <p>Additional recruiting categories can be added as your needs grow.</p>
      </div>
{practice_html()}
    </div>
  </section>

{DOORS}

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="kicker">Why Express Recruiting Group</span>
        <h2>Backed by Express Network. Focused on legal.</h2>
      </div>
      <div class="grid-auto">
{why_html()}
      </div>
    </div>
  </section>"""
    written.append(build("index.html",
                     "Legal Talent. Delivered. | Express Recruiting Group",
                     "The legal recruiting division of Express Network. Placing attorneys, paralegals and legal operations staff with law firms nationwide since 1985.",
                     home, active="index.html",
                     ogtitle="Legal Talent. Delivered. | Express Recruiting Group"))

    # --------------------------------------------------------------- ABOUT
    about = page_hero("About", "The legal recruiting division of Express Network",
                      "Created to bring four decades of legal-industry infrastructure to a new service: legal talent acquisition.") + f"""

  <section class="section">
    <div class="wrap split-2">
      <div class="prose">
        <span class="eyebrow eyebrow--light">Who We Are</span>
        <h2>Not an outside agency learning the industry.</h2>
        <p>Express Recruiting Group is the legal recruiting division of Express Network &mdash; not a partner, not an affiliate, and not a separate company. We operate inside the same organization, with the same infrastructure and the same relationships Express Network has built since 1985.</p>
        <p>That matters because law firm hiring is not generic hiring. Understanding how a litigation practice actually runs &mdash; how intake works, what a case manager carries, why an operations director makes or breaks a growing firm &mdash; is the difference between filling a seat and making a placement that holds.</p>
        <h3>Our specialization</h3>
        <p>Every search we run is legal. We recruit attorneys across commercial litigation, employment, personal injury, plaintiff-side, defense and corporate practices, and we recruit the legal support and management professionals who keep those practices running.</p>
        <h3>Nationwide capability</h3>
        <p>Eight offices across five states, with established relationships in each legal community. A search in Phoenix draws on the same network as a search in New York.</p>
      </div>
      <div class="media"><img src="https://images.unsplash.com/photo-1497366216548-37526070297c?auto=format&fit=crop&w=800&q=80" alt="Express Network office environment" loading="lazy"></div>
    </div>
  </section>

  <section class="section section--powder">
    <div class="wrap">
      <div class="section-head">
        <span class="kicker">Express Network</span>
        <a class="en-mark" href="https://www.expressnetwork.com" rel="noopener" style="display:inline-block;margin-bottom:16px"><img src="assets/img/express-network.png" alt="Express Network — a legal support network company"></a>
        <h2>Four decades serving the legal industry</h2>
        <p>Express Recruiting Group inherits this history &mdash; it does not have to build it.</p>
      </div>
      <div class="stat-grid stat-grid--4">
        <div class="stat"><div class="stat__n">1985</div><div class="stat__l">Express Network founded</div></div>
        <div class="stat"><div class="stat__n">8</div><div class="stat__l">Offices nationwide</div></div>
        <div class="stat"><div class="stat__n">~117</div><div class="stat__l">U.S.-based full-time employees &mdash; to be confirmed</div></div>
        <div class="stat"><div class="stat__n">40+</div><div class="stat__l">Years serving the legal industry</div></div>
      </div>
      <div class="video-frame">
        <div class="video-ph">
          <span class="ring">{PLAY}</span>
          <strong>Express Network company video</strong>
          <em>Embedded from expressnetwork.com/about-us &mdash; placeholder in this concept</em>
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="kicker">Why Express Recruiting Group</span>
        <h2>What separates us from an independent agency</h2>
      </div>
      <div class="grid-auto">
{why_html()}
      </div>
    </div>
  </section>

{marquee_html()}"""
    written.append(build("about.html",
                     "About Us | Express Recruiting Group",
                     "Not an outside agency. Express Recruiting Group operates inside Express Network, with four decades of legal-industry infrastructure behind it.",
                     about, active="about.html",
                     ogtitle="About Express Recruiting Group", jsonld=breadcrumb_ld([("Home", ''), ("About", None)])))

    # ------------------------------------------------------------ EMPLOYER
    employer = page_hero("Employers", "Fast-Track Your Search for Legal Talent",
                         "Submit your hiring needs and let our recruiting team get to work — backed by Express Network's nationwide reach and four decades of legal industry relationships.") + f"""

  <section class="section">
    <div class="wrap split-2 split-2--top">
      <div class="prose">
        <span class="eyebrow eyebrow--light">How It Works</span>
        <h2>A search that starts with understanding the role</h2>
        <p>Before we present a single candidate, we scope the role with you &mdash; the practice, the team, the caseload, and the kind of person who actually succeeds in your firm. That conversation is why our placements hold.</p>
        <h3>What you get</h3>
        <ul class="checklist">
          <li>A named recruiter who owns your search end to end</li>
          <li>Candidates screened for cultural fit, not just credentials</li>
          <li>Access to Express Network's nationwide legal community</li>
          <li>Attorneys through legal support and operations, from one partner</li>
        </ul>
        <p style="margin-top:32px"><strong>Prefer to talk first?</strong> Call <a href="{TEL}" class="inline-link">{PHONE}</a> or <a href="contact.html" class="inline-link">book a call</a>.</p>
      </div>

      <div class="form-card">
        <h2 style="font-size:1.3rem;font-weight:800;margin-bottom:8px">Submit a hiring need</h2>
        <p style="color:var(--muted-slate);font-size:.94rem;margin-bottom:24px">We'll come back to you within one business day.</p>
        <form data-concept>
          <div class="form-row">
            <div class="field"><label for="e-name">Name <span class="req" aria-hidden="true">*</span></label><input id="e-name" name="name" required></div>
            <div class="field"><label for="e-firm">Law Firm <span class="req" aria-hidden="true">*</span></label><input id="e-firm" name="firm" required></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="e-email">Email <span class="req" aria-hidden="true">*</span></label><input id="e-email" type="email" name="email" required></div>
            <div class="field"><label for="e-phone">Phone <span class="opt">(optional)</span></label><input id="e-phone" type="tel" name="phone"></div>
          </div>
          <div class="field"><label for="e-title">Position Title <span class="req" aria-hidden="true">*</span></label><input id="e-title" name="title" required></div>
          <div class="form-row">
            <div class="field"><label for="e-area">Practice Area</label>
              <select id="e-area" name="area">
                <option>Commercial Litigation</option><option>Employment</option><option>Personal Injury</option>
                <option>Plaintiff-Side</option><option>Defense</option><option>Corporate</option>
                <option>Legal Support &amp; Management</option><option>Other</option>
              </select></div>
            <div class="field"><label for="e-loc">Location</label><input id="e-loc" name="location" placeholder="City, State or Remote"></div>
          </div>
          <div class="field"><label for="e-salary">Salary Range <span class="opt">(optional)</span></label><input id="e-salary" name="salary"></div>
          <div class="field"><label for="e-desc">Brief Description / Hiring Needs</label><textarea id="e-desc" name="description"></textarea></div>
          <button class="btn btn--primary btn--block" type="submit">Start Your Search</button>
          <p class="spam-note">Protected by an invisible challenge. No CAPTCHA puzzle.</p>
        </form>
      </div>
    </div>
  </section>

  <section class="section section--powder">
    <div class="wrap">
      <div class="section-head">
        <span class="kicker">Client Success Stories</span>
        <h2>Successful placements. Stronger legal teams.</h2>
      </div>
      <div class="grid-3">
{stories_html()}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="kicker">Why Express Recruiting Group</span>
        <h2>Backed by Express Network. Focused on legal.</h2>
      </div>
      <div class="grid-auto">
{why_html()}
      </div>
    </div>
  </section>"""
    written.append(build("hire-legal-talent.html",
                     "Hire Legal Talent | Express Recruiting Group",
                     "Submit a hiring need and get a named recruiter, candidates screened for cultural fit, and the nationwide reach of Express Network behind your search.",
                     employer, active="hire-legal-talent.html",
                     ogtitle="Fast-Track Your Search for Legal Talent", jsonld=breadcrumb_ld([("Home", ''), ("Employers", None)])))

    # ----------------------------------------------------------- CANDIDATE
    candidate = page_hero("Candidates", "Looking for Your Next Legal Opportunity?",
                          "Your search stays private. Your next opportunity starts here.") + f"""

  <section class="section">
    <div class="wrap split-2 split-2--top">
      <div>
{CONFIDENTIAL}
        <div class="prose">
          <h2 style="font-size:1.3rem">How we represent you</h2>
          <p>You will always know which firm your materials are going to before they go. No blind submissions, no resume blasting, and no conversation with your current employer &mdash; ever.</p>
          <p>We recruit across attorney roles and legal support and management positions, in eight markets nationwide. If the right role isn't open today, we'll tell you that too.</p>
          <p style="margin-top:32px"><a href="opportunities.html" class="inline-link">Browse current opportunities &rarr;</a></p>
        </div>
      </div>

      <div class="form-card">
        <h2 style="font-size:1.3rem;font-weight:800;margin-bottom:8px">Submit your resume</h2>
        <p style="color:var(--muted-slate);font-size:.94rem;margin-bottom:24px">Confidential. Reviewed by a recruiter, not an algorithm.</p>
        <form data-concept>
          <div class="form-row">
            <div class="field"><label for="c-name">Name <span class="req" aria-hidden="true">*</span></label><input id="c-name" name="name" required></div>
            <div class="field"><label for="c-email">Email <span class="req" aria-hidden="true">*</span></label><input id="c-email" type="email" name="email" required></div>
          </div>
          <div class="field"><label for="c-phone">Phone <span class="opt">(optional)</span></label><input id="c-phone" type="tel" name="phone"></div>
          <div class="form-row">
            <div class="field"><label for="c-current">Current Position</label><input id="c-current" name="current"></div>
            <div class="field"><label for="c-desired">Desired Position</label><input id="c-desired" name="desired"></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="c-area">Practice Area</label>
              <select id="c-area" name="area">
                <option>Commercial Litigation</option><option>Employment</option><option>Personal Injury</option>
                <option>Plaintiff-Side</option><option>Defense</option><option>Corporate</option>
                <option>Legal Support &amp; Management</option><option>Other</option>
              </select></div>
            <div class="field"><label for="c-loc">Location</label><input id="c-loc" name="location" placeholder="City, State or Remote"></div>
          </div>
          <div class="form-row">
            <div class="field"><label for="c-comp">Desired Compensation <span class="opt">(optional)</span></label><input id="c-comp" name="compensation"></div>
            <div class="field"><label for="c-li">LinkedIn Profile <span class="opt">(optional)</span></label><input id="c-li" type="url" name="linkedin" placeholder="https://"></div>
          </div>
          <div class="field">
            <label for="c-resume">Resume <span class="req" aria-hidden="true">*</span></label>
            <label class="upload" data-upload for="c-resume">
              <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><path d="M7 10l5-5 5 5"/><path d="M12 5v12"/></svg>
              <strong data-upload-label>Drop your resume here, or browse</strong>
              <span>PDF, DOC or DOCX &middot; 10&nbsp;MB maximum</span>
              <input id="c-resume" type="file" name="resume" accept=".pdf,.doc,.docx" hidden required>
            </label>
            <p class="field__help">Stored outside this website, scanned on upload, and never written to a public directory.</p>
          </div>
          <div class="field"><label for="c-notes">Additional comments <span class="opt">(optional)</span></label><textarea id="c-notes" name="notes"></textarea></div>
          <button class="btn btn--primary btn--block" type="submit">Submit Your Resume Confidentially</button>
          <p class="spam-note">Protected by an invisible challenge. No CAPTCHA puzzle.</p>
        </form>
      </div>
    </div>
  </section>

  <section class="section section--powder">
    <div class="wrap">
      <div class="section-head">
        <span class="kicker">Legal Recruiting Positions</span>
        <h2>Roles we place</h2>
      </div>
{practice_html()}
    </div>
  </section>"""
    written.append(build("find-a-position.html",
                     "Find a Legal Position | Express Recruiting Group",
                     "Your search stays private. Submit your resume confidentially to a recruiter who never contacts your current employer or shares your name unapproved.",
                     candidate, active="find-a-position.html",
                     ogtitle="Looking for Your Next Legal Opportunity?", jsonld=breadcrumb_ld([("Home", ''), ("Candidates", None)])))

    # ------------------------------------------------------- OPPORTUNITIES
    role_items = []
    for title, area, area_label, loc, sen, posted, is_new in ROLES:
        tag = '<span class="tag tag--new">New</span>' if is_new else '<span class="tag">Open</span>'
        role_items.append(f"""          <li>
            <a class="role" href="opportunity-detail.html" data-area="{area}">
              <div class="role__top"><span class="role__area">{area_label}</span>{tag}</div>
              <h3>{title}</h3>
              <div class="role__meta"><span>{loc}</span><i></i><span>{sen}</span><i></i><span>Posted {posted}</span></div>
            </a>
          </li>""")
    opportunities = page_hero("Positions", "Current Opportunities",
                              "Open legal roles across eight nationwide markets. New positions are added weekly.") + f"""

  <section class="section">
    <div class="wrap">
      <div class="filters" role="group" aria-label="Filter by practice area">
        <button class="chip" data-filter="all" aria-pressed="true">All positions</button>
        <button class="chip" data-filter="litigation" aria-pressed="false">Litigation</button>
        <button class="chip" data-filter="employment" aria-pressed="false">Employment</button>
        <button class="chip" data-filter="corporate" aria-pressed="false">Corporate</button>
        <button class="chip" data-filter="support" aria-pressed="false">Legal Support</button>
      </div>
      <p style="color:var(--muted-slate);font-size:.94rem;margin-bottom:24px"><strong data-result-count>{len(ROLES)} positions</strong> &mdash; placeholder listings for concept purposes.</p>
      <h2 class="vh">Open positions</h2>
      <ul class="role-list grid-auto">
{chr(10).join(role_items)}
      </ul>

      <div class="callout">
        <h2>Don't see the right role?</h2>
        <p>Most of our placements never get posted. Submit your resume confidentially and we'll reach out when something fits.</p>
        <a class="btn btn--primary" href="find-a-position.html">Submit Your Resume Confidentially</a>
      </div>
    </div>
  </section>"""
    written.append(build("opportunities.html",
                     "Current Legal Job Openings | Express Recruiting Group",
                     "Browse open attorney, paralegal and legal operations roles across eight nationwide markets. Most placements are never posted, so submit your resume.",
                     opportunities, active="opportunities.html",
                     ogtitle="Current Opportunities", jsonld=breadcrumb_ld([("Home", ''), ("Positions", None)])))

    # ------------------------------------------------------- ROLE DETAIL
    detail = f"""  <section class="page-hero on-navy">
    <div class="wrap">
      <nav class="breadcrumb" aria-label="Breadcrumb"><a href="index.html">Home</a><span>/</span><a href="opportunities.html">Positions</a><span>/</span>Commercial Litigation Associate</nav>
      <span class="eyebrow">Commercial Litigation</span>
      <h1>Commercial Litigation Associate</h1>
      <p>Los Angeles, CA &middot; 4&ndash;6 years &middot; Posted 2 days ago</p>
    </div>
  </section>

  <section class="section">
    <div class="wrap split-2 split-2--top split-2--wide">
      <div class="prose">
        <h2 style="font-size:1.3rem">About the role</h2>
        <p>A well-established regional litigation practice is adding an associate to its commercial disputes team. The role carries a genuine caseload from day one, with first-chair opportunities on smaller matters within the first year.</p>
        <h3>What the firm is looking for</h3>
        <ul class="checklist">
          <li>4&ndash;6 years of commercial litigation experience at a firm of comparable size</li>
          <li>Substantive motion practice and deposition experience</li>
          <li>California bar admission in good standing</li>
          <li>Comfort working directly with clients early</li>
        </ul>
        <h3>Compensation</h3>
        <p>Competitive base with a performance bonus structure. Full range shared in first conversation.</p>
        <p style="font-size:.88rem;color:var(--muted-slate);border-top:1px solid var(--hairline);padding-top:20px;margin-top:32px">Placeholder listing created for design evaluation. Not a live position.</p>
      </div>

      <aside class="form-card sticky-aside">
        <h2 style="font-size:1.15rem;font-weight:800;margin-bottom:8px">Apply confidentially</h2>
        <p style="color:var(--muted-slate);font-size:.94rem;margin-bottom:20px">We never contact your current employer.</p>
        <a class="btn btn--primary btn--block" href="find-a-position.html" style="margin-bottom:12px">Submit Your Resume</a>
        <a class="btn btn--ghost btn--block" href="contact.html">Speak With a Recruiter</a>
        <div class="spec">
          <div class="method__k">Role details</div>
          <dl>
            <div style="display:flex;justify-content:space-between;gap:16px"><dt style="color:var(--muted-slate)">Practice</dt><dd style="font-weight:600">Commercial Litigation</dd></div>
            <div style="display:flex;justify-content:space-between;gap:16px"><dt style="color:var(--muted-slate)">Location</dt><dd style="font-weight:600">Los Angeles, CA</dd></div>
            <div style="display:flex;justify-content:space-between;gap:16px"><dt style="color:var(--muted-slate)">Experience</dt><dd style="font-weight:600">4&ndash;6 years</dd></div>
            <div style="display:flex;justify-content:space-between;gap:16px"><dt style="color:var(--muted-slate)">Type</dt><dd style="font-weight:600">Full time</dd></div>
          </dl>
        </div>
      </aside>
    </div>
  </section>"""
    written.append(build("opportunity-detail.html",
                     "Commercial Litigation Associate | Los Angeles, CA",
                     "Commercial Litigation Associate in Los Angeles. 4-6 years' experience, substantive motion practice, first-chair opportunity in year one. Apply confidentially.",
                     detail, active="opportunities.html",
                     ogtitle="Commercial Litigation Associate — Los Angeles, CA", jsonld=breadcrumb_ld([("Home", ''), ("Positions", 'opportunities.html'), ("Commercial Litigation Associate", None)]) + JOB_LD))

    # ------------------------------------------------------------ OUR TEAM
    people = "\n".join(f"""        <article class="person">
          <img src="{img}" alt="" loading="lazy">
          <div class="person__body">
            <div class="person__name">{name}</div>
            <div class="person__title">{title}</div>
            <p class="person__bio">{bio}</p>
            <a class="person__li" href="#"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5a2.5 2.5 0 1 0 0 5 2.5 2.5 0 0 0 0-5ZM3 9h4v12H3zM10 9h3.8v1.7h.05a4.2 4.2 0 0 1 3.75-2c4 0 4.75 2.6 4.75 6V21h-4v-5.3c0-1.3 0-2.9-1.8-2.9s-2.05 1.4-2.05 2.8V21h-4z"/></svg>LinkedIn</a>
          </div>
        </article>""" for img, name, title, bio in TEAM)

    team = page_hero("Our Team", "The recruiters behind your search",
                     "A named recruiter owns every search end to end. You will always know who is representing you.") + f"""

  <section class="section">
    <div class="wrap">
      <div class="grid-auto">
{people}
      </div>
      <p class="panel-note">Placeholder team members shown for design purposes. Photos, names and biographies to be confirmed before publication.</p>
    </div>
  </section>

  <section class="section section--powder">
    <div class="wrap split-2">
      <div class="prose">
        <span class="eyebrow eyebrow--light">Working With Us</span>
        <h2>One recruiter, start to finish</h2>
        <p>You will not be handed between coordinators, and you will not repeat your situation to three people. The recruiter who scopes your search is the recruiter who runs it.</p>
        <p>That is only possible because of what sits behind us &mdash; Express Network's infrastructure handles the operational weight so our recruiters stay on the searches themselves.</p>
        <a class="btn btn--primary" href="contact.html">Connect With a Recruiter</a>
      </div>
      <div class="media"><img src="https://images.unsplash.com/photo-1600880292203-757bb62b4baf?auto=format&fit=crop&w=800&q=80" alt="Recruiting team in conversation" loading="lazy"></div>
    </div>
  </section>"""
    written.append(build("our-team.html",
                     "Our Recruiting Team | Express Recruiting Group",
                     "Meet the recruiters behind your search. One named recruiter owns every search end to end, backed by Express Network's nationwide infrastructure.",
                     team, active="our-team.html",
                     ogtitle="The Recruiters Behind Your Search", jsonld=breadcrumb_ld([("Home", ''), ("Our Team", None)])))

    # ------------------------------------------------------------- CONTACT
    contact = page_hero("Contact", "Let's talk",
                        "Whether you're hiring or looking, the fastest route is a conversation.") + f"""

  <section class="section">
    <div class="wrap split-2 split-2--top">
      <div>
        <div class="prose">
          <span class="eyebrow eyebrow--light">Get In Touch</span>
          <h2>Three ways to reach us</h2>
        </div>
        <div class="stack" style="margin-top:24px">
          <div class="method">
            <div class="method__k">Call</div>
            <a class="method__big" href="{TEL}">{PHONE}</a>
            <p>Monday to Friday, 8am&ndash;6pm across all eight markets.</p>
          </div>
          <div class="method">
            <div class="method__k">Book a call</div>
            <p style="margin-bottom:16px">Pick a time that works. Opens in place &mdash; you won't lose this page.</p>
            <a class="btn btn--primary" href="#book">Open Scheduler</a>
            <p>Calendly embed &mdash; placeholder in this concept.</p>
          </div>
          <div class="method">
            <div class="method__k">Offices</div>
            <p>Eight locations across five states, through Express Network. <a href="https://www.expressnetwork.com/offices" rel="noopener" class="inline-link">View all offices &rarr;</a></p>
          </div>
        </div>
      </div>

      <div class="form-card">
        <h2 style="font-size:1.3rem;font-weight:800;margin-bottom:8px">Send us a message</h2>
        <p style="color:var(--muted-slate);font-size:.94rem;margin-bottom:24px">We reply within one business day.</p>
        <form data-concept>
          <div class="field"><label for="k-who">I am a&hellip;</label>
            <select id="k-who" name="who"><option>Law firm looking to hire</option><option>Candidate looking for a position</option><option>Something else</option></select>
          </div>
          <div class="form-row">
            <div class="field"><label for="k-name">Name <span class="req" aria-hidden="true">*</span></label><input id="k-name" name="name" required></div>
            <div class="field"><label for="k-email">Email <span class="req" aria-hidden="true">*</span></label><input id="k-email" type="email" name="email" required></div>
          </div>
          <div class="field"><label for="k-phone">Phone <span class="opt">(optional)</span></label><input id="k-phone" type="tel" name="phone"></div>
          <div class="field"><label for="k-msg">Message <span class="req" aria-hidden="true">*</span></label><textarea id="k-msg" name="message" required></textarea></div>
          <button class="btn btn--primary btn--block" type="submit">Send Message</button>
          <p class="spam-note">Protected by an invisible challenge. No CAPTCHA puzzle.</p>
        </form>
      </div>
    </div>
  </section>"""
    written.append(build("contact.html",
                     "Contact Us | Express Recruiting Group",
                     "Call (800) 555-0188, book a call, or send a message to the legal recruiting division of Express Network, whether you are hiring or looking.",
                     contact, active="contact.html",
                     ogtitle="Let's Talk | Express Recruiting Group", jsonld=breadcrumb_ld([("Home", ''), ("Contact", None)])))

    return written
