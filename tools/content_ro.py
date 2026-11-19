# Textul în română al lamscapital.com (/ro/). Prima piață: România; detalii locale (DNSC, e-Factura, granturi regionale).

NAV = {
    "nis2": "Conformitate NIS2", "packages": "Pachete", "approach": "Cum lucrăm", "aws": "AWS", "funding": "Granturi",
    "privacy": "Confidențialitate", "terms": "Termeni", "contact": "Contact", "switch": "EN",
    "menu": "Meniu", "aria": "Principal", "foot_aria": "Site", "skip": "Sari la conținut",
}

FOOT_LEGAL = "© 2026 LAMS Capital Invest LLC. Toate drepturile rezervate."

FORM = {
    "title": "Să vorbim.",
    "intro": "Spuneți-ne pe scurt despre firmă și despre decizia pe care o aveți de luat. Răspundem în cel mult două zile lucrătoare, iar orice discuție rămâne confidențială.",
    "subject": "Mesaj nou de pe lamscapital.com (RO)",
    "name": "Nume", "company": "Firmă (și CUI, dacă doriți verificarea NIS2)", "email": "Email de serviciu", "country": "Țară",
    "size": "Număr de angajați", "size_opts": ["10–49", "50–249", "Sub 10", "250 sau mai mulți"],
    "topic": "Ce vă interesează", "topic_opts": ["Diagnostic strategic", "Gestiune și e-Factura", "Automatizare și AI", "Integrare e-commerce", "Conformitate NIS2", "Granturi", "Altceva"],
    "message": "Despre ce doriți să discutăm?",
    "consent": "Sunt de acord să primesc ocazional pe email informări de la LAMS despre creștere, digitalizare, conformitate și granturi. Pot retrage acordul oricând.",
    "privacy": 'Folosim datele doar ca să vă răspundem. Detalii în <a href="/ro/confidentialitate/">politica de confidențialitate</a>.',
    "send": "Trimite mesajul",
    "alt": 'Sau scrieți-ne la <a href="mailto:info@lamscapital.com">info@lamscapital.com</a>',
}


def pages(P):
    home = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">Pentru firme mici și mijlocii</p>
    <h1>Strategie și software pentru firmele în creștere, de la <span class="accent">un singur partener responsabil</span>.</h1>
    <p class="lead">Găsim unde pierde firma marjă și timp, apoi construim software-ul și automatizările care rezolvă problema și le ținem în funcțiune. Lucrăm cu firme din România și din Uniunea Europeană.</p>
    <div class="btn-row"><a class="btn primary" href="#contact">Să vorbim</a><a class="btn" href="{P['packages']['ro']}">Vedeți pachetele</a></div>
  </div>
</section>

<section class="band" aria-label="Angajamentele noastre">
  <div class="wrap band-grid">
    <div><b>5 săptămâni</b><span>de la cifrele firmei la un plan pe 12 luni</span></div>
    <div><b>Un singur contract</b><span>pentru strategie, software și suport</span></div>
    <div><b>Lunar</b><span>raport scris, fișă de ore și proces-verbal</span></div>
    <div><b>2 zile lucrătoare</b><span>pentru răspuns la orice solicitare, sub confidențialitate</span></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="label">Ce facem</p>
    <div class="cols3">
      <div><h3>Creștere și strategie</h3><p>Un diagnostic strategic construit pe cifrele firmei: marje, piețe, canale, operațiuni și un plan pe 12 luni, cu responsabili și buget.</p><p><a class="more" href="{P['packages']['ro']}">Diagnostic strategic →</a></p></div>
      <div><h3>Software și automatizare</h3><p>Stocuri, vânzări și achiziții într-un singur sistem, e-Factura, integrare e-commerce și automatizări sau asistenți AI pentru munca repetitivă.</p><p><a class="more" href="{P['packages']['ro']}">Pachete software →</a></p></div>
      <div><h3>Conformitate și finanțare</h3><p>Conformitate NIS2 pentru firmele vizate de lege și pregătirea proiectelor de digitalizare pentru fonduri europene.</p><p><a class="more" href="{P['nis2']['ro']}">NIS2 →</a> &nbsp; <a class="more" href="{P['funding']['ro']}">Granturi →</a></p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="label">Întrebări la care vă ajutăm să răspundeți</p>
    <ol class="q-list">
      <li><span>01</span>Unde pierdem marjă și ce reparăm întâi?</li>
      <li><span>02</span>Cum scăpăm de tastarea comenzilor și facturilor de două ori, între Excel, depozit și contabilitate?</li>
      <li><span>03</span>Ce merită automatizat întâi și cât economisim pe lună?</li>
      <li><span>04</span>Cum vindem pe marketplace-uri fără erori de stoc și facturare manuală?</li>
      <li><span>05</span>Intră firma sub NIS2 sau ne-a trimis cel mai mare client un chestionar de securitate la care trebuie să răspundem?</li>
      <li><span>06</span>Putem acoperi o parte din investiție cu un grant, fără să punem proiectul în pericol?</li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Pachete cu perimetru și rezultat clar.</h2>
      <p>Consultanța deschide proiectul, software-ul și automatizările aduc economiile, iar abonamentul lunar le ține în funcțiune. Fiecare pachet poate fi cumpărat separat sau ca parte a unui singur plan.</p>
    </div>
    <div class="pk-grid">
      <div class="pk feature"><span class="tag">Consultanță</span><h3>Diagnostic strategic</h3><p>Cinci săptămâni, șapte livrabile: marje, piețe, canale și un plan pe 12 luni, construit pe cifrele firmei.</p><p class="price"><a class="more" href="#contact">Cereți o ofertă →</a></p></div>
      <div class="pk"><span class="tag">Pachetul A</span><h3>Gestiune &amp; e-Factura</h3><p>Stocuri, vânzări și achiziții pe Odoo, legate de programul de contabilitate și de e-Factura (ANAF).</p><p class="price"><a class="more" href="#contact">Cereți o ofertă →</a></p></div>
      <div class="pk"><span class="tag">Pachetul D</span><h3>Automatizare &amp; AI</h3><p>Un atelier de identificare, apoi o automatizare sau un asistent AI livrat în aproximativ patru săptămâni.</p><p class="price"><a class="more" href="#contact">Cereți o ofertă →</a></p></div>
      <div class="pk"><span class="tag">Pachetul E</span><h3>Integrare e-commerce</h3><p>Feed-uri către marketplace-uri, sincronizare de stoc și e-Factura automată pentru magazinele online.</p><p class="price"><a class="more" href="#contact">Cereți o ofertă →</a></p></div>
      <div class="pk"><span class="tag">Pachetul B</span><h3>ERP &amp; transformare operațională</h3><p>Diagnostic strategic complet, apoi ERP și automatizări în toată firma. Potrivit pentru proiecte cu grant.</p><p class="price"><a class="more" href="#contact">Cereți o ofertă →</a></p></div>
      <div class="pk"><span class="tag">Pachetul C</span><h3>NIS2 Conform</h3><p>Încadrare, analiză de risc, politici scrise, procedură de incident și pregătirea auditului, cu urmărire lunară.</p><p class="price"><a class="more" href="{P['nis2']['ro']}">Detalii NIS2 →</a></p></div>
    </div>
    <p style="margin-top:28px"><a href="{P['packages']['ro']}">Toate pachetele și detaliile →</a></p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="label">Cu cine lucrăm</p>
    <div class="cl-grid">
      <h3>Firme conduse de proprietar și firme mijlocii, de la 10 la 249 de angajați, în momentul în care creșterea are nevoie de structură.</h3>
      <div class="sectors">
        <div><b>Producție</b><span>Alimentar, utilaje, echipamente, componente și bunuri de consum</span></div>
        <div><b>Distribuție și comerț en-gros</b><span>Importatori, distribuitori și comerț cu ridicata</span></div>
        <div><b>Comerț online</b><span>Magazine proprii și vânzători pe marketplace-uri</span></div>
        <div><b>Transport și logistică</b><span>Transport rutier, depozitare și curierat</span></div>
      </div>
    </div>
  </div>
</section>

<section class="night">
  <div class="wrap">
    <div>
      <p class="label">Cum lucrăm</p>
      <h2>Întâi diagnosticul. Apoi un plan, o echipă.</h2>
    </div>
    <div>
      <p>Strategia, software-ul și conformitatea sunt livrate de aceeași echipă, sub un singur contract. O echipă dedicată de dezvoltatori din Europa, coordonată de noi, construiește și întreține software-ul; răspunderea față de dumneavoastră rămâne a noastră.</p>
      <div class="steps">
        <div><b>Diagnostic</b><span>Analiză cu perimetru fix a cifrelor, operațiunilor și obligațiilor.</span></div>
        <div><b>Plan</b><span>Măsuri prioritizate, cu responsabili, termene și buget.</span></div>
        <div><b>Implementare</b><span>Politici, software și integrări, livrate în etape scurte, cu proces-verbal de predare.</span></div>
        <div><b>Suport</b><span>Un abonament lunar ține la zi conformitatea și sistemele.</span></div>
      </div>
      <p style="margin-top:28px"><a href="{P['approach']['ro']}">Metoda în detaliu →</a> &nbsp; <a href="{P['aws']['ro']}">AWS Marketplace →</a></p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:88px">
  <div class="wrap">
    <p class="label">Principii</p>
    <div class="cols3">
      <div><h3>Transparenți</h3><p>Vindem consultanță și software și o spunem de la început. Diagnosticul vă arată și ce nu merită cumpărat, inclusiv de la noi.</p></div>
      <div><h3>Confidențiali</h3><p>Acordul de confidențialitate se semnează înainte de orice informație. Datele fiecărui client sunt ținute separat și folosite doar pentru lucrarea lui.</p></div>
      <div><h3>Responsabili</h3><p>O echipă, un plan și un set de indicatori, de la diagnostic la livrare, cu proces-verbal semnat la fiecare etapă.</p></div>
    </div>
  </div>
</section>"""

    nis2 = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">Pachetul C · NIS2 Conform</p>
    <h1>Aflați unde sunteți față de NIS2 și fiți <span class="accent">pregătiți pentru control</span>.</h1>
    <p class="lead">NIS2 este directiva europeană de securitate cibernetică. Prin ea, mii de firme mijlocii din România au intrat pentru prima dată sub lege. Stabilim dacă vi se aplică, pregătim ce cere DNSC și vă ajutăm să țineți totul la zi, lunar.</p>
    <div class="btn-row"><a class="btn primary" href="#check">Verificați în 1 minut</a><a class="btn" href="{P['packages']['ro']}">Toate pachetele</a></div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Intră firma dumneavoastră sub NIS2?</h2>
      <p>Probabil da, dacă ambele condiții de mai jos sunt adevărate. Răspunsul exact depinde de codurile CAEN, de grupul de firme și de anexele legii.</p>
    </div>
    <ul class="ticks">
      <li><b>Mărime:</b> cel puțin 50 de angajați sau o cifră de afaceri anuală peste 10 mil. EUR (firme mijlocii și mari).</li>
      <li><b>Sector:</b> activați într-un sector din anexele legii, de exemplu producția și distribuția de alimente, fabricarea de utilaje, echipamente electrice, electronice, autovehicule sau dispozitive medicale, industria chimică, transporturile, serviciile poștale și de curierat sau gestionarea deșeurilor.</li>
      <li><b>Unele firme mai mici</b> intră și ele, indiferent de mărime, dacă autoritatea le desemnează drept critice.</li>
      <li><b>Prin clienții dumneavoastră:</b> firmele aflate sub NIS2 trebuie să gestioneze securitatea furnizorilor. Chiar dacă legea nu vă vizează direct, clienții mari vă vor trimite chestionare de securitate, audituri și clauze contractuale. Fără răspunsuri, contractele sunt în risc.</li>
    </ul>
    <p class="note"><b>Verificare completă de încadrare, gratuită.</b> Trimiteți-ne numele firmei și codul unic de înregistrare (CUI). În două zile lucrătoare vă spunem dacă NIS2 vi se aplică, dacă ați fi entitate esențială sau importantă și ce termene aveți.</p>
  </div>
</section>
<!--CHECKER-->

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Ce cere legea în România</h2>
      <p>Ordonanța de urgență 155/2024, aprobată prin Legea 124/2025, și ordinele DNSC. Termenele curg de la momentul în care firma intră sub incidența legii sau de la decizia DNSC.</p>
    </div>
    <div class="steps light">
      <div><b>30 de zile</b><span>Înregistrarea la DNSC, pe platforma NIS2@RO.</span></div>
      <div><b>30 de zile</b><span>Desemnarea responsabilului cu securitatea rețelelor și sistemelor informatice, de la decizia de înregistrare.</span></div>
      <div><b>60 + 60 de zile</b><span>Evaluarea nivelului de risc, apoi autoevaluarea maturității măsurilor de securitate, după metodologia DNSC.</span></div>
      <div><b>30 de zile</b><span>Planul de remediere, pentru entitățile esențiale, după autoevaluare.</span></div>
      <div><b>24 h · 72 h · o lună</b><span>Raportarea unui incident semnificativ: avertizare timpurie, notificare și raport final.</span></div>
    </div>
    <p class="source">Amenzi: pentru entitățile esențiale de la 10.000 lei până la 10 mil. EUR sau 2% din cifra de afaceri; pentru cele importante de la 5.000 lei până la 7 mil. EUR sau 1,4%; la repetare, majorare cu 50%. Surse: OUG 155/2024, aprobată prin Legea 124/2025; Directiva (UE) 2022/2555, art. 23. Reverificăm cadrul legal la fiecare client.</p>
  </div>
</section>

<section class="night">
  <div class="wrap">
    <div>
      <p class="label">Ce livrăm</p>
      <h2>Șase până la opt săptămâni, de la încadrare la dosarul pentru audit.</h2>
    </div>
    <div>
      <div class="steps">
        <div><b>Încadrare</b><span>Coduri CAEN, mărime și grup, verificate față de lege, cu sursă pentru fiecare cifră.</span></div>
        <div><b>Inventar și risc</b><span>Registrul sistemelor, datelor și furnizorilor critici; registrul de riscuri cu responsabili și termene.</span></div>
        <div><b>Autoevaluare</b><span>Pregătită pe dovezi, nu pe declarații, în formatul DNSC.</span></div>
        <div><b>Politici</b><span>Setul complet de politici scrise, adaptate firmei și aprobate de conducere.</span></div>
        <div><b>Procedura de incident</b><span>Cine decide, cine notifică DNSC și șabloanele pentru 24 de ore, 72 de ore și o lună.</span></div>
        <div><b>Pregătirea auditului</b><span>Plan de remediere pe 3, 6 și 12 luni și dosarul complet pentru auditor.</span></div>
      </div>
      <p style="margin-top:28px"><b style="color:var(--paper);font-weight:500">Apoi un abonament lunar</b> pentru instrumentul de conformitate în limba română, revizuirea trimestrială a riscurilor, actualizarea politicilor la schimbări legislative și sprijin la raportarea incidentelor.</p>
    </div>
  </div>
</section>

<section class="section" style="padding-top:88px">
  <div class="wrap">
    <div class="section-head">
      <h2>Unde ne oprim</h2>
      <p>Ca să nu existe surprize în ofertă.</p>
    </div>
    <ul class="ticks">
      <li>Acolo unde legea cere audit extern, îl face un auditor atestat de DNSC. Noi pregătim dosarul și coordonăm auditul împreună cu dumneavoastră; auditorul se contractează separat, ca auditul să rămână independent.</li>
      <li>Lucrăm pe dovezi și cu acces doar de citire. Nu cerem acces de administrator la sistemele firmei.</li>
      <li>Nu depunem nimic la DNSC în numele firmei fără mandat scris.</li>
    </ul>
  </div>
</section>"""

    packages = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">Pachete</p>
    <h1>Consultanță și software, vândute ca <span class="accent">pachete cu perimetru fix</span>.</h1>
    <p class="lead">Fiecare pachet are un rezultat definit și un calendar, stabilite înainte de începerea lucrului. Consultanța deschide proiectul, software-ul și automatizările aduc economiile, iar abonamentul lunar le ține în funcțiune.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    {pkd("Consultanță", "Diagnostic strategic", "Firme conduse de proprietar, în momentul în care creșterea are nevoie de structură.",
         ["Cinci săptămâni, șapte livrabile: performanță, piață, canale, operațiuni, oportunități, indicatori și plan pe 12 luni", "Construit pe cifrele firmei, sub acord de confidențialitate"],
         "5 săptămâni", "", "", "", "")}
    {pkd("Pachetul A", "Gestiune &amp; e-Factura", "Distribuitori și producători cu 10–49 de angajați.",
         ["Audit digital, inclus în pachet", "Stocuri, vânzări și achiziții pe Odoo Community (open-source, fără licențe)", "Integrare cu programul de contabilitate", "Conectare la e-Factura (ANAF)"],
         "Stabilită după audit", "", "", "", "")}
    {pkd("Pachetul D", "Automatizare &amp; AI", "Orice firmă cu muncă repetitivă: comenzi, documente, rapoarte, cereri de la clienți.",
         ["Atelier de identificare a procesului cu cel mai bun randament", "O automatizare sau un asistent AI, construit și pus în funcțiune", "Măsurare înainte și după, ca economia să se vadă"],
         "Aproximativ 4 săptămâni", "", "Suportul lunar include costurile de utilizare a AI.", "", "")}
    {pkd("Pachetul E", "Integrare e-commerce", "Magazine online cu o cifră de afaceri anuală de 1–20 mil. lei.",
         ["Feed-uri de produse către marketplace-uri", "Sincronizarea stocului între magazin, marketplace-uri și depozit", "e-Factura automată"],
         "Aproximativ 4 săptămâni", "", "", "", "")}
    {pkd("Pachetul B", "ERP &amp; transformare operațională", "Firme cu 50–249 de angajați, inclusiv proiecte cofinanțate din fonduri europene.",
         ["Diagnostic strategic complet: șapte livrabile, de la marje la planul pe 12 luni", "ERP și automatizări pentru vânzări, depozit, producție și financiar", "Livrare în etape, cu proces-verbal la fiecare etapă", "Suport lunar după punerea în funcțiune"],
         "Stabilită după diagnostic", "", "", P['funding']['ro'], "Cum lucrăm pe granturi")}
    {pkd("Pachetul C", "NIS2 Conform", "Firme sub incidența NIS2, de regulă cu 50–249 de angajați.",
         ["Încadrarea față de lege și ordinele DNSC", "Registrul activelor și registrul riscurilor", "Autoevaluarea, pregătită pe dovezi", "Politici scrise, aprobate de conducere", "Procedura de incident și șabloanele", "Planul de remediere și dosarul de audit"],
         "6–8 săptămâni", "", "Auditul extern, făcut de un auditor atestat DNSC, se contractează separat.", P['nis2']['ro'], "Detalii NIS2")}
    <p class="note"><b>Oferte.</b> Fiecare ofertă se personalizează după o discuție de 30 de minute și arată complet perimetrul, calendarul și condițiile. Odoo este marcă a Odoo S.A.; LAMS nu este afiliată cu Odoo S.A.</p>
  </div>
</section>"""

    aws = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">AWS Marketplace</p>
    <h1>Contractare și facturare prin <span class="accent">AWS Marketplace</span>.</h1>
    <p class="lead">Pe lângă contractul direct, orice pachet LAMS se poate cumpăra ca ofertă privată pe AWS Marketplace, catalogul de software și servicii al Amazon Web Services. Amazon Web Services facturează firma dumneavoastră și ne plătește pe noi.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>De ce aleg firmele această variantă</h2>
      <p>Oferta privată este o ofertă pe AWS Marketplace făcută doar pentru firma dumneavoastră, în condițiile convenite.</p>
    </div>
    <div class="cols3">
      <div><h3>Un furnizor cunoscut</h3><p>Factura vine de la Amazon Web Services, un furnizor pe care contabilitatea și achizițiile îl pot verifica ușor.</p></div>
      <div><h3>Plata într-un singur loc</h3><p>Plata trece prin contul AWS al firmei, cu card sau prin transfer bancar, unde este disponibil, iar facturile stau într-un singur loc.</p></div>
      <div><h3>Documente complete</h3><p>Lunar primiți raportul de activitate, fișa de ore și procesul-verbal de predare, cu numărul ofertei și al facturii AWS, utile la controlul fiscal.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="label">Pașii</p>
    <div class="steps light">
      <div><b>1. Stabilim lucrarea</b><span>Semnăm acordul de confidențialitate și stabilim descrierea lucrării: perimetru, livrabile, calendar și condiții.</span></div>
      <div><b>2. Deschidem contul</b><span>Dacă firma nu are cont AWS, îl creăm împreună într-o ședință online de 30–45 de minute, pe numele firmei și cu autentificare în doi pași.</span></div>
      <div><b>3. Acceptați oferta</b><span>Vă trimitem oferta privată. O acceptați din contul AWS; descrierea lucrării este atașată ofertei.</span></div>
      <div><b>4. Livrare</b><span>Livrăm în etape. Lunar primiți raportul, fișa de ore și procesul-verbal de semnat.</span></div>
    </div>
    <p class="source">Amazon Web Services, AWS și AWS Marketplace sunt mărci ale Amazon.com, Inc. sau ale afiliaților săi. LAMS este vânzător independent și nu este susținut de Amazon.</p>
  </div>
</section>"""

    funding = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">Granturi pentru digitalizare</p>
    <h1>Folosiți fondurile europene pentru digitalizare, <span class="accent">fără să riscați proiectul</span>.</h1>
    <p class="lead">Programele regionale 2021–2027 finanțează digitalizarea întreprinderilor mici și mijlocii. Verificăm eligibilitatea, pregătim partea tehnică și putem livra software-ul, dacă suntem aleși furnizor.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Apelurile pe care le urmărim</h2>
      <p>Urmărim apelurile pentru digitalizarea întreprinderilor mici și mijlocii din programele regionale 2021–2027, în toate regiunile de dezvoltare.</p>
    </div>
    <ul class="ticks">
      <li><b>Diferă de la o regiune la alta:</b> calendarul de depunere, valoarea grantului, procentul de cofinanțare și sectoarele excluse.</li>
      <li><b>Condiții frecvente:</b> auditul de maturitate digitală înainte de depunere și încadrarea codurilor CAEN în lista eligibilă.</li>
      <li><b>Situația pentru regiunea dumneavoastră:</b> o primiți la cerere, verificată pe ghidul oficial în vigoare. <a href="#contact">Cereți situația actualizată →</a></li>
    </ul>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="cols3">
      <div><h3>Eligibilitate</h3><p>Verificăm codurile CAEN, mărimea și regiunea față de ghidul solicitantului, inclusiv sectoarele excluse.</p></div>
      <div><h3>Pregătire tehnică</h3><p>Auditul de maturitate digitală, specificațiile și un buget realist pentru software, gata pentru cerere.</p></div>
      <div><h3>Implementare</h3><p>Dacă suntem aleși furnizor, livrăm software-ul și documentele cerute de autoritatea de management.</p></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <p class="label">Regulile noastre</p>
    <ul class="ticks">
      <li><b>Un singur rol pe proiect.</b> Într-un proiect cu grant suntem fie consultant, fie furnizor, niciodată amândouă, cum cer regulile privind conflictul de interese.</li>
      <li><b>Nu promitem finanțarea.</b> Decizia aparține autorității de management. Vă spunem cinstit dacă o cerere are șanse.</li>
      <li><b>Calendarul contează.</b> Apelurile au ferestre fixe. Vă spunem de la început dacă termenele se potrivesc și ce faceți dacă nu.</li>
    </ul>
  </div>
</section>"""

    privacy = """
<section class="section" style="padding-top:56px">
  <div class="wrap legal">
    <h1>Politica de confidențialitate</h1>
    <p>LAMS respectă confidențialitatea tuturor celor care ne contactează. Această politică arată cum tratăm datele personale primite prin acest site.</p>
    <h2>Ce date colectăm</h2>
    <p>Doar ce ne trimiteți prin formularul de contact sau pe email: numele, firma, emailul de serviciu, țara și conținutul mesajului. Dacă sunteți de acord, înregistrăm și acordul pentru informări ocazionale.</p>
    <h2>Cum le folosim</h2>
    <p>Ca să răspundem solicitării și să pregătim o propunere, ca demersuri făcute la cererea dumneavoastră (art. 6 alin. (1) lit. b) GDPR). Doar cu acordul dumneavoastră, ca să trimitem informări ocazionale despre creștere, digitalizare, conformitate și granturi (art. 6 alin. (1) lit. a) GDPR). Nu vindem datele și nu le transmitem în scop de marketing terților.</p>
    <h2>Cookie-uri și urmărire</h2>
    <p>Site-ul nu folosește cookie-uri de analiză, de publicitate sau de urmărire.</p>
    <h2>Furnizori de servicii</h2>
    <p>Folosim furnizori selectați pentru găzduire, livrarea formularelor și email, obligați prin clauze de prelucrare a datelor. Când datele sunt prelucrate în afara Spațiului Economic European, transferul se bazează pe garanții adecvate, precum clauzele contractuale standard ale Comisiei Europene sau Cadrul UE–SUA privind protecția datelor.</p>
    <h2>Păstrare</h2>
    <p>Datele unei solicitări se păstrează cel mult 24 de luni de la ultimul contact, dacă nu urmează o colaborare. Dovada acordului se păstrează cât timp trebuie să o putem demonstra.</p>
    <h2>Drepturile dumneavoastră</h2>
    <p>Puteți cere accesul la date, rectificarea sau ștergerea lor, restricționarea prelucrării și portabilitatea, și vă puteți opune prelucrării. Puteți retrage oricând acordul, fără efect asupra prelucrării anterioare. Puteți depune plângere la autoritatea de protecție a datelor din țara dumneavoastră; în România, ANSPDCP.</p>
    <h2>Colaborări cu clienții</h2>
    <p>Informațiile primite într-o colaborare sunt protejate prin acord de confidențialitate și, când includ date personale, prin acord de prelucrare a datelor conform art. 28 GDPR.</p>
    <h2>Contact</h2>
    <p>Operator de date: LAMS Capital Invest LLC. Pentru orice solicitare: <a href="mailto:info@lamscapital.com">info@lamscapital.com</a>.</p>
  </div>
</section>"""

    terms = """
<section class="section" style="padding-top:56px">
  <div class="wrap legal">
    <h1>Termeni de utilizare</h1>
    <p>Acești termeni se aplică utilizării lamscapital.com, operat de LAMS Capital Invest LLC („LAMS”).</p>
    <h2>Informare</h2>
    <p>Conținutul site-ului are caracter general. Nu constituie consultanță juridică, fiscală sau de securitate pentru o situație anume. Rezumatele legilor și regulilor de finanțare reflectă interpretarea noastră la data publicării.</p>
    <h2>Colaborări</h2>
    <p>Nimic de pe site nu reprezintă o ofertă. Orice colaborare este guvernată exclusiv de un contract semnat sau de o ofertă privată acceptată, împreună cu descrierea lucrării.</p>
    <h2>Proprietate intelectuală</h2>
    <p>Textele, numele și logo-ul LAMS și designul site-ului aparțin LAMS. Celelalte nume și mărci aparțin proprietarilor lor; menționarea lor nu înseamnă parteneriat sau susținere.</p>
    <h2>Răspundere</h2>
    <p>Avem grijă ca site-ul să fie corect și disponibil. În limita permisă de lege, LAMS nu răspunde pentru decizii luate doar pe baza conținutului său.</p>
    <h2>Contact</h2>
    <p><a href="mailto:info@lamscapital.com">info@lamscapital.com</a></p>
  </div>
</section>"""

    approach = f"""
<section class="hero">
  <div class="wrap">
    <p class="kicker">Cum lucrăm</p>
    <h1>O metodă pe care o puteți verifica <span class="accent">săptămână de săptămână</span>.</h1>
    <p class="lead">Fiecare colaborare are aceeași structură: un început cu perimetru fix, livrabile scrise la termene stabilite și aprobare înainte de etapa următoare. Mai jos vedeți ce primiți, când și cum arată.</p>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Diagnosticul strategic: cinci săptămâni</h2>
      <p>Construit pe cifrele firmei, sub acord de confidențialitate semnat înainte de orice informație.</p>
    </div>
    <div class="steps light">
      <div><b>Săptămâna 1</b><span>Întâlnirea de start cu conducerea, lista de date, interviuri cu cei care conduc vânzările, achizițiile, depozitul și financiarul.</span></div>
      <div><b>Săptămâna 2</b><span>Performanța: marja pe produs, client și canal; banii blocați în stoc și în creanțe.</span></div>
      <div><b>Săptămâna 3</b><span>Piața și canalele: unde câștigați, unde pierdeți și ce oferă concurența, la ce nivel de serviciu.</span></div>
      <div><b>Săptămâna 4</b><span>Operațiunile și oportunitățile: unde se pierd timp și bani, fiecare oportunitate dimensionată și ordonată.</span></div>
      <div><b>Săptămâna 5</b><span>Indicatorii și planul pe 12 luni, cu responsabili, termene și buget, prezentate conducerii și aprobate.</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Software și automatizări: etape scurte</h2>
      <p>Nimic nu intră în funcțiune fără acceptul dumneavoastră. Fiecare etapă se încheie cu un proces-verbal de predare semnat.</p>
    </div>
    <div class="steps light">
      <div><b>Perimetru</b><span>Procesele descrise așa cum funcționează azi, specificația scrisă și planul de etape, aprobate de dumneavoastră.</span></div>
      <div><b>Construcție</b><span>Livrare în etape de două până la patru săptămâni, fiecare testată pe datele firmei înainte de acceptare.</span></div>
      <div><b>Punere în funcțiune</b><span>Migrarea datelor, instruirea utilizatorilor și o perioadă de lucru în paralel, ca activitatea să nu se oprească.</span></div>
      <div><b>Suport</b><span>Abonament lunar: corecturi, actualizări, raport lunar scris și fișă de ore.</span></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Cum arată un livrabil</h2>
      <p>Două extrase, ca să judecați nivelul de detaliu înainte să vorbim.</p>
    </div>
    <p class="ill">Exemplu ilustrativ. Firmă-model: distribuitor cu 35 de angajați. Cifrele nu provin de la un client.</p>
    <div class="sample-wrap">
      <table class="sample">
        <caption>Din planul pe 12 luni</caption>
        <thead><tr><th>Măsură</th><th>Responsabil</th><th>Termen</th><th>Indicator</th></tr></thead>
        <tbody>
          <tr><td>Un singur sistem pentru comenzi, stoc și facturare; fără dublă introducere</td><td>Directorul operațional</td><td>Luna 3</td><td>Timpul de la comandă la factură</td></tr>
          <tr><td>Revizuirea celor 20 de clienți cu marja cea mai mică; termene de plată noi</td><td>Directorul de vânzări</td><td>Luna 2</td><td>Marja pe client, zile de încasare</td></tr>
          <tr><td>Stocul mai vechi de 180 de zile, lichidat printr-un canal dedicat</td><td>Achiziții</td><td>Luna 4</td><td>Valoarea stocului cu mișcare lentă</td></tr>
        </tbody>
      </table>
    </div>
    <div class="sample-wrap">
      <table class="sample">
        <caption>Din registrul de riscuri NIS2</caption>
        <thead><tr><th>Risc</th><th>Nivel</th><th>Măsură</th><th>Responsabil și termen</th></tr></thead>
        <tbody>
          <tr><td>Serverul de contabilitate fără copie de rezervă offline testată</td><td>Ridicat</td><td>Copie zilnică offline, test de restaurare trimestrial</td><td>IT, 30 de zile</td></tr>
          <tr><td>Cont de administrator folosit în comun</td><td>Ridicat</td><td>Conturi personale, cu autentificare în doi pași</td><td>IT, 14 zile</td></tr>
          <tr><td>Furnizor critic fără clauze de securitate</td><td>Mediu</td><td>Anexă la contract și chestionar anual</td><td>Achiziții, 60 de zile</td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head">
      <h2>Situații pe care ni se cere să le rezolvăm</h2>
      <p>Problemele care aduc firmele la noi și cum le abordăm.</p>
    </div>
    <div class="cols3">
      <div><h3>Creștere fără marjă</h3><p>Cifra de afaceri crește, banii nu. Arătăm marja pe client, produs și canal și ce vânzări costă mai mult decât aduc.</p></div>
      <div><h3>Aceeași comandă, tastată de trei ori</h3><p>Excelul, depozitul și contabilitatea nu comunică. Punem comenzile, stocul și facturarea într-un singur sistem, legat de e-Factura.</p></div>
      <div><h3>Vânzări pe marketplace, erori de stoc</h3><p>Vânzări pe mai multe canale, stoc actualizat de mână. Sincronizăm stocul și automatizăm facturarea între magazin și marketplace-uri.</p></div>
      <div><h3>Chestionar de securitate de la un client important</h3><p>Un client mare cere dovezi ale măsurilor de securitate cibernetică. Pregătim răspunsurile și dovezile din spatele lor.</p></div>
      <div><h3>Muncă repetitivă care nu mai ține pasul</h3><p>Comenzi, documente și rapoarte procesate de mână. Automatizăm întâi procesul cu cel mai bun randament și măsurăm economia.</p></div>
      <div><h3>O investiție care are nevoie de finanțare</h3><p>Un proiect de digitalizare prea mare pentru resursele proprii. Verificăm eligibilitatea și pregătim partea tehnică a cererii.</p></div>
    </div>
  </div>
</section>"""

    return {
        "approach": ("Cum lucrăm", "Cum lucrează LAMS: diagnosticul strategic în cinci săptămâni, livrarea software în etape, exemple de livrabile și situațiile pe care le rezolvăm.", approach, True),
        "home": ("LAMS · Strategie, software și automatizare pentru firme în creștere",
                 "Diagnostic strategic, ERP, e-Factura, e-commerce, automatizare și AI pentru firme mici și mijlocii, plus conformitate NIS2 și granturi. Pachete cu perimetru fix, un singur partener responsabil.", home, True),
        "nis2": ("Conformitate NIS2 pentru firme mijlocii",
                 "Intră firma sub NIS2? Încadrare, analiză de risc, politici, procedură de incident și pregătirea auditului DNSC în 6–8 săptămâni.", nis2, True),
        "packages": ("Pachete",
                     "Pachete cu perimetru fix: diagnostic strategic, Gestiune & e-Factura, Automatizare & AI, Integrare e-commerce, ERP și NIS2 Conform.", packages, True),
        "aws": ("AWS Marketplace",
                "Cumpărați consultanța și software-ul LAMS ca ofertă privată pe AWS Marketplace, facturată firmei de Amazon Web Services.", aws, True),
        "funding": ("Granturi pentru digitalizare",
                    "Cum ajută LAMS firmele mici și mijlocii să folosească fondurile europene pentru digitalizare: eligibilitate, pregătire tehnică și implementare.", funding, True),
        "privacy": ("Politica de confidențialitate", "Cum prelucrează LAMS Capital Invest LLC datele personale colectate prin lamscapital.com.", privacy, False),
        "terms": ("Termeni de utilizare", "Termenii de utilizare ai lamscapital.com.", terms, False),
    }


def pkd(tag, title, who, items, duration, price, note, link, link_label):
    lis = "".join(f"<li>{i}</li>" for i in items)
    extra = f'<dt>Notă</dt><dd>{note}</dd>' if note else ""
    more = f'<dt>Detalii</dt><dd><a href="{link}">{link_label} →</a></dd>' if link else ""
    return f"""<div class="pkd">
      <div><p class="tag">{tag}</p><h2>{title}</h2><p class="for">{who}</p></div>
      <dl><dt>Include</dt><dd><ul>{lis}</ul></dd><dt>Durată</dt><dd>{duration}</dd>{extra}{more}</dl>
    </div>"""

CHECK = {
    "label": "Autoverificare NIS2",
    "title": "Intrați sub NIS2? Cinci întrebări, un minut.",
    "intro": "Un răspuns orientativ, după regulile de mărime și sector ale legii. Nimic din ce bifați nu este trimis sau salvat.",
    "q": [
        ("sector", "Ce descrie cel mai bine activitatea principală?", [
            ("a1", "Energie, transport, bănci, sănătate, apă sau infrastructură digitală"),
            ("a2", "Alimentar, industria prelucrătoare, chimice, poștă și curierat, deșeuri sau servicii digitale"),
            ("a3", "Niciuna dintre acestea"),
        ]),
        ("size", "Cât de mare este firma, inclusiv grupul din care face parte?", [
            ("s1", "Sub 50 de angajați și sub 10 mil. EUR cifră de afaceri"),
            ("s2", "50–249 de angajați sau 10–50 mil. EUR cifră de afaceri"),
            ("s3", "250 de angajați sau mai mulți, sau peste 50 mil. EUR cifră de afaceri"),
        ]),
        ("chain", "Vă trimit clienții mari chestionare de securitate sau clauze contractuale?", [("yes", "Da"), ("no", "Nu")]),
        ("reg", "Este firma înregistrată la DNSC?", [("yes", "Da"), ("no", "Nu"), ("unsure", "Nu știu")]),
        ("inc", "Aveți o procedură scrisă de incident, testată?", [("yes", "Da"), ("no", "Nu")]),
    ],
    "submit": "Vedeți rezultatul",
    "missing": "Răspundeți la toate cele cinci întrebări ca să vedeți rezultatul.",
    "out_t": "Probabil NIS2 nu vi se aplică direct.",
    "out_b": "Excepția: firmele desemnate de DNSC drept critice, indiferent de mărime.",
    "ess_t": "Probabil sunteți entitate esențială.",
    "ess_b": "Regimul cel mai strict: control proactiv al DNSC și amenzi de până la 10 mil. EUR sau 2% din cifra de afaceri mondială.",
    "imp_t": "Probabil sunteți entitate importantă.",
    "imp_b": "Aceleași măsuri de securitate, control după incidente sau sesizări și amenzi de până la 7 mil. EUR sau 1,4% din cifra de afaceri mondială.",
    "gap_reg_no": "Înregistrarea la DNSC pare restantă. Este primul lucru pe care îl verifică un control; DNSC amendează întâi firmele neînregistrate.",
    "gap_reg_unsure": "Verificați dacă firma este înregistrată la DNSC; termenul este de 30 de zile de la intrarea sub incidența legii.",
    "gap_inc": "Procedura de incident netestată este o lipsă: avertizarea timpurie de 24 de ore curge de la descoperirea incidentului.",
    "gap_chain": "Clienții dumneavoastră aplică deja NIS2 furnizorilor. Răspunsuri clare la chestionare protejează aceste contracte.",
    "gaps": "Ce verificați întâi",
    "cta": "Cereți verificarea completă",
    "note": "Rezultat orientativ, nu opinie juridică. Răspunsul exact depinde de codurile CAEN, de grupul de firme și de lege.",
    "msg": "Rezultatul autoverificării NIS2: ",
}
