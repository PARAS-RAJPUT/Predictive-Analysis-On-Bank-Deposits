// Dark mode toggle with persistence
const body = document.body;
const toggle = document.getElementById('theme-toggle');
const storedTheme = localStorage.getItem('theme');

// Initialize theme on page load
if (storedTheme === 'dark') {
  body.classList.add('dark');
  if (toggle) toggle.checked = true;
} else {
  if (toggle) toggle.checked = false;
}

// Handle toggle changes
if (toggle) {
  toggle.addEventListener('change', () => {
    if (toggle.checked) {
      body.classList.add('dark');
      localStorage.setItem('theme', 'dark');
    } else {
      body.classList.remove('dark');
      localStorage.setItem('theme', 'light');
    }
  });
}

// Smooth scroll for nav links
document.querySelectorAll('a[href^=\"#\"]').forEach(anchor => {
  anchor.addEventListener('click', e => {
    const target = document.querySelector(anchor.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
  });
});

// Predict form handler
const predictForm = document.getElementById('predict-form');
const predictResult = document.getElementById('predict-result');
if (predictForm) {
  predictForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(predictForm);
    const payload = Object.fromEntries(formData.entries());
    predictResult.innerHTML = '<div class=\"text-center text-slate-500\">Predicting...</div>';
    try {
      const res = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      predictResult.innerHTML = `
        <div class=\"p-4 rounded-2xl glass shadow-soft\">
          <div class=\"flex items-center justify-between\">
            <div>
              <p class=\"text-sm uppercase tracking-wide text-slate-500\">Predicted Deposit</p>
              <p class=\"text-3xl font-bold\">$${data.predicted_deposit}</p>
              <p class=\"text-sm mt-2 text-slate-500\">Confidence: ${(data.confidence * 100).toFixed(1)}%</p>
            </div>
            <span class=\"metric-chip\">${data.model_name}</span>
          </div>
          <p class=\"mt-3 text-sm text-slate-600 dark:text-slate-300\">${data.interpretation}</p>
        </div>
      `;
    } catch (err) {
      predictResult.innerHTML = '<div class=\"text-red-500\">Unable to predict right now.</div>';
    }
  });
}

// Animated charts with Chart.js where canvases exist
const chartConfigs = {
  'results-chart': {
    type: 'bar',
    data: {
      labels: ['Linear', 'Random Forest', 'Gradient Boost', 'SVR', 'KNN'],
      datasets: [{
        label: 'R² Score',
        data: [0.82, 0.91, 0.89, 0.85, 0.84],
        backgroundColor: ['#6366f1', '#22c55e', '#f59e0b', '#3b82f6', '#ec4899']
      }]
    },
    options: { responsive: true, animation: { duration: 1200 } }
  },
  'cluster-chart': {
    type: 'doughnut',
    data: {
      labels: ['Cluster A', 'Cluster B', 'Cluster C'],
      datasets: [{
        data: [45, 35, 20],
        backgroundColor: ['#22d3ee', '#a78bfa', '#fb7185']
      }]
    },
    options: { responsive: true, animation: { duration: 1200 } }
  }
};

Object.entries(chartConfigs).forEach(([id, cfg]) => {
  const ctx = document.getElementById(id);
  if (ctx && window.Chart) {
    new Chart(ctx, cfg);
  }
});

