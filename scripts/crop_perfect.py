import zlib
import struct
import math

def write_png(filename, width, height, raw_rgba):
    # raw_rgba is bytearray of size width * height * 4
    # Prepend filter byte 0 to each scanline
    scanlines = bytearray()
    for y in range(height):
        scanlines.append(0) # filter type 0
        start = y * width * 4
        scanlines.extend(raw_rgba[start : start + width * 4])
        
    compressed = zlib.compress(scanlines)
    
    ihdr = struct.pack('>IIBBBBB', width, height, 8, 6, 0, 0, 0)
    
    def chunk(chunk_type, data):
        c = chunk_type + data
        crc = zlib.crc32(c)
        return struct.pack('>I', len(data)) + c + struct.pack('>I', crc)
        
    out = b'\x89PNG\r\n\x1a\n'
    out += chunk(b'IHDR', ihdr)
    out += chunk(b'IDAT', compressed)
    out += chunk(b'IEND', b'')
    
    with open(filename, 'wb') as f:
        f.write(out)

from inspect_png import read_png

w, h, bpp, raw = read_png("/Users/amankumar/.gemini/antigravity-ide/scratch/ashirwad-optics/assets/media_1789936911644.png")

# Let's find the 7 circle centers
# Looking at the width 1024 and 7 roundels:
# The roundels are evenly distributed across the 1024px width.
# Total width = 1024. 7 items.
# Let's inspect the exact centers by finding the circle centers or labels.
centers_x = [78, 224, 370, 516, 663, 810, 956]
# Let's verify and refine centers by scanning for the circular background
# Circle diameter is approx 130px, y center approx 72px

# Let's crop each roundel with width 140, height 183
shapes_meta = [
    ("shape_rectangle.png", "frame_rectangle.png", 78, "Rectangle"),
    ("shape_cateye.png", "frame_cateye.png", 224, "Cateye"),
    ("shape_aviator.png", "frame_aviator.png", 370, "Aviator"),
    ("shape_geometric.png", "frame_geometric.png", 516, "Geometric"),
    ("shape_round.png", "frame_round.png", 663, "Round"),
    ("shape_clubmaster.png", "frame_clubmaster.png", 810, "Clubmaster"),
    ("shape_square.png", "frame_square.png", 956, "Square"),
]

for shape_filename, frame_filename, cx, name in shapes_meta:
    # 1. Roundel full crop (width 140, height 183)
    crop_w, crop_h = 140, 183
    x0 = max(0, cx - crop_w // 2)
    x1 = min(w, x0 + crop_w)
    actual_w = x1 - x0
    
    cropped = bytearray(crop_h * actual_w * 4)
    for y in range(crop_h):
        for x in range(actual_w):
            src_x = x0 + x
            src_y = y
            src_idx = (src_y * w + src_x) * bpp
            dst_idx = (y * actual_w + x) * 4
            
            r, g, b = raw[src_idx], raw[src_idx+1], raw[src_idx+2]
            a = raw[src_idx+3] if bpp == 4 else 255
            cropped[dst_idx] = r
            cropped[dst_idx+1] = g
            cropped[dst_idx+2] = b
            cropped[dst_idx+3] = a
            
    write_png(f"/Users/amankumar/.gemini/antigravity-ide/scratch/ashirwad-optics/assets/{shape_filename}", actual_w, crop_h, cropped)
    
    # 2. Pure frame glasses crop (isolated glasses inside the circle, y from 30 to 110, x +/- 58)
    fw, fh = 120, 80
    fx0 = max(0, cx - fw // 2)
    fy0 = 32
    frame_crop = bytearray(fh * fw * 4)
    for y in range(fh):
        for x in range(fw):
            src_x = fx0 + x
            src_y = fy0 + y
            if 0 <= src_x < w and 0 <= src_y < h:
                src_idx = (src_y * w + src_x) * bpp
                r, g, b = raw[src_idx], raw[src_idx+1], raw[src_idx+2]
                # If background is near white/light grey, make it transparent or keep clean white
                dst_idx = (y * fw + x) * 4
                frame_crop[dst_idx] = r
                frame_crop[dst_idx+1] = g
                frame_crop[dst_idx+2] = b
                frame_crop[dst_idx+3] = 255
    write_png(f"/Users/amankumar/.gemini/antigravity-ide/scratch/ashirwad-optics/assets/{frame_filename}", fw, fh, frame_crop)
    print(f"Generated perfect {shape_filename} and {frame_filename}")

print("Shapes cropping complete!")

w2, h2, bpp2, raw2 = read_png("/Users/amankumar/.gemini/antigravity-ide/scratch/ashirwad-optics/assets/media_1789937046674.png")

cards_meta = [
    ("card_crystal_clear.png", 0, 0, 341, 248),
    ("card_masaba.png", 341, 0, 341, 248),
    ("card_bold_signature.png", 682, 0, 342, 248),
    ("card_devil_wears_prada.png", 0, 248, 341, 248),
    ("card_two_in_one.png", 341, 248, 341, 248),
    ("card_feather_light.png", 682, 248, 342, 248),
]

for card_name, cx, cy, cw, ch in cards_meta:
    cropped = bytearray(ch * cw * 4)
    for y in range(ch):
        for x in range(cw):
            src_x = cx + x
            src_y = cy + y
            src_idx = (src_y * w2 + src_x) * bpp2
            dst_idx = (y * cw + x) * 4
            r, g, b = raw2[src_idx], raw2[src_idx+1], raw2[src_idx+2]
            a = raw2[src_idx+3] if bpp2 == 4 else 255
            cropped[dst_idx] = r
            cropped[dst_idx+1] = g
            cropped[dst_idx+2] = b
            cropped[dst_idx+3] = a
    write_png(f"/Users/amankumar/.gemini/antigravity-ide/scratch/ashirwad-optics/assets/{card_name}", cw, ch, cropped)
    print(f"Generated clean {card_name}")

print("All card crops generated successfully!")
