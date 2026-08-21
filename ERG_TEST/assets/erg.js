/* Express Recruiting Group — concept build behaviours.
   Kept deliberately small: no framework, no jQuery. Everything here maps to
   an enqueued script in the WordPress block theme. */
(function () {
  'use strict';

  /* Mobile navigation ---------------------------------------------------- */
  var toggle = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.nav');
  if (toggle && nav) {
    toggle.setAttribute('aria-expanded', 'false');
    toggle.addEventListener('click', function () {
      var open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('is-open')) {
        nav.classList.remove('is-open');
        toggle.setAttribute('aria-expanded', 'false');
        toggle.focus();
      }
    });
  }

  /* Marquee — duplicate the track so the -50% loop is seamless, and stop
     entirely under reduced motion rather than merely slowing it. */
  var track = document.querySelector('.marquee__track');
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (track && !reduce && !track.dataset.cloned) {
    var items = Array.prototype.slice.call(track.children);
    items.forEach(function (node) {
      var copy = node.cloneNode(true);
      copy.setAttribute('aria-hidden', 'true');
      track.appendChild(copy);
    });
    track.dataset.cloned = 'true';
  }

  /* Opportunity filters -------------------------------------------------- */
  var chips = document.querySelectorAll('.chip[data-filter]');
  var roles = document.querySelectorAll('.role[data-area]');
  if (chips.length && roles.length) {
    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        var val = chip.dataset.filter;
        chips.forEach(function (c) { c.setAttribute('aria-pressed', String(c === chip)); });
        roles.forEach(function (role) {
          var show = val === 'all' || role.dataset.area === val;
          role.closest('li').hidden = !show;
        });
        var shown = document.querySelectorAll('.role-list li:not([hidden])').length;
        var count = document.querySelector('[data-result-count]');
        if (count) count.textContent = shown + (shown === 1 ? ' position' : ' positions');
      });
    });
  }

  /* Resume upload — filename feedback. Real handling posts to external
     storage; nothing confidential is ever written to wp-content/uploads. */
  var upload = document.querySelector('[data-upload]');
  if (upload) {
    var input = upload.querySelector('input[type=file]');
    var label = upload.querySelector('[data-upload-label]');
    if (input && label) {
      input.addEventListener('change', function () {
        label.textContent = input.files.length
          ? input.files[0].name
          : 'Drop your resume here, or browse';
      });
    }
  }

  /* SyncReach badge fades out as the credit band arrives ------------------ */
  var badge = document.querySelector('.sr-badge-wrap');
  var credit = document.querySelector('.sr-credit');
  if (badge && credit && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var hide = entry.isIntersecting;
        badge.style.opacity = hide ? '0' : '1';
        badge.style.transform = hide ? 'translateY(10px)' : 'none';
        badge.style.pointerEvents = hide ? 'none' : 'auto';
      });
    }, { threshold: 0.05 });
    io.observe(credit);
  }

  /* Concept-only guard: forms and video cards do not submit or play. */
  document.querySelectorAll('form[data-concept]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      alert('Concept build — this form is not wired to a handler.');
    });
  });
})();
