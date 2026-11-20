#!/usr/bin/env python3
"""Generates the static pages of lamscapital.com (English at the root, Romanian under /ro/).

Run from the repository root:  python3 tools/build.py
Edit the text in tools/content_en.py and tools/content_ro.py, then rebuild and commit the generated files.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
import content_en  # noqa: E402
import content_ro  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://lamscapital.com"

# Page key -> path per language. Keeps the language switch pointing to the twin page.
PATHS = {
    "home":    {"en": "/",          "ro": "/ro/"},
    "approach": {"en": "/approach/", "ro": "/ro/cum-lucram/"},
    "nis2":    {"en": "/nis2/",     "ro": "/ro/nis2/"},
    "packages": {"en": "/packages/", "ro": "/ro/pachete/"},
    "aws":     {"en": "/aws/",      "ro": "/ro/aws/"},
    "funding": {"en": "/funding/",  "ro": "/ro/granturi/"},
    "prediag": {"en": "/pre-diagnostic/", "ro": "/ro/pre-diagnostic/"},
    "privacy": {"en": "/privacy/",  "ro": "/ro/confidentialitate/"},
    "terms":   {"en": "/terms/",    "ro": "/ro/termeni/"},
}

LOGO = ('<svg width="38" height="38" viewBox="0 0 64 64" aria-hidden="true">'
        '<rect x="8" y="40" width="10" height="16" fill="#16275C"/><rect x="21" y="30" width="10" height="26" fill="#16275C"/>'
        '<rect x="34" y="20" width="10" height="36" fill="#16275C"/><rect x="47" y="8" width="10" height="48" fill="#E0457B"/></svg>')
FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%2316275C'/%3E"
           "%3Crect x='8' y='40' width='10' height='16' fill='%23F6F6F3'/%3E%3Crect x='21' y='30' width='10' height='26' fill='%23F6F6F3'/%3E"
           "%3Crect x='34' y='20' width='10' height='36' fill='%23F6F6F3'/%3E%3Crect x='47' y='8' width='10' height='48' fill='%23E0457B'/%3E%3C/svg%3E")


def page(lang, key, title, description, body, C):
    other = "ro" if lang == "en" else "en"
    here = PATHS[key][lang]
    nav_items = [("packages", C.NAV["packages"]), ("approach", C.NAV["approach"]), ("nis2", C.NAV["nis2"]), ("funding", C.NAV["funding"]), ("aws", C.NAV["aws"])]
    nav = "".join(
        f'<a href="{PATHS[k][lang]}"{" aria-current=\"page\"" if k == key else ""}>{label}</a>' for k, label in nav_items
    )
    nav += f'<a href="{PATHS["home"][lang]}#contact">{C.NAV["contact"]}</a>'
    nav += f'<a class="lang" href="{PATHS[key][other]}" hreflang="{other}" lang="{other}">{C.NAV["switch"]}</a>'
    foot_links = "".join(f'<a href="{PATHS[k][lang]}">{C.NAV[k]}</a>' for k in ("packages", "approach", "nis2", "funding", "aws", "prediag", "privacy", "terms"))
    full_title = title if key == "home" else f"{title} | LAMS"
    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{SITE}{here}">
<link rel="alternate" hreflang="en" href="{SITE}{PATHS[key]['en']}">
<link rel="alternate" hreflang="ro" href="{SITE}{PATHS[key]['ro']}">
<link rel="alternate" hreflang="x-default" href="{SITE}{PATHS[key]['en']}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{SITE}{here}">
<meta property="og:type" content="website">
<meta property="og:image" content="{SITE}/assets/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="{FAVICON}">
<link rel="preload" href="/assets/fonts/source-serif-4-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/ibm-plex-sans-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
<a class="skip" href="#main">{C.NAV["skip"]}</a>
<header class="wrap">
  <div class="top">
    <a class="brand" href="{PATHS['home'][lang]}" aria-label="LAMS">
      {LOGO}
      <span class="brand-word"><b>LAMS</b><span>ADVISORY &amp; VENTURES</span></span>
    </a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">{C.NAV["menu"]}</button>
    <nav class="nav" id="nav" aria-label="{C.NAV['aria']}">{nav}</nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer>
  <div class="wrap">
    <div>
      <p><a href="mailto:info@lamscapital.com">info@lamscapital.com</a></p>
      <p>{C.FOOT_LEGAL}</p>
    </div>
    <nav aria-label="{C.NAV['foot_aria']}">{foot_links}</nav>
  </div>
</footer>
<script src="/assets/site.js" defer></script>
</body>
</html>
"""


def contact(lang, C):
    K = C.FORM
    opts_size = "".join(f"<option>{o}</option>" for o in K["size_opts"])
    opts_topic = "".join(f"<option>{o}</option>" for o in K["topic_opts"])
    next_url = SITE + PATHS["home"][lang] + "#thanks"
    return f"""
<section class="contact" id="contact" aria-labelledby="contact-h">
  <div class="wrap">
    <div class="intro">
      <h2 id="contact-h">{K['title']}</h2>
      <p>{K['intro']}</p>
      <p class="pre-link">{C.PRE['link']}</p>
    </div>
    <div class="form-box">
      <form class="cf" action="https://formsubmit.co/info@lamscapital.com" method="POST" id="cf" novalidate>
        <input type="hidden" name="_subject" value="{K['subject']}">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="{next_url}">
        <input type="hidden" name="language" value="{lang}">
        <input type="hidden" name="page" value="">
        <input type="hidden" name="consent_text" value="{K['consent']}">
        <input type="hidden" name="consent_timestamp" value="">
        <p style="display:none"><label for="hp">Leave empty</label><input id="hp" name="_honey" tabindex="-1" autocomplete="off"></p>
        <div class="two">
          <div><label for="f-name">{K['name']}</label><input id="f-name" name="name" autocomplete="name" required></div>
          <div><label for="f-company">{K['company']}</label><input id="f-company" name="company" autocomplete="organization" required></div>
        </div>
        <div class="two">
          <div><label for="f-email">{K['email']}</label><input id="f-email" name="email" type="email" autocomplete="email" required></div>
          <div><label for="f-country">{K['country']}</label><input id="f-country" name="country" autocomplete="country-name"></div>
        </div>
        <div class="two">
          <div><label for="f-size">{K['size']}</label><select id="f-size" name="employees">{opts_size}</select></div>
          <div><label for="f-topic">{K['topic']}</label><select id="f-topic" name="topic">{opts_topic}</select></div>
        </div>
        <div><label for="f-msg">{K['message']}</label><textarea id="f-msg" name="message" required></textarea></div>
        <label class="check"><input type="checkbox" name="marketing_consent" value="yes"><span>{K['consent']}</span></label>
        <p class="fine">{K['privacy']}</p>
        <p class="err" id="f-err" aria-live="polite"></p>
        <button class="btn primary" type="submit">{K['send']}</button>
      </form>
      <p class="alt">{K['alt']}</p>
    </div>
  </div>
</section>"""


def checker(C):
    import json
    K = C.CHECK
    qs = ""
    for i, (name, text, opts) in enumerate(K["q"], 1):
        radios = "".join(
            f'<label class="opt"><input type="radio" name="{name}" value="{v}"><span>{t}</span></label>' for v, t in opts
        )
        qs += f'<fieldset class="q"><legend><span>{i:02d}</span>{text}</legend><div class="opts">{radios}</div></fieldset>'
    texts = {k: v for k, v in K.items() if k not in ("q",)}
    data = json.dumps(texts, ensure_ascii=False).replace("</", "<\\/")
    return f"""
<section class="section checker-sec" id="check" aria-labelledby="check-h">
  <div class="wrap">
    <p class="label">{K['label']}</p>
    <div class="section-head"><h2 id="check-h">{K['title']}</h2><p>{K['intro']}</p></div>
    <form class="checker" id="nis2-check" novalidate>
      {qs}
      <p class="err" id="check-err" aria-live="polite"></p>
      <button class="btn primary" type="submit">{K['submit']}</button>
    </form>
    <div class="result" id="nis2-result" hidden tabindex="-1" aria-live="polite"></div>
    <div class="report-box" id="nis2-report" hidden>
      <h3>{K['rep_h']}</h3>
      <p>{K['rep_p']}</p>
      <form class="cf" id="nis2-rep" novalidate>
        <p style="display:none"><label for="r-hp">Leave empty</label><input id="r-hp" name="_honey" tabindex="-1" autocomplete="off"></p>
        <div class="two">
          <div><label for="r-name">{K['rep_name']}</label><input id="r-name" name="name" autocomplete="name" required></div>
          <div><label for="r-company">{K['rep_company']}</label><input id="r-company" name="company" autocomplete="organization" required></div>
        </div>
        <div><label for="r-email">{K['rep_email']}</label><input id="r-email" name="email" type="email" autocomplete="email" required></div>
        <label class="check"><input type="checkbox" name="report_consent" value="yes"><span>{K['rep_ok']}</span></label>
        <label class="check"><input type="checkbox" name="marketing_consent" value="yes"><span>{K['rep_mkt']}</span></label>
        <p class="err" id="r-err" aria-live="polite"></p>
        <button class="btn primary" type="submit">{K['rep_send']}</button>
      </form>
    </div>
    <script type="application/json" id="nis2-texts">{data}</script>
  </div>
</section>"""


def prediag(lang, C):
    K = C.PRE
    def sel(name, key):
        return f'<select id="p-{name}" name="{name}">' + "".join(f"<option>{o}</option>" for o in K[key]) + "</select>"
    def boxes(name, key):
        return '<div class="boxes">' + "".join(
            f'<label class="opt"><input type="checkbox" data-group="{name}" value="{o}"><span>{o}</span></label>' for o in K[key]) + f'</div><input type="hidden" name="{name}" value="">'
    next_url = SITE + PATHS["prediag"][lang] + "#thanks"
    return f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">{K['kicker']}</p>
    <h1>{K['h1']}</h1>
    <p class="lead">{K['lead']}</p>
  </div>
</section>
<section class="section prediag-sec">
  <div class="wrap">
    <div class="form-box" id="pd-box">
      <form class="cf pd" id="pd" action="https://formsubmit.co/info@lamscapital.com" method="POST" novalidate>
        <input type="hidden" name="_subject" value="{K['subject']}">
        <input type="hidden" name="_template" value="table">
        <input type="hidden" name="_captcha" value="false">
        <input type="hidden" name="_next" value="{next_url}">
        <input type="hidden" name="language" value="{lang}">
        <input type="hidden" name="consent_text" value="{K['consent']}">
        <input type="hidden" name="consent_timestamp" value="">
        <p style="display:none"><label for="p-hp">Leave empty</label><input id="p-hp" name="_honey" tabindex="-1" autocomplete="off"></p>
        <h2>{K['s1']}</h2>
        <div class="two">
          <div><label for="p-name">{K['name']}</label><input id="p-name" name="name" autocomplete="name" required></div>
          <div><label for="p-role">{K['role']}</label><input id="p-role" name="role" autocomplete="organization-title"></div>
        </div>
        <div class="two">
          <div><label for="p-email">{K['email']}</label><input id="p-email" name="email" type="email" autocomplete="email" required></div>
          <div><label for="p-country">{K['country']}</label><input id="p-country" name="country" autocomplete="country-name"></div>
        </div>
        <h2>{K['s2']}</h2>
        <div class="two">
          <div><label for="p-company">{K['company']}</label><input id="p-company" name="company" autocomplete="organization" required></div>
          <div><label for="p-employees">{K['emp']}</label>{sel('employees', 'emp_opts')}</div>
        </div>
        <div><label for="p-sector">{K['sector']}</label>{sel('sector', 'sector_opts')}</div>
        <fieldset><legend>{K['channels']}</legend>{boxes('channels', 'channels_opts')}</fieldset>
        <fieldset><legend>{K['systems']}</legend>{boxes('systems', 'systems_opts')}</fieldset>
        <h2>{K['s3']}</h2>
        <fieldset><legend>{K['problems']}</legend>{boxes('problems', 'problems_opts')}</fieldset>
        <div><label for="p-goal">{K['goal']}</label><textarea id="p-goal" name="goal"></textarea></div>
        <h2>{K['s4']}</h2>
        <div class="two">
          <div><label for="p-start">{K['when']}</label>{sel('start', 'when_opts')}</div>
          <div><label for="p-call_slot">{K['slot']}</label>{sel('call_slot', 'slot_opts')}</div>
        </div>
        <label class="check"><input type="checkbox" name="marketing_consent" value="yes"><span>{K['consent']}</span></label>
        <p class="fine">{K['privacy']}</p>
        <p class="err" id="p-err" aria-live="polite"></p>
        <button class="btn primary" type="submit">{K['send']}</button>
      </form>
    </div>
    <script type="application/json" id="pd-texts">{{"fill": "{K['fill']}", "max3": "{K['max3']}", "thanks": "{K['thanks']}"}}</script>
  </div>
</section>"""


def write(path, html):
    out = os.path.join(ROOT, path.strip("/"), "index.html") if path != "/" else os.path.join(ROOT, "index.html")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as fh:
        fh.write(html)
    print("wrote", os.path.relpath(out, ROOT))


def build():
    for lang, C in (("en", content_en), ("ro", content_ro)):
        for key, (title, desc, body, with_contact) in C.pages(PATHS).items():
            body = body.replace("<!--CHECKER-->", checker(C))
            if with_contact:
                body += contact(lang, C)
            write(PATHS[key][lang], page(lang, key, title, desc, body, C))
        write(PATHS["prediag"][lang], page(lang, "prediag", C.PRE["title"], C.PRE["desc"], prediag(lang, C), C))
    # 404 page (served by GitHub Pages for any missing path)
    body = """
<section class="hero">
  <div class="wrap">
    <p class="kicker">404</p>
    <h1>This page does not exist.</h1>
    <p class="lead">The address may have changed. Go to the <a href="/">home page</a> or write to us at <a href="mailto:info@lamscapital.com">info@lamscapital.com</a>.</p>
    <p class="lead" lang="ro">Pagina nu există. Mergeți la <a href="/ro/">pagina principală</a> sau scrieți-ne la <a href="mailto:info@lamscapital.com">info@lamscapital.com</a>.</p>
  </div>
</section>"""
    html = page("en", "home", "Page not found | LAMS", "Page not found.", body, content_en)
    html = html.replace("<title>Page not found | LAMS</title>", '<title>Page not found | LAMS</title>\n<meta name="robots" content="noindex">')
    import re
    html = re.sub(r'<link rel="(canonical|alternate)"[^>]*>\n', "", html)
    html = re.sub(r'<meta property="og:url"[^>]*>\n', "", html)
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as fh:
        fh.write(html)
    print("wrote 404.html")
    # sitemap
    urls = "".join(f"<url><loc>{SITE}{p[l]}</loc></url>" for p in PATHS.values() for l in ("en", "ro"))
    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as fh:
        fh.write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>\n')
    with open(os.path.join(ROOT, "robots.txt"), "w", encoding="utf-8") as fh:
        fh.write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    print("wrote sitemap.xml, robots.txt")


if __name__ == "__main__":
    build()
