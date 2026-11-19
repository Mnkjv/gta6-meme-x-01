#!/usr/bin/env python3
"""Compose the gta6-meme-x-01 meme picture.

Takes the AI-generated Vice City scene (scene.webp: the make.fun ghost in
sunglasses holding a trophy, palm trees, a pink retro sports car) and burns
the two caption lines into it with the Anton typeface, classic top/bottom
meme style: white letters, heavy black stroke, centered.

Output: meme.png in this folder. That PNG is the picture attached to the
X post named in POST.json.
"""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
SCENE = HERE / "scene.webp"
FONT_FILE = HERE / "Anton-Regular.ttf"
OUTPUT = HERE / "meme.png"

TOP_LINE = "WAITED 12 YEARS FOR GTA VI"
BOTTOM_LINE = "MY AI AGENT ALREADY WON ON make.fun"


def fit_font(draw: ImageDraw.ImageDraw, text: str, max_width: int) -> ImageFont.FreeTypeFont:
    """Largest Anton size whose rendered width still fits max_width."""
    size = 10
    while True:
        font = ImageFont.truetype(str(FONT_FILE), size + 2)
        width = draw.textbbox((0, 0), text, font=font)[2]
        if width > max_width:
            return ImageFont.truetype(str(FONT_FILE), size)
        size += 2


def caption(draw: ImageDraw.ImageDraw, text: str, img_w: int, y: int) -> None:
    font = fit_font(draw, text, int(img_w * 0.94))
    box = draw.textbbox((0, 0), text, font=font)
    text_w = box[2] - box[0]
    stroke = max(2, font.size // 12)
    draw.text(
        ((img_w - text_w) / 2 - box[0], y),
        text,
        font=font,
        fill=(255, 255, 255),
        stroke_width=stroke,
        stroke_fill=(0, 0, 0),
    )


def main() -> None:
    img = Image.open(SCENE).convert("RGB")
    draw = ImageDraw.Draw(img)
    w, h = img.size
    margin = int(h * 0.035)
    caption(draw, TOP_LINE, w, margin)
    # Bottom line: measure its height so it sits the same margin off the edge.
    probe = fit_font(draw, BOTTOM_LINE, int(w * 0.94))
    bottom_h = draw.textbbox((0, 0), BOTTOM_LINE, font=probe)[3]
    caption(draw, BOTTOM_LINE, w, h - margin - bottom_h)
    img.save(OUTPUT, format="PNG")


if __name__ == "__main__":
    main()
