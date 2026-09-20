import os

svg_dir = "/Users/amankumar/.gemini/antigravity-ide/scratch/ashirwad-optics/assets"

svgs = {
    "shape_rectangle.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 60" fill="none" stroke="#000042" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
  <!-- Rectangle Eyeglasses -->
  <rect x="12" y="16" width="38" height="26" rx="6" fill="rgba(0,180,216,0.04)" stroke="#0f172a" stroke-width="3"/>
  <rect x="70" y="16" width="38" height="26" rx="6" fill="rgba(0,180,216,0.04)" stroke="#0f172a" stroke-width="3"/>
  <path d="M50 24 Q60 21 70 24" stroke="#0f172a" stroke-width="3"/>
  <path d="M12 22 L2 20" stroke="#0f172a" stroke-width="3"/>
  <path d="M108 22 L118 20" stroke="#0f172a" stroke-width="3"/>
</svg>''',

    "shape_cateye.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 60" fill="none" stroke="#000042" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
  <!-- Cateye Eyeglasses -->
  <path d="M12 18 Q32 14 48 24 Q48 42 30 42 Q14 42 12 18 Z" fill="rgba(0,180,216,0.04)" stroke="#0f172a" stroke-width="3"/>
  <path d="M108 18 Q88 14 72 24 Q72 42 90 42 Q106 42 108 18 Z" fill="rgba(0,180,216,0.04)" stroke="#0f172a" stroke-width="3"/>
  <path d="M48 24 Q60 21 72 24" stroke="#0f172a" stroke-width="3"/>
  <path d="M12 18 L2 16" stroke="#0f172a" stroke-width="3"/>
  <path d="M108 18 L118 16" stroke="#0f172a" stroke-width="3"/>
</svg>''',

    "shape_aviator.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 60" fill="none" stroke="#000042" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
  <!-- Aviator Eyeglasses with Double Bridge -->
  <path d="M14 18 Q32 14 48 18 Q50 38 32 44 Q14 38 14 18 Z" fill="rgba(0,180,216,0.04)" stroke="#0f172a" stroke-width="2.6"/>
  <path d="M106 18 Q88 14 72 18 Q70 38 88 44 Q106 38 106 18 Z" fill="rgba(0,180,216,0.04)" stroke="#0f172a" stroke-width="2.6"/>
  <!-- Double Bridge -->
  <path d="M46 16 L74 16" stroke="#0f172a" stroke-width="2.6"/>
  <path d="M48 22 Q60 26 72 22" stroke="#0f172a" stroke-width="2.6"/>
  <path d="M14 20 L4 18" stroke="#0f172a" stroke-width="2.6"/>
  <path d="M106 20 L116 18" stroke="#0f172a" stroke-width="2.6"/>
</svg>''',

    "shape_geometric.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 60" fill="none" stroke="#000042" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
  <!-- Geometric Hexagonal Eyeglasses -->
  <path d="M18 16 L42 16 L50 28 L42 42 L18 42 L10 28 Z" fill="rgba(0,180,216,0.04)" stroke="#0f172a" stroke-width="2.6"/>
  <path d="M78 16 L102 16 L110 28 L102 42 L78 42 L70 28 Z" fill="rgba(0,180,216,0.04)" stroke="#0f172a" stroke-width="2.6"/>
  <path d="M50 28 Q60 25 70 28" stroke="#0f172a" stroke-width="2.6"/>
  <path d="M10 28 L2 26" stroke="#0f172a" stroke-width="2.6"/>
  <path d="M110 28 L118 26" stroke="#0f172a" stroke-width="2.6"/>
</svg>''',

    "shape_round.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 60" fill="none" stroke="#000042" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
  <!-- Round Eyeglasses -->
  <circle cx="31" cy="29" r="18" fill="rgba(0,180,216,0.04)" stroke="#0f172a" stroke-width="2.6"/>
  <circle cx="89" cy="29" r="18" fill="rgba(0,180,216,0.04)" stroke="#0f172a" stroke-width="2.6"/>
  <path d="M49 27 Q60 21 71 27" stroke="#0f172a" stroke-width="2.6"/>
  <path d="M13 27 L3 25" stroke="#0f172a" stroke-width="2.6"/>
  <path d="M107 27 L117 25" stroke="#0f172a" stroke-width="2.6"/>
</svg>''',

    "shape_clubmaster.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 60" fill="none" stroke="#000042" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
  <!-- Clubmaster Browline Eyeglasses -->
  <!-- Upper thick brow -->
  <path d="M12 18 Q32 14 48 18 L50 24 L10 24 Z" fill="#0f172a"/>
  <path d="M72 18 Q88 14 108 18 L110 24 L70 24 Z" fill="#0f172a"/>
  <!-- Lower thin metal rim -->
  <path d="M12 24 Q14 42 30 42 Q46 42 48 24" stroke="#0f172a" stroke-width="2" fill="rgba(0,180,216,0.04)"/>
  <path d="M72 24 Q74 42 90 42 Q106 42 108 24" stroke="#0f172a" stroke-width="2" fill="rgba(0,180,216,0.04)"/>
  <!-- Bridge -->
  <path d="M48 20 Q60 17 72 20" stroke="#0f172a" stroke-width="2.8"/>
  <path d="M10 20 L2 18" stroke="#0f172a" stroke-width="2.6"/>
  <path d="M110 20 L118 18" stroke="#0f172a" stroke-width="2.6"/>
</svg>''',

    "shape_square.svg": '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 120 60" fill="none" stroke="#000042" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
  <!-- Square Chunky Eyeglasses -->
  <rect x="12" y="14" width="36" height="32" rx="4" fill="rgba(0,180,216,0.04)" stroke="#0f172a" stroke-width="3.2"/>
  <rect x="72" y="14" width="36" height="32" rx="4" fill="rgba(0,180,216,0.04)" stroke="#0f172a" stroke-width="3.2"/>
  <path d="M48 22 Q60 19 72 22" stroke="#0f172a" stroke-width="3.2"/>
  <path d="M12 20 L2 18" stroke="#0f172a" stroke-width="3.2"/>
  <path d="M108 20 L118 18" stroke="#0f172a" stroke-width="3.2"/>
</svg>'''
}

for filename, content in svgs.items():
    path = os.path.join(svg_dir, filename)
    with open(path, 'w') as f:
        f.write(content)
    print(f"Generated {filename}")

print("All vector SVGs created successfully!")
