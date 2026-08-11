async function loadAdvice() {
  const box = document.getElementById('advice');
  try {
    const response = await fetch('/api/frase');
    const data = await response.json();
    box.textContent = data.advice;
  } catch (_) {
    box.textContent = 'Continue avançando, uma tarefa de cada vez.';
  }
}
document.addEventListener('DOMContentLoaded', () => { loadAdvice(); document.getElementById('newAdvice')?.addEventListener('click', loadAdvice); });
