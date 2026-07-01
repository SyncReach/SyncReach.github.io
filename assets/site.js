/* SyncReach — shared site JS: injects the brand mark + globe motif and small glyphs.
   Any element with these data-attrs gets the SVG injected on load. */
(function(){
  var MARK = '<svg viewBox="0 0 100 100" fill="none" aria-hidden="true"><g stroke="currentColor" stroke-width="4" stroke-linecap="round"><circle cx="50" cy="50" r="44"/><line x1="50" y1="6" x2="50" y2="94"/><ellipse cx="50" cy="50" rx="22" ry="44"/><line x1="6" y1="50" x2="94" y2="50"/><line x1="11.34" y1="29" x2="88.66" y2="29"/><line x1="11.34" y1="71" x2="88.66" y2="71"/><line x1="19.8" y1="18" x2="80.2" y2="18"/><line x1="19.8" y1="82" x2="80.2" y2="82"/></g></svg>';
  var GLOBE = '<svg viewBox="0 0 400 400" fill="none" aria-hidden="true"><g stroke="currentColor" stroke-width="1" stroke-linecap="round"><circle cx="200" cy="200" r="190"/><circle cx="200" cy="200" r="150"/><circle cx="200" cy="200" r="100"/><circle cx="200" cy="200" r="50"/><line x1="200" y1="10" x2="200" y2="390"/><line x1="10" y1="200" x2="390" y2="200"/><ellipse cx="200" cy="200" rx="95" ry="190"/><ellipse cx="200" cy="200" rx="160" ry="190"/><ellipse cx="200" cy="200" rx="190" ry="95"/><ellipse cx="200" cy="200" rx="190" ry="160"/><line x1="32" y1="120" x2="368" y2="120"/><line x1="32" y1="280" x2="368" y2="280"/><line x1="58" y1="70" x2="342" y2="70"/><line x1="58" y1="330" x2="342" y2="330"/><line x1="120" y1="32" x2="120" y2="368"/><line x1="280" y1="32" x2="280" y2="368"/></g></svg>';
  var CHECK = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>';
  var ARROW = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>';
  function fill(sel, svg){ document.querySelectorAll(sel).forEach(function(el){ el.innerHTML = svg; }); }
  fill('[data-globe-mark]', MARK);
  fill('[data-globe]', GLOBE);
  fill('[data-check]', CHECK);
  fill('[data-arrow]', ARROW);

  /* ---- Cookie consent banner ----
     Stores choice in localStorage ('sr-cookie-consent' = 'accepted' | 'declined').
     Shows once until a choice is made. Wire your analytics to load only when accepted:
       if (localStorage.getItem('sr-cookie-consent') === 'accepted') { loadAnalytics(); }
  */
  (function(){
    var KEY = 'sr-cookie-consent';
    try { if (localStorage.getItem(KEY)) return; } catch(e){ return; }

    var CSS = ''
      + '.sr-cookie{position:fixed;left:16px;right:16px;bottom:16px;z-index:9999;max-width:680px;margin:0 auto;'
      + 'background:var(--surface-inverse,#02020E);color:var(--text-on-inverse,#EDEAE0);'
      + 'border:1px solid var(--border-inverse-strong,#3A3C52);border-radius:var(--radius-md,6px);'
      + 'box-shadow:0 12px 32px -8px rgba(12,13,23,0.5);'
      + 'display:flex;align-items:center;gap:18px;padding:16px 18px;'
      + "font-family:var(--font-sans),system-ui,sans-serif;"
      + 'transform:translateY(140%);transition:transform .4s cubic-bezier(0.16,1,0.3,1);}'
      + '.sr-cookie.in{transform:translateY(0);}'
      + '.sr-cookie__txt{flex:1;font-size:13.5px;line-height:1.55;color:var(--text-on-inverse-muted,#9A9FB8);}'
      + '.sr-cookie__txt b{color:var(--text-on-inverse,#EDEAE0);font-weight:600;}'
      + '.sr-cookie__txt a{color:var(--text-on-inverse-accent,#E5483D);text-underline-offset:2px;}'
      + '.sr-cookie__btns{display:flex;gap:9px;flex:none;}'
      + '.sr-cookie__b{font-family:var(--font-sans),system-ui,sans-serif;font-weight:600;font-size:13px;'
      + 'height:38px;padding:0 14px;border-radius:var(--radius-xs,2px);cursor:pointer;white-space:nowrap;'
      + 'border:1px solid transparent;transition:background .12s,border-color .12s,color .12s;}'
      + '.sr-cookie__b--no{background:transparent;color:var(--text-on-inverse,#EDEAE0);border-color:var(--border-inverse-strong,#3A3C52);}'
      + '.sr-cookie__b--no:hover{border-color:var(--text-on-inverse-muted,#9A9FB8);}'
      + '.sr-cookie__b--yes{background:var(--brand-red,#840902);color:#FFFDF6;border-color:var(--brand-red,#840902);}'
      + '.sr-cookie__b--yes:hover{background:#6E0701;border-color:#6E0701;}'
      + '.sr-cookie__b:focus-visible{outline:2px solid var(--text-on-inverse-accent,#E5483D);outline-offset:2px;}'
      + '@media (max-width:560px){.sr-cookie{flex-direction:column;align-items:stretch;gap:13px;}.sr-cookie__btns{justify-content:flex-end;}}'
      + '@media (prefers-reduced-motion:reduce){.sr-cookie{transition:none;}}';

    var style = document.createElement('style');
    style.textContent = CSS;
    document.head.appendChild(style);

    var bar = document.createElement('div');
    bar.className = 'sr-cookie';
    bar.setAttribute('role', 'dialog');
    bar.setAttribute('aria-label', 'Cookie notice');
    bar.innerHTML = ''
      + '<div class="sr-cookie__txt"><b>We use cookies.</b> We use cookies to run this site and understand how it&rsquo;s used. '
      + 'See our <a href="privacy.html">Privacy Policy</a>.</div>'
      + '<div class="sr-cookie__btns">'
      + '<button type="button" class="sr-cookie__b sr-cookie__b--no" data-cc="declined">Decline</button>'
      + '<button type="button" class="sr-cookie__b sr-cookie__b--yes" data-cc="accepted">Accept</button>'
      + '</div>';

    function mount(){
      document.body.appendChild(bar);
      requestAnimationFrame(function(){ requestAnimationFrame(function(){ bar.classList.add('in'); }); });
    }
    if (document.body) mount(); else document.addEventListener('DOMContentLoaded', mount);

    bar.addEventListener('click', function(e){
      var b = e.target.closest('[data-cc]');
      if (!b) return;
      try { localStorage.setItem(KEY, b.getAttribute('data-cc')); } catch(err){}
      bar.classList.remove('in');
      setTimeout(function(){ bar.remove(); }, 420);
    });
  })();
})();
