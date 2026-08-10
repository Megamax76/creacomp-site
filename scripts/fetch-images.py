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
# clé locale, identifiant Unsplash, identifiant de fichier, auteur, compte, largeur
SELECTION = [
    ('hero', 'LX3YF0Rv524', 'photo-1727334291061-fd29582ef9dc',
     'Luciano Oliveira', 'lucianooliveira', 1400),
    ('cadre', '_ar2ENzmqb0', 'photo-1507738978512-35798112892c',
     'Sylvia Yang', 'sylviasyang', 1800),
    ('contact', 'L9wxrShZboU', 'photo-1685444857197-a7739c9017fc',
     'Ries Bosch', 'ries_bosch', 1400),
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


def main() -> None:
    IMAGES.mkdir(parents=True, exist_ok=True)
    credits = []
    total = 0

    for key, photo_id, file_id, author, username, width in SELECTION:
        target = IMAGES / f'{key}.jpg'
        if target.exists():
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
