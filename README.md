<div align="center">

# CréaComp

**Le référentiel de compétences pour l'ère des créateurs**

Sept rubriques, 28 compétences, 124 descripteurs, quatre niveaux de maîtrise.
Bilingue français / anglais, librement réutilisable.

[**creacomp.org**](https://creacomp.org) · [Le référentiel](https://creacomp.org/referentiel/) · [Le cadre](https://creacomp.org/cadre/) · [English](https://creacomp.org/en/)

[![Déploiement](https://github.com/Megamax76/creacomp-site/actions/workflows/deploy.yml/badge.svg)](https://github.com/Megamax76/creacomp-site/actions/workflows/deploy.yml)
[![Contenu CC BY-SA 4.0](https://img.shields.io/badge/contenu-CC%20BY--SA%204.0-1a7f5a)](https://creativecommons.org/licenses/by-sa/4.0/deed.fr)
[![Code MIT](https://img.shields.io/badge/code-MIT-informational)](LICENSE-CODE)
[![Astro](https://img.shields.io/badge/Astro-7.2-bc52ee)](https://astro.build)

![Page d'accueil du site CréaComp](docs/media/accueil.webp)

</div>

---

## Sommaire

- [De quoi s'agit-il](#de-quoi-sagit-il)
- [Le référentiel en un coup d'œil](#le-référentiel-en-un-coup-dœil)
- [Utiliser le référentiel](#utiliser-le-référentiel-sans-toucher-au-code)
- [Faire tourner le site](#faire-tourner-le-site)
- [Comment le site est fait](#comment-le-site-est-fait)
- [Modifier le contenu](#modifier-le-contenu)
- [Mise en ligne](#mise-en-ligne)
- [Sécurité](#sécurité)
- [Contribuer](#contribuer)
- [Citer CréaComp](#citer-créacomp)
- [Licences](#licences)
- [English summary](#english-summary)

---

## De quoi s'agit-il

**CréaComp est un référentiel de compétences**, c'est-à-dire une description
structurée de ce qu'il faut savoir faire pour créer, diffuser et vivre de
contenus numériques. Il couvre ce que les référentiels existants traitent mal
ou pas du tout : la lecture critique d'un flux algorithmique, la construction
d'une voix, le travail avec l'IA génératrice, l'économie de l'attention, la
soutenabilité d'une pratique créative.

Il s'adresse à qui doit **former, évaluer ou se situer** : enseignants et
formateurs qui adossent une progression à un cadre explicite, organismes qui
construisent une certification, créateurs qui veulent savoir ce qu'il leur
reste à apprendre, chercheurs qui étudient ces compétences.

Ce dépôt contient **deux choses** : le référentiel lui-même, sous forme de
données structurées réutilisables, et le site qui le publie.

| | |
|---|---|
| **Version** | CréaComp 1.0 — édition 2026 |
| **Auteur** | Maxime Hébert |
| **Langues** | français (source), anglais (traduction maintenue à la main) |
| **Adossement** | niveaux alignés sur DigComp 1–8 |
| **Contenu** | CC BY-SA 4.0 — réutilisation, traduction et adaptation libres |
| **Statut** | publié ; le protocole de validation empirique est ouvert aux contributions |

> [!NOTE]
> Le référentiel décrit **un territoire, pas un parcours**. Nul n'est censé
> tout maîtriser, et il n'existe aucun ordre imposé de progression.

## Le référentiel en un coup d'œil

**Sept rubriques**, qui suivent le trajet d'une intention créative — de ce
qu'on reçoit à ce qu'on en tire :

| # | Rubrique | Ce qu'elle couvre |
|---|---|---|
| 1 | **S'informer** | Recevoir, évaluer et organiser l'information et les cultures numériques |
| 2 | **Analyser** | Comprendre les systèmes qui distribuent, mesurent et génèrent les contenus |
| 3 | **Créer** | Imaginer, concevoir et donner une forme singulière à une intention |
| 4 | **Faire** | Produire, publier, tenir une cadence |
| 5 | **Collaborer** | Travailler avec d'autres, une communauté, des pairs |
| 6 | **Entreprendre** | Construire une activité, se professionnaliser |
| 7 | **Rentabiliser** | Vivre de sa pratique, diversifier ses revenus |

**Trois fils transversaux**, qui traversent les sept rubriques au lieu de s'y
ranger :

| Code | Fil | Enjeu |
|---|---|---|
| **T1** | Discerner | Créer de manière transparente, loyale et non manipulatoire |
| **T2** | Durer | Préserver son énergie, son attention et son équilibre |
| **T3** | Se réinventer | Acquérir vite, abandonner ce qui ne fonctionne plus |

**Quatre niveaux de maîtrise**, décrits pour chacune des 31 entrées — soit
124 descripteurs :

| Niveau | Nom | Posture | Repère | DigComp |
|---|---|---|---|---|
| **N1** | Découverte | Je découvre et je comprends en pratiquant à petite échelle | Collège · grand débutant | 1–2 |
| **N2** | Application | J'applique consciemment dans une pratique régulière | Lycée · débutant avancé | 3–4 |
| **N3** | Autonomie | J'expérimente, je mesure et j'améliore en autonomie | Post-bac · professionnel junior | 5–6 |
| **N4** | Expertise | Je systématise et je maîtrise au bénéfice d'autrui | Professionnel confirmé · formateur | 7–8 |

La carte du site affiche les 31 entrées d'un seul regard, et le sélecteur de
niveau réécrit **tous** les descripteurs à la fois — on lit le référentiel à
hauteur de N1, puis de N4, sans quitter la page :

![La carte du référentiel, avec le sélecteur de niveau](docs/media/referentiel.webp)

## Utiliser le référentiel sans toucher au code

Le référentiel est publié en **CC BY-SA 4.0** : vous pouvez le reprendre, le
traduire, l'adapter à un contexte national ou sectoriel, y compris
commercialement — à condition de citer l'auteur et de partager vos adaptations
aux mêmes conditions.

Si vous voulez seulement **les données**, elles sont ici, sans passer par le
site :

| Fichier | Contenu |
|---|---|
| [`src/data/fr/framework.json`](src/data/fr/framework.json) | Les 7 rubriques, 28 compétences et 3 fils, avec définitions, composantes et 124 descripteurs |
| [`src/data/en/framework.json`](src/data/en/framework.json) | La traduction anglaise, structurellement identique |

La structure est stable et lisible directement :

```jsonc
{
  "rubrics":     [ { "id": 1, "title": "S'INFORMER", "definition": "…" } ],
  "competences": [ {
      "code": "1.1",                       // clé stable entre les langues
      "slug": "rechercher-et-sourcer",
      "title": "Rechercher et sourcer l'information",
      "definition": "…",
      "components": [ "…" ],               // ce que la compétence recouvre
      "levels": { "N1": "…", "N2": "…", "N3": "…", "N4": "…" },
      "rubricId": 1
  } ],
  "threads":     [ { "code": "T1", "title": "Discerner", "definition": "…" } ]
}
```

Le champ `code` (`1.1`, `T2`…) est la **clé stable** entre les deux langues.
C'est lui qui permet à une traduction de rester alignée sur l'original — et au
sélecteur de langue du site de mener à la page équivalente plutôt qu'à
l'accueil.

## Faire tourner le site

**Prérequis** : [Node.js](https://nodejs.org) 22 ou plus.

```bash
git clone https://github.com/Megamax76/creacomp-site.git
cd creacomp-site
npm install
npm run dev
```

Le site est alors servi sur <http://localhost:4321>.

| Commande | Effet |
|---|---|
| `npm run dev` | Serveur de développement, rechargement à chaud |
| `npm run build` | Construit le site statique dans `dist/` |
| `npm run preview` | Sert `dist/` localement, pour vérifier avant de publier |
| `npx astro check` | Vérifie les types ; doit rester à zéro erreur |
| `npm audit` | Vérifie les dépendances ; **doit rester à zéro vulnérabilité** |

## Comment le site est fait

[Astro](https://astro.build) en sortie entièrement statique : 73 pages HTML,
aucun serveur, aucune base de données, aucun cookie.

- **Rien n'est chargé de l'extérieur.** Polices et photographies sont
  auto-hébergées ; le site n'émet **aucune** requête vers un tiers, n'embarque
  aucun script tiers et ne pose aucun traceur.
- **Lisible sans JavaScript.** Les 124 descripteurs sont rendus à la
  construction, et le sélecteur de niveau de la carte repose sur des boutons
  radio et `:has()` — pas sur du script. Le JavaScript n'ajoute que la
  recherche, le bouton de copie et la bascule de thème.
- **Aucun contenu saisi deux fois.** Les 62 pages de compétences
  (31 entrées × 2 langues) sont générées par itération sur les données ; une vue
  par type de page est partagée entre les deux langues.
- **Accessibilité tenue.** Contraste AA vérifié en thème clair et sombre,
  navigation clavier complète, `prefers-reduced-motion` respecté.
- **Sept encres de rubriques**, portées par une variable CSS `--accent` héritée
  par tous les composants d'une page.
- **Des motifs, pas des photographies,** pour les rubriques : une figure SVG par
  rubrique, tracée dans sa propre encre, qui ne pèse rien puisqu'elle est écrite
  dans le HTML — voir [`Motif.astro`](src/components/Motif.astro).

```
src/
  data/fr/framework.json   les 7 rubriques, 28 compétences et 3 fils, en français
  data/en/framework.json   la traduction anglaise, structurellement identique
  data/fr/site.json        textes éditoriaux : accueil, cadre, usage, contact
  data/en/site.json        idem en anglais
  data/credits.json        auteurs et liens des photographies
  lib/i18n.ts              routage bilingue, accès aux données, citations
  lib/images.ts            résolution des images et de leurs crédits
  layouts/Base.astro       squelette commun : métadonnées, thème, en-tête, pied
  views/                   une vue par type de page, partagée entre les langues
  pages/                   routes françaises à la racine, anglaises sous /en/
  components/              en-tête, pied, carte, grille, motifs, bouton de copie
  styles/global.css        encres, typographie, thèmes clair et sombre
  assets/images/           les trois photographies, stockées dans le dépôt
scripts/
  extract-framework.py     régénère les données françaises depuis le document Word
  fetch-images.py          retélécharge les photographies et réécrit les crédits
site.config.mjs            le seul fichier à modifier pour mettre le site en ligne
```

## Modifier le contenu

**Les descripteurs, définitions et composantes** vivent dans
`src/data/<langue>/framework.json`. Les modifier suffit : les pages, la carte et
les compteurs se mettent à jour à la construction suivante.

> [!IMPORTANT]
> Ne changez pas un `code` (`1.1`, `T2`…) sans le changer dans **les deux**
> langues : c'est la clé qui les apparie.

**Les textes éditoriaux** (accueil, cadre, usage, contact) sont dans
`src/data/<langue>/site.json`.

**Si le document Word source évolue**, la version française peut être réextraite :

```bash
python3 scripts/extract-framework.py
```

Le script échoue bruyamment si la structure du document a changé, plutôt que de
produire des données silencieusement fausses. La traduction anglaise, elle, est
maintenue à la main et doit être mise à jour en parallèle.

**Pour changer une photographie** : remplacez le fichier dans
`src/assets/images/` en gardant son nom, et mettez à jour son auteur dans
`src/data/credits.json`. Les trois photographies viennent d'Unsplash et sont
utilisées sous licence Unsplash ; leurs crédits figurent sur la page
« Utiliser & citer ».

## Mise en ligne

Le site se publie **tout seul** : chaque poussée sur `main` déclenche
[le workflow](.github/workflows/deploy.yml) qui construit et publie sur GitHub
Pages. Rien à lancer à la main.

Pour le déployer ailleurs, `dist/` est un site statique ordinaire : il se dépose
tel quel sur Netlify, Vercel, Cloudflare Pages ou un hébergement FTP.

Tout le réglage tient dans un seul fichier, [`site.config.mjs`](site.config.mjs) :

| Réglage | Effet |
|---|---|
| `siteUrl` | Le nom de domaine, sans barre finale. Renseigné, il active les URL canoniques et la génération de `sitemap.xml`. Laissé vide, le site se construit en chemins relatifs et se déploie n'importe où. |
| `contactEmail` | L'adresse affichée sur la page Contact. Elle est publiée en clair et sera moissonnée : préférez une adresse de fonction sur votre domaine. |
| `formspreeId` | Identifiant d'un formulaire [Formspree](https://formspree.io) gratuit. Laissé vide, la page Contact affiche l'adresse directe à la place du formulaire — le site reste utilisable en l'état. |

## Sécurité

Le site est statique : ni serveur, ni base de données, ni session, ni cookie. La
surface d'attaque tient donc à ce qu'il charge et à ce qui le construit. Les
deux sont verrouillés — voir [SECURITY.md](SECURITY.md) pour le détail et pour
signaler une faille.

- **Politique de sécurité du contenu à empreintes SHA-256**, partant de
  `default-src 'none'`, sans aucun `unsafe-inline`. Un script étranger injecté
  dans le HTML ne s'exécuterait pas.
- **`connect-src` et `form-action` restent à `'none'`** tant que Formspree n'est
  pas configuré ; les renseigner ouvre la politique pour ce seul domaine.
- **Les actions du workflow sont épinglées à une empreinte de commit**, jamais à
  une étiquette : une étiquette peut être redirigée vers un autre code, une
  empreinte non.
- **Dependabot, analyse de secrets et protection à la poussée** sont actifs.

> [!WARNING]
> La politique de sécurité interdit les attributs `style=` en ligne : elle les
> bloque **silencieusement**, sans casser la construction. Passez par une classe
> ou un attribut de données, puis vérifiez que la console du navigateur est vide.

## Contribuer

Les retours, usages signalés et objections argumentées nourrissent les révisions
du référentiel. Voir [CONTRIBUTING.md](CONTRIBUTING.md) pour ce qui est attendu
selon que vous corrigiez une coquille, discutiez un descripteur ou proposiez une
traduction.

Le canal le plus simple reste [une issue](https://github.com/Megamax76/creacomp-site/issues/new/choose).

## Citer CréaComp

Le dépôt contient un fichier [CITATION.cff](CITATION.cff) : GitHub affiche donc
un bouton **« Cite this repository »** en haut de cette page, qui produit la
citation au format BibTeX ou APA.

En clair :

> Hébert, M. (2026). *CréaComp : référentiel de littératie créative numérique*
> (version 1.0, édition 2026). https://creacomp.org

La page [« Utiliser & citer »](https://creacomp.org/utiliser/) du site donne les
formulations recommandées dans les deux langues.

## Licences

Ce dépôt est **sous double licence**, parce qu'il contient deux natures de
travail :

| Ce qui est couvert | Licence | Texte |
|---|---|---|
| **Le référentiel** — les fichiers de `src/data/`, les descripteurs, définitions et textes éditoriaux | **CC BY-SA 4.0** | [LICENSE](LICENSE) |
| **Le code du site** — composants, mises en page, styles, scripts, configuration | **MIT** | [LICENSE-CODE](LICENSE-CODE) |

Autrement dit : réutilisez le **contenu** en citant l'auteur et en partageant
vos adaptations aux mêmes conditions ; réutilisez le **code** comme il vous
plaira.

[**NOTICE**](NOTICE) dit en français, et précisément, ce que chaque licence
couvre — utile avant une traduction ou une adaptation.

Trois catégories d'éléments présents dans le dépôt n'en relèvent pas : les
photographies, qui viennent d'Unsplash et suivent la
[licence Unsplash](https://unsplash.com/license) — leurs auteurs sont crédités
dans [`src/data/credits.json`](src/data/credits.json) et sur le site ; les
polices Fraunces, Archivo et JetBrains Mono, sous SIL Open Font License ; et les
dépendances npm, sous leurs licences propres.

---

## English summary

**CréaComp is a digital creative literacy framework** — a structured
description of the skills needed to create, publish and make a living from
digital content. It covers what existing frameworks handle poorly or not at
all: reading an algorithmic feed critically, building a voice, working with
generative AI, the attention economy, and sustaining a creative practice.

**7 rubrics, 28 competences, 3 cross-cutting threads, 124 descriptors across
4 mastery levels**, aligned with DigComp 1–8. Fully bilingual; the English
translation is structurally identical to the French source and shares the same
stable `code` keys.

This repository holds both the framework — as reusable structured data in
[`src/data/en/framework.json`](src/data/en/framework.json) — and the static
[Astro](https://astro.build) site that publishes it at
[creacomp.org/en](https://creacomp.org/en/).

**Reuse.** The framework content is **CC BY-SA 4.0**: reuse, translate and
adapt it freely, including commercially, provided you credit the author and
share adaptations under the same terms. Translations into other languages and
adaptations to national or sectoral contexts are explicitly welcome — please
[open an issue](https://github.com/Megamax76/creacomp-site/issues/new/choose)
first so the work can be coordinated. The site code is **MIT**.

**Running it.** Node.js 22+, then `npm install && npm run dev`. See
[Faire tourner le site](#faire-tourner-le-site) above — the commands are the
same in any language.
