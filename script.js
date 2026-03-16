/**
 * Portfolio slider — vanilla JS, no dependencies.
 * Features: filter buttons, keyboard nav, wheel, pointer swipe, dot indicators.
 */

const slides = [
  {
    src: "ClickUP_dashboard.png",
    title: "Delivery dashboards — ClickUp",
    desc: "PMO/engineering control hybrid: resources, releases, variance 3–5%.",
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
    title: "Ads & growth campaign",
    desc: "Grant-funded ad campaign: strategy, creatives, metric tracking.",
    tags: ["growth", "marketing"]
  },
  {
    src: "Website_neobank.png",
    title: "Neobank landing",
    desc: "Fintech landing + P2P/wallet, organic traffic ×4, conversion ×2.",
    tags: ["fintech", "web", "growth"]
  },
  {
    src: "Game.png",
    title: "WebGL game — GTA POV",
    desc: "WebGL game + digital-goods marketplace with PSP payment gateway.",
    tags: ["gaming", "webgl", "payments"]
  },
  {
    src: "Game 2.png",
    title: "Game UI pack 1",
    desc: "HUD and mission components.",
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
    desc: "Progress and rewards screen.",
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
    desc: "User profile and orders.",
    tags: ["gaming", "auth"]
  },
  {
    src: "Game 7.png",
    title: "Game UI pack 6",
    desc: "Scenes and cut-scenes.",
    tags: ["gaming"]
  },
  {
    src: "Road_map_template.png",
    title: "Roadmap template",
    desc: "Program template for 10+ streams with release synchronisation.",
    tags: ["roadmap", "pmo"]
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
    desc: "Traffic sources breakdown, unit-economics evaluation.",
    tags: ["fintech", "analytics"]
  },
  {
    src: "Monosnap Stimulus - Sources, summary - Yandex.Metr.png",
    title: "Analytics — marketing",
    desc: "Stimulus campaigns, post-analysis by channel.",
    tags: ["analytics", "growth"]
  }
];

// ── DOM refs ───────────────────────────────────────────────────────────────
const track = document.getElementById("track");
const viewport = document.getElementById("viewport");
const dotsWrap = document.getElementById("dots");
const filtersWrap = document.getElementById("filters");
const prevBtn = document.getElementById("prevBtn");
const nextBtn = document.getElementById("nextBtn");

// ── State ──────────────────────────────────────────────────────────────────
let activeTag = "all";
let current = 0;
let filtered = slides;

// ── Filters ────────────────────────────────────────────────────────────────
function renderFilters() {
  const tags = Array.from(new Set(slides.flatMap(s => s.tags))).sort();
  filtersWrap.appendChild(createFilterBtn("all", "All"));
  tags.forEach(tag => filtersWrap.appendChild(createFilterBtn(tag, `#${tag}`)));
  setActiveFilter("all");
}

function createFilterBtn(tag, label) {
  const btn = document.createElement("button");
  btn.className = "filter-btn";
  btn.dataset.tag = tag;
  btn.textContent = label;
  btn.setAttribute("aria-pressed", "false");
  btn.addEventListener("click", () => {
    activeTag = tag;
    filtered = tag === "all" ? slides : slides.filter(s => s.tags.includes(tag));
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
    b.setAttribute("aria-pressed", String(isActive));
  });
}

// ── Slides ─────────────────────────────────────────────────────────────────
function renderSlides() {
  track.innerHTML = "";
  filtered.forEach((s, idx) => {
    const slide = document.createElement("article");
    slide.className = "slide";
    slide.setAttribute("aria-label", s.title);
    slide.setAttribute("role", "listitem");

    const img = document.createElement("img");
    img.src = encodeURI(s.src);
    img.alt = s.title;
    img.loading = "lazy";
    img.style.cursor = "zoom-in";
    img.addEventListener("click", () => openLightbox(idx));

    const info = document.createElement("div");
    const h3 = document.createElement("h3");
    h3.textContent = s.title;
    const p = document.createElement("p");
    p.textContent = s.desc;
    const tagsDiv = document.createElement("div");
    tagsDiv.className = "tags";
    s.tags.forEach(t => {
      const span = document.createElement("span");
      span.className = "tag";
      span.textContent = "#" + t;
      tagsDiv.appendChild(span);
    });

    info.append(h3, p, tagsDiv);
    slide.append(img, info);
    track.appendChild(slide);
  });

  track.setAttribute("role", "list");
  track.setAttribute("aria-label", `Showing ${filtered.length} slides`);
  updateDots();
  updatePosition(false);
}

// ── Dots ───────────────────────────────────────────────────────────────────
function updateDots() {
  dotsWrap.innerHTML = "";
  filtered.forEach((_, i) => {
    const dot = document.createElement("button");
    dot.className = "dot" + (i === current ? " active" : "");
    dot.setAttribute("role", "listitem");
    dot.setAttribute("aria-label", `Go to slide ${i + 1}`);
    dot.setAttribute("aria-current", i === current ? "true" : "false");
    dot.addEventListener("click", () => { current = i; updatePosition(); });
    dotsWrap.appendChild(dot);
  });
}

// ── Position ───────────────────────────────────────────────────────────────
function updatePosition(animate = true) {
  const firstSlide = track.querySelector(".slide");
  if (!firstSlide) return;

  const slideWidth = firstSlide.getBoundingClientRect().width;
  const gap = 16;
  track.style.transition = animate ? "transform 0.28s cubic-bezier(0.4,0,0.2,1)" : "none";
  track.style.transform = `translateX(${-(slideWidth + gap) * current}px)`;

  dotsWrap.querySelectorAll(".dot").forEach((d, i) => {
    d.classList.toggle("active", i === current);
    d.setAttribute("aria-current", i === current ? "true" : "false");
  });

  prevBtn.disabled = current === 0;
  nextBtn.disabled = current >= filtered.length - 1;

  viewport.setAttribute("aria-label",
    `Slide ${current + 1} of ${filtered.length}: ${filtered[current]?.title ?? ""}`);
}

// ── Nav buttons ────────────────────────────────────────────────────────────
prevBtn.addEventListener("click", () => {
  if (current > 0) { current--; updatePosition(); }
});
nextBtn.addEventListener("click", () => {
  if (current < filtered.length - 1) { current++; updatePosition(); }
});

// ── Keyboard ───────────────────────────────────────────────────────────────
window.addEventListener("keydown", e => {
  const focused = document.activeElement;
  const inSlider = viewport.contains(focused) || focused === viewport
    || focused === prevBtn || focused === nextBtn;

  if (!inSlider && focused !== document.body) return;

  if (e.key === "ArrowRight" || e.key === "ArrowDown") {
    e.preventDefault();
    if (current < filtered.length - 1) { current++; updatePosition(); }
  } else if (e.key === "ArrowLeft" || e.key === "ArrowUp") {
    e.preventDefault();
    if (current > 0) { current--; updatePosition(); }
  }
});

// ── Mouse wheel ────────────────────────────────────────────────────────────
viewport.addEventListener("wheel", e => {
  if (Math.abs(e.deltaX) > Math.abs(e.deltaY)) return;
  e.preventDefault();
  if (e.deltaY > 0) {
    if (current < filtered.length - 1) { current++; updatePosition(); }
  } else {
    if (current > 0) { current--; updatePosition(); }
  }
}, { passive: false });

// ── Pointer / touch swipe ──────────────────────────────────────────────────
let startX = 0;
let startY = 0;
let dragging = false;

viewport.addEventListener("pointerdown", e => {
  startX = e.clientX;
  startY = e.clientY;
  dragging = false;
});

viewport.addEventListener("pointermove", e => {
  if (!dragging && Math.abs(e.clientX - startX) > 8) {
    dragging = true;
    viewport.setPointerCapture(e.pointerId);
  }
});

viewport.addEventListener("pointerup", e => {
  const dx = e.clientX - startX;
  const dy = e.clientY - startY;
  if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 40) {
    if (dx < 0 && current < filtered.length - 1) { current++; updatePosition(); }
    else if (dx > 0 && current > 0) { current--; updatePosition(); }
  }
  dragging = false;
});

// ── Resize ─────────────────────────────────────────────────────────────────
window.addEventListener("resize", () => updatePosition(false));

// ── Lightbox ───────────────────────────────────────────────────────────────
const lb = document.getElementById("lb");
const lbImg = document.getElementById("lbImg");
const lbCaption = document.getElementById("lbCaption");
const lbCounter = document.getElementById("lbCounter");
const lbClose = document.getElementById("lbClose");
const lbPrev = document.getElementById("lbPrev");
const lbNext = document.getElementById("lbNext");

let lbIndex = 0;   // index within current filtered[]

function openLightbox(idx) {
  lbIndex = idx;
  lbRender();
  lb.showModal();
  lbImg.focus();
}

function lbRender() {
  const s = filtered[lbIndex];
  if (!s) return;
  lbImg.src = encodeURI(s.src);
  lbImg.alt = s.title;
  lbCaption.textContent = s.title;
  lbCounter.textContent = `${lbIndex + 1} / ${filtered.length}`;
  lbPrev.disabled = lbIndex === 0;
  lbNext.disabled = lbIndex >= filtered.length - 1;
}

function lbGo(dir) {
  const next = lbIndex + dir;
  if (next < 0 || next >= filtered.length) return;
  lbIndex = next;
  lbRender();
}

lbClose.addEventListener("click", () => lb.close());
lbPrev.addEventListener("click", () => lbGo(-1));
lbNext.addEventListener("click", () => lbGo(1));

// Close on backdrop click (click lands on the <dialog> element itself)
lb.addEventListener("click", e => { if (e.target === lb) lb.close(); });

// Keyboard inside lightbox
lb.addEventListener("keydown", e => {
  if (e.key === "ArrowRight" || e.key === "ArrowDown") { e.preventDefault(); lbGo(1); }
  else if (e.key === "ArrowLeft" || e.key === "ArrowUp") { e.preventDefault(); lbGo(-1); }
  // Escape is handled natively by <dialog>
});

// Swipe inside lightbox
let lbStartX = 0;
let lbStartY = 0;
lb.addEventListener("pointerdown", e => {
  lbStartX = e.clientX;
  lbStartY = e.clientY;
});
lb.addEventListener("pointerup", e => {
  const dx = e.clientX - lbStartX;
  const dy = e.clientY - lbStartY;
  if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 40) {
    lbGo(dx < 0 ? 1 : -1);
  }
});

// ── Init ───────────────────────────────────────────────────────────────────
renderFilters();
renderSlides();
