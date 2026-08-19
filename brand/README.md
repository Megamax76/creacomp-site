# Identité visuelle CreaComp

La marque est un **obturateur à six lames refermé sur un C**.

Six lames pour les rubriques 2 à 7. La première, *S'informer*, n'est pas une
lame : **c'est l'ouverture elle-même**, et c'est elle qui porte le C. Sept
rubriques, donc, dont une est le trou par lequel tout entre — ce que dit
exactement le référentiel, où recevoir précède produire.

Le choix de l'obturateur n'est pas décoratif. C'est l'organe par lequel une
caméra décide de ce qu'elle laisse entrer, et un diaphragme s'ouvre par degrés,
jamais en tout ou rien, comme les quatre niveaux de maîtrise.

Le C est géométrique, terminaisons coupées à la verticale, quand le mot est en
Fraunces : le symbole dit l'outil, le mot dit le référentiel.

## Couleurs

Le C, et le mot, sont en **pétrole `#1B5068`** — la couleur de la rubrique 1,
qui est aussi l'accent du site. Les six lames, dans le sens des aiguilles depuis
le haut :

| Lame | Rubrique | Clair | Sombre |
|---|---|---|---|
| — | **1 · S'informer** — *l'ouverture, le C* | `#1B5068` pétrole | `#6FB4D6` |
| 1 | 2 · Analyser | `#454391` indigo | `#A29FEE` |
| 2 | 3 · Créer | `#9C2C4A` carmin | `#EA8BA3` |
| 3 | 4 · Faire | `#A9551F` terre | `#EAA269` |
| 4 | 5 · Collaborer | `#2A6B4B` forêt | `#78C9A0` |
| 5 | 6 · Entreprendre | `#14707F` sarcelle | `#62C4D4` |
| 6 | 7 · Rentabiliser | `#7A5C15` bronze | `#D6B660` |

La ligne de définition est en `#6B6558` (`#968D7E` sur fond sombre). Ce sont les
variables de [`src/styles/global.css`](../src/styles/global.css) : le logo et le
site ne peuvent pas diverger.

### Pourquoi c'est le pétrole qui quitte le cercle

Mesuré, pas choisi à l'œil. Sur les sept teintes du référentiel, une seule paire
est franchement trop proche : **pétrole / sarcelle, ΔE 16** — deux bleus-verts.
Toutes les autres paires sont au-delà de 26.

Sortir l'une des deux du cercle fait passer l'écart minimal entre lames de 16 à
26. C'est le pétrole qui sort, pour deux raisons : il est déjà l'accent du site,
donc le C et le mot restent de la même encre ; et la rubrique 1 est celle dont
le rôle d'ouverture se justifie.

## Géométrie

Rayon extérieur 47, ouverture 34, vrille des lames 35°, jeu 2,6°, dans un carré
de 100. Le C mesure 28,49 de rayon pour 12,5 d'épaisseur : il occupe presque
toute l'ouverture, ce qui le tient lisible jusqu'à 16 px. Il est décalé de 1,2
unité vers la droite — centré géométriquement, il paraissait pencher à gauche,
sa masse étant du côté fermé — mais pas davantage : au-delà, il vient buter sur
le bord de lame en haut à droite et le jour se referme d'un seul côté. Ce rayon
n'est pas saisi à la main, il se déduit du décalage : voir `loge()` dans le
script.

## Les fichiers

### Verrous — le logo complet

| Fichier | Usage |
|---|---|
| `creacomp-logo.svg` | Verrou horizontal, français. Le cas courant. |
| `creacomp-logo-en.svg` | Verrou horizontal, anglais. |
| `creacomp-logo-sombre.svg`, `creacomp-logo-en-sombre.svg` | Les mêmes, pour un fond sombre. |
| `creacomp-logo-centre.svg`, `-en`, `-sombre` | Verrou centré : couverture, page de titre, diapositive. |

La ligne de définition est justifiée sur la largeur exacte du mot. Ne pas la
redimensionner seule.

### Le symbole seul

| Fichier | Usage |
|---|---|
| `creacomp-marque.svg` | L'obturateur en six couleurs. Avatar, favicon, vignette. |
| `creacomp-marque-sombre.svg` | Le même, teintes du thème sombre. |
| `creacomp-marque-petrole.svg` | Version monochrome pétrole — **à préférer en dessous de 24 px**. |
| `creacomp-marque-mono.svg` | Monochrome en `currentColor` : hérite de la couleur du texte. |
| `creacomp-marque-tuile.svg`, `-sombre` | Le symbole posé sur une tuile pleine. |
| `creacomp-mot.svg` | Le mot seul, sans symbole ni ligne. |
| `favicon.svg` | La tuile, qui bascule seule en thème sombre. |

### Exports matriciels

`creacomp-icone-{32,180,512,1024}.png` pour les icônes (180 = `apple-touch-icon`),
`creacomp-marque-1024.png` pour le symbole sur fond transparent,
`creacomp-logo-2000.png`, `creacomp-logo-sombre-2000.png`,
`creacomp-logo-centre-1200.png` et `creacomp-mot-2000.png` pour les usages qui
n'acceptent pas le SVG.

### Carte sociale

`creacomp-carte-sociale.svg` / `.png` et leurs jumelles `-en`, en 1200 × 630,
pour l'aperçu des liens partagés. Le site en sert une copie depuis
`public/carte-sociale.png`.

### Pour le site

`traces.json` contient les tracés bruts du symbole — six lames et le C. C'est ce
que recopie [`src/components/Logo.astro`](../src/components/Logo.astro), qui
peint le symbole avec les variables du thème et suit donc la bascule
clair/sombre sans second fichier.

## Règles d'emploi

- **Air.** Réserver autour du verrou une marge au moins égale au rayon du
  symbole.
- **Réduction.** Le verrou complet tient jusqu'à 22 px de haut. Le symbole en
  couleurs tient jusqu'à 24 px ; en dessous, employer
  `creacomp-marque-petrole.svg`, qui reste net à 16 px.
- **Ordre des lames.** Il suit l'ordre des rubriques. Ne pas le permuter pour
  des raisons d'équilibre chromatique : la position de chaque couleur veut dire
  quelque chose.
- **À ne pas faire.** Ne pas faire tourner le symbole (la vrille des lames a un
  sens de lecture), ne pas colorer le C dans une couleur de lame, ne pas poser
  la version claire sur un fond sombre.

## Une autre piste, gardée

`variante-accent/` contient une première direction : le é de *Créa* taillé dans
le Fraunces du site, posé dans un carré pétrole.

Elle est antérieure à la chute de l'accent : son symbole comme son mot portent
encore *CréaComp*. Elle est donc conservée pour mémoire, et non réutilisable
telle quelle — la reprendre demanderait de la redessiner sur *CreaComp*, ce qui
la priverait de ce qui en faisait l'idée.

## Refabriquer les fichiers

Tout ce dossier est produit par deux scripts. Les lames sont calculées ; le mot
et la ligne sont des contours extraits des fontes du projet — on instancie la
fonte variable aux axes voulus, on compose le texte avec HarfBuzz pour récupérer
le crénage, on convertit les glyphes en chemins. Aucun fichier produit n'a
besoin qu'une fonte soit installée pour s'afficher.

```bash
python3 -m venv .venv && .venv/bin/pip install fonttools brotli uharfbuzz
.venv/bin/python scripts/logo/construire.py   # les SVG
node scripts/logo/rasteriser.mjs              # les PNG
```

La géométrie et les couleurs sont en tête de
[`scripts/logo/construire.py`](../scripts/logo/construire.py), commentées : c'est
là qu'on change quelque chose, jamais dans les SVG produits.

Après un changement, recopier dans `public/` les fichiers que le site sert —
`favicon.svg`, les icônes, les cartes sociales — et reporter les tracés dans
`src/components/Logo.astro` depuis `traces.json`.
