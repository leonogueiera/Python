async function loadProgress() {
  const response = await fetch('/api/tarefas');
  const tasks = await response.json();
  const counts = { pendente: 0, em_andamento: 0, concluida: 0 };
  tasks.forEach(t => counts[t.status]++);
  new Chart(document.getElementById('progressChart'), {
    type: 'bar',
    data: { labels: ['Pendente', 'Em andamento', 'Concluída'], datasets: [{ label: 'Quantidade de tarefas', data: [counts.pendente, counts.em_andamento, counts.concluida], borderWidth: 1 }] },
    options: { responsive: true, maintainAspectRatio: false, scales: { y: { beginAtZero: true, ticks: { precision: 0 } } } }
  });
  const list = document.getElementById('taskList');
  list.innerHTML = tasks.length ? tasks.map(t => `<div class="col-md-6"><div class="border rounded p-3"><strong>${escapeHtml(t.titulo)}</strong><div class="small text-secondary">${label(t.status)}</div></div></div>`).join('') : '<div class="col-12 text-secondary">Nenhuma tarefa cadastrada.</div>';
}
function label(s) { return s === 'pendente' ? 'Pendente' : s === 'em_andamento' ? 'Em andamento' : 'Concluída'; }
function escapeHtml(value) { return String(value).replace(/[&<>'"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;',"'":'&#39;','"':'&quot;'}[c])); }
document.addEventListener('DOMContentLoaded', loadProgress);
