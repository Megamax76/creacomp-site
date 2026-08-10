# CréaComp — site du référentiel

Site public du **référentiel de littératie créative numérique CréaComp**
(*Digital Creative Literacy Framework*), version 1.0 — édition 2026.
Bilingue français / anglais, entièrement statique, publié sous licence
Creative Commons Attribution – Partage dans les mêmes conditions 4.0.

Auteur du référentiel : Maxime Hébert.

## Démarrer

```bash
npm install
npm run dev
```

Le site est alors servi sur <http://localhost:4321>.

```bash
npm run build     # génère dist/, prêt à déployer
npm run preview   # sert dist/ localement pour vérification
```

## Mise en ligne

Tout se règle dans un seul fichier : [`site.config.mjs`](site.config.mjs).

| Réglage | Effet |
|---|---|
| `siteUrl` | Renseignez le nom de domaine (`https://exemple.org`, sans barre finale) pour activer les URL canoniques et la génération de `sitemap.xml`. Laissé vide, le site fonctionne avec des chemins relatifs et se déploie n'importe où. |
| `formspreeId` | Identifiant du formulaire [Formspree](https://formspree.io) (gratuit). Laissé vide, la page Contact affiche l'adresse e-mail directe à la place du formulaire. |

Le dossier `dist/` est un site statique ordinaire : il se dépose tel quel sur
Netlify, Vercel, GitHub Pages, ou un simple hébergement FTP.

## Structure

```
src/
  data/fr/framework.json   les 7 rubriques, 28 compétences et 3 fils, en français
  data/en/framework.json   la traduction anglaise, structurellement identique
  data/fr/site.json        textes éditoriaux : accueil, cadre, usage, contact
  data/en/site.json        idem en anglais
  lib/i18n.ts              routage bilingue, accès aux données, citations
  views/                   une vue par type de page, partagée entre les deux langues
  pages/                   routes françaises à la racine, anglaises sous /en/
  components/              en-tête, pied de page, carte, grille, bouton de copie
  assets/images/           les trois photographies, stockées dans le dépôt
  data/credits.json        auteurs et liens des photographies
scripts/
  extract-framework.py     régénère les données françaises depuis le document Word
  fetch-images.py          retélécharge les photographies et réécrit les crédits
```

Les 62 pages de compétences (31 entrées × 2 langues) sont générées par
itération sur les fichiers de données : aucun contenu n'est saisi deux fois.

## Modifier le contenu du référentiel

Les descripteurs, définitions et composantes vivent dans
`src/data/<langue>/framework.json`. Modifier ces fichiers suffit : les pages,
la carte et les compteurs se mettent à jour à la construction suivante.

Le champ `code` (`1.1`, `T2`…) est la clé stable entre les deux langues : c'est
lui qui permet au sélecteur de langue de mener à la page équivalente plutôt
qu'à l'accueil. Ne le modifiez pas sans changer les deux versions.

Si le document Word source évolue, la version française peut être réextraite :

```bash
python3 scripts/extract-framework.py
```

Le script échoue bruyamment si la structure du document a changé, plutôt que
de produire des données silencieusement fausses. La traduction anglaise, elle,
est maintenue à la main et doit être mise à jour en parallèle.

## Images et motifs

**Trois photographies** seulement, sur les pages où une illustration a du sens :
l'accueil (dans le hero, à droite du titre), « Le cadre » et « Contact ». Elles
proviennent d'Unsplash, sont utilisées sous licence Unsplash — usage libre, y
compris commercial — et sont stockées dans le dépôt : le site n'émet aucune
requête vers un service d'images. Les crédits figurent sur la page
« Utiliser & citer ».

Pour en changer une : remplacez le fichier dans `src/assets/images/` en gardant
son nom, et mettez à jour son auteur dans `src/data/credits.json`. Pour repartir
d'autres photographies, modifiez la table `SELECTION` de `scripts/fetch-images.py`
et relancez-le.

**Les rubriques du référentiel ne portent pas de photographies** mais des
**motifs géométriques dessinés en SVG** — voir `src/components/Motif.astro`. Une
figure par rubrique, qui dit ce qu'elle fait : des strates pour S'informer, une
trame de points pour Analyser, des arcs pour Créer, une cadence de barres pour
Faire, des cercles entrelacés pour Collaborer, une élévation pour Entreprendre,
une accumulation pour Rentabiliser ; et trois figures pour les fils transversaux.

Chaque motif est tracé dans `var(--accent)` sur un dégradé de la même encre : il
suit donc la couleur de sa rubrique et le thème clair ou sombre sans réglage,
et ne pèse rien puisqu'il est écrit dans le HTML.

## Partis pris techniques

- **Aucune dépendance externe au chargement.** Polices et photographies
  auto-hébergées, aucun script tiers, aucun traceur, aucun cookie.
- **Lisible sans JavaScript.** Les 124 descripteurs sont rendus côté serveur ;
  le sélecteur de niveau de la carte repose sur des boutons radio et `:has()`.
  Le JavaScript n'ajoute que la recherche, le bouton de copie et le thème.
- **Contraste AA vérifié** dans les thèmes clair et sombre, navigation clavier
  complète, `prefers-reduced-motion` respecté.
- **Sept encres de rubriques** portées par une variable CSS `--accent`, héritée
  par tous les composants d'une page.

## Licence

Le **contenu du référentiel** est publié sous licence
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.fr) :
réutilisation, traduction et adaptation libres, avec citation de l'auteur et
partage aux mêmes conditions.
