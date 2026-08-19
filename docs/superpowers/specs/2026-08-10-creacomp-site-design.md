# CreaComp — Site du référentiel · Spécification de conception

Date : 2026-08-10
Auteur du référentiel : Maxime Hébert
Licence du contenu : CC BY-SA 4.0

## 1. Objet

Site web public présentant **CreaComp**, référentiel mondial de littératie créative numérique
(*Digital Creative Literacy Framework*). Le site est bilingue français/anglais, statique,
et sert trois fonctions : faire comprendre le référentiel à un visiteur qui le découvre,
permettre sa consultation compétence par compétence, et en organiser la réutilisation
sous licence Creative Commons.

Le nom « DCLIC » et la graphie « Créacompe » n'apparaissent nulle part. Le nom retenu est
**CreaComp**, en français comme en anglais.

Version affichée : **CreaComp 1.0 — édition 2026**.

Baseline (hero) : « Le référentiel de compétences pour l'ère des créateurs » /
*The competency framework for the creator era*.

## 2. Source de contenu

Le contenu provient de `DCLIC_V7_Referentiel.docx` : préambule, 7 principes directeurs,
architecture, grammaire des 4 niveaux, 7 rubriques × 4 compétences, 3 fils transversaux,
méthodologie d'évaluation, annexe B (interface DigComp / EMI).

**Exclusion :** l'annexe A (table de correspondance V5 → V7) est retirée du site. Elle
documente une réorganisation interne vers une version jamais publiée et n'a pas d'usage
pour le lecteur.

Chaque compétence porte : un code (`1.1`), un intitulé, une définition, une liste de
composantes, et pour chacun des 4 niveaux un descripteur observable et une preuve
d'évaluation. Les 3 fils transversaux (`T1`, `T2`, `T3`) suivent exactement la même
structure. Total : 31 entrées, 124 descripteurs.

## 3. Décisions techniques

| Axe | Décision |
|---|---|
| Générateur | Astro, sortie 100 % statique |
| Langues | FR à la racine, EN sous `/en/`, contenu intégralement traduit |
| Contact | Formulaire Formspree (identifiant à configurer), lien e-mail en repli |
| Hébergement | Non décidé — aucune URL absolue câblée, chemins relatifs |
| Polices | Auto-hébergées en woff2, aucun appel réseau externe |
| JavaScript | Progressif : le site est entièrement lisible sans JS |

## 4. Architecture des pages

```
/                                          Homepage
/referentiel/                              Carte des 31 entrées
/referentiel/<slug>/                       ×31 — une page par compétence et par fil
/cadre/                                    Le cadre théorique et méthodologique
/utiliser/                                 Usages, licence, citation
/contact/
```

Chaque route existe en miroir sous `/en/`. Total : 74 pages générées.

**Pas de page intermédiaire par rubrique.** Les 7 rubriques sont des sections ancrées
dans `/referentiel/` (`#s-informer`, `#analyser`, …), portant leur chapeau et leur clause
de frontière. Une page par rubrique n'ajouterait qu'un clic.

### 4.1 Homepage

Séquence imposée, du plus général au plus précis :

1. **Hero** — nom, baseline, ligne de chiffres (7 rubriques · 28 compétences · 3 fils
   transversaux · 4 niveaux · 124 descripteurs observables), deux appels à l'action.
2. **Encart d'avertissement — « Ce que CreaComp est, ce qu'il n'est pas »**. Bloc court,
   sans emphase, en quatre oppositions : une cartographie et non un programme ; nul n'est
   censé tout maîtriser ; aucune note globale ni moyenne ; aucun logiciel nommé. Ce bloc
   est la réponse au risque principal du projet — être lu comme un curriculum prescriptif.
3. **Pourquoi ce référentiel** — le basculement de l'économie de l'attention à l'économie
   de l'intention, et l'effondrement du coût de production qui déplace la valeur vers
   l'amont (le regard) et l'aval (la relation). Accompagné d'un schéma sobre de la chaîne
   créative montrant la valeur quitter le milieu.
4. **La carte** — les 7 rubriques en blocs colorés ; l'interaction révèle les 4 compétences
   de chacune. Aperçu du référentiel entier tenu en un écran.
5. **Les 4 niveaux** — les quatre postures à la première personne, avec repère indicatif et
   équivalence DigComp.
6. **À qui ça sert** — quatre profils (enseignant, organisme de formation, créateur,
   institution), chacun menant vers `/utiliser/`.
7. **Pied de section** — licence, auteur, lien vers le cadre complet.

### 4.2 `/referentiel/` — la carte

Grille de 7 colonnes × 4 lignes affichant les 28 compétences simultanément, surmontée du
chapeau de chaque rubrique et suivie d'une bande transversale portant les 3 fils.

**Sélecteur de niveau N1 → N4.** Le dispositif central de la page : en changeant de niveau,
chaque case affiche son descripteur observable à ce niveau. Le visiteur lit la grammaire
des niveaux sur 31 compétences à la fois au lieu de se la faire expliquer. Sans JavaScript,
la page affiche les intitulés et les définitions courtes — elle reste utilisable.

**Champ de recherche** filtrant sur intitulés, définitions et composantes.

En tête de page, rappel condensé de l'encart d'avertissement.

### 4.3 Page compétence

- Fil d'Ariane, code, intitulé, rubrique d'appartenance (couleur porteuse).
- Définition.
- Composantes, en liste.
- Les 4 niveaux en cartes empilées : posture, descripteur observable, preuve d'évaluation.
- Navigation précédent / suivant à l'intérieur de la rubrique.
- Bouton « citer cette compétence » copiant la référence formatée.
- Lien vers la même page dans l'autre langue.

### 4.4 `/cadre/`

Page longue avec sommaire latéral ancré : préambule et définition de la littératie créative
numérique · de l'économie de l'attention à l'économie de l'intention · l'ère des créateurs
et le déplacement de la valeur · les 7 principes directeurs · l'architecture · la grammaire
des 4 niveaux · la méthodologie d'évaluation (preuve de création, portfolio, exigences de
validité) · annexe B, interface avec DigComp et l'EMI.

### 4.5 `/utiliser/`

- Ce que le référentiel permet de faire, par profil d'usage.
- Ce qu'il ne prescrit pas — rappel du principe P1.
- Licence CC BY-SA 4.0 : ce qui est autorisé, ce qui est exigé, ce qui est demandé en cas
  d'adaptation ou de traduction.
- Formats de citation : citation courte, forme académique, BibTeX. Chacun copiable.
- Invitation à signaler un usage, renvoyant vers `/contact/`.

### 4.6 `/contact/`

Page éditoriale orientant la prise de contact (usage pédagogique, traduction, recherche,
partenariat institutionnel), suivie du formulaire Formspree et de l'adresse e-mail en repli.
L'identifiant du formulaire est lu depuis un fichier de configuration unique ; tant qu'il
n'est pas renseigné, le formulaire est remplacé par le lien e-mail.

## 5. Modèle de données

Deux fichiers, un par langue : `src/data/framework.fr.json` et `framework.en.json`,
validés par un schéma Astro Content Collections. Structure :

```
meta        { name, version, edition, author, license, tagline, counts }
levels      [ { id: "N1", label, posture, repere, digcomp } × 4 ]
rubrics     [ { id: 1, slug, title, object, intro, boundary, color } × 7 ]
competences [ { code, slug, rubricId, title, definition,
                components: [...],
                levels: { N1: { descriptor, evidence }, … N4 } } × 28 ]
threads     [ même forme que competences, avec code T1..T3 ] × 3
```

Les textes longs hors référentiel (préambule, principes, méthodologie, annexe B, pages
Utiliser et Contact) vivent en Markdown sous `src/content/pages/<lang>/`.

Conséquence : les 62 pages de compétences et les deux cartes sont générées par itération.
Aucun contenu n'est saisi deux fois dans une même langue.

## 6. Système visuel

**Registre** : sobriété d'un référentiel institutionnel européen — grille stricte, blanc
dominant, hiérarchie typographique nette — tempérée par un système de couleurs qui rend la
cartographie immédiatement lisible.

- Titres en serif, texte en sans-serif, polices auto-hébergées.
- Sept couleurs de rubriques, assez saturées pour identifier, assez sourdes pour rester
  institutionnelles. Les trois fils transversaux en graphite, distincts des sept rubriques.
- Mode sombre, piloté par `prefers-color-scheme` avec bascule manuelle persistée.
- Contraste AA minimum sur tout texte, dans les deux thèmes.
- Navigation clavier complète, ordre de tabulation cohérent, focus visible.
- `prefers-reduced-motion` respecté : toute animation devient une transition instantanée.

## 7. Internationalisation

- FR à la racine (`/referentiel/`), EN sous `/en/` (`/en/framework/`).
- Les slugs sont localisés dans chaque langue ; une table de correspondance permet au
  sélecteur de langue de pointer vers la page équivalente et non vers l'accueil.
- `<html lang>`, `hreflang` réciproques et `og:locale` corrects sur chaque page.
- Traduction intégrale : les 31 entrées, les 124 descripteurs, les 124 preuves
  d'évaluation, les 7 principes, la méthodologie et l'annexe B.
- Terminologie fixée avant traduction dans un glossaire court (rubrique → *domain*,
  fil transversal → *transversal thread*, descripteur observable → *observable descriptor*,
  preuve d'évaluation → *evidence of assessment*, littératie créative numérique →
  *digital creative literacy*), afin que les 124 descripteurs restent cohérents entre eux.

## 8. Non-objectifs

Explicitement hors périmètre de cette version :

- Aucun compte utilisateur, aucune auto-évaluation enregistrée, aucun portfolio en ligne.
- Aucun back-office ni CMS : le contenu se modifie dans les fichiers de données.
- Aucune analytique, aucun traceur, aucun cookie.
- Aucune version PDF générée par le site.
- Aucun moteur de recherche serveur : le filtrage de `/referentiel/` est côté client.

## 9. Critères de réussite

1. Un visiteur qui découvre le référentiel comprend en moins d'une minute de lecture ce
   qu'il est, ce qu'il n'est pas, et à quoi il sert.
2. Les 31 entrées sont atteignables en deux clics depuis n'importe quelle page.
3. Les 124 descripteurs sont consultables en français et en anglais.
4. Le site fonctionne sans JavaScript, en lecture intégrale.
5. Contraste AA vérifié, navigation clavier complète, dans les deux thèmes.
6. Aucune requête réseau vers un tiers au chargement d'une page.
7. Le format de citation académique est présent et copiable.
