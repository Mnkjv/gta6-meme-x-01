// gta6-meme-x-01 entry program.
//
// The whole job of this program is to hand the house one file: POST.json,
// which names the X post that carries the meme. When the grader runs this
// file it copies POST.json from the bot directory into the output
// directory and exits. Nothing else is produced on purpose: the judge
// reads the post itself on X, not anything this program writes.

import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, resolve } from "node:path";
import { fileURLToPath } from "node:url";

// Where the repository lives. The grader says MAKEFUN_BOT_DIR; when it is
// absent (a human running the file by hand) the script's own folder is the
// only sensible answer, because POST.json sits beside main.ts.
const scriptDir = dirname(fileURLToPath(import.meta.url));
const botDir = process.env.MAKEFUN_BOT_DIR
  ? resolve(process.env.MAKEFUN_BOT_DIR)
  : scriptDir;

// Where the copy goes. MAKEFUN_OUTPUT_DIR wins; otherwise a plain ./out
// under the current working directory, created on demand below.
const outputDir = process.env.MAKEFUN_OUTPUT_DIR
  ? resolve(process.env.MAKEFUN_OUTPUT_DIR)
  : resolve(process.cwd(), "out");

mkdirSync(outputDir, { recursive: true });

const source = resolve(botDir, "POST.json");
const target = resolve(outputDir, "POST.json");
try {
  copyFileSync(source, target);
} catch (err) {
  // Fail loudly rather than exit 0 with nothing handed in: a missing or
  // unreadable POST.json means there is no entry at all.
  console.error(`gta6-meme-x-01: cannot copy ${source} -> ${target}: ${err}`);
  process.exit(1);
}
