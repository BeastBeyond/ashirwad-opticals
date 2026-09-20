import os

svg_dir = "/Users/amankumar/.gemini/antigravity-ide/scratch/ashirwad-optics/assets"

product_svgs = {
    "prod_screen_bluecut_round.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 60" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <defs>
    <linearGradient id="blueGlow" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#38bdf8" stop-opacity="0.35"/>
      <stop offset="100%" stop-color="#0284c7" stop-opacity="0.1"/>
    </linearGradient>
  </defs>
  <!-- Screen Round Glasses with Blue Anti-Reflective Lens Coating -->
  <circle cx="31" cy="29" r="18" fill="url(#blueGlow)" stroke="#0284c7" stroke-width="2.6"/>
  <circle cx="89" cy="29" r="18" fill="url(#blueGlow)" stroke="#0284c7" stroke-width="2.6"/>
  <!-- Blue anti-glare reflection arcs -->
  <path d="M22 20 Q32 16 38 22" stroke="#38bdf8" stroke-width="1.8" opacity="0.85"/>
  <path d="M80 20 Q90 16 96 22" stroke="#38bdf8" stroke-width="1.8" opacity="0.85"/>
  <!-- Bridge & Temples -->
  <path d="M49 27 Q60 21 71 27" stroke="#0f172a" stroke-width="2.6"/>
  <path d="M13 27 L3 25" stroke="#0f172a" stroke-width="2.6"/>
  <path d="M107 27 L117 25" stroke="#0f172a" stroke-width="2.6"/>
</svg>''',

    "prod_gaming_shield.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 60" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <defs>
    <linearGradient id="amberGlow" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#f59e0b" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#d97706" stop-opacity="0.15"/>
    </linearGradient>
  </defs>
  <!-- Gunnar Gaming Shield Amber Lenses -->
  <rect x="12" y="14" width="36" height="32" rx="5" fill="url(#amberGlow)" stroke="#1e293b" stroke-width="3"/>
  <rect x="72" y="14" width="36" height="32" rx="5" fill="url(#amberGlow)" stroke="#1e293b" stroke-width="3"/>
  <!-- Shield reflection -->
  <path d="M16 20 L38 20" stroke="#fbbf24" stroke-width="1.5" opacity="0.75"/>
  <path d="M76 20 L98 20" stroke="#fbbf24" stroke-width="1.5" opacity="0.75"/>
  <path d="M48 22 Q60 19 72 22" stroke="#1e293b" stroke-width="3"/>
  <path d="M12 20 L2 18" stroke="#1e293b" stroke-width="3"/>
  <path d="M108 20 L118 18" stroke="#1e293b" stroke-width="3"/>
</svg>''',

    "prod_kids_flexi_green.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 60" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Kids Flexible Silicone Teal/Green Frame -->
  <circle cx="31" cy="29" r="17" fill="rgba(16,185,129,0.06)" stroke="#059669" stroke-width="3.6"/>
  <circle cx="89" cy="29" r="17" fill="rgba(16,185,129,0.06)" stroke="#059669" stroke-width="3.6"/>
  <path d="M48 27 Q60 21 72 27" stroke="#059669" stroke-width="3.6"/>
  <path d="M14 27 Q8 25 3 27" stroke="#10b981" stroke-width="3.6"/>
  <path d="M106 27 Q112 25 117 27" stroke="#10b981" stroke-width="3.6"/>
</svg>''',

    "prod_kids_active_blue.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 60" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Kids Active Navy & Coral Frame -->
  <rect x="12" y="15" width="36" height="28" rx="6" fill="rgba(37,99,235,0.06)" stroke="#2563eb" stroke-width="3.4"/>
  <rect x="72" y="15" width="36" height="28" rx="6" fill="rgba(37,99,235,0.06)" stroke="#2563eb" stroke-width="3.4"/>
  <path d="M48 23 Q60 20 72 23" stroke="#2563eb" stroke-width="3.4"/>
  <path d="M12 21 L3 19" stroke="#ef4444" stroke-width="3.6"/>
  <path d="M108 21 L117 19" stroke="#ef4444" stroke-width="3.6"/>
</svg>''',

    "prod_kids_pastel_pink.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 60" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Teens Petite Pastel Pink Cateye -->
  <path d="M12 18 Q32 14 48 24 Q48 42 30 42 Q14 42 12 18 Z" fill="rgba(244,114,182,0.1)" stroke="#ec4899" stroke-width="3.2"/>
  <path d="M108 18 Q88 14 72 24 Q72 42 90 42 Q106 42 108 18 Z" fill="rgba(244,114,182,0.1)" stroke="#ec4899" stroke-width="3.2"/>
  <path d="M48 24 Q60 21 72 24" stroke="#db2777" stroke-width="3.2"/>
  <path d="M12 18 L2 16" stroke="#db2777" stroke-width="3.2"/>
  <path d="M108 18 L118 16" stroke="#db2777" stroke-width="3.2"/>
</svg>'''
}

for filename, content in product_svgs.items():
    path = os.path.join(svg_dir, filename)
    with open(path, 'w') as f:
        f.write(content)
    print(f"Generated {filename}")

print("All dedicated product SVGs created successfully!")
