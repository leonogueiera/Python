(() => {
  const root = document.documentElement;
  const saved = localStorage.getItem('theme') || 'light';
  root.setAttribute('data-bs-theme', saved);
  const button = document.getElementById('themeToggle');
  if (!button) return;
  const update = () => {
    const dark = root.getAttribute('data-bs-theme') === 'dark';
    button.innerHTML = dark ? '<i class="bi bi-sun"></i>' : '<i class="bi bi-moon-stars"></i>';
    button.title = dark ? 'Ativar modo claro' : 'Ativar modo escuro';
  };
  update();
  button.addEventListener('click', () => {
    const next = root.getAttribute('data-bs-theme') === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-bs-theme', next);
    localStorage.setItem('theme', next);
    update();
  });
})();
