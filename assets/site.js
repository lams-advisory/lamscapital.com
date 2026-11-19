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
