import zlib
import struct

def read_png(filename):
    with open(filename, 'rb') as f:
        data = f.read()
    
    assert data[:8] == b'\x89PNG\r\n\x1a\n'
    pos = 8
    width = height = 0
    idat = bytearray()
    
    while pos < len(data):
        length, chunk_type = struct.unpack('>I4s', data[pos:pos+8])
        pos += 8
        chunk_data = data[pos:pos+length]
        pos += length + 4 # skip crc
        
        if chunk_type == b'IHDR':
            width, height, bit_depth, color_type, compression, filter_method, interlace = struct.unpack('>IIBBBBB', chunk_data)
            print(f"IHDR: width={width}, height={height}, bit_depth={bit_depth}, color_type={color_type}")
        elif chunk_type == b'IDAT':
            idat.extend(chunk_data)
        elif chunk_type == b'IEND':
            break
            
    decompressed = zlib.decompress(idat)
    # color_type 6 is RGBA (4 bytes), color_type 2 is RGB (3 bytes)
    bpp = 4 if color_type == 6 else 3
    stride = width * bpp + 1
    
    # Simple scanline filter un-filtering (support type 0, 1, 2, 3, 4)
    raw = bytearray(height * width * bpp)
    prev_row = bytearray(width * bpp)
    
    for y in range(height):
        filter_type = decompressed[y * stride]
        row = bytearray(decompressed[y * stride + 1 : (y + 1) * stride])
        for x in range(width * bpp):
            a = row[x - bpp] if x >= bpp else 0
            b = prev_row[x]
            c = prev_row[x - bpp] if x >= bpp else 0
            
            if filter_type == 0:
                val = row[x]
            elif filter_type == 1:
                val = (row[x] + a) & 0xff
            elif filter_type == 2:
                val = (row[x] + b) & 0xff
            elif filter_type == 3:
                val = (row[x] + ((a + b) // 2)) & 0xff
            elif filter_type == 4:
                p = a + b - c
                pa = abs(p - a)
                pb = abs(p - b)
                pc = abs(p - c)
                pr = a if pa <= pb and pa <= pc else (b if pb <= pc else c)
                val = (row[x] + pr) & 0xff
            else:
                val = row[x]
            row[x] = val
        raw[y * width * bpp : (y + 1) * width * bpp] = row
        prev_row = row
        
    return width, height, bpp, raw

w, h, bpp, raw = read_png("/Users/amankumar/.gemini/antigravity-ide/scratch/ashirwad-optics/assets/media_1789936911644.png")

# Let's find columns with dark pixels (glasses frames)
# Glasses frames have dark pixels (R < 100, G < 100, B < 100)
dark_cols = []
for x in range(w):
    count = 0
    for y in range(h):
        idx = (y * w + x) * bpp
        r, g, b = raw[idx], raw[idx+1], raw[idx+2]
        if r < 120 and g < 120 and b < 120:
            count += 1
    dark_cols.append(count)

# Let's print out intervals of dark pixels to find exact centers of the 7 frames
in_shape = False
start_x = 0
regions = []
for x in range(w):
    if dark_cols[x] > 5 and not in_shape:
        in_shape = True
        start_x = x
    elif dark_cols[x] <= 5 and in_shape:
        in_shape = False
        regions.append((start_x, x))
if in_shape:
    regions.append((start_x, w))

print("Dark regions found:", regions)
