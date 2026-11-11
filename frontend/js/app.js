// ALPHA AI — logika frontend (vanilla JavaScript)

const API_BASE = "/api";

/* ---------- Halaman Generator (index.html) ---------- */
function initGenerator() {
  const form = document.getElementById("generate-form");
  if (!form) return;

  const promptEl = document.getElementById("prompt");
  const button = document.getElementById("generate-btn");
  const charCount = document.getElementById("char-count");
  const resultCard = document.getElementById("result-card");
  const resultEl = document.getElementById("result");
  const copyBtn = document.getElementById("copy-btn");

  promptEl.addEventListener("input", () => {
    charCount.textContent = `${promptEl.value.length} / ${promptEl.maxLength}`;
  });

  function showResult(text, isError = false) {
    resultEl.textContent = text;
    resultCard.classList.remove("hidden");
    resultCard.classList.toggle("error", isError);
    copyBtn.classList.toggle("hidden", isError);
  }

  form.addEventListener("submit", async (event) => {
    event.preventDefault();
    const prompt = promptEl.value.trim();
    if (!prompt) return;

    button.disabled = true;
    button.textContent = "Sedang membuat...";

    try {
      const response = await fetch(`${API_BASE}/text/generate`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt }),
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok) {
        const detail = typeof data.detail === "string" ? data.detail : "Terjadi kesalahan pada server.";
        showResult(detail, true);
      } else {
        showResult(data.result);
      }
    } catch (error) {
      showResult("Tidak dapat terhubung ke server. Pastikan server sedang berjalan.", true);
    } finally {
      button.disabled = false;
      button.textContent = "Generate";
    }
  });

  copyBtn.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(resultEl.textContent);
      copyBtn.textContent = "Tersalin!";
      setTimeout(() => (copyBtn.textContent = "Salin"), 1500);
    } catch {
      copyBtn.textContent = "Gagal menyalin";
    }
  });
}

/* ---------- Halaman Harga (pricing.html) ---------- */
const PLANS = [
  { name: "Free", price: "$0", features: ["5 generate / bulan", "Model AI dasar"] },
  { name: "Creator", price: "$19", features: ["100 generate / bulan", "Model AI lebih baik", "Dukungan prioritas"], featured: true },
  { name: "Pro", price: "$49", features: ["Generate tanpa batas", "Model AI terbaik", "Akses API"] },
];

function initPricing() {
  const container = document.getElementById("pricing");
  if (!container) return;

  container.innerHTML = PLANS.map((plan) => `
    <article class="plan${plan.featured ? " featured" : ""}">
      <h3>${plan.name}</h3>
      <div class="price">${plan.price}<small>/bulan</small></div>
      <ul>${plan.features.map((f) => `<li>${f}</li>`).join("")}</ul>
      <button class="btn ${plan.featured ? "btn-primary" : "btn-ghost"}" data-plan="${plan.name}">Pilih ${plan.name}</button>
    </article>
  `).join("");

  // Pembayaran belum tersedia; tombol hanya memberi informasi.
  container.addEventListener("click", (event) => {
    const button = event.target.closest("button[data-plan]");
    if (button) alert(`Paket ${button.dataset.plan} segera hadir. Pembayaran belum tersedia.`);
  });
}

document.addEventListener("DOMContentLoaded", () => {
  initGenerator();
  initPricing();
});
