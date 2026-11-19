(function(){
  // Mobile menu
  var btn=document.querySelector('.menu-btn'), nav=document.getElementById('nav');
  if(btn&&nav){btn.addEventListener('click',function(){var o=nav.classList.toggle('open');btn.setAttribute('aria-expanded',o?'true':'false');});}

  // Contact form
  var f=document.getElementById('cf'); if(!f) return;
  var err=document.getElementById('f-err'), lang=document.documentElement.lang||'en';
  var T={
    en:{fill:'Fill in your name, company, work email and message to send.',mail:'Enter a valid email address.',preview:'Preview only: the form sends once the site is live at lamscapital.com.',thanks:'Thank you. Your message has been received, and we will reply within two business days.'},
    ro:{fill:'Completați numele, firma, emailul de serviciu și mesajul.',mail:'Introduceți o adresă de email validă.',preview:'Previzualizare: formularul trimite doar pe lamscapital.com.',thanks:'Mulțumim. Am primit mesajul și vă răspundem în cel mult două zile lucrătoare.'}
  }[lang]||{};
  f.addEventListener('input',function(){err.textContent='';});
  f.addEventListener('submit',function(e){
    var v=function(n){return (f.elements[n]&&f.elements[n].value||'').trim();};
    if(!v('name')||!v('company')||!v('email')||!v('message')){e.preventDefault();err.textContent=T.fill;return;}
    if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v('email'))){e.preventDefault();err.textContent=T.mail;return;}
    var c=f.elements['marketing_consent'], ts=f.elements['consent_timestamp'], pg=f.elements['page'];
    if(ts) ts.value=(c&&c.checked)?new Date().toISOString():'';
    if(pg) pg.value=location.href;
    if(!/(^|\.)lamscapital\.com$/.test(location.hostname)){e.preventDefault();err.textContent=T.preview;}
  });
  if(location.hash==='#thanks'){
    var box=document.querySelector('#contact .form-box');
    if(box){box.innerHTML='<p class="thanks"></p>';box.firstChild.textContent=T.thanks;}
    var s=document.getElementById('contact'); if(s) s.scrollIntoView();
  }
})();

// NIS2 self-check (runs in the browser only; nothing is sent)
(function(){
  var f=document.getElementById('nis2-check'); if(!f) return;
  var T=JSON.parse(document.getElementById('nis2-texts').textContent);
  var out=document.getElementById('nis2-result'), err=document.getElementById('check-err');
  function val(n){var r=f.querySelector('input[name="'+n+'"]:checked');return r?r.value:'';}
  function el(tag,cls,text){var e=document.createElement(tag);if(cls)e.className=cls;if(text)e.textContent=text;return e;}
  f.addEventListener('change',function(){err.textContent='';});
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var a={sector:val('sector'),size:val('size'),chain:val('chain'),reg:val('reg'),inc:val('inc')};
    for(var k in a){if(!a[k]){err.textContent=T.missing;return;}}
    var inScope=!(a.sector==='a3'||a.size==='s1');
    var key=!inScope?'out':(a.sector==='a1'&&a.size==='s3'?'ess':'imp');
    var gaps=[];
    if(inScope&&a.reg==='no')gaps.push(T.gap_reg_no);
    if(inScope&&a.reg==='unsure')gaps.push(T.gap_reg_unsure);
    if(inScope&&a.inc==='no')gaps.push(T.gap_inc);
    if(a.chain==='yes')gaps.push(T.gap_chain);
    out.innerHTML='';
    out.className='result '+key;
    out.appendChild(el('h3',null,T[key+'_t']));
    out.appendChild(el('p',null,T[key+'_b']));
    if(gaps.length){
      out.appendChild(el('p','gaps-h',T.gaps));
      var ul=el('ul','ticks');gaps.forEach(function(g){ul.appendChild(el('li',null,g));});out.appendChild(ul);
    }
    var cta=el('a','btn primary',T.cta);cta.href='#contact';out.appendChild(cta);
    out.appendChild(el('p','source',T.note));
    out.hidden=false;out.focus({preventScroll:true});out.scrollIntoView({behavior:'smooth',block:'start'});
    cta.addEventListener('click',function(){
      var m=document.getElementById('f-msg'), t=document.getElementById('f-topic');
      if(m&&!m.value){m.value=T.msg+T[key+'_t']+(gaps.length?' '+gaps.join(' '):'');}
      if(t&&t.options.length){t.selectedIndex=0;}
    });
  });
})();
