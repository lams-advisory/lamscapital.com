# English text of lamscapital.com (root of the site). European positioning.

NAV = {
    "nis2": "NIS2 compliance", "packages": "Packages", "aws": "AWS", "funding": "EU funding",
    "privacy": "Privacy", "terms": "Terms", "contact": "Contact", "switch": "RO",
    "menu": "Menu", "aria": "Main", "foot_aria": "Site", "skip": "Skip to content",
}

FOOT_LEGAL = "© 2026 LAMS Capital Invest LLC. All rights reserved."

FORM = {
    "title": "Start a conversation.",
    "intro": "Tell us briefly about your company and the decision ahead. We reply within two business days, and every conversation is treated as confidential.",
    "subject": "New enquiry from lamscapital.com (EN)",
    "name": "Name", "company": "Company", "email": "Work email", "country": "Country",
    "size": "Employees", "size_opts": ["10–49", "50–249", "Fewer than 10", "250 or more"],
    "topic": "Main interest", "topic_opts": ["Strategic diagnostic", "ERP and e-invoicing", "Automation and AI", "E-commerce integration", "NIS2 compliance", "EU funding", "Something else"],
    "message": "What would you like to discuss?",
    "consent": "I agree to receive occasional emails from LAMS about growth, digitalisation, compliance and funding. I can withdraw this consent at any time.",
    "privacy": 'We use your details only to answer this enquiry. See our <a href="/privacy/">privacy notice</a>.',
    "send": "Send message",
    "alt": 'Or write to <a href="mailto:info@lamscapital.com">info@lamscapital.com</a>',
}


def pages(P):
    home = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">For small and mid-sized companies in Europe</p>
    <h1>Strategy and software for growing companies, from <span class="accent">one accountable partner</span>.</h1>
    <p class="lead">We find where your company loses margin and time, then build the software and automation that fix it, and keep it running. For companies across the European Union, with local delivery in Romania.</p>
    <div class="btn-row"><a class="btn primary" href="#contact">Start a conversation</a><a class="btn" href="{P['packages']['en']}">See the packages</a></div>
  </div>
</section>

<section class="band" aria-label="How we commit">
  <div class="wrap band-grid">
    <div><b>5 weeks</b><span>from your numbers to a 12-month plan</span></div>
    <div><b>One contract</b><span>for strategy, software and support</span></div>
    <div><b>Every month</b><span>a written report, timesheet and sign-off</span></div>
    <div><b>2 business days</b><span>to answer any enquiry, in confidence</span></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="label">What we do</p>
    <div class="cols3">
      <div><h3>Growth and strategy</h3><p>A strategic diagnostic built on your own numbers: margins, markets, channels, operations and a 12-month plan with owners and a budget.</p><p><a class="more" href="{P['packages']['en']}">Strategic diagnostic →</a></p></div>
      <div><h3>Software and automation</h3><p>Stock, sales and purchasing on one system, e-invoicing, e-commerce integration, and automation or AI assistants for repetitive work.</p><p><a class="more" href="{P['packages']['en']}">Software packages →</a></p></div>
      <div><h3>Compliance and funding</h3><p>NIS2 cybersecurity compliance for companies covered by the law, and preparation of digitalisation projects for EU funding.</p><p><a class="more" href="{P['nis2']['en']}">NIS2 →</a> &nbsp; <a class="more" href="{P['funding']['en']}">EU funding →</a></p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="label">Questions we help answer</p>
    <ol class="q-list">
      <li><span>01</span>Where are we losing margin, and what do we fix first?</li>
      <li><span>02</span>How do we stop re-typing orders and invoices between spreadsheets, the warehouse and accounting?</li>
      <li><span>03</span>What should we automate first, and what does it save us each month?</li>
      <li><span>04</span>How do we sell on marketplaces without stock errors and manual invoicing?</li>
      <li><span>05</span>Does NIS2 apply to us, or has our largest client sent us a security questionnaire we must answer?</li>
      <li><span>06</span>Can EU funding cover part of the investment without putting the project at risk?</li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Fixed-scope packages with a defined result.</h2>
      <p>Advisory opens the project; software and automation deliver the savings; a monthly subscription keeps it running. Every package can run on its own or as part of one plan.</p>
    </div>
    <div class="pk-grid">
      <div class="pk feature"><span class="tag">Advisory</span><h3>Strategic diagnostic</h3><p>Five weeks, seven deliverables: margins, markets, channels and a 12-month plan, built on your own numbers.</p><p class="price"><a class="more" href="#contact">Request an offer →</a></p></div>
      <div class="pk"><span class="tag">Package A</span><h3>Operations &amp; e-invoicing</h3><p>Stock, sales and purchasing on Odoo, connected to accounting and to national e-invoicing.</p><p class="price"><a class="more" href="#contact">Request an offer →</a></p></div>
      <div class="pk"><span class="tag">Package D</span><h3>Automation &amp; AI</h3><p>A discovery workshop, then one automation or AI assistant delivered in about four weeks.</p><p class="price"><a class="more" href="#contact">Request an offer →</a></p></div>
      <div class="pk"><span class="tag">Package E</span><h3>E-commerce integration</h3><p>Marketplace feeds, stock synchronisation and automatic e-invoicing for online sellers.</p><p class="price"><a class="more" href="#contact">Request an offer →</a></p></div>
      <div class="pk"><span class="tag">Package B</span><h3>ERP &amp; operational transformation</h3><p>Full strategic diagnostic, then ERP and automation across the business. Suited to funded projects.</p><p class="price"><a class="more" href="#contact">Request an offer →</a></p></div>
      <div class="pk"><span class="tag">Package C</span><h3>NIS2 Compliant</h3><p>Scoping, risk analysis, written policies, incident procedure and audit preparation, with monthly follow-up.</p><p class="price"><a class="more" href="{P['nis2']['en']}">NIS2 details →</a></p></div>
    </div>
    <p style="margin-top:28px"><a href="{P['packages']['en']}">All packages and details →</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="label">Who we work with</p>
    <div class="cl-grid">
      <h3>Owner-led and mid-sized companies, from 10 to 249 employees, at the point where growth needs structure.</h3>
      <div class="sectors">
        <div><b>Manufacturing</b><span>Food, machinery, equipment, components and consumer goods</span></div>
        <div><b>Distribution and wholesale</b><span>Importers, distributors and wholesale trade</span></div>
        <div><b>Online retail</b><span>Own shops and marketplace sellers</span></div>
        <div><b>Transport and logistics</b><span>Road transport, warehousing and courier services</span></div>
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
      <p>Strategy, software and compliance are delivered by one team under one contract. A dedicated development team in Europe, coordinated by us, builds and maintains the software; we stay accountable to you for the result.</p>
      <div class="steps">
        <div><b>Diagnose</b><span>Fixed-scope review of numbers, operations and obligations.</span></div>
        <div><b>Plan</b><span>Prioritised measures with owners, deadlines and a budget.</span></div>
        <div><b>Implement</b><span>Policies, software and integrations, delivered in short stages with sign-off.</span></div>
        <div><b>Support</b><span>A monthly subscription keeps compliance and systems up to date.</span></div>
      </div>
      <p style="margin-top:28px"><a href="{P['aws']['en']}">AWS Marketplace →</a></p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:88px">
  <div class="wrap">
    <p class="label">Principles</p>
    <div class="cols3">
      <div><h3>Transparent</h3><p>We sell advisory and software, and say so upfront. The diagnostic also tells you what is not worth buying, including from us.</p></div>
      <div><h3>Confidential</h3><p>A non-disclosure agreement is signed before any information is shared, and each client's data is kept separate and used only for that client's work.</p></div>
      <div><h3>Accountable</h3><p>One team, one plan and one set of indicators, from diagnosis to delivery, with written sign-off at every stage.</p></div>
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
    <p class="source">Sources: Directive (EU) 2022/2555; for Romania, Government Emergency Ordinance 155/2024, approved by Law 124/2025. National rules change, so we re-check them for every client.</p>
  </div>
</section>"""

    packages = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">Packages</p>
    <h1>Advisory and software, sold as <span class="accent">fixed-scope packages</span>.</h1>
    <p class="lead">Each package has a defined result and a schedule, agreed before work starts. Advisory opens the project; software and automation deliver the savings; a monthly subscription keeps it running.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    {pkd("Advisory", "Strategic diagnostic", "Owner-led companies at the point where growth needs structure.",
         ["Five weeks, seven deliverables: performance, market, channels, operations, opportunities, key indicators and a 12-month plan", "Built on your own numbers, under a non-disclosure agreement"],
         "5 weeks", "", "", "", "")}
    {pkd("Package A", "Operations &amp; e-invoicing", "Distributors and manufacturers, 10–49 employees.",
         ["Digital audit, included in the package", "Stock, sales and purchasing on Odoo Community (open source, no licence fees)", "Integration with your accounting software", "Connection to national e-invoicing (in Romania: e-Factura)"],
         "Agreed after the audit", "", "", "", "")}
    {pkd("Package D", "Automation &amp; AI", "Any company with repetitive work: orders, documents, reporting, customer requests.",
         ["Discovery workshop to pick the process with the best return", "One automation or AI assistant, built and deployed", "Measured before and after, so the saving is visible"],
         "About 4 weeks", "", "Monthly support includes the AI usage costs.", "", "")}
    {pkd("Package E", "E-commerce integration", "Online sellers with annual turnover of roughly €0.2–4 million.",
         ["Product feeds to marketplaces", "Stock synchronisation between shop, marketplaces and warehouse", "Automatic e-invoicing"],
         "About 4 weeks", "", "", "", "")}
    {pkd("Package B", "ERP &amp; operational transformation", "Companies with 50–249 employees, including projects co-financed by EU funds.",
         ["Full strategic diagnostic: seven deliverables, from margins to a 12-month plan", "ERP and automation across sales, warehouse, production and finance", "Staged delivery with sign-off at each stage", "Monthly support after go-live"],
         "Agreed after the diagnostic", "", "", P['funding']['en'], "How EU funding works")}
    {pkd("Package C", "NIS2 Compliant", "Companies covered by NIS2, typically 50–249 employees.",
         ["Scoping against the law and the national rules", "Asset and risk registers", "Self-assessment prepared on evidence", "Written policies approved by management", "Incident procedure and templates", "Remediation plan and audit file"],
         "6–8 weeks", "", "External audit by an accredited auditor is contracted separately.", P['nis2']['en'], "NIS2 details")}
    <p class="note"><b>Offers.</b> Every offer is personalised after a 30-minute call and states the full scope, schedule and terms. Odoo is a trademark of Odoo S.A.; LAMS is not affiliated with Odoo S.A.</p>
  </div>
</section>"""

    aws = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">AWS Marketplace</p>
    <h1>Contracting and billing through <span class="accent">AWS Marketplace</span>.</h1>
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
    <p style="margin-top:32px"><a href="{P['funding']['ro']}" hreflang="ro">EU funding in Romania (Romanian page) →</a></p>
  </div>
</section>"""

    privacy = """
<section class="section" style="padding-top:56px">
  <div class="wrap legal">
    <h1>Privacy notice</h1>
    <p>LAMS respects the confidentiality of everyone who contacts us. This notice explains how we handle personal data received through this website.</p>
    <h2>Data we collect</h2>
    <p>Only what you send us through the contact form or by email: your name, company, work email, country and the content of your message. If you agree, we also record your consent to receive occasional updates.</p>
    <h2>How we use it</h2>
    <p>To answer your enquiry and prepare a proposal, as steps taken at your request (Article 6(1)(b) GDPR). Only with your consent, to send occasional updates on growth, digitalisation, compliance and funding (Article 6(1)(a) GDPR). We never sell your data or share it for third-party marketing.</p>
    <h2>Cookies and tracking</h2>
    <p>This website uses no analytics, advertising or tracking cookies.</p>
    <h2>Service providers</h2>
    <p>We rely on carefully selected providers for hosting, form delivery and email, bound by data-processing terms. Where data is processed outside the European Economic Area, transfers rely on appropriate safeguards, such as the European Commission's Standard Contractual Clauses or the EU–US Data Privacy Framework.</p>
    <h2>Retention</h2>
    <p>Enquiry data is kept for up to 24 months after our last contact, unless an engagement follows. Records of consent are kept for as long as we need to demonstrate it.</p>
    <h2>Your rights</h2>
    <p>You may request access to your data, its correction or deletion, restriction of processing and data portability, and you may object to processing. You may withdraw consent at any time, without affecting earlier processing. You may also lodge a complaint with the data protection authority in your country.</p>
    <h2>Client engagements</h2>
    <p>Information shared during an engagement is protected by a non-disclosure agreement and, where personal data is involved, by a data processing agreement under Article 28 GDPR.</p>
    <h2>Contact</h2>
    <p>Data controller: LAMS Capital Invest LLC. For any request: <a href="mailto:info@lamscapital.com">info@lamscapital.com</a>.</p>
  </div>
</section>"""

    terms = """
<section class="section" style="padding-top:56px">
  <div class="wrap legal">
    <h1>Terms of use</h1>
    <p>These terms apply to the use of lamscapital.com, operated by LAMS Capital Invest LLC (“LAMS”).</p>
    <h2>Information</h2>
    <p>The content of this website is general information. It does not constitute legal, tax or security advice for a specific situation. Summaries of laws and funding rules reflect our understanding at the time of publication.</p>
    <h2>Engagements</h2>
    <p>Nothing on this website is an offer. Every engagement is governed exclusively by a signed agreement or an accepted private offer, together with its statement of work.</p>
    <h2>Intellectual property</h2>
    <p>The texts, the LAMS name and logo and the design of this website belong to LAMS. Other names and trademarks belong to their respective owners; their mention implies no partnership or endorsement.</p>
    <h2>Liability</h2>
    <p>We take care to keep this website accurate and available. To the extent permitted by law, LAMS is not liable for decisions taken solely on the basis of its content.</p>
    <h2>Contact</h2>
    <p><a href="mailto:info@lamscapital.com">info@lamscapital.com</a></p>
  </div>
</section>"""

    return {
        "home": ("LAMS · Strategy, software and automation for growing companies",
                 "Strategic diagnostic, ERP, e-invoicing, e-commerce, automation and AI for small and mid-sized companies in Europe, plus NIS2 compliance and EU funding. Fixed-scope packages, one accountable partner.", home, True),
        "nis2": ("NIS2 compliance for mid-sized companies",
                 "Does NIS2 apply to your company? Scoping, risk analysis, policies, incident procedure and audit preparation in 6–8 weeks.", nis2, True),
        "packages": ("Packages",
                     "Fixed-scope packages: strategic diagnostic, Operations & e-invoicing, Automation & AI, E-commerce integration, ERP transformation and NIS2 Compliant.", packages, True),
        "aws": ("AWS Marketplace",
                "Buy LAMS advisory and software as a private offer on AWS Marketplace, invoiced by Amazon Web Services to your company.", aws, True),
        "funding": ("EU funding for digitalisation",
                    "How LAMS helps small and mid-sized companies use EU cohesion funds for digitalisation: eligibility, technical preparation and implementation.", funding, True),
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
