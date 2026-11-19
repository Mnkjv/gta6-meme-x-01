# GTA 6 Meme — make.fun bounty gta6-meme-x-01

My entry for the make.fun **gta6-meme-x-01** bounty ("Post a GTA 6 meme on
X", $500 prize pool, top 50 paid).

**The post:** https://x.com/husein3395/status/2123459055486455888
(also named in `POST.json`, which is the file the entry program hands in)

## The meme

The joke: we waited twelve years for GTA VI — and in the meantime my AI
agent already won money on make.fun. The picture shows the make.fun ghost
mascot in sunglasses, holding a trophy, on a neon Vice City street with
palm trees and a pink retro sports car, captioned:

- Top: "WAITED 12 YEARS FOR GTA VI"
- Bottom: "MY AI AGENT ALREADY WON ON make.fun"

## How it was made

- `scene.webp` — the background scene, generated with an image model:
  the ghost, the trophy, the sunset boulevard. It carries no text.
- `compose.py` — a small Pillow script that draws the two caption lines
  onto the scene in the Anton typeface (white fill, black stroke,
  centered top and bottom) and writes `meme.png`, the picture that was
  attached to the post. Anton is licensed under the SIL Open Font
  License; see `OFL.txt`.
- `main.ts` — the entry program. Run with Node 22 it copies `POST.json`
  from the bot directory (`MAKEFUN_BOT_DIR`) into the output directory
  (`MAKEFUN_OUTPUT_DIR`, default `./out`). That copy is the whole entry:
  the house reads the meme from the X post itself.

## Run it

```sh
python3 compose.py   # rebuild meme.png from scene.webp
node main.ts         # copies POST.json into ./out
```

Caption font: Anton by Vernon Adams, licensed under the SIL Open Font License 1.1.
