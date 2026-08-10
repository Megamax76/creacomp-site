#!/usr/bin/env python3
"""Télécharge les photographies Unsplash utilisées par le site et écrit leurs crédits.

Les images sont stockées dans le dépôt plutôt que chargées depuis un CDN : le site
ne doit émettre aucune requête vers un tiers. Toutes les photographies retenues
relèvent de la licence Unsplash (usage libre, y compris commercial) ; les images
« Unsplash+ », payantes, sont exclues de la sélection.

Le référentiel comporte une compétence « Créditer et respecter les droits des
autres » : le site se doit de l'appliquer à lui-même. Ce script produit donc
aussi le fichier de crédits affiché sur la page « Utiliser & citer ».
"""

import json
import pathlib
import sys
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
IMAGES = ROOT / 'src' / 'assets' / 'images'
CREDITS = ROOT / 'src' / 'data' / 'credits.json'

UTM = 'utm_source=creacomp&utm_medium=referral'

# clé locale, identifiant Unsplash, identifiant de fichier, auteur, compte, largeur
SELECTION = [
    ('hero', 'LX3YF0Rv524', 'photo-1727334291061-fd29582ef9dc',
     'Luciano Oliveira', 'lucianooliveira', 2000),
    ('rubrique-1', 'HeNrEdA4Zp4', 'photo-1573812195421-50a396d17893',
     'Utsav Srestha', 'utsavsrestha', 1000),
    ('rubrique-2', 'XoDggF_bnUA', 'photo-1743765361019-931455dbfe55',
     'Lucas Gallone', 'lucasgallone', 1000),
    ('rubrique-3', '8yF_140vczg', 'photo-1642285230633-cf8012546f14',
     'FÍA YANG', 'fiayang', 1000),
    ('rubrique-4', '_c-4a2-Wig8', 'photo-1752625151622-aae91be89216',
     'camera obscura', 'cameraobscura2000', 1000),
    ('rubrique-5', 'VQMszEo0x9c', 'photo-1610659714633-937a272e5279',
     'Nick Fewings', 'jannerboy62', 1000),
    ('rubrique-6', 'Ijhk9CAkPeQ', 'photo-1750989873854-b93d1bf2d3ea',
     'Andrés Silva', 'andrew07', 1000),
    ('rubrique-7', 'sMfZrBPSgk8', 'photo-1697497710118-0d5cb5a7094a',
     'Joe Halinar', 'jhalinar', 1000),
    ('fil-t1', 'C5y5N7apuv8', 'photo-1623376551152-6c5780adf9ad',
     'WELLSTUDIO', 'wellstudio', 1000),
    ('fil-t2', '-H8KwSFxfR4', 'photo-1506689205310-0a29c388691c',
     'Peter Aschoff', 'farbensammler', 1000),
    ('fil-t3', 'WEjv3BMP2ik', 'photo-1636837955417-2d8a4e49368f',
     'Pawel Czerwinski', 'pawel_czerwinski', 1000),
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
