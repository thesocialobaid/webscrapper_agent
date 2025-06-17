const scrapeBtn = document.getElementById("scrapeBtn");
const urlInput = document.getElementById("urlInput");
const instructions = document.getElementById("instructions");
const status = document.getElementById("status");
const resultPreview = document.getElementById("resultPreview");
const BACKEND_URL = "https://refactored-space-couscous-wwpvr6jr556fvjgp-8000.app.github.dev"; // No trailing slash

scrapeBtn.addEventListener("click", async () => {
  const url = urlInput.value;
  const prompt = instructions.value;

  if (!url) {
    alert("Please enter a URL.");
    return;
  }

  status.textContent = "Scraping in progress...";

  try {
    const response = await fetch(`${BACKEND_URL}/scrape`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ url, instructions: prompt })
    });

    if (!response.ok) {
      throw new Error(`Server responded with status ${response.status}`);
    }

    const data = await response.json();
    resultPreview.value = JSON.stringify(data, null, 2);
    status.textContent = "✅ Scraping complete.";
  } catch (err) {
    console.error("Error occurred:", err);
    status.textContent = "❌ Error: Could not scrape data.";
  }
});

// PDF/JSON Download Function
function download(type) {
  if (!resultPreview.value.trim()) {
    alert("There's no data to download!");
    return;
  }

  if (type === "pdf") {
    const doc = new window.jspdf.jsPDF();
    const lines = doc.splitTextToSize(resultPreview.value, 180); // Wrap text
    doc.text(lines, 10, 10);
    doc.save("data.pdf");
    return;
  }

  if (type === "json") {
    const blob = new Blob([resultPreview.value], { type: "application/json" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = "data.json";
    a.click();
  }
}
