#!/usr/bin/env python3
"""Télécharge les photographies Unsplash utilisées par le site et écrit leurs crédits.

Les images sont stockées dans le dépôt plutôt que chargées depuis un CDN : le site
ne doit émettre aucune requête vers un tiers. Toutes les photographies retenues
relèvent de la licence Unsplash (usage libre, y compris commercial) ; les images
« Unsplash+ », payantes, sont exclues de la sélection.

Le script produit aussi le fichier de crédits affiché sur la page
« Utiliser & citer ».
"""

import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMAGES = ROOT / 'src' / 'assets' / 'images'
CREDITS = ROOT / 'src' / 'data' / 'credits.json'

UTM = 'utm_source=creacomp&utm_medium=referral'

# Trois photographies seulement : accueil, page du cadre, page de contact.
# Les rubriques du référentiel sont signalées par des motifs dessinés, pas
# par des images — voir src/components/Motif.astro.
#
# Les largeurs sont celles de la source conservée dans le dépôt, pas celles
# qui partent en ligne : Astro en tire des rendus WebP de 640 à 2560 px. Elles
# valent 2600 px parce que les trois cadres sont recadrés en `cover` et qu'un
# écran à deux points par pixel demande jusqu'à ~2500 px de source pour rester
# net ; en dessous, le navigateur agrandit et l'image se pixellise.
# clé locale, identifiant Unsplash, identifiant de fichier, auteur, compte, largeur
SELECTION = [
    ('hero', 'CTflmHHVrBM', 'photo-1603993097397-89c963e325c7',
     'Jakob Owens', 'jakobowens1', 2600),
    ('cadre', '_ar2ENzmqb0', 'photo-1507738978512-35798112892c',
     'Sylvia Yang', 'sylviasyang', 2600),
    ('contact', 'L9wxrShZboU', 'photo-1685444857197-a7739c9017fc',
     'Ries Bosch', 'ries_bosch', 2600),
]


def download(file_id: str, width: int, target: pathlib.Path) -> int:
    url = f'https://images.unsplash.com/{file_id}?w={width}&q=80&fm=jpg&fit=max'
    request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(request, timeout=60) as response:
        payload = response.read()
    if not payload.startswith(b'\xff\xd8'):
        raise SystemExit(f'{target.name} : la réponse n\'est pas un JPEG')
    target.write_bytes(payload)
    return len(payload)


def largeur(chemin: pathlib.Path) -> int:
    """Largeur d'un JPEG, lue dans son premier segment SOF."""
    octets = chemin.read_bytes()
    i = 2
    while i + 9 < len(octets):
        if octets[i] != 0xFF:
            return 0
        marqueur, taille = octets[i + 1], int.from_bytes(octets[i + 2:i + 4], 'big')
        if 0xC0 <= marqueur <= 0xCF and marqueur not in (0xC4, 0xC8, 0xCC):
            return int.from_bytes(octets[i + 7:i + 9], 'big')
        i += 2 + taille
    return 0


def main() -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    credits = []
    total = 0

    for key, photo_id, file_id, author, username, width in SELECTION:
        target = IMAGES / f'{key}.jpg'
        # La largeur demandée fait partie de l'identité du fichier : l'augmenter
        # doit relancer le téléchargement, sinon le dépôt garde l'ancienne source.
        if target.exists() and largeur(target) >= width:
            size = target.stat().st_size
        else:
            size = download(file_id, width, target)
        total += size
        credits.append({
            'key': key,
            'author': author,
            'photoUrl': f'https://unsplash.com/photos/{photo_id}?{UTM}',
            'authorUrl': f'https://unsplash.com/@{username}?{UTM}',
        })
        print(f'{key:12} {author:22} {size / 1024:7.0f} Kio')

    CREDITS.write_text(
        json.dumps({'source': 'Unsplash', 'sourceUrl': f'https://unsplash.com/?{UTM}',
                    'items': credits}, ensure_ascii=False, indent=2) + '\n',
        encoding='utf-8')
    print(f'\n{len(credits)} images · {total / 1024 / 1024:.1f} Mio · crédits → {CREDITS.relative_to(ROOT)}')


if __name__ == '__main__':
    sys.exit(main())
