/**
 * Ashirwad Optics - Interactive Frontend Application
 * Pure Informational & High-Impact Eyewear Showcase
 */

document.addEventListener('DOMContentLoaded', () => {
  initCategoryNavigation();
  initShapeRoundels();
  initLineupTiltAndModals();
  initVibeMatcher();
  initSearchFilter();
  initStoreStatus();
  initModalHandling();
});

/* --------------------------------------------------------------------------
   1. Category Sticky Navigation & Smooth Scrolling
   -------------------------------------------------------------------------- */
function initCategoryNavigation() {
  const navLinks = document.querySelectorAll('.category-nav-link');
  const sections = [];

  navLinks.forEach(link => {
    const targetId = link.getAttribute('data-target');
    const section = document.getElementById(targetId);
    if (section) {
      sections.push({ id: targetId, element: section, link: link });
    }

    link.addEventListener('click', (e) => {
      e.preventDefault();
      if (section) {
        // Native smooth scroll respecting CSS scroll-margin-top
        section.scrollIntoView({ behavior: 'smooth' });

        navLinks.forEach(l => l.classList.remove('active'));
        link.classList.add('active');
      }
    });
  });

  // ScrollSpy using IntersectionObserver
  const observerOptions = {
    root: null,
    rootMargin: '-15% 0px -65% 0px',
    threshold: 0
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const currentId = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          if (link.getAttribute('data-target') === currentId) {
            link.classList.add('active');
          } else {
            link.classList.remove('active');
          }
        });
      }
    });
  }, observerOptions);

  sections.forEach(s => observer.observe(s.element));
}

/* --------------------------------------------------------------------------
   2. Frame Shapes Roundels Bar Interactivity
   -------------------------------------------------------------------------- */
const shapeData = {
  rectangle: {
    name: "Classic Rectangle",
    bestFor: "Round, Oval, and Soft Heart Face Shapes",
    tagline: "Sharp, balanced angles that add structure and professional polish.",
    stylesInStore: "Matte Black Acetate, Titanium Semi-Rimless, Tortoise Shell",
    recommendedLens: "Crizal Blue-Cut & High-Index 1.67 Aspheric",
    svg: "assets/shape_rectangle.svg"
  },
  cateye: {
    name: "Runway Cat-Eye",
    bestFor: "Square, Oval, and Diamond Face Shapes",
    tagline: "Upswept browline curves that lift facial features with glamour.",
    stylesInStore: "Gloss Black, Rose Gold Wire, Pastel Pink & Gradient Tint",
    recommendedLens: "Transitions Gen 8 Light Adapt & Anti-Glare",
    svg: "assets/shape_cateye.svg"
  },
  aviator: {
    name: "Iconic Aviator",
    bestFor: "Square, Rectangular, and Heart Face Shapes",
    tagline: "Double-bridge timeless silhouette engineered for commanding presence.",
    stylesInStore: "Ray-Ban Classic Gold, Gunmetal Steel, Polarized G-15 Green",
    recommendedLens: "UV400 Polarized Driving & Anti-Reflective",
    svg: "assets/shape_aviator.svg"
  },
  geometric: {
    name: "Architectural Geometric",
    bestFor: "Oval, Round, and Oblong Face Shapes",
    tagline: "Contemporary hexagonal and octagonal wireforms with avant-garde flair.",
    stylesInStore: "Brushed Copper, Slim Silver, Dual-Tone Metal",
    recommendedLens: "Carl Zeiss ClearView & Zero-Glare Screen Shield",
    svg: "assets/shape_geometric.svg"
  },
  round: {
    name: "Retro Intellectual Round",
    bestFor: "Square, Angular, and Diamond Face Shapes",
    tagline: "Smooth circular contours that soften sharp jawlines with artistic warmth.",
    stylesInStore: "Vintage Gold Wire, Clear Crystal, Tortoise Havana",
    recommendedLens: "Essilor Crizal Rock & Blue UV Capture",
    svg: "assets/shape_round.svg"
  },
  clubmaster: {
    name: "Executive Clubmaster",
    bestFor: "All Face Types (Universal Classic)",
    tagline: "Prominent upper acetate brow with delicate lower metallic rims.",
    stylesInStore: "Titan Executive, Black & Gold, Woodgrain Acetate",
    recommendedLens: "Varilux Progressive & Blue-Shield Computing",
    svg: "assets/shape_clubmaster.svg"
  },
  square: {
    name: "Structured Bold Square",
    bestFor: "Round and Oval Face Shapes",
    tagline: "Wide eye-box with substantial bridge presence for modern statement look.",
    stylesInStore: "Chunky Amber Acetate, Matte Navy, TR90 Sport",
    recommendedLens: "Polarized Sun Shield & High-Impact Polycarbonate",
    svg: "assets/shape_square.svg"
  }
};

function initShapeRoundels() {
  const roundelButtons = document.querySelectorAll('.shape-roundel-btn');

  roundelButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      roundelButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const shapeKey = btn.getAttribute('data-shape');
      const details = shapeData[shapeKey];

      if (details) {
        openShapeModal(shapeKey, details);
      }
    });
  });
}

function openShapeModal(shapeKey, details) {
  const modal = document.getElementById('interactive-modal');
  const modalBody = document.getElementById('modal-dynamic-body');
  
  modalBody.innerHTML = `
    <div style="display: flex; align-items: center; gap: 1.25rem; margin-bottom: 1.5rem;">
      <div style="width: 88px; height: 88px; border-radius: 50%; background: #f8fafc; border: 2px solid #00b4d8; display: flex; align-items: center; justify-content: center; flex-shrink: 0; box-shadow: 0 4px 12px rgba(0, 180, 216, 0.2);">
        <img src="${details.svg}" alt="${details.name}" style="max-width: 68px; object-fit: contain;">
      </div>
      <div>
        <span style="font-size: 0.78rem; font-weight: 700; color: #0077b6; text-transform: uppercase; letter-spacing: 0.05em;">Shape Spotlight</span>
        <h3 style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.45rem; font-weight: 800; color: #000042;">${details.name}</h3>
        <p style="font-size: 0.85rem; color: #64748b;">${details.tagline}</p>
      </div>
    </div>

    <div style="background: #f8fafc; border-radius: 12px; padding: 1.25rem; border: 1px solid #e2e8f0; margin-bottom: 1.5rem;">
      <div style="margin-bottom: 0.85rem;">
        <span style="font-weight: 700; font-size: 0.85rem; color: #000042;">✨ Best Suited For:</span>
        <div style="font-size: 0.88rem; color: #334155; margin-top: 0.15rem;">${details.bestFor}</div>
      </div>
      <div style="margin-bottom: 0.85rem;">
        <span style="font-weight: 700; font-size: 0.85rem; color: #000042;">👓 In-Store Frame Varieties:</span>
        <div style="font-size: 0.88rem; color: #334155; margin-top: 0.15rem;">${details.stylesInStore}</div>
      </div>
      <div>
        <span style="font-weight: 700; font-size: 0.85rem; color: #000042;">🔬 Recommended Lens Pairings:</span>
        <div style="font-size: 0.88rem; color: #334155; margin-top: 0.15rem;">${details.recommendedLens}</div>
      </div>
    </div>

    <div style="display: flex; gap: 0.75rem; flex-wrap: wrap;">
      <a href="#eyeglasses" onclick="document.getElementById('interactive-modal').classList.remove('active')" style="flex: 1; min-width: 180px; text-align: center; background: #000042; color: #ffffff; padding: 0.75rem 1.25rem; border-radius: 9999px; font-weight: 700; font-size: 0.9rem; text-decoration: none;">
        Browse All Eyeglasses
      </a>
      <a href="#store-visit" onclick="document.getElementById('interactive-modal').classList.remove('active')" style="flex: 1; min-width: 180px; text-align: center; background: #00b4d8; color: #ffffff; padding: 0.75rem 1.25rem; border-radius: 9999px; font-weight: 700; font-size: 0.9rem; text-decoration: none;">
        Try On at Store
      </a>
    </div>
  `;

  modal.classList.add('active');
}

/* --------------------------------------------------------------------------
   3. Lineup Cards & Modal Viewer
   -------------------------------------------------------------------------- */
function initLineupTiltAndModals() {
  const cards = document.querySelectorAll('.lineup-card-item');

  cards.forEach(card => {
    // 3D Perspective Tilt on Mouse Move
    card.addEventListener('mousemove', (e) => {
      const rect = card.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      
      const centerX = rect.width / 2;
      const centerY = rect.height / 2;
      
      const rotateX = ((y - centerY) / centerY) * -6;
      const rotateY = ((x - centerX) / centerX) * 6;
      
      card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) translateY(-5px)`;
    });

    card.addEventListener('mouseleave', () => {
      card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateY(0px)';
    });

    // Modal Trigger
    card.addEventListener('click', () => {
      const title = card.getAttribute('data-card-title');
      const sub = card.getAttribute('data-card-sub');
      const desc = card.getAttribute('data-card-desc');
      const imgSrc = card.getAttribute('data-card-img') || 'assets/hero_store_interior.jpg';
      
      openLineupModal(title, sub, desc, imgSrc);
    });
  });
}

function openLineupModal(title, sub, desc, imgSrc) {
  const modal = document.getElementById('interactive-modal');
  const modalBody = document.getElementById('modal-dynamic-body');
  
  modalBody.innerHTML = `
    <div style="margin-bottom: 1.25rem;">
      <span style="font-size: 0.75rem; font-weight: 700; color: #00b4d8; text-transform: uppercase; letter-spacing: 0.08em;">Curated Lineup Showcase</span>
      <h3 style="font-family: 'Plus Jakarta Sans', sans-serif; font-size: 1.55rem; font-weight: 800; color: #000042; margin: 0.2rem 0;">${title}</h3>
      <div style="font-size: 0.95rem; font-weight: 600; color: #0077b6;">${sub}</div>
    </div>

    <div style="border-radius: 12px; overflow: hidden; margin-bottom: 1.5rem; border: 1px solid #e2e8f0; background: #0f172a;">
      <img src="${imgSrc}" alt="${title}" style="width: 100%; max-height: 280px; object-fit: cover; margin: 0 auto; display: block;">
    </div>

    <p style="font-size: 0.92rem; color: #475569; line-height: 1.65; margin-bottom: 1.5rem;">
      ${desc}
    </p>

    <div style="background: #f1f5f9; border-radius: 10px; padding: 1rem 1.25rem; margin-bottom: 1.5rem; display: grid; grid-template-columns: 1fr 1fr; gap: 1rem;">
      <div>
        <div style="font-size: 0.75rem; color: #64748b; font-weight: 600; text-transform: uppercase;">In-Store Stock Status</div>
        <div style="font-size: 0.88rem; font-weight: 700; color: #16a34a; margin-top: 0.15rem;">● Ready to Try On</div>
      </div>
      <div>
        <div style="font-size: 0.75rem; color: #64748b; font-weight: 600; text-transform: uppercase;">Prescription Compatibility</div>
        <div style="font-size: 0.88rem; font-weight: 700; color: #000042; margin-top: 0.15rem;">Single Vision & Progressive</div>
      </div>
    </div>

    <div style="display: flex; gap: 0.75rem;">
      <a href="#store-visit" onclick="document.getElementById('interactive-modal').classList.remove('active')" style="flex: 1; text-align: center; background: #000042; color: #ffffff; padding: 0.8rem; border-radius: 9999px; font-weight: 700; font-size: 0.9rem; text-decoration: none;">
        Visit Store to Try On
      </a>
      <a href="https://wa.me/919876543210?text=Hi%20Ashirwad%20Optics%2C%20I%20am%20interested%20in%20the%20${encodeURIComponent(title)}" target="_blank" style="flex: 1; text-align: center; background: #25d366; color: #ffffff; padding: 0.8rem; border-radius: 9999px; font-weight: 700; font-size: 0.9rem; text-decoration: none;">
        Inquire on WhatsApp
      </a>
    </div>
  `;

  modal.classList.add('active');
}

/* --------------------------------------------------------------------------
   4. Vibe & Audience Matcher
   -------------------------------------------------------------------------- */
const vibePresets = {
  executive: {
    title: "Executive & Boardroom Professional",
    desc: "Sleek semi-rimless browlines, sharp architectural rectangles, and brushed titanium metal finishes that project authority, clarity, and refined polish in business meetings.",
    shapes: ["Clubmaster", "Slim Rectangle", "Titanium Wire"],
    img: "assets/store_titan_tray.jpg"
  },
  minimal: {
    title: "Minimalist & Feather-Light",
    desc: "Understated rimless and ultra-thin circular wireframes engineered from aerospace Beta-Titanium for all-day weightless comfort and clean elegance.",
    shapes: ["Round Wire", "Rimless Contour", "Geometric Hex"],
    img: "assets/card_feather_light.jpg"
  },
  bold: {
    title: "Bold & High-Fashion Statement",
    desc: "Sculpted Italian acetate in chunky silhouettes, rich Havana tortoiseshell, and runway cat-eyes designed to become your signature personal aesthetic.",
    shapes: ["Thick Square", "Dramatic Cateye", "Masaba Runway"],
    img: "assets/card_masaba.jpg"
  },
  active: {
    title: "Active, Driving & Outdoor Sports",
    desc: "Impact-resistant TR90 memory polymers paired with UV400 polarized anti-glare lenses and magnetic clip-on sunshades for driving and sports.",
    shapes: ["Wrap Aviator", "Hustlr Switch 2-in-1", "Sport Shield"],
    img: "assets/prod_sunglasses_aviator.jpg"
  },
  creative: {
    title: "Creative & Colorful Acetate",
    desc: "Two-tone gradient tones, crystal transparent jewel hues, and playful geometric profiles for designers, creatives, and youth.",
    shapes: ["Crystal Clear", "Teal Geometric", "Pastel Cateye"],
    img: "assets/store_frame_tray.jpg"
  }
};

function initVibeMatcher() {
  const buttons = document.querySelectorAll('.vibe-tab-btn');
  const titleEl = document.getElementById('vibe-title');
  const descEl = document.getElementById('vibe-desc');
  const shapesEl = document.getElementById('vibe-shapes');
  const imgEl = document.getElementById('vibe-img');

  buttons.forEach(btn => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const key = btn.getAttribute('data-vibe');
      const data = vibePresets[key];

      if (data) {
        titleEl.textContent = data.title;
        descEl.textContent = data.desc;
        imgEl.src = data.img;

        shapesEl.innerHTML = data.shapes
          .map(s => `<span class="vibe-shape-tag">${s}</span>`)
          .join('');
      }
    });
  });
}

/* --------------------------------------------------------------------------
   5. Search Filter for Navigation
   -------------------------------------------------------------------------- */
function initSearchFilter() {
  const input = document.getElementById('global-search-input');
  if (!input) return;

  input.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
      const q = input.value.trim().toLowerCase();
      if (!q) return;

      if (q.includes('sun') || q.includes('shades') || q.includes('ray-ban') || q.includes('oakley')) {
        scrollToId('sunglasses');
      } else if (q.includes('screen') || q.includes('blue') || q.includes('computer') || q.includes('gunnar')) {
        scrollToId('screen-glasses');
      } else if (q.includes('kid') || q.includes('child') || q.includes('teen') || q.includes('junior')) {
        scrollToId('kids-glasses');
      } else if (q.includes('contact') || q.includes('lens') || q.includes('bausch') || q.includes('acuvue')) {
        scrollToId('contact-lenses');
      } else if (q.includes('test') || q.includes('power') || q.includes('checkup') || q.includes('doctor')) {
        scrollToId('eye-testing');
      } else if (q.includes('brand') || q.includes('zeiss') || q.includes('crizal') || q.includes('transitions')) {
        scrollToId('brands-lenses');
      } else if (q.includes('store') || q.includes('address') || q.includes('location') || q.includes('map')) {
        scrollToId('store-visit');
      } else {
        scrollToId('eyeglasses');
      }
    }
  });
}

function scrollToId(id) {
  const el = document.getElementById(id);
  if (el) {
    el.scrollIntoView({ behavior: 'smooth' });
  }
}

/* --------------------------------------------------------------------------
   6. Live Store Hours Status
   -------------------------------------------------------------------------- */
function initStoreStatus() {
  const statusEl = document.getElementById('live-store-status');
  if (!statusEl) return;

  const now = new Date();
  const hours = now.getHours();
  const minutes = now.getMinutes();
  const currentTimeVal = hours + minutes / 60;

  // Open 10:00 AM (10.0) to 9:30 PM (21.5)
  if (currentTimeVal >= 10.0 && currentTimeVal < 21.5) {
    statusEl.textContent = "Store Open Now (Closes at 9:30 PM)";
  } else {
    statusEl.textContent = "Opens Today at 10:00 AM";
  }
}

/* --------------------------------------------------------------------------
   7. Modal Handling
   -------------------------------------------------------------------------- */
function initModalHandling() {
  const modal = document.getElementById('interactive-modal');
  const closeBtn = document.getElementById('modal-close-btn');

  if (closeBtn) {
    closeBtn.addEventListener('click', () => {
      modal.classList.remove('active');
    });
  }

  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.classList.remove('active');
      }
    });
  }

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && modal && modal.classList.contains('active')) {
      modal.classList.remove('active');
    }
  });
}
