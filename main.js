(() => {
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const calm = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Barre de progression en haut */
  const bar = document.querySelector('.progress');
  const onScroll = () => {
    const h = document.documentElement;
    bar && bar.style.setProperty('--p', (h.scrollTop / Math.max(1, h.scrollHeight - h.clientHeight)).toFixed(4));
  };
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* Vue ordinateur / téléphone des sites livrés */
  $$('[data-view-btn]').forEach((b) => b.addEventListener('click', () => {
    const shot = b.closest('.venture').querySelector('.v-shot');
    const phone = shot.dataset.view !== 'phone';
    shot.dataset.view = phone ? 'phone' : 'desk';
    b.textContent = phone ? b.dataset.desk : b.dataset.phone;
    b.setAttribute('aria-pressed', phone);
  }));

  /* Aperçu qui suit la souris sur les lignes de projets */
  $$('.row').forEach((row) => {
    const pv = row.querySelector('.preview');
    if (!pv) return;
    row.querySelector('summary').addEventListener('mousemove', (e) => {
      const r = row.getBoundingClientRect();
      pv.style.setProperty('--x', Math.min(e.clientX - r.left + 28, r.width - 360) + 'px');
      pv.style.setProperty('--y', (e.clientY - r.top - 60) + 'px');
    });
  });

  /* Formulaire : ouvre l'e-mail avec le message déjà rempli */
  const form = document.querySelector('.c-form');
  form && form.addEventListener('submit', (e) => {
    e.preventDefault();
    if (!form.reportValidity()) return;
    const d = new FormData(form);
    const subject = d.get('sujet') || 'Portfolio';
    const body = `${d.get('message')}\n\n${d.get('nom')} · ${d.get('email')}`;
    location.href = `mailto:${form.dataset.mailto}?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
  });

  /* Apparitions */
  const els = $$('[data-rise]');
  if ('IntersectionObserver' in window && !calm) {
    const io = new IntersectionObserver((ents) => ents.forEach((en) => {
      if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); }
    }), { rootMargin: '0px 0px -6% 0px' });
    els.forEach((el) => io.observe(el));
  } else els.forEach((el) => el.classList.add('in'));
})();
