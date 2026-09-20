import subprocess
import os

assets_dir = "/Users/amankumar/.gemini/antigravity-ide/scratch/ashirwad-optics/assets"

# Crop shapes from media_1789936911644.png (1024x183)
# 7 shapes: Rectangle, Cateye, Aviator, Geometric, Round, Clubmaster, Square
shapes = [
    ("shape_rectangle.png", 0, 0, 146, 183),
    ("shape_cateye.png", 146, 0, 146, 183),
    ("shape_aviator.png", 292, 0, 146, 183),
    ("shape_geometric.png", 438, 0, 146, 183),
    ("shape_round.png", 584, 0, 146, 183),
    ("shape_clubmaster.png", 730, 0, 146, 183),
    ("shape_square.png", 876, 0, 148, 183),
]

# In sips: --cropToHeightWidth H W --cropOffset offsetY offsetX
# But let's check sips behavior:
# sips -s format png --cropToHeightWidth 183 146 --cropOffset 0 X src.png --out dst.png
for name, x, y, w, h in shapes:
    out_path = os.path.join(assets_dir, name)
    src_path = os.path.join(assets_dir, "media_1789936911644.png")
    # First copy src to dst then crop
    cmd = f'cp "{src_path}" "{out_path}" && sips -c {h} {w} --cropOffset {y} {x} "{out_path}"'
    subprocess.run(cmd, shell=True, check=True)
    print(f"Created {name}")

# Crop cards from media_1789937046674.png (1024x496)
# 6 cards: 2 rows of 3
# Row 1 (y=0, h=248): Crystal Clear (0-341), Masaba (341-682), Bold Signature (682-1024)
# Row 2 (y=248, h=248): Devil Wears Prada (0-341), 2 in 1 (341-682), Feather Light (682-1024)
cards = [
    ("card_crystal_clear.png", 0, 0, 341, 248),
    ("card_masaba.png", 341, 0, 341, 248),
    ("card_bold_signature.png", 682, 0, 342, 248),
    ("card_devil_wears_prada.png", 0, 248, 341, 248),
    ("card_two_in_one.png", 341, 248, 341, 248),
    ("card_feather_light.png", 682, 248, 342, 248),
]

for name, x, y, w, h in cards:
    out_path = os.path.join(assets_dir, name)
    src_path = os.path.join(assets_dir, "media_1789937046674.png")
    cmd = f'cp "{src_path}" "{out_path}" && sips -c {h} {w} --cropOffset {y} {x} "{out_path}"'
    subprocess.run(cmd, shell=True, check=True)
    print(f"Created {name}")

print("All crops completed successfully!")
