const slides = [
  {
    src: "ClickUP_dashboard.png",
    title: "Delivery dashboards — ClickUp",
    desc: "Hybrid PMO/engineering control: resources, releases, variance within 3–5%.",
    tags: ["pmo", "delivery", "analytics"]
  },
  {
    src: "ClickUP_dashboard.png 2.png",
    title: "Delivery pipelines — ClickUp",
    desc: "Roadmap and sprint transparency across 12+ teams.",
    tags: ["pmo", "process"]
  },
  {
    src: "Ads grant campaign.png",
    title: "Ads & growth",
    desc: "Grant ad campaign: strategy, creatives, metric tracking.",
    tags: ["growth", "marketing"]
  },
  {
    src: "Website_neobank.png",
    title: "NEOBANK landing",
    desc: "Fintech landing + P2P wallet, organic growth ×4, conversion ×2.",
    tags: ["fintech", "web", "growth"]
  },
  {
    src: "Game.png",
    title: "WebGL game — GTA POV",
    desc: "WebGL + digital goods marketplace, payment gateway PSP.",
    tags: ["gaming", "webgl", "payments"]
  },
  {
    src: "Game 2.png",
    title: "Game UI pack 1",
    desc: "HUD and mission component library.",
    tags: ["gaming", "ui"]
  },
  {
    src: "Game 3.png",
    title: "Game UI pack 2",
    desc: "Inventory and economy screens.",
    tags: ["gaming", "ui"]
  },
  {
    src: "Game 4.png",
    title: "Game UI pack 3",
    desc: "Progress screen and rewards.",
    tags: ["gaming"]
  },
  {
    src: "Game 5.png",
    title: "Game UI pack 4",
    desc: "Digital goods catalogue.",
    tags: ["gaming", "commerce"]
  },
  {
    src: "Game 6.png",
    title: "Game UI pack 5",
    desc: "User profile and order history.",
    tags: ["gaming", "auth"]
  },
  {
    src: "Game 7.png",
    title: "Game UI pack 6",
    desc: "Scene and cutscene layouts.",
    tags: ["gaming"]
  },
  {
    src: "Road_map_template.png",
    title: "Roadmap template",
    desc: "Template for 10+ stream programs, release synchronisation.",
    tags: ["roadmap", "pmo"]
  },
  {
    src: "Seo positions yandex- Google Таблицы — Mozilla .png",
    title: "SEO positions — Yandex & Google",
    desc: "Organic search position tracking across both search engines.",
    tags: ["analytics", "growth", "seo"]
  },
  {
    src: "Monosnap Microsoft Office Picture Manager 2026-03-.png",
    title: "Ops — file tooling",
    desc: "Asset organisation for cross-team collaboration.",
    tags: ["ops"]
  },
  {
    src: "Monosnap New fintech website  — Sources, summary — Yandex.Me.png",
    title: "Analytics — fintech site",
    desc: "Traffic source breakdown and unit economics assessment.",
    tags: ["fintech", "analytics"]
  },
  {
    src: "Monosnap Stimulus - Sources, summary - Yandex.Metr.png",
    title: "Analytics — marketing",
    desc: "Stimulus campaigns, post-analysis of acquisition channels.",
    tags: ["analytics", "growth"]
  },
  {
    src: "SEO google pruf.png",
    title: "SEO — Google positions proof",
    desc: "Organic search rankings growth on Google across key product queries.",
    tags: ["seo", "analytics", "growth"]
  },
  {
    src: "SEO pruf 2.png",
    title: "SEO positions — proof 2",
    desc: "Further evidence of top search positions achieved through SEO strategy.",
    tags: ["seo", "analytics", "growth"]
  },
  {
    src: "SEO keywords.png",
    title: "SEO keywords map",
    desc: "Keyword research and mapping for product landing pages.",
    tags: ["seo", "analytics"]
  },
  {
    src: "SEO pruf crypto 3.png",
    title: "SEO — crypto project proof",
    desc: "Search position results for crypto wallet product pages.",
    tags: ["seo", "analytics", "crypto"]
  },
  {
    src: "SEO pruf crypto ru.png",
    title: "SEO — crypto RU market",
    desc: "Russian-market SEO results for crypto wallet product.",
    tags: ["seo", "analytics", "crypto"]
  },
  {
    src: "SEO to top.jpg",
    title: "SEO — growth to TOP",
    desc: "Dynamic of organic traffic growth from page 3 to TOP-10 positions.",
    tags: ["seo", "growth", "analytics"]
  },
  {
    src: "SEO to TOP 2.jpg",
    title: "SEO — growth to TOP (2)",
    desc: "Further position growth across additional keyword clusters.",
    tags: ["seo", "growth", "analytics"]
  },
  {
    src: "Gant plan.png",
    title: "Gantt plan — delivery roadmap",
    desc: "Program-level Gantt chart used for multi-team delivery coordination.",
    tags: ["pmo", "roadmap", "delivery"]
  },
  {
    src: "Untitled.png",
    title: "Project tracking overview",
    desc: "High-level project status overview for portfolio governance.",
    tags: ["pmo", "delivery"]
  },
  {
    src: "doc_2023-03-03_21-39-32.png",
    title: "Game production — document 1",
    desc: "Internal production documentation from game development program.",
    tags: ["gaming", "pmo", "process"]
  },
  {
    src: "doc_2023-03-03_21-40-00.png",
    title: "Game production — document 2",
    desc: "Sprint planning and team coordination artifacts.",
    tags: ["gaming", "pmo", "process"]
  },
  {
    src: "doc_2023-03-03_21-40-11.png",
    title: "Game production — document 3",
    desc: "Release tracking and milestone reporting.",
    tags: ["gaming", "pmo", "delivery"]
  },
  {
    src: "photo_2020-11-29_21-24-31.jpg",
    title: "Product team — 2020",
    desc: "Team at work during NEOBANK crypto wallet product development phase.",
    tags: ["fintech", "crypto", "team"]
  },
  {
    src: "photo_2021-08-31_03-39-37.jpg",
    title: "Product team — 2021",
    desc: "Team during Redrift gamedev PMO program.",
    tags: ["gaming", "team"]
  },
  {
    src: "photo_2022-12-26_15-12-58.jpg",
    title: "Team event — 2022",
    desc: "Team gathering during active game production cycle.",
    tags: ["gaming", "team"]
  },
  {
    src: "photo_2022-12-26_15-13-00.jpg",
    title: "Team event — 2022 (2)",
    desc: "Cross-functional team collaboration session.",
    tags: ["gaming", "team"]
  },
  {
    src: "photo_2022-12-26_15-13-01.jpg",
    title: "Team event — 2022 (3)",
    desc: "End of year team review and retrospective.",
    tags: ["gaming", "team"]
  },
  {
    src: "photo_2023-02-26_00-13-39.jpg",
    title: "Team — early 2023",
    desc: "Team at the start of a new game launch cycle.",
    tags: ["gaming", "team"]
  }
];

const track = document.getElementById("track");
const viewport = document.getElementById("viewport");
const dotsWrap = document.getElementById("dots");
const filtersWrap = document.getElementById("filters");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");

let activeTag = "all";
let current = 0;
let filtered = [...slides];

// ─── Filters ────────────────────────────────────────────────────────────────

function renderFilters() {
  const tags = Array.from(new Set(slides.flatMap(s => s.tags))).sort();
  filtersWrap.appendChild(createFilterBtn("all", "All"));
  tags.forEach(tag => filtersWrap.appendChild(createFilterBtn(tag, tag)));
  setActiveFilter("all");
}

function createFilterBtn(tag, label) {
  const btn = document.createElement("button");
  btn.className = "filter-btn";
  btn.dataset.tag = tag;
  btn.textContent = label;
  btn.setAttribute("aria-pressed", tag === activeTag ? "true" : "false");
  btn.addEventListener("click", () => {
    activeTag = tag;
    filtered = tag === "all" ? [...slides] : slides.filter(s => s.tags.includes(tag));
    setActiveFilter(tag);
    current = 0;
    renderSlides();
  });
  return btn;
}

function setActiveFilter(tag) {
  filtersWrap.querySelectorAll(".filter-btn").forEach(b => {
    const isActive = b.dataset.tag === tag;
    b.classList.toggle("active", isActive);
    b.setAttribute("aria-pressed", isActive ? "true" : "false");
  });
}

// ─── Slides ──────────────────────────────────────────────────────────────────

function renderSlides() {
  track.innerHTML = "";
  filtered.forEach((s) => {
    const slide = document.createElement("article");
    slide.className = "slide";
    const img = document.createElement("img");
    img.src = encodeURI(s.src);
    img.alt = s.title;
    img.loading = "lazy";
    const info = document.createElement("div");
    const heading = document.createElement("h3");
    heading.textContent = s.title;
    const desc = document.createElement("p");
    desc.textContent = s.desc;
    const tagsDiv = document.createElement("div");
    tagsDiv.className = "tags";
    s.tags.forEach(t => {
      const span = document.createElement("span");
      span.className = "tag";
      span.textContent = "#" + t;
      tagsDiv.appendChild(span);
    });
    info.append(heading, desc, tagsDiv);
    slide.append(img, info);
    track.appendChild(slide);
  });
  renderDots();
  updatePosition();
}

// ─── Dots ────────────────────────────────────────────────────────────────────

function renderDots() {
  dotsWrap.innerHTML = "";
  filtered.forEach((_, i) => {
    const dot = document.createElement("button");
    dot.className = "dot" + (i === current ? " active" : "");
    dot.setAttribute("role", "tab");
    dot.setAttribute("aria-label", "Go to slide " + (i + 1));
    dot.setAttribute("aria-selected", i === current ? "true" : "false");
    dot.addEventListener("click", () => { current = i; updatePosition(); });
    dotsWrap.appendChild(dot);
  });
}

function syncDots() {
  dotsWrap.querySelectorAll(".dot").forEach((d, i) => {
    const isActive = i === current;
    d.classList.toggle("active", isActive);
    d.setAttribute("aria-selected", isActive ? "true" : "false");
  });
}

// ─── Position ────────────────────────────────────────────────────────────────

function updatePosition() {
  const firstSlide = track.querySelector(".slide");
  const slideWidth = firstSlide ? firstSlide.getBoundingClientRect().width : 0;
  const gap = 16;
  track.style.transform = `translateX(${-(slideWidth + gap) * current}px)`;
  prevBtn.disabled = current === 0;
  nextBtn.disabled = current >= filtered.length - 1;
  syncDots();
}

// ─── Controls ────────────────────────────────────────────────────────────────

prevBtn.addEventListener("click", () => {
  if (current > 0) { current--; updatePosition(); }
});
nextBtn.addEventListener("click", () => {
  if (current < filtered.length - 1) { current++; updatePosition(); }
});

window.addEventListener("keydown", (e) => {
  const sliderFocused =
    viewport.contains(document.activeElement) ||
    dotsWrap.contains(document.activeElement) ||
    document.activeElement === prevBtn ||
    document.activeElement === nextBtn;
  if (!sliderFocused) return;
  if (["ArrowRight", "ArrowDown"].includes(e.key)) {
    e.preventDefault();
    if (current < filtered.length - 1) { current++; updatePosition(); }
  } else if (["ArrowLeft", "ArrowUp"].includes(e.key)) {
    e.preventDefault();
    if (current > 0) { current--; updatePosition(); }
  }
});

viewport.addEventListener("wheel", (e) => {
  if (Math.abs(e.deltaX) > Math.abs(e.deltaY)) return;
  e.preventDefault();
  if (e.deltaY > 0 && current < filtered.length - 1) { current++; updatePosition(); }
  else if (e.deltaY < 0 && current > 0) { current--; updatePosition(); }
}, { passive: false });

let startX = 0;
viewport.addEventListener("pointerdown", (e) => {
  startX = e.clientX;
  viewport.setPointerCapture(e.pointerId);
});
viewport.addEventListener("pointerup", (e) => {
  const dx = e.clientX - startX;
  if (Math.abs(dx) > 40) {
    if (dx < 0 && current < filtered.length - 1) { current++; updatePosition(); }
    else if (dx > 0 && current > 0) { current--; updatePosition(); }
  }
});

window.addEventListener("resize", updatePosition);

// ─── Init ────────────────────────────────────────────────────────────────────

renderFilters();
renderSlides();
