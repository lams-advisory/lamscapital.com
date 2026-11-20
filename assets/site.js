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

// NIS2 self-check (runs in the browser; answers are sent only if the visitor asks for the report)
(function(){
  var f=document.getElementById('nis2-check'); if(!f) return;
  var T=JSON.parse(document.getElementById('nis2-texts').textContent);
  var out=document.getElementById('nis2-result'), err=document.getElementById('check-err');
  var repBox=document.getElementById('nis2-report'), rep=document.getElementById('nis2-rep'), rerr=document.getElementById('r-err');
  var live=/(^|\.)lamscapital\.com$/.test(location.hostname), last=null;
  function val(n){var r=f.querySelector('input[name="'+n+'"]:checked');return r?r.value:'';}
  function el(tag,cls,text){var e=document.createElement(tag);if(cls)e.className=cls;if(text)e.textContent=text;return e;}
  f.addEventListener('change',function(){err.textContent='';});
  f.addEventListener('submit',function(e){
    e.preventDefault();
    var names=['sector','emp','turn','bal','where','chain','reg','risk','inc','base'], a={};
    for(var i=0;i<names.length;i++){a[names[i]]=val(names[i]);if(!a[names[i]]){err.textContent=T.missing;return;}}
    var large=a.emp==='e3'||(a.turn==='t3'&&a.bal==='b3');
    var small=a.emp==='e1'&&(a.turn==='t1'||a.bal==='b1');
    var key=a.sector==='a3'?'out':a.sector==='a4'?'spec':small?'small':(a.sector==='a1'&&large?'ess':'imp');
    var inScope=(key==='ess'||key==='imp'||key==='spec'), gaps=[];
    if(inScope&&a.reg==='no')gaps.push(T.gap_reg_no);
    if(inScope&&a.reg==='unsure')gaps.push(T.gap_reg_unsure);
    if(inScope&&a.risk==='no')gaps.push(T.gap_risk);
    if(inScope&&a.inc==='no')gaps.push(T.gap_inc);
    if(inScope&&a.base!=='yes')gaps.push(T.gap_base);
    if(a.chain==='yes')gaps.push(T.gap_chain);
    if(a.where==='non')gaps.push(T.gap_non);
    var answers=[];
    [].forEach.call(f.querySelectorAll('fieldset.q'),function(fs){
      var q=fs.querySelector('legend').textContent.replace(/^\d+/,'').trim(), c=fs.querySelector('input:checked');
      answers.push(q+' '+(c?c.parentNode.textContent.trim():''));
    });
    last={key:key,title:T[key+'_t'],body:T[key+'_b'],gaps:gaps,answers:answers};
    out.innerHTML='';
    out.className='result '+key;
    out.appendChild(el('h3',null,last.title));
    out.appendChild(el('p',null,last.body));
    if(gaps.length){
      out.appendChild(el('p','gaps-h',T.gaps));
      var ul=el('ul','ticks');gaps.forEach(function(g){ul.appendChild(el('li',null,g));});out.appendChild(ul);
    }
    var cta=el('a','btn primary',T.cta);cta.href='#contact';out.appendChild(cta);
    out.appendChild(el('p','source',T.note));
    out.hidden=false;out.focus({preventScroll:true});out.scrollIntoView({behavior:'smooth',block:'start'});
    if(repBox){repBox.hidden=false;}
    cta.addEventListener('click',function(){
      var m=document.getElementById('f-msg'), t=document.getElementById('f-topic');
      if(m&&!m.value){m.value=T.msg+last.title+(gaps.length?' '+gaps.join(' '):'');}
      if(t&&t.options.length){t.selectedIndex=0;}
    });
  });
  if(!rep) return;
  rep.addEventListener('input',function(){rerr.textContent='';});
  rep.addEventListener('submit',function(e){
    e.preventDefault();
    if(!last) return;
    var v=function(n){return (rep.elements[n]&&rep.elements[n].value||'').trim();};
    if(!v('name')||!v('company')||!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v('email'))||!rep.elements['report_consent'].checked){rerr.textContent=T.rep_fill;return;}
    if(v('_honey')) return;
    var mk=rep.elements['marketing_consent'].checked, now=new Date().toISOString();
    var text=T.rep_intro+'\n\n'+last.title+'\n'+last.body+'\n\n'+(last.gaps.length?T.gaps+':\n- '+last.gaps.join('\n- ')+'\n\n':'')+T.rep_answers+':\n- '+last.answers.join('\n- ')+'\n\n'+T.rep_outro;
    var d=new FormData();
    d.append('_subject',T.rep_lead);d.append('_template','table');d.append('_captcha','false');
    d.append('_autoresponse',text);
    d.append('name',v('name'));d.append('company',v('company'));d.append('email',v('email'));
    d.append('language',document.documentElement.lang||'en');d.append('page',location.href);
    d.append('result',last.title);d.append('gaps',last.gaps.join(' | '));d.append('answers',last.answers.join(' | '));
    d.append('report_consent','yes ('+now+'): '+T.rep_ok);
    d.append('marketing_consent',mk?'yes':'no');d.append('consent_text',T.rep_mkt);d.append('consent_timestamp',mk?now:'');
    var btn=rep.querySelector('button');
    if(!live){rerr.textContent='Preview only: the report is sent once the site is live at lamscapital.com.';return;}
    btn.disabled=true;rerr.textContent=T.rep_wait;
    fetch('https://formsubmit.co/ajax/info@lamscapital.com',{method:'POST',headers:{'Accept':'application/json'},body:d})
      .then(function(r){return r.json();})
      .then(function(j){if(j&&(j.success===true||j.success==='true')){repBox.innerHTML='';repBox.appendChild(el('p','thanks',T.rep_done));}else{throw 0;}})
      .catch(function(){btn.disabled=false;rerr.textContent=T.rep_fail;});
  });
})();

// Pre-diagnostic form
(function(){
  var f=document.getElementById('pd'); if(!f) return;
  var T=JSON.parse(document.getElementById('pd-texts').textContent), err=document.getElementById('p-err');
  var live=/(^|\.)lamscapital\.com$/.test(location.hostname);
  f.addEventListener('change',function(e){
    err.textContent='';
    if(e.target.getAttribute('data-group')==='problems'&&f.querySelectorAll('[data-group="problems"]:checked').length>3){e.target.checked=false;err.textContent=T.max3;}
  });
  f.addEventListener('submit',function(e){
    var v=function(n){return (f.elements[n]&&f.elements[n].value||'').trim();};
    ['channels','systems','problems'].forEach(function(g){
      f.elements[g].value=[].map.call(f.querySelectorAll('[data-group="'+g+'"]:checked'),function(c){return c.value;}).join(', ');
    });
    if(!v('name')||!v('company')||!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v('email'))||!v('problems')){e.preventDefault();err.textContent=T.fill;return;}
    var c=f.elements['marketing_consent'];f.elements['consent_timestamp'].value=(c&&c.checked)?new Date().toISOString():'';
    if(!live){e.preventDefault();err.textContent=(document.documentElement.lang==='ro'?'Previzualizare: formularul trimite doar pe lamscapital.com.':'Preview only: the form sends once the site is live at lamscapital.com.');}
  });
  if(location.hash==='#thanks'){var b=document.getElementById('pd-box');if(b){b.innerHTML='<p class="thanks"></p>';b.firstChild.textContent=T.thanks;}}
})();
