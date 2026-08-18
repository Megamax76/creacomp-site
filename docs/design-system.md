# Design system CréaComp

Le système tient dans un seul fichier de style,
[`src/styles/global.css`](../src/styles/global.css), et dans une poignée de
composants. Ce document n'en est pas une copie : il dit **quand employer quoi**,
et pourquoi les valeurs sont ce qu'elles sont.

Règle générale : **rien n'est écrit en dur.** Toute couleur, toute taille, tout
espacement passe par une variable. Une valeur littérale dans un composant est un
bogue, pas un raccourci.

---

## 1. Les intentions

Trois décisions gouvernent tout le reste.

**Le registre est celui du papier, pas celui de l'écran.** Fond blanc cassé
chaud, encre brune plutôt que noire, filets fins, rayon de 3 px. Le référentiel
est un document ; il devait en avoir l'air.

**La couleur porte du sens, jamais de la décoration.** Chaque teinte d'accent
est attachée à une rubrique du référentiel. On ne choisit pas une couleur parce
qu'elle est jolie à cet endroit : on hérite de celle de la rubrique.

**Rien ne dépend de la seule couleur.** Le référentiel s'adresse au monde
éducatif. Un daltonien, une photocopie, une impression en gris doivent laisser
le document entièrement lisible.

---

## 2. Couleurs

### Les neutres — le papier et l'encre

| Variable | Rôle | Clair | Sombre |
|---|---|---|---|
| `--paper` | Fond de page | `#FBF9F5` | `#131210` |
| `--paper-raised` | Fond des fiches, au-dessus du papier | `#FFFFFF` | `#1C1A17` |
| `--paper-sunken` | Fond des sections en creux | `#F3EFE7` | `#0E0D0B` |
| `--ink` | Texte principal, titres | `#1A1814` | `#F1EEE6` |
| `--ink-soft` | Texte courant, paragraphes | `#4D4840` | `#B8B2A5` |
| `--ink-faint` | Mentions, légendes, métadonnées | `#6B6558` | `#968D7E` |
| `--rule` | Filets, bordures de fiches | `#DED8CB` | `#322E28` |
| `--rule-strong` | Filets appuyés, bordures de contrôles | `#C6BFAE` | `#4A443B` |

Le blanc n'est jamais pur et le noir jamais neutre : `#FBF9F5` tire vers le
chaud, `#1A1814` vers le brun. C'est ce qui donne l'aspect papier, et c'est
aussi ce qui rend le thème sombre supportable.

### Les accents — un par rubrique

| Variable | Rubrique | Clair | Sombre |
|---|---|---|---|
| `--petrole` | 1 · S'informer | `#1B5068` | `#6FB4D6` |
| `--indigo` | 2 · Analyser | `#454391` | `#A29FEE` |
| `--carmin` | 3 · Créer | `#9C2C4A` | `#EA8BA3` |
| `--terre` | 4 · Faire | `#A9551F` | `#EAA269` |
| `--foret` | 5 · Collaborer | `#2A6B4B` | `#78C9A0` |
| `--sarcelle` | 6 · Entreprendre | `#14707F` | `#62C4D4` |
| `--bronze` | 7 · Rentabiliser | `#7A5C15` | `#D6B660` |
| `--graphite` | Neutre, hors rubrique | `#4A4640` | `#B0A89A` |

Le **pétrole est l'accent par défaut** : c'est la couleur du site quand aucune
rubrique n'est en jeu, et celle du logo.

### Le mécanisme d'accent

`--accent` est un alias qui pointe vers l'une des huit teintes. On ne le
redéfinit pas à la main : on pose l'attribut `data-accent` sur `<html>`, ce que
fait le layout.

```astro
<Base lang="fr" page="framework" accent="carmin">
```

Tout ce qui emploie `--accent` suit alors : `.eyebrow`, `.code-chip`,
`:focus-visible`, `::selection`, le survol des boutons, le soulignement de
l'onglet courant.

Deux dérivés, pour les fonds teintés :

```css
--accent-wash: color-mix(in srgb, var(--accent) 8%, transparent);
--accent-edge: color-mix(in srgb, var(--accent) 26%, transparent);
```

**Le logo est la seule exception.** Il garde ses couleurs propres quel que soit
`data-accent` : un logo ne se recolore pas avec la page.

### Contrastes, mesurés

Rapports WCAG sur `--paper`, dans les deux thèmes. Tout le texte passe AA
(4,5 : 1) ; la plupart passe AAA (7 : 1).

| | Clair | Sombre |
|---|---|---|
| `--ink` | 16,9 · AAA | 16,2 · AAA |
| `--ink-soft` | 8,6 · AAA | 8,9 · AAA |
| `--ink-faint` | 5,5 · AA | 5,7 · AA |
| `--petrole` | 8,3 · AAA | 8,2 · AAA |
| `--indigo` | 8,1 · AAA | 7,8 · AAA |
| `--carmin` | 7,0 · AA | 7,8 · AAA |
| `--terre` | **5,0 · AA** | 8,8 · AAA |
| `--foret` | 6,1 · AA | 9,5 · AAA |
| `--sarcelle` | 5,5 · AA | 9,2 · AAA |
| `--bronze` | 5,9 · AA | 9,6 · AAA |

Le **terre en thème clair est le point bas, à 5,0**. Il reste conforme, mais
c'est la teinte à ne pas assombrir davantage le fond sous laquelle on l'emploie,
et à ne jamais employer en dessous de la taille du texte courant.

> **Point ouvert.** `--rule` (1,35 : 1) et `--rule-strong` (1,74 : 1) sont sous
> le seuil de 3 : 1 que WCAG 1.4.11 demande aux bordures qui *identifient* un
> contrôle. Pour les filets décoratifs — séparateurs, bordures de fiches — c'est
> sans conséquence. Cela en a pour `.btn--ghost` et `.lang-switch`, dont la
> bordure est le seul contour. Ils restent identifiables par leur libellé, ce
> qui est l'argument habituel pour ne pas s'en alarmer, mais la remarque tiendra
> devant un audit. La corriger suppose d'assombrir ces deux bordures, donc de
> changer l'allure du site : c'est une décision de conception, pas un correctif.

---

## 3. Typographie

| Variable | Fonte | Emploi |
|---|---|---|
| `--font-display` | **Fraunces Variable** | Titres, nom de la marque |
| `--font-body` | **Archivo Variable** | Tout le texte courant |
| `--font-mono` | **JetBrains Mono Variable** | Codes, surtitres, chiffres |

Fraunces est une fonte variable à quatre axes. Les titres emploient
`'SOFT' 20, 'WONK' 1, 'opsz' 40` ; le nom de la marque, plus petit, descend à
`'opsz' 20`. `WONK` active les formes penchées qui donnent son caractère à la
fonte — c'est le réglage qui fait qu'un titre CréaComp ne ressemble pas à un
titre par défaut. Ne pas y toucher.

### L'échelle

Six échelons fluides, qui interpolent entre mobile et grand écran sans point de
rupture.

| Variable | Mobile → écran large | Emploi |
|---|---|---|
| `--step-0` | 1 → 1,08 rem | Texte courant. C'est la taille du `body`. |
| `--step-1` | 1,15 → 1,35 rem | `.lead`, chapeaux |
| `--step-2` | 1,4 → 1,85 rem | `.title-3`, titres de fiche |
| `--step-3` | 1,75 → 2,6 rem | `.title-2`, titres de section |
| `--step-4` | 2,1 → 3,8 rem | Titres de page |
| `--step-5` | 2,6 → 5,6 rem | Titre d'accueil, unique par page |

Interlignage : **1,65** pour le texte courant, **1,08** pour les titres.
Approche : **−0,017 em** sur les titres, **0** sur le texte.

### Les classes de texte

| Classe | Ce que c'est |
|---|---|
| `.eyebrow` | Surtitre en mono, capitales, interlettré, en `--accent`. Annonce une section. |
| `.lead` | Chapeau : `--step-1`, interligne 1,5, `--ink-soft`, largeur max 44 rem. |
| `.title-2`, `.title-3` | Titres de section et de sous-section. |
| `.prose` | Bloc de texte suivi : largeur limitée à `--measure`, rythme vertical automatique. |
| `.code-chip` | Code d'entrée (`1.1`, `T2`) en mono, chiffres tabulaires, en `--accent`. |

---

## 4. Mise en page

| Variable | Valeur | Rôle |
|---|---|---|
| `--page` | `78rem` | Largeur maximale du contenu |
| `--measure` | `38rem` | Largeur de lecture confortable — environ 70 signes |
| `--gutter` | `1,25 → 4rem` | Marge latérale, fluide |

Deux classes portent toute la grille :

```html
<div class="wrap">…</div>        <!-- centre et borne à --page -->
<div class="prose">…</div>       <!-- borne à --measure, rythme vertical -->
```

Et trois modificateurs de section :

| Classe | Effet |
|---|---|
| `.section` | Respiration verticale fluide, de 3,5 à 7,5 rem |
| `.section--sunken` | Pose la section sur `--paper-sunken` |
| `.section--ruled` | Ajoute un filet supérieur |

L'alternance papier / creux est ce qui découpe les longues pages. Ne pas
enchaîner deux sections creuses.

---

## 5. Formes

| Variable | Valeur |
|---|---|
| `--radius` | `3px` |
| `--shadow` | Ombre double, très basse — `0 1px 2px` + `0 8px 28px -18px` |

**Trois pixels, partout.** Le système est quasi anguleux : c'est un choix, pas
un oubli. Les seules formes rondes du site sont le symbole du logo et les
pastilles de niveau.

L'ombre ne sert qu'aux éléments réellement flottants. Une fiche posée dans le
flux se signale par sa bordure et son fond, pas par une ombre.

---

## 6. Composants

### Boutons

```html
<a class="btn" href="…">Libellé <span class="btn__arrow">→</span></a>
<a class="btn btn--ghost" href="…">Libellé</a>
```

Le bouton plein est en `--ink` sur `--paper` — **pas** en `--accent`. C'est au
survol qu'il passe à l'accent, avec une remontée d'un pixel. La flèche avance de
trois pixels. Ces deux mouvements sont les seules animations du site, et ils
sont annulés sous `prefers-reduced-motion`.

### Fiches

```html
<article class="card">…</article>
```

Fond `--paper-raised`, bordure `--rule`, rayon `--radius`, marge intérieure
fluide. Pour une grille de fiches jointives, `.grid` produit un espacement d'un
pixel qui laisse le fond faire les séparateurs.

### En-tête et pied de page

L'en-tête est collant, translucide (`color-mix` à 88 %) et flouté. Il porte le
verrou complet : symbole, nom, ligne de définition. Le pied de page reprend
symbole et nom, sans la ligne.

---

## 7. Le logo dans le site

Le symbole vit dans [`src/components/Logo.astro`](../src/components/Logo.astro),
écrit en clair dans la page plutôt que chargé comme image.

```astro
<span class="brand__mark"><Logo /></span>
```

Trois conséquences utiles :

- **Aucune requête réseau.** Le symbole fait moins d'un kilo-octet.
- **La bascule clair/sombre est gratuite.** Les lames sont peintes avec
  `var(--indigo)`, `var(--carmin)`… qui changent déjà avec le thème. Un seul
  fichier couvre les deux.
- **La taille tient dans une seule règle.** Le symbole fait `1em` de côté :
  c'est la `font-size` du conteneur qui le dimensionne.

Par défaut le symbole est décoratif — `aria-hidden` — parce que le nom est écrit
à côté en toutes lettres. Passer `title` ne se justifie que s'il apparaît seul.

Les fichiers exportables — verrous, déclinaisons, PNG, carte sociale — sont dans
[`brand/`](../brand/), avec leurs règles d'emploi dans
[`brand/README.md`](../brand/README.md). Ils sont refabriqués par
`scripts/logo/construire.py`.

### Ce que le site expose

| Chemin | Rôle |
|---|---|
| `public/favicon.svg` | Favicon vectoriel, bascule clair/sombre seul |
| `public/favicon-32.png` | Repli matriciel |
| `public/apple-touch-icon.png` | Icône d'écran d'accueil iOS, 180 px |
| `public/icone-512.png` | Grande icône, 512 px |
| `public/carte-sociale.png`, `-en.png` | Carte de partage, 1200 × 630 |

La carte sociale n'est déclarée qu'une fois `siteUrl` renseigné dans
`site.config.mjs` : les robots des réseaux ne résolvent pas les chemins
relatifs.

---

## 8. Accessibilité — les règles qui ne se négocient pas

- **Jamais d'information portée par la seule couleur.** Une rubrique se signale
  par son nom et son numéro autant que par sa teinte.
- **Focus visible partout** : contour de 2 px en `--accent`, décalé de 3 px.
  Ne jamais poser `outline: none` sans remplacement équivalent.
- **Lien d'évitement** en tête de page (`.skip`), qui apparaît au premier
  `Tab`.
- **`prefers-reduced-motion`** neutralise toutes les transitions.
- **Texte en dessous de `--step-0`** : réservé aux mentions, jamais au contenu.
- **Cibles tactiles** d'au moins 44 px de côté.

---

## 9. Ajouter quelque chose au système

Dans l'ordre :

1. **Chercher d'abord.** `.card`, `.btn`, `.prose`, `.eyebrow` couvrent
   l'essentiel. Un composant de plus est un composant à maintenir.
2. **Employer les variables.** Si la valeur voulue n'existe pas, la question
   n'est pas « quelle valeur » mais « quel échelon existant s'en approche ».
3. **Vérifier dans les deux thèmes.** Chaque ajout se regarde en clair et en
   sombre avant d'être considéré comme fini.
4. **Vérifier en monochrome.** Imprimer la page en niveaux de gris reste le
   test le plus rapide pour savoir si la couleur porte de l'information.
5. **Mesurer le contraste**, ne pas l'estimer.
