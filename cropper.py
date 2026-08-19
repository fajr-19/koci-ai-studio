from PIL import Image

# Koordinat berdasarkan sheet master kamu
BASE_W = 1369
BASE_H = 1149

BASE_BOXES = {
    "Yoyin": (55, 75, 205, 365),
    "Cecep": (520, 85, 645, 365),
    "Kokow": (945, 100, 1075, 365),
    "Nian": (55, 610, 200, 825),
    "Ompel": (520, 620, 655, 810),
    "Family": (760, 520, 1335, 930),
}

def _scaled_box(box, w, h):
    x1, y1, x2, y2 = box
    sx = w / BASE_W
    sy = h / BASE_H
    return (
        int(x1 * sx),
        int(y1 * sy),
        int(x2 * sx),
        int(y2 * sy),
    )

def crop_character(master_image, character):
    img = master_image.convert("RGB")
    w, h = img.size
    if character not in BASE_BOXES:
        raise ValueError(f"Character '{character}' not found.")

    box = _scaled_box(BASE_BOXES[character], w, h)
    cropped = img.crop(box)

    # buat canvas square supaya enak untuk backend video
    bg = img.getpixel((5, 5))
    canvas = Image.new("RGB", (768, 768), bg)

    max_w = int(768 * 0.76)
    max_h = int(768 * 0.88)

    ratio = min(max_w / cropped.width, max_h / cropped.height)
    new_w = int(cropped.width * ratio)
    new_h = int(cropped.height * ratio)

    cropped = cropped.resize((new_w, new_h), Image.Resampling.LANCZOS)

    x = (768 - new_w) // 2
    y = 768 - new_h - int(768 * 0.05)
    canvas.paste(cropped, (x, y))

    return canvas
