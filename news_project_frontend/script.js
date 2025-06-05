let selectedCategory = null;

document.querySelectorAll('.category-btn').forEach(btn => {
  btn.addEventListener('click', () => {
    document.querySelectorAll('.category-btn').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    selectedCategory = btn.dataset.category;
  });
});

async function getNews() {
  if (!selectedCategory) {
    alert("Please select a category first!");
    return;
  }

  const count = document.getElementById("count").value;
  let url = `http://localhost:8000/neutralize/${selectedCategory}`;
  if (count) {
    url += `?count=${count}`;
  }

  try {
    const response = await fetch(url);
    const news = await response.json();

    const container = document.getElementById("news-container");
    container.innerHTML = '';

    news.forEach(item => {
      const div = document.createElement("div");
      div.className = "news-item";

      // Handle both object and string items
      let text = typeof item === "object" && item.title ? item.title : String(item).replace(/^"|"$/g, '');

      div.textContent = text;
      container.appendChild(div);
    });

  } catch (error) {
    console.error("Error fetching news:", error);
    alert("Failed to fetch news. Please check the backend.");
  }
}
