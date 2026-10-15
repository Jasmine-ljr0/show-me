from PIL import Image
src = r"D:/word文档/求职/材料、证件照/作品集自拍.png"
im = Image.open(src).convert("RGBA")
bbox = im.getbbox()  # based on alpha? getbbox uses non-zero pixels; for RGBA use alpha channel
alpha = im.split()[3]
bbox = alpha.getbbox()
print("orig size:", im.size, "bbox:", bbox)
if bbox:
    pad = 6
    l, t, r, b = bbox
    l = max(0, l - pad); t = max(0, t - pad)
    r = min(im.width, r + pad); b = min(im.height, b + pad)
    im2 = im.crop((l, t, r, b))
else:
    im2 = im
im2.save(r"D:/personal-site/public/portrait.png")
print("saved:", im2.size, "ratio:", round(im2.width / im2.height, 3))
