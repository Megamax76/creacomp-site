#!/usr/bin/env python3
"""Fabrique tous les fichiers de `brand/` — le logo CreaComp, en SVG vectorisé.

La marque est un obturateur à six lames refermé sur un C. Les lames sont
calculées ; le mot « CreaComp » et la ligne de définition sont des contours
extraits des fontes du projet, de sorte qu'aucun fichier produit n'ait besoin
qu'une fonte soit installée pour s'afficher — chez un imprimeur comme dans un
navigateur.

    python3 -m venv .venv && .venv/bin/pip install fonttools brotli uharfbuzz
    .venv/bin/python scripts/logo/construire.py

Puis, pour les exports matriciels :  node scripts/logo/rasteriser.mjs
"""

import json
import math
import os

import uharfbuzz as hb
from fontTools.misc.transform import Transform
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer

RACINE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FONTES = os.path.join(RACINE, "node_modules", "@fontsource-variable")
FRAUNCES = f"{FONTES}/fraunces/files/fraunces-latin-full-normal.woff2"
ARCHIVO = f"{FONTES}/archivo/files/archivo-latin-wght-normal.woff2"
SORTIE = os.path.join(RACINE, "brand")

# ─── Couleurs ───────────────────────────────────────────────────────────────
# Six lames pour les rubriques 2 à 7. La première, S'informer, n'est pas une
# lame : c'est l'ouverture elle-même, et c'est elle qui porte le C. Elle sort
# du cercle parce qu'elle est le seul quasi-doublon de la palette — pétrole et
# sarcelle sont à ΔE 16, quand toutes les autres paires dépassent 26.
LAMES_CLAIR = ["#454391", "#9c2c4a", "#a9551f", "#2a6b4b", "#14707f", "#7a5c15"]
LAMES_SOMBRE = ["#a29fee", "#ea8ba3", "#eaa269", "#78c9a0", "#62c4d4", "#d6b660"]
PETROLE, PETROLE_CLAIR = "#1b5068", "#6fb4d6"
PAPIER, NUIT = "#fbf9f5", "#131210"
GRIS, GRIS_SOMBRE = "#6b6558", "#968d7e"

# ─── Géométrie, arrêtée après épreuves ──────────────────────────────────────
N = 6
PAS = 360 / N
CX = CY = 50.0
R = 47.0                 # rayon extérieur du disque
RI = 34.0                # rayon de l'ouverture
VRILLE = 35.0            # décalage angulaire du bord intérieur de chaque lame
JEU = 2.6                # blanc entre deux lames, en degrés
C_EP = 12.5              # épaisseur du C
C_DX = 1.2               # recentrage optique : la masse du C est du côté fermé
C_JOUR = 0.25            # jour entre le C et le bord de lame le plus proche

# L'ouverture est un hexagone : ses côtés sont les bords intérieurs des lames,
# chacun tendu entre deux points du cercle de rayon RI et distant du centre de
# RI × cos(moitié de l'arc qu'il sous-tend).
INSCRIT = math.cos(math.radians((PAS - JEU) / 2))


def loge(dx):
    """Rayon du plus grand cercle tenant dans l'ouverture, centré à dx du milieu.

    Le décalage optique rapproche le C de certains côtés et l'éloigne des
    autres ; c'est le plus serré des six qui commande. Chaque côté est normal
    à sa bissectrice, à mi-chemin de l'arc qu'il sous-tend.
    """
    return min(RI * INSCRIT - dx * math.cos(math.radians(k * PAS + PAS / 2 + VRILLE - 90))
               for k in range(N))


C_EXT = round(loge(C_DX) - C_JOUR, 2)
C_COUPE = round(C_EXT * 0.42, 2)

NOTE = (
    "<!-- CreaComp — six lames d'obturateur pour les rubriques 2 à 7 ; la première,\n"
    "     S'informer, est l'ouverture elle-même, et porte le C. Contours vectorisés :\n"
    "     aucune fonte n'est requise. Refabriqué par scripts/logo/construire.py. -->\n"
)


# ─── Le symbole ─────────────────────────────────────────────────────────────
def point(r, deg, cx=CX, cy=CY):
    """0° en haut, sens des aiguilles d'une montre."""
    a = math.radians(deg - 90)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def lame(k):
    a0, a1 = k * PAS + JEU / 2, (k + 1) * PAS - JEU / 2
    x0, y0 = point(R, a0)
    x1, y1 = point(R, a1)
    u1, v1 = point(RI, a1 + VRILLE)
    u0, v0 = point(RI, a0 + VRILLE)
    return (f"M{x0:.2f} {y0:.2f}A{R:g} {R:g} 0 0 1 {x1:.2f} {y1:.2f}"
            f"L{u1:.2f} {v1:.2f}L{u0:.2f} {v0:.2f}Z")


def lettre_c():
    """Un C géométrique : anneau ouvert à droite, terminaisons droites."""
    r_int = round(C_EXT - C_EP, 2)
    cx, cy = CX + C_DX, CY
    ho = C_EXT * math.sin(math.acos(C_COUPE / C_EXT))
    hi = r_int * math.sin(math.acos(C_COUPE / r_int))
    x = cx + C_COUPE
    return (f"M{x:.2f} {cy - ho:.2f}"
            f"A{C_EXT:g} {C_EXT:g} 0 1 0 {x:.2f} {cy + ho:.2f}"
            f"L{x:.2f} {cy + hi:.2f}"
            f"A{r_int:g} {r_int:g} 0 1 1 {x:.2f} {cy - hi:.2f}Z")


LAME_D = [lame(k) for k in range(N)]
C_D = lettre_c()


def symbole(lames, couleur_c):
    return ("".join(f'<path fill="{lames[k]}" d="{LAME_D[k]}"/>' for k in range(N))
            + f'<path fill="{couleur_c}" d="{C_D}"/>')


def monochrome(couleur):
    return symbole([couleur] * N, couleur)


# ─── Les contours typographiques ────────────────────────────────────────────
def instance(source, axes, tag):
    f = instancer.instantiateVariableFont(TTFont(source), axes, inplace=False,
                                          updateFontNames=False)
    f.flavor = None
    chemin = os.path.join("/tmp", f"_creacomp_{tag}.ttf")
    f.save(chemin)
    return f, chemin


def compose(font, chemin, texte, approche=0.0):
    """Positions des glyphes, crénage compris, en unités de la fonte."""
    face = hb.Face(hb.Blob.from_file_path(chemin))
    tampon = hb.Buffer()
    tampon.add_str(texte)
    tampon.guess_segment_properties()
    hb.shape(hb.Font(face), tampon, {"kern": True, "liga": True})
    noms = font.getGlyphOrder()
    suite, x = [], 0.0
    ecart = approche * face.upem
    for info, pos in zip(tampon.glyph_infos, tampon.glyph_positions):
        suite.append((noms[info.codepoint], x + pos.x_offset, pos.y_offset))
        x += pos.x_advance + ecart
    return suite


def _tracer(font, suite, plume, echelle, dx, dy):
    glyphes = font.getGlyphSet()
    for nom, gx, gy in suite:
        t = Transform(echelle, 0, 0, -echelle, dx + gx * echelle, dy - gy * echelle)
        glyphes[nom].draw(TransformPen(plume, t))


def boite(font, suite):
    p = BoundsPen(font.getGlyphSet())
    _tracer(font, suite, p, 1.0, 0, 0)
    return p.bounds


def contour(font, suite, echelle, dx, dy):
    p = SVGPathPen(font.getGlyphSet(), ntos=lambda v: f"{v:.2f}")
    _tracer(font, suite, p, echelle, dx, dy)
    return p.getCommands()


def normalise(source, axes, tag, texte, approche):
    """Trace un texte dans une boîte de 100 de haut, calée en haut à gauche."""
    font, chemin = instance(source, axes, tag)
    suite = compose(font, chemin, texte, approche)
    x0, haut, x1, bas = boite(font, suite)
    e = 100.0 / (bas - haut)
    return {"d": contour(font, suite, e, -x0 * e, -haut * e),
            "w": round((x1 - x0) * e, 3), "font": font, "chemin": chemin,
            "suite": suite, "haut": haut, "bas": bas, "echelle": e}


AXES_MOT = {"wght": 600, "opsz": 24, "SOFT": 20, "WONK": 1}
AXES_LIGNE = {"wght": 500}

MOT = normalise(FRAUNCES, AXES_MOT, "mot", "CreaComp", -0.022)
# Hauteur de capitale du mot, dans sa boîte de 100 : sert à caler tout le reste.
# Le mot ne porte ni accent ni jambage : le haut de la boîte est le haut du « C »,
# donc la capitale va du haut de boîte à la ligne de pied.
CAPITALE = round(-MOT["haut"] * MOT["echelle"], 3)

LIGNES = {
    "subFr": "RÉFÉRENTIEL DE LITTÉRATIE NUMÉRIQUE CRÉATIVE",
    "subEn": "DIGITAL CREATIVE LITERACY FRAMEWORK",
    "subFrCourt": "LITTÉRATIE NUMÉRIQUE CRÉATIVE",
    "subEnCourt": "DIGITAL CREATIVE LITERACY",
}
G = {"word": MOT}
for cle, texte in LIGNES.items():
    G[cle] = normalise(ARCHIVO, AXES_LIGNE, cle, texte, 0.13)


# ─── Assemblage ─────────────────────────────────────────────────────────────
def svg(w, h, corps, titre):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w:g} {h:g}" '
            f'width="{w:g}" height="{h:g}" role="img" aria-label="{titre}">\n'
            f'{NOTE}{corps}\n</svg>\n')


def ecrire(nom, contenu):
    with open(os.path.join(SORTIE, nom), "w") as f:
        f.write(contenu)
    print(f"{nom:36s} {len(contenu):6d} o")


def pose(cle, hauteur, x, y, couleur):
    return (f'<path transform="translate({x:.2f} {y:.2f}) scale({hauteur / 100:.6f})" '
            f'fill="{couleur}" d="{G[cle]["d"]}"/>')


def largeur(cle, hauteur):
    return G[cle]["w"] * hauteur / 100


SYM_CLAIR = symbole(LAMES_CLAIR, PETROLE)
SYM_SOMBRE = symbole(LAMES_SOMBRE, PETROLE_CLAIR)
os.makedirs(SORTIE, exist_ok=True)

ecrire("creacomp-marque.svg", svg(100, 100, SYM_CLAIR, "CreaComp"))
ecrire("creacomp-marque-sombre.svg", svg(100, 100, SYM_SOMBRE, "CreaComp"))
ecrire("creacomp-marque-mono.svg", svg(100, 100, monochrome("currentColor"), "CreaComp"))
ecrire("creacomp-marque-petrole.svg", svg(100, 100, monochrome(PETROLE), "CreaComp"))

ZOOM = "translate(50 50) scale(0.9) translate(-50 -50)"
ecrire("creacomp-marque-tuile.svg",
       svg(100, 100, f'<rect width="100" height="100" rx="2.5" fill="{PAPIER}"/>'
                     f'<g transform="{ZOOM}">{SYM_CLAIR}</g>', "CreaComp"))
ecrire("creacomp-marque-tuile-sombre.svg",
       svg(100, 100, f'<rect width="100" height="100" rx="2.5" fill="{NUIT}"/>'
                     f'<g transform="{ZOOM}">{SYM_SOMBRE}</g>', "CreaComp"))
ecrire("creacomp-mot.svg",
       svg(round(G["word"]["w"], 2), 100, pose("word", 100, 0, 0, PETROLE), "CreaComp"))


def verrou(ligne, nom, titre, sym, couleur_mot, couleur_ligne):
    """Verrou horizontal : le symbole, puis le mot et sa ligne de définition."""
    TAILLE, ECART, CAP = 66.0, 17.0, 30.0
    hm = CAP * 100 / CAPITALE                   # boîte complète du mot
    lm = largeur("word", hm)
    hl = lm * 100 / G[ligne]["w"]               # ligne justifiée sur le mot
    x = TAILLE + ECART
    W, H = x + lm, TAILLE
    haut = (H - (hm + 6.5 + hl)) / 2
    corps = (f'<g transform="scale({TAILLE / 100:.6f})">{sym}</g>'
             + pose("word", hm, x, haut, couleur_mot)
             + pose(ligne, hl, x, haut + hm + 6.5, couleur_ligne))
    ecrire(nom, svg(round(W, 2), round(H, 2), corps, titre))


TITRE_FR = "CreaComp — Référentiel de littératie numérique créative"
TITRE_EN = "CreaComp — Digital Creative Literacy Framework"
verrou("subFr", "creacomp-logo.svg", TITRE_FR, SYM_CLAIR, PETROLE, GRIS)
verrou("subEn", "creacomp-logo-en.svg", TITRE_EN, SYM_CLAIR, PETROLE, GRIS)
verrou("subFr", "creacomp-logo-sombre.svg", TITRE_FR, SYM_SOMBRE, PETROLE_CLAIR, GRIS_SOMBRE)
verrou("subEn", "creacomp-logo-en-sombre.svg", TITRE_EN, SYM_SOMBRE, PETROLE_CLAIR, GRIS_SOMBRE)


def centre(ligne, nom, titre, sym, couleur_mot, couleur_ligne):
    TAILLE, CAP = 92.0, 32.0
    hm = CAP * 100 / CAPITALE
    lm = largeur("word", hm)
    hl = lm * 100 / G[ligne]["w"]
    W = max(TAILLE, lm)
    y_mot = TAILLE + 17.0
    y_ligne = y_mot + hm + 7.0                  # dégage la descendante du « p »
    corps = (f'<g transform="translate({(W - TAILLE) / 2:.2f} 0) '
             f'scale({TAILLE / 100:.6f})">{sym}</g>'
             + pose("word", hm, (W - lm) / 2, y_mot, couleur_mot)
             + pose(ligne, hl, (W - lm) / 2, y_ligne, couleur_ligne))
    ecrire(nom, svg(round(W, 2), round(y_ligne + hl, 2), corps, titre))


centre("subFrCourt", "creacomp-logo-centre.svg", "CreaComp", SYM_CLAIR, PETROLE, GRIS)
centre("subEnCourt", "creacomp-logo-centre-en.svg", "CreaComp", SYM_CLAIR, PETROLE, GRIS)
centre("subFrCourt", "creacomp-logo-centre-sombre.svg", "CreaComp",
       SYM_SOMBRE, PETROLE_CLAIR, GRIS_SOMBRE)

FAV = "translate(50 50) scale(0.88) translate(-50 -50)"
ecrire("favicon.svg", svg(100, 100,
       f'  <style>\n'
       f'    .fond {{ fill: {PAPIER}; }} .sombre {{ display: none; }}\n'
       f'    @media (prefers-color-scheme: dark) {{\n'
       f'      .fond {{ fill: {NUIT}; }}\n'
       f'      .clair {{ display: none; }} .sombre {{ display: inline; }}\n'
       f'    }}\n'
       f'  </style>\n'
       f'  <rect width="100" height="100" rx="10" class="fond"/>\n'
       f'  <g class="clair" transform="{FAV}">{SYM_CLAIR}</g>\n'
       f'  <g class="sombre" transform="{FAV}">{SYM_SOMBRE}</g>\n', "CreaComp"))

# ─── Carte sociale, 1200 × 630 ──────────────────────────────────────────────
def carte(ligne, nom, titre):
    W, H, T = 1200.0, 630.0, 190.0
    hm = 96.0 * 100 / CAPITALE
    lm = largeur("word", hm)
    hl = lm * 100 / G[ligne]["w"]
    bloc = T + 54 + hm + 22 + hl
    y = (H - bloc) / 2
    corps = (f'<rect width="{W:g}" height="{H:g}" fill="{PAPIER}"/>'
             f'<g transform="translate({(W - T) / 2:.2f} {y:.2f}) scale({T / 100:.6f})">'
             f'{SYM_CLAIR}</g>'
             + pose("word", hm, (W - lm) / 2, y + T + 54, PETROLE)
             + pose(ligne, hl, (W - lm) / 2, y + T + 54 + hm + 22, GRIS))
    ecrire(nom, svg(W, H, corps, titre))


carte("subFr", "creacomp-carte-sociale.svg", TITRE_FR)
carte("subEn", "creacomp-carte-sociale-en.svg", TITRE_EN)

# ─── Les tracés, pour le composant Astro du site ────────────────────────────
with open(os.path.join(SORTIE, "traces.json"), "w") as f:
    json.dump({"lames": LAME_D, "c": C_D}, f, ensure_ascii=False, indent=2)
print(f"{'traces.json':36s} (tracés bruts, pour src/components/Logo.astro)")
