/**
 * Exports matriciels du logo, pour les usages qui n'acceptent pas le SVG.
 * Dépend de `sharp`, déjà présent via Astro.   node scripts/logo/rasteriser.mjs
 */
import sharp from 'sharp';
import { readFileSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const RACINE = dirname(dirname(dirname(fileURLToPath(import.meta.url))));
const B = join(RACINE, 'brand');

const travaux = [
  ['creacomp-marque-tuile', 'creacomp-icone-1024.png', 1024],
  ['creacomp-marque-tuile', 'creacomp-icone-512.png', 512],
  ['creacomp-marque-tuile', 'creacomp-icone-180.png', 180],
  ['creacomp-marque-tuile', 'creacomp-icone-32.png', 32],
  ['creacomp-marque', 'creacomp-marque-1024.png', 1024],
  ['creacomp-logo', 'creacomp-logo-2000.png', 2000],
  ['creacomp-logo-sombre', 'creacomp-logo-sombre-2000.png', 2000],
  ['creacomp-logo-centre', 'creacomp-logo-centre-1200.png', 1200],
  ['creacomp-mot', 'creacomp-mot-2000.png', 2000],
  ['creacomp-carte-sociale', 'creacomp-carte-sociale.png', 1200],
  ['creacomp-carte-sociale-en', 'creacomp-carte-sociale-en.png', 1200],
];

for (const [source, sortie, largeur] of travaux) {
  const svg = readFileSync(join(B, `${source}.svg`));
  const [, , vw, vh] = svg.toString().match(/viewBox="([\d.]+) ([\d.]+) ([\d.]+) ([\d.]+)"/)
    .slice(1).map(Number);
  const info = await sharp(svg, { density: 900 })
    .resize({ width: largeur, height: Math.round((largeur * vh) / vw) })
    .png({ compressionLevel: 9 })
    .toFile(join(B, sortie));
  console.log(sortie.padEnd(34), `${info.width}×${info.height}`, `${(info.size / 1024).toFixed(1)} ko`);
}
