# Contribuer à CréaComp

Le référentiel est un travail ouvert : les retours, les usages signalés et les
objections argumentées en nourrissent les révisions. Ce document dit ce qui est
attendu selon ce que vous apportez.

Le canal par défaut est
[une issue](https://github.com/Megamax76/creacomp-site/issues/new/choose). Pour
une faille de sécurité, ne passez pas par là — voir [SECURITY.md](SECURITY.md).

## Deux natures de contribution, deux exigences

Ce dépôt contient **le référentiel** et **le site qui le publie**. Une coquille
dans un descripteur et un correctif de mise en page ne se traitent pas de la
même façon.

### Discuter le référentiel lui-même

C'est la contribution la plus utile, et la plus exigeante. Un descripteur mal
formulé, un niveau mal calibré, une compétence manquante ou redondante : dites
lequel, et **pourquoi**.

Ce qui rend une objection utile :

- **Elle nomme précisément sa cible** — le `code` de l'entrée (`1.1`, `T2`…) et
  le niveau concerné (`N1`…`N4`).
- **Elle argumente depuis un usage réel** — une formation que vous avez conduite,
  une évaluation qui n'a pas fonctionné, une pratique professionnelle que le
  descripteur décrit mal. Un désaccord de principe se discute aussi, mais un
  cas concret pèse plus lourd.
- **Elle propose une reformulation** quand c'est possible, même imparfaite.

Les descripteurs sont volontairement **observables** : ils commencent par « Est
capable de… » et décrivent une action qu'on peut constater. Une proposition qui
retourne à une formulation d'intention (« comprend l'importance de… ») sera
discutée sur ce point.

### Proposer une traduction

Les traductions sont explicitement bienvenues, et la structure des données est
faite pour elles.

**Ouvrez une issue avant de commencer.** Une traduction représente 124
descripteurs plus les textes éditoriaux : autant ne pas découvrir à la fin que
quelqu'un d'autre s'y était mis, ou que le référentiel était en cours de
révision.

Une traduction se fait en dupliquant `src/data/fr/` vers `src/data/<langue>/` et
en conservant **rigoureusement** les champs `code` : ce sont eux qui apparient
les langues et permettent au sélecteur de langue de mener à la page équivalente.
Le routage bilingue vit dans [`src/lib/i18n.ts`](src/lib/i18n.ts) ; ajouter une
troisième langue demande d'y toucher, ainsi qu'à `astro.config.mjs`.

Rappel de licence : une traduction est une adaptation, et doit donc être
diffusée sous **CC BY-SA 4.0**, comme l'original.

### Corriger ou améliorer le site

Coquilles, problèmes d'affichage, défauts d'accessibilité, améliorations de
performance : une demande de fusion directe convient, sans issue préalable.

## Mettre en place l'environnement

Node.js 22 ou plus.

```bash
git clone https://github.com/Megamax76/creacomp-site.git
cd creacomp-site
npm install
npm run dev
```

## Ce qui doit passer avant de proposer une fusion

Aucune de ces vérifications n'est automatisée en dehors de la construction :
faites-les tourner vous-même.

```bash
npx astro check    # doit rester à 0 erreur
npm run build      # doit produire 73 pages sans avertissement
npm audit          # doit rester à 0 vulnérabilité
npm run preview    # puis ouvrir le site et vérifier la console
```

**La console du navigateur doit être vide au chargement.** Ce n'est pas une
coquetterie : c'est le seul signal qui révèle une violation de la politique de
sécurité du contenu, laquelle échoue en silence.

> [!WARNING]
> **N'utilisez aucun attribut `style=` en ligne.** La politique de sécurité les
> bloque sans casser la construction : le style ne s'applique tout simplement
> pas. Passez par une classe ou un attribut de données ciblé en CSS — voir
> [`Motif.astro`](src/components/Motif.astro) pour le motif à suivre.

Si vous modifiez le contenu du référentiel, changez un `code` **dans les deux
langues** ou dans aucune.

## Régénérer les captures du README

Les deux captures de `docs/media/` vieilliront avec le design. Elles sont
produites en headless, sans dépendance ajoutée au projet — Chrome suffit.

Servez d'abord le site construit :

```bash
npm run build && npm run preview   # sert dist/ sur le port 4321
```

Puis, dans un autre terminal :

```bash
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

"$CHROME" --headless=old --disable-gpu --hide-scrollbars \
  --virtual-time-budget=8000 --force-device-scale-factor=2 \
  --window-size=1280,800 --user-data-dir="$(mktemp -d)" \
  --screenshot=accueil.png http://localhost:4321/

"$CHROME" --headless=old --disable-gpu --hide-scrollbars \
  --virtual-time-budget=8000 --force-device-scale-factor=2 \
  --window-size=1280,1750 --user-data-dir="$(mktemp -d)" \
  --screenshot=referentiel.png http://localhost:4321/referentiel/
```

`--virtual-time-budget` est indispensable : sans lui Chrome écrit le fichier
puis ne rend jamais la main. Il peut malgré tout rester en arrière-plan —
`pkill -f 'Google Chrome.*headless'` s'il traîne.

Convertissez enfin en webp, ce qui divise le poids par dix, avec le `sharp`
qu'Astro installe déjà :

```bash
node -e "
const sharp = require('sharp');
sharp('accueil.png').resize({width:1600}).webp({quality:86}).toFile('docs/media/accueil.webp');
sharp('referentiel.png').resize({width:1400}).webp({quality:86}).toFile('docs/media/referentiel.webp');
"
```

Ne versionnez pas les PNG intermédiaires.

## Style

- **Le code suit le code existant** : mêmes conventions de nommage, même densité
  de commentaires, mêmes idiomes. Regardez le fichier voisin avant d'écrire.
- **Les commentaires et les messages de commit sont en français**, comme le reste
  du dépôt. Un commentaire dit *pourquoi*, pas *quoi*.
- **Pas de dépendance nouvelle sans raison forte.** Le site ne charge rien de
  l'extérieur et n'embarque aucun script tiers : c'est une propriété qu'on tient,
  pas un hasard. Une demande de fusion qui ajoute une dépendance doit dire ce
  qu'elle apporte que le code existant ne sait pas faire.

## Conduite

Discutez des idées, pas des personnes. Une objection technique sur un
descripteur est bienvenue quelle qu'en soit la vigueur ; une attaque personnelle
ne l'est pas et sera fermée sans discussion. Voir
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).

## Ce que vous conservez

Vous gardez la paternité de vos contributions. En les proposant, vous acceptez
qu'elles soient publiées sous les licences du dépôt : **CC BY-SA 4.0** pour le
contenu du référentiel, **MIT** pour le code. Les contributeurs d'une traduction
ou d'une révision substantielle sont crédités.
