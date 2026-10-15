from PIL import Image, ImageFilter

SRC = "D:/personal-site/public/portrait.png"
OUT = "D:/personal-site/public/portrait-stroke.png"

im = Image.open(SRC).convert("RGBA")
W, H = im.size
mask = im.split()[3]

P = 120  # padding for stroke spill
cw, ch = W + 2 * P, H + 2 * P

def stroke_layer(r, rgb, dx, dy):
    """Square dilation (straight 90deg edges) + offset -> misregistered stroke layer"""
    m = mask.filter(ImageFilter.MaxFilter(2 * r + 1))
    a = Image.new("L", (cw, ch), 0)
    a.paste(m, (P + dx, P + dy))
    layer = Image.new("RGBA", (cw, ch), rgb + (255,))
    layer.putalpha(a)
    return layer

canvas = Image.new("RGBA", (cw, ch), (0, 0, 0, 0))
# 三层错位描边：外棕 / 中橄榄绿 / 内深绿（直线条、多笔画）
canvas = Image.alpha_composite(canvas, stroke_layer(16, (111, 78, 55), 12, -8))   # brown
canvas = Image.alpha_composite(canvas, stroke_layer(9,  (80, 77, 39),  -9, 9))    # olive #504D27-ish
canvas = Image.alpha_composite(canvas, stroke_layer(3,  (58, 56, 23),  2, 4))     # deep green
canvas.paste(im, (P, P), im)
canvas.save(OUT)
print("saved:", canvas.size)
