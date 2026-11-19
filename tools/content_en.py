# English text of lamscapital.com (root of the site). European positioning.

NAV = {
    "nis2": "NIS2 compliance", "packages": "Packages", "aws": "Buy via AWS", "funding": "EU funding",
    "privacy": "Privacy", "terms": "Terms", "contact": "Contact", "switch": "RO",
    "menu": "Menu", "aria": "Main", "foot_aria": "Site", "skip": "Skip to content",
}

FOOT_LEGAL = "© 2026 LAMS Capital Invest LLC."

FORM = {
    "title": "Start a conversation.",
    "intro": "Tell us briefly about your company and the decision ahead. We reply within two business days, and every conversation is treated as confidential.",
    "subject": "New enquiry from lamscapital.com (EN)",
    "name": "Name", "company": "Company", "email": "Work email", "country": "Country",
    "size": "Employees", "size_opts": ["50–249", "10–49", "250 or more", "Fewer than 10"],
    "topic": "Main interest", "topic_opts": ["NIS2 compliance", "ERP and e-invoicing", "Automation and AI", "E-commerce integration", "Strategic diagnostic", "EU funding", "Something else"],
    "message": "What would you like to discuss?",
    "consent": "I agree to receive occasional emails from LAMS about NIS2, digitalisation and funding. I can withdraw this consent at any time.",
    "privacy": 'We use your details only to answer this enquiry. See our <a href="/privacy/">privacy notice</a>.',
    "send": "Send message",
    "alt": 'Or write to <a href="mailto:info@lamscapital.com">info@lamscapital.com</a>',
}


def pages(P):
    home = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">For mid-sized manufacturers and distributors in Europe</p>
    <h1>NIS2 compliance, digital operations and software, from <span class="accent">one accountable partner</span>.</h1>
    <p class="lead">We start with the cybersecurity obligations your company now carries under EU law, then bring operations, e-invoicing and automation into a single plan. For companies across the European Union, with local delivery in Romania.</p>
    <div class="btn-row"><a class="btn primary" href="{P['nis2']['en']}#check">Check if NIS2 applies to you</a><a class="btn" href="{P['packages']['en']}">See the packages</a></div>
  </div>
</section>

<section class="band" aria-label="How we commit">
  <div class="wrap band-grid">
    <div><b>6–8 weeks</b><span>from NIS2 scoping to an audit-ready file</span></div>
    <div><b>One contract</b><span>for compliance, software and support</span></div>
    <div><b>Every month</b><span>a written report, timesheet and sign-off</span></div>
    <div><b>2 business days</b><span>to answer any enquiry, under NDA</span></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="label">Why now</p>
    <div class="facts">
      <div><b>Up to €10 million</b><span>or 2% of worldwide turnover: the ceiling for fines on essential entities under the NIS2 Directive. For important entities: €7 million or 1.4%.</span></div>
      <div><b>Management is accountable</b><span>Boards must approve cybersecurity measures, oversee them and take training. Responsibility cannot be delegated to IT alone.</span></div>
      <div><b>24 hours</b><span>to send an early warning to the authority after a significant incident, 72 hours for the notification and one month for the final report.</span></div>
    </div>
    <p class="source">Source: Directive (EU) 2022/2555 (NIS2), Articles 20, 23 and 34. National laws set the details; in Romania, fines have been applied since September 2026.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="label">Questions we help answer</p>
    <ol class="q-list">
      <li><span>01</span>Does NIS2 apply to our company, and what do we have to file, and by when?</li>
      <li><span>02</span>If the authority audited us tomorrow, what would management have to show?</li>
      <li><span>03</span>How do we stop re-typing orders and invoices between spreadsheets, the warehouse and accounting?</li>
      <li><span>04</span>What should we automate first, and what does it save us each month?</li>
      <li><span>05</span>Our largest client sent us a security questionnaire. What do we answer, and what do we need to prove it?</li>
      <li><span>06</span>Can EU funding cover part of the investment without putting the project at risk?</li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Fixed-scope packages, each with a clear scope and result.</h2>
      <p>Compliance opens the door; the operational work is where the savings come from. Every package can run on its own or as part of one plan.</p>
    </div>
    <div class="pk-grid">
      <div class="pk feature"><span class="tag">Package C</span><h3>NIS2 Compliant</h3><p>Scoping, risk analysis, written policies, incident procedure and audit preparation, with monthly follow-up.</p><p class="price"><a class="more" href="#contact">Request an offer →</a></p></div>
      <div class="pk"><span class="tag">Package A</span><h3>Operations &amp; e-invoicing</h3><p>Stock, sales and purchasing on Odoo, connected to accounting and to national e-invoicing.</p><p class="price"><a class="more" href="#contact">Request an offer →</a></p></div>
      <div class="pk"><span class="tag">Package B</span><h3>ERP &amp; operational transformation</h3><p>Full strategic diagnostic, then ERP and automation across the business. Suited to funded projects.</p><p class="price"><a class="more" href="#contact">Request an offer →</a></p></div>
      <div class="pk"><span class="tag">Package D</span><h3>Automation &amp; AI</h3><p>A discovery workshop, then one automation or AI assistant delivered in about four weeks.</p><p class="price"><a class="more" href="#contact">Request an offer →</a></p></div>
      <div class="pk"><span class="tag">Package E</span><h3>E-commerce integration</h3><p>Marketplace feeds, stock synchronisation and automatic e-invoicing for online sellers.</p><p class="price"><a class="more" href="#contact">Request an offer →</a></p></div>
      <div class="pk"><span class="tag">Advisory</span><h3>Strategic diagnostic</h3><p>Five weeks, seven deliverables: margins, markets, channels and a 12-month plan, built on your own numbers.</p><p class="price"><a class="more" href="{P['packages']['en']}">All packages and details →</a></p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="label">Who we work with</p>
    <div class="cl-grid">
      <h3>Manufacturers and distributors with 50–249 employees, in the sectors covered by NIS2.</h3>
      <div class="sectors">
        <div><b>Food and beverage</b><span>Production, processing and distribution</span></div>
        <div><b>Manufacturing</b><span>Machinery, electrical equipment, vehicles and parts, electronics</span></div>
        <div><b>Transport and courier</b><span>Road transport, logistics and postal services</span></div>
        <div><b>Chemicals and wholesale</b><span>Production and distribution of chemicals, wholesale trade</span></div>
      </div>
    </div>
  </div>
</section>

<section class="night">
  <div class="wrap">
    <div>
      <p class="label">How we work</p>
      <h2>Diagnose first. Then one plan, one team.</h2>
    </div>
    <div>
      <p>Strategy, compliance and software are delivered by one team under one contract. A dedicated development team in Europe, coordinated by us, builds and maintains the software; we stay accountable to you for the result.</p>
      <div class="steps">
        <div><b>Diagnose</b><span>Fixed-scope review of obligations, operations and numbers.</span></div>
        <div><b>Plan</b><span>Prioritised measures with owners, deadlines and a budget.</span></div>
        <div><b>Implement</b><span>Policies, software and integrations, delivered in short stages with sign-off.</span></div>
        <div><b>Support</b><span>A monthly subscription keeps compliance and systems up to date.</span></div>
      </div>
      <p style="margin-top:28px"><a href="{P['aws']['en']}">You can also buy through AWS Marketplace →</a></p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:88px">
  <div class="wrap">
    <p class="label">Principles</p>
    <div class="cols3">
      <div><h3>Transparent</h3><p>We sell advisory and software, and say so upfront. The diagnostic also tells you what is not worth buying, including from us.</p></div>
      <div><h3>Confidential</h3><p>A non-disclosure agreement is signed before any information is shared, and each client's data is kept separate and used only for that client's work.</p></div>
      <div><h3>Accountable</h3><p>One team, one plan and one set of measures, from diagnosis to delivery, with written sign-off at every stage.</p></div>
    </div>
  </div>
</section>"""

    nis2 = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">Package C · NIS2 Compliant</p>
    <h1>Know where you stand under NIS2, and be <span class="accent">ready for an audit</span>.</h1>
    <p class="lead">The EU NIS2 Directive brings thousands of mid-sized companies under cybersecurity law for the first time. We establish whether it applies to you, prepare what the authority requires, and keep it current every month.</p>
    <div class="btn-row"><a class="btn primary" href="#check">Check in 1 minute</a><a class="btn" href="{P['packages']['en']}">All packages</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Does NIS2 apply to your company?</h2>
      <p>Probably yes, if both of these are true. The exact answer depends on your activity codes, your group structure and the national law.</p>
    </div>
    <ul class="ticks">
      <li><b>Size:</b> at least 50 employees, or annual turnover above €10 million (medium-sized and larger companies).</li>
      <li><b>Sector:</b> you operate in a sector listed by the directive, for example food production and distribution, manufacturing of machinery, electrical equipment, electronics, vehicles or medical devices, chemicals, transport, postal and courier services, or waste management.</li>
      <li><b>Some smaller companies</b> are also covered, regardless of size, when a member state designates them as critical.</li>
      <li><b>Through your clients:</b> companies covered by NIS2 must manage the security of their supply chain. Even if the law does not cover you directly, expect security questionnaires, audits and contract clauses from your largest clients. Without answers, contracts are at risk.</li>
    </ul>
    <p class="note"><b>Full scoping check, free of charge.</b> Send us your company name and registration number. Within two business days we tell you whether NIS2 applies, whether you would be an essential or an important entity, and which deadlines you face.</p>
  </div>
</section>
<!--CHECKER-->

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>What the law asks of you</h2>
      <p>The directive sets the minimum; each member state adds its own procedure and deadlines.</p>
    </div>
    <div class="cols2">
      <div><h3>Register and assess</h3><p>Register with the national cybersecurity authority, then assess your risk level and the maturity of your security measures within the deadlines the authority sets.</p></div>
      <div><h3>Manage risk</h3><p>Put in place measures that fit your risk: policies, access control, backups and recovery, supplier security, encryption, staff training and business continuity.</p></div>
      <div><h3>Report incidents</h3><p>Early warning within 24 hours of a significant incident, notification within 72 hours and a final report within one month.</p></div>
      <div><h3>Involve management</h3><p>Management approves the measures, oversees them and follows cybersecurity training. Breaches can lead to fines and to measures against the people in charge.</p></div>
    </div>
  </div>
</section>

<section class="night">
  <div class="wrap">
    <div>
      <p class="label">What we deliver</p>
      <h2>Six to eight weeks, from scoping to an audit-ready file.</h2>
    </div>
    <div>
      <div class="steps">
        <div><b>Scoping</b><span>Activity codes, size and group checked against the law, with a source for every figure.</span></div>
        <div><b>Inventory and risk</b><span>Register of systems, data and critical suppliers; risk register with owners and deadlines.</span></div>
        <div><b>Self-assessment</b><span>Prepared on evidence, not on declarations, in the authority's format.</span></div>
        <div><b>Policies</b><span>A full set of written policies, adapted to your company and approved by management.</span></div>
        <div><b>Incident procedure</b><span>Who decides, who notifies the authority, and pre-filled templates for 24 hours, 72 hours and one month.</span></div>
        <div><b>Audit preparation</b><span>A remediation plan for 3, 6 and 12 months and a complete file for the external auditor.</span></div>
      </div>
      <p style="margin-top:28px"><b style="color:var(--paper);font-weight:500">Then a monthly subscription</b> for the compliance tool, quarterly risk review, policy updates when the law changes and support when you report an incident.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:88px">
  <div class="wrap">
    <div class="section-head">
      <h2>Where we stop</h2>
      <p>So there are no surprises in the offer.</p>
    </div>
    <ul class="ticks">
      <li>Where the law requires an external audit, it is carried out by an auditor accredited by the national authority. We prepare the audit file and coordinate the audit with you; the auditor is contracted separately, so the audit stays independent.</li>
      <li>We work on evidence and read-only access. We do not ask for administrator access to your systems.</li>
      <li>We do not file with the authority in your name without a written mandate.</li>
    </ul>
    <h2 style="font-size:28px;margin:56px 0 16px">In Romania</h2>
    <p style="color:var(--ink-soft);max-width:46em;margin:0">NIS2 is transposed by Government Emergency Ordinance 155/2024, approved by Law 124/2025, and enforced by the National Cybersecurity Directorate (DNSC). Companies must register within 30 days of falling under the law, and the DNSC began applying fines in September 2026. <a href="{P['nis2']['ro']}" hreflang="ro">Read the Romanian page</a>.</p>
    <p class="source">Sources: Directive (EU) 2022/2555; for Romania, CMS legal updates of 17 July and 26 August 2025 and StartupCafe, 9 September 2026. Checked November 2026; national rules change, so we re-check them for every client.</p>
  </div>
</section>"""

    packages = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">Packages</p>
    <h1>Advisory and software, sold as <span class="accent">fixed-scope packages</span>.</h1>
    <p class="lead">Each package has a defined result, and a schedule agreed before work starts. Advisory opens the project; software and automation deliver the savings; a monthly subscription keeps it running.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    {pkd("Package C", "NIS2 Compliant", "Companies covered by NIS2, typically 50–249 employees.",
         ["Scoping against the law and the national rules", "Asset and risk registers", "Self-assessment prepared on evidence", "Written policies approved by management", "Incident procedure and templates", "Remediation plan and audit file"],
         "6–8 weeks", "From €6,000 + €149/month", "External audit by an accredited auditor is contracted separately.", P['nis2']['en'], "NIS2 details")}
    {pkd("Package A", "Operations &amp; e-invoicing", "Distributors and manufacturers, 10–49 employees.",
         ["Digital audit, included in the package", "Stock, sales and purchasing on Odoo Community (open source, no licence fees)", "Integration with your accounting software", "Connection to national e-invoicing (in Romania: e-Factura)"],
         "Agreed after the audit", "Price on request + monthly support", "", "", "")}
    {pkd("Package B", "ERP &amp; operational transformation", "Companies with 50–249 employees, including projects co-financed by EU funds.",
         ["Full strategic diagnostic: seven deliverables, from margins to a 12-month plan", "ERP and automation across sales, warehouse, production and finance", "Staged delivery with sign-off at each stage", "Monthly support after go-live"],
         "Agreed after the diagnostic", "Price on request + monthly support", "", P['funding']['en'], "How EU funding works")}
    {pkd("Package D", "Automation &amp; AI", "Any company with repetitive work: orders, documents, reporting, customer requests.",
         ["Discovery workshop to pick the process with the best return", "One automation or AI assistant, built and deployed", "Measured before and after, so the saving is visible"],
         "About 4 weeks", "From €7,900 + €190/month", "Monthly support includes the AI usage costs.", "", "")}
    {pkd("Package E", "E-commerce integration", "Online sellers with annual turnover of roughly €0.2–4 million.",
         ["Product feeds to marketplaces", "Stock synchronisation between shop, marketplaces and warehouse", "Automatic e-invoicing"],
         "About 4 weeks", "From €6,900 + €150/month", "", "", "")}
    {pkd("Advisory", "Strategic diagnostic", "Owner-led companies at the point where growth needs structure.",
         ["Five weeks, seven deliverables: performance, market, channels, operations, opportunities, KPIs and a 12-month plan", "Built on your own numbers, under a non-disclosure agreement"],
         "5 weeks", "Price on request", "", "", "")}
    <p class="note"><b>Offers.</b> Every offer is personalised after a 30-minute call and states the full scope, schedule and terms. Odoo is a trademark of Odoo S.A.; LAMS is not affiliated with Odoo S.A.</p>
  </div>
</section>"""

    aws = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">Buying through AWS Marketplace</p>
    <h1>Buy our services through <span class="accent">your company's AWS account</span>.</h1>
    <p class="lead">Besides a direct contract, you can buy any LAMS package as a private offer on AWS Marketplace, the Amazon Web Services catalogue for software and services. Amazon Web Services invoices your company and pays us.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Why companies choose it</h2>
      <p>A private offer is an offer on AWS Marketplace made only for your company, on the terms we agreed.</p>
    </div>
    <div class="cols3">
      <div><h3>A familiar supplier</h3><p>The invoice comes from Amazon Web Services, a supplier your accounting and procurement teams can verify easily.</p></div>
      <div><h3>One place to pay</h3><p>Payment goes through your company's AWS account, by card or bank transfer where available, with the invoices in one place.</p></div>
      <div><h3>Full paperwork</h3><p>Every month you receive an activity report, a timesheet and a handover report that cites the AWS offer and invoice number.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="label">How it works</p>
    <div class="steps light">
      <div><b>1. Agree the work</b><span>We sign a non-disclosure agreement and agree the statement of work: scope, deliverables, schedule and terms.</span></div>
      <div><b>2. Open the account</b><span>If your company has no AWS account, we set it up together in a 30–45 minute online session, in the company's name and with two-step sign-in.</span></div>
      <div><b>3. Accept the offer</b><span>We send the private offer. You accept it in your AWS account; the statement of work is attached to it.</span></div>
      <div><b>4. Delivery</b><span>We deliver in stages. Each month you receive the report, timesheet and handover document to sign.</span></div>
    </div>
    <p class="source">Amazon Web Services, AWS and AWS Marketplace are trademarks of Amazon.com, Inc. or its affiliates. LAMS is an independent seller and is not endorsed by Amazon.</p>
  </div>
</section>"""

    funding = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">EU funding for digitalisation</p>
    <h1>Use EU funding for digitalisation, <span class="accent">without risking the project</span>.</h1>
    <p class="lead">EU cohesion funds 2021–2027 co-finance the digitalisation of small and medium-sized companies through regional programmes. We help you check eligibility and prepare the technical side, and we can deliver the software if we are selected as supplier.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>What we do</h2>
      <p>In Romania, through the regional programmes for SME digitalisation; in other member states, through their national and regional programmes.</p>
    </div>
    <div class="cols3">
      <div><h3>Eligibility</h3><p>We check your activity codes, size and region against the applicant guide, including excluded sectors.</p></div>
      <div><h3>Technical preparation</h3><p>Digital maturity audit, specifications and a realistic software budget, ready for the application.</p></div>
      <div><h3>Implementation</h3><p>If selected as supplier, we deliver the software and the paperwork the funding authority asks for.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="label">Our rules</p>
    <ul class="ticks">
      <li><b>One role per project.</b> In a funded project we are either the consultant or the supplier, never both, as the rules on conflicts of interest require.</li>
      <li><b>No promises of funding.</b> The decision belongs to the managing authority. We tell you honestly whether an application has a chance.</li>
      <li><b>The schedule comes first.</b> Funding calls have fixed windows. We tell you upfront whether the timing works, and what to do if it does not.</li>
    </ul>
    <p style="margin-top:32px"><a href="{P['funding']['ro']}" hreflang="ro">Current calls in Romania (Romanian page) →</a></p>
  </div>
</section>"""

    privacy = """
<section class="section" style="padding-top:56px">
  <div class="wrap legal">
    <h1>Privacy notice</h1>
    <p class="meta">Last updated: 19 November 2026</p>
    <h2>Who we are</h2>
    <p>LAMS Capital Invest LLC, 30 N Gould St, Ste R, Sheridan, WY 82801, USA, is the controller of the personal data described here. Contact: <a href="mailto:info@lamscapital.com">info@lamscapital.com</a>.</p>
    <h2>What we collect and why</h2>
    <div class="table-scroll"><table>
      <tr><th>Data</th><th>Purpose</th><th>Legal basis (GDPR)</th><th>Kept for</th></tr>
      <tr><td>Name, company, work email, country, company size, interest, message</td><td>Answering your enquiry and preparing an offer</td><td>Steps taken at your request before a contract, Art. 6(1)(b)</td><td>24 months after the last contact, unless a contract follows</td></tr>
      <tr><td>Your consent to receive emails, with date and time</td><td>Sending occasional information about NIS2, digitalisation and funding</td><td>Consent, Art. 6(1)(a)</td><td>Until you withdraw consent, then as proof for 3 years</td></tr>
      <tr><td>Technical data (IP address, browser) in the hosting provider's logs</td><td>Security and operation of the website</td><td>Legitimate interest, Art. 6(1)(f)</td><td>As set by the hosting provider</td></tr>
    </table></div>
    <p>The site uses no analytics, no advertising cookies and no tracking. Fonts are served from our own site.</p>
    <h2>Who processes the data for us</h2>
    <ul>
      <li>GitHub, Inc. (website hosting, GitHub Pages), USA.</li>
      <li>FormSubmit (delivery of the contact form to our mailbox).</li>
      <li>Zoho Corporation (our email service).</li>
    </ul>
    <p>Some of these providers process data outside the European Economic Area, including in the USA. Such transfers rely on the safeguards the providers offer, such as the EU–US Data Privacy Framework or the European Commission's standard contractual clauses.</p>
    <h2>Your rights</h2>
    <p>You may ask for access to, correction or deletion of your data, restriction of processing, data portability, and object to processing based on legitimate interest. You may withdraw consent at any time by writing to <a href="mailto:info@lamscapital.com">info@lamscapital.com</a> or by using the unsubscribe link in any email; withdrawal does not affect earlier processing. You may also complain to the data protection authority in your country; in Romania, the National Supervisory Authority for Personal Data Processing (ANSPDCP).</p>
    <h2>Client data</h2>
    <p>Data you share during an engagement is covered by the non-disclosure agreement and, where personal data is involved, by a separate data processing agreement under Article 28 GDPR.</p>
  </div>
</section>"""

    terms = """
<section class="section" style="padding-top:56px">
  <div class="wrap legal">
    <h1>Terms of use</h1>
    <p class="meta">Last updated: 19 November 2026</p>
    <h2>Operator</h2>
    <p>This website is operated by LAMS Capital Invest LLC, 30 N Gould St, Ste R, Sheridan, WY 82801, USA, <a href="mailto:info@lamscapital.com">info@lamscapital.com</a>.</p>
    <h2>Information only</h2>
    <p>The content of this site is general information. It is not legal, tax or security advice for your situation, and it does not make LAMS your adviser. Summaries of laws and funding rules reflect our reading on the date shown and may change.</p>
    <h2>Offers</h2>
    <p>This site does not make offers. A binding commitment exists only in a signed contract or an accepted private offer on AWS Marketplace, together with its statement of work.</p>
    <h2>Intellectual property</h2>
    <p>Texts, the LAMS name and logo and the design of this site belong to LAMS Capital Invest LLC. Other names and marks belong to their owners; mentioning them does not imply a partnership or endorsement.</p>
    <h2>Liability</h2>
    <p>We take care to keep the site accurate and available, but we do not guarantee that it is error-free or always online. To the extent the law allows, we are not liable for decisions taken solely on the basis of this site.</p>
  </div>
</section>"""

    return {
        "home": ("LAMS · NIS2 compliance, digital operations and software",
                 "NIS2 compliance, ERP, e-invoicing, automation and AI for mid-sized manufacturers and distributors in Europe. Fixed-scope packages, one accountable partner.", home, True),
        "nis2": ("NIS2 compliance for mid-sized companies",
                 "Does NIS2 apply to your company? Scoping, risk analysis, policies, incident procedure and audit preparation in 6–8 weeks.", nis2, True),
        "packages": ("Packages",
                     "Fixed-scope packages: NIS2 Compliant, Operations & e-invoicing, ERP transformation, Automation & AI, E-commerce integration and the strategic diagnostic.", packages, True),
        "aws": ("Buy through AWS Marketplace",
                "Buy LAMS advisory and software as a private offer on AWS Marketplace, invoiced by Amazon Web Services to your company.", aws, True),
        "funding": ("EU funding for digitalisation",
                    "How LAMS helps mid-sized companies use EU cohesion funds for digitalisation: eligibility, technical preparation and implementation.", funding, True),
        "privacy": ("Privacy notice", "How LAMS Capital Invest LLC processes personal data collected through lamscapital.com.", privacy, False),
        "terms": ("Terms of use", "Terms of use of lamscapital.com.", terms, False),
    }


def pkd(tag, title, who, items, duration, price, note, link, link_label):
    lis = "".join(f"<li>{i}</li>" for i in items)
    extra = f'<dt>Note</dt><dd>{note}</dd>' if note else ""
    more = f'<dt>More</dt><dd><a href="{link}">{link_label} →</a></dd>' if link else ""
    return f"""<div class="pkd">
      <div><p class="tag">{tag}</p><h2>{title}</h2><p class="for">{who}</p></div>
      <dl><dt>Includes</dt><dd><ul>{lis}</ul></dd><dt>Duration</dt><dd>{duration}</dd>{extra}{more}</dl>
    </div>"""

CHECK = {
    "label": "NIS2 self-check",
    "title": "Does NIS2 apply to you? Five questions, one minute.",
    "intro": "An indicative answer based on the directive's size and sector rules. Nothing you select is sent or stored.",
    "q": [
        ("sector", "Which best describes your main activity?", [
            ("a1", "Energy, transport, banking, health, water or digital infrastructure"),
            ("a2", "Food, manufacturing, chemicals, postal and courier, waste, or digital services"),
            ("a3", "None of these"),
        ]),
        ("size", "How large is the company, including its group?", [
            ("s1", "Fewer than 50 employees and under €10 million turnover"),
            ("s2", "50–249 employees, or €10–50 million turnover"),
            ("s3", "250 or more employees, or over €50 million turnover"),
        ]),
        ("chain", "Do large clients send you security questionnaires or contract clauses?", [("yes", "Yes"), ("no", "No")]),
        ("reg", "Is the company registered with the national cybersecurity authority?", [("yes", "Yes"), ("no", "No"), ("unsure", "Not sure")]),
        ("inc", "Do you have a written incident procedure that has been tested?", [("yes", "Yes"), ("no", "No")]),
    ],
    "submit": "See the result",
    "missing": "Answer all five questions to see the result.",
    "out_t": "NIS2 probably does not apply to you directly.",
    "out_b": "The exception is a company the authority designates as critical, regardless of size.",
    "ess_t": "You are probably an essential entity.",
    "ess_b": "The strictest regime: proactive supervision and fines of up to €10 million or 2% of worldwide turnover.",
    "imp_t": "You are probably an important entity.",
    "imp_b": "The same security measures apply, with supervision after incidents or complaints and fines of up to €7 million or 1.4% of worldwide turnover.",
    "gap_reg_no": "Registration with the authority appears to be overdue. It is the first thing an inspection checks.",
    "gap_reg_unsure": "Check whether the company is registered with the authority; the deadline usually runs from when the law first applies to you.",
    "gap_inc": "An untested incident procedure is a gap: the 24-hour early warning runs from when the incident is detected.",
    "gap_chain": "Your clients already apply NIS2 to their suppliers. Clear answers to their questionnaires protect those contracts.",
    "gaps": "What to look at first",
    "cta": "Request the full check",
    "note": "Indicative result, not legal advice. The exact answer depends on activity codes, group structure and national law.",
    "msg": "NIS2 self-check result: ",
}
