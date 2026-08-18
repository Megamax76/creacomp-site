# CréaComp — Page d'accueil didactique · Spécification de conception

Date : 2026-08-18
Auteur du référentiel : Maxime Hébert
Licence du contenu : CC BY-SA 4.0

## 1. Objet

Refondre la page d'accueil pour qu'elle **introduise** le référentiel au lieu de
le résumer. Le lecteur visé est institutionnel — décideur, chercheur, cadre d'un
organisme — et CréaComp se présente à lui comme ce qu'il est : un cadre de
référence, rigoureux et citable, dont enseignants et créateurs sont des usagers
parmi d'autres.

Aucun contenu n'est perdu. La refonte réordonne, déduplique et ajoute un seul
élément neuf : un spécimen d'entrée.

## 2. Diagnostic de la page actuelle

**On nie avant d'avoir posé.** La section « Ce que CréaComp est, ce qu'il n'est
pas » suit immédiatement le hero. C'est un procédé de correction de
préconception : il ne fonctionne que sur un lecteur qui a déjà la préconception.
Celui qui découvre lit quatre négations et se retrouve devant un vide.

**On ne voit jamais l'objet.** Nulle part sur la page ne figure une compétence
réelle, un descripteur, un exemple. Le lecteur reçoit une définition abstraite,
puis une carte de sept rubriques, puis quatre niveaux, sans jamais toucher la
matière.

**La thèse arrive trop tôt et trop dense.** Le basculement attention → intention
et l'effondrement du coût de production sont de l'argumentation. Placés en
troisième position, ils exigent un effort avant que l'objet soit posé.

**La page duplique les trois autres.**

| Section de la page d'accueil | Doublon de |
|---|---|
| « De l'économie de l'attention à l'économie de l'intention » | `/cadre` § `intention` — texte quasi mot pour mot |
| « L'ère des créateurs et le déplacement de la valeur » | `/cadre` § `ere-des-createurs` — texte quasi mot pour mot |
| Les quatre paires « est / n'est pas » | `/cadre` principes P1, P2, P3 et `/utiliser` § `notPrescriptive` |
| « À qui ce référentiel sert-il ? » | `/utiliser` § `profiles` |
| « Un bien commun » | `/utiliser` § `license` |

C'est la cause de fond : la page tente d'être une version condensée du site
entier. Elle résume au lieu d'introduire, et c'est pourquoi elle est dense sans
être guidante.

## 3. Décisions de cadrage

**Registre institutionnel.** « Didactique » ne signifie pas « accessible » : cela
signifie rigueur de l'exposition. On pose l'objet, on l'illustre, on en dit la
portée et les limites, on dit comment s'en servir et comment le citer. Pas de
tutoiement du lecteur, pas de récit, pas d'aiguillage par public en tête de page.

**Répartition du travail entre les pages.** La page d'accueil introduit ; `/cadre`
argumente ; `/referentiel` déroule ; `/utiliser` outille. Aucun texte n'est écrit
deux fois : ce qui existe ailleurs est annoncé, pas recopié.

**Dispositif de guidage : parcours numéroté et sommaire de page.** Le noyau
d'exposition est séquencé en quatre temps numérotés. La numérotation rend la
progression visible — c'est le procédé le plus éprouvé pour guider une première
lecture — et elle relève aussi de la convention institutionnelle, comme les sept
principes P1–P7 de `/cadre`. Elle ne couvre que le noyau d'exposition, jamais les
sections d'aval. Un sommaire de page en tête sert le lecteur pressé sans pénaliser
celui qui découvre.

## 4. La séquence

### 4.1 En-tête

Mise en page, image et crédit photographique inchangés.

Le titre est conservé tel quel : « Le référentiel de compétences pour l'ère des
créateurs ». C'est une accroche assumée ; le registre institutionnel est porté par
le corps de page, pas par le H1.

Le chapô est raccourci. La définition à six verbes n'est pas une accroche mais la
matière du premier chapitre : elle descend en **01**. Ce qui reste tient en une
phrase — vingt-cinq mots au plus — qui dit ce qu'est le document et à quoi il
sert, sans définir la littératie numérique créative. La formulation exacte est
arrêtée à l'implémentation ; la contrainte de longueur et l'interdiction de
définir ne le sont pas.

Les cinq compteurs quittent l'en-tête. Alignés sans explication, « 7 rubriques ·
28 compétences · 3 fils transversaux · 4 niveaux · 124 descripteurs observables »
sont des slogans pour qui ignore ce qu'est une rubrique ou un descripteur. Ils
remontent en **02**, où chaque nombre est suivi de sa définition.

À leur place, sous les appels à l'action, une **ligne d'identité du document** :
version, édition, auteur, licence — « CréaComp 1.0 · édition 2026 · Maxime
Hébert · CC BY-SA 4.0 ». C'est le signal de crédibilité qu'attend un lecteur
institutionnel, et c'est la fonction que les compteurs remplissaient mal.

Le surtitre actuel, qui affiche déjà « CréaComp 1.0 — édition 2026 », **est
supprimé** : il est absorbé par cette ligne. La version ne doit pas figurer deux
fois dans le même écran.

Détail d'exactitude à corriger : l'appel à l'action primaire dit « Explorer les 31
compétences » alors que le référentiel compte 28 compétences et 3 fils
transversaux, soit 31 **entrées**. Dans un document qui se veut citable, le mot
juste est requis.

### 4.2 Sommaire de page

Placé immédiatement sous l'en-tête. Un filet horizontal portant les quatre ancres
numérotées, puis les trois sections d'aval. Corps mono, teinte `--ink-faint`,
même vocabulaire visuel que `ui.onThisPage` déjà employé sur les fiches de
compétence.

### 4.3 — 01 · L'objet — ce que le référentiel décrit

La définition de la littératie numérique créative, en une phrase.

Les six verbes sont dépliés en bande plutôt qu'empilés dans une phrase de
quarante mots : *recevoir de façon critique · comprendre · imaginer · fabriquer ·
diffuser · valoriser*. C'est le gain de lisibilité le plus immédiat de la refonte,
et il ne coûte qu'une mise en forme.

Le développement — le parallèle avec la lecture, l'écriture et le calcul — reste
sur `/cadre` § `preambule`, où il est déjà écrit. La page d'accueil ne le reprend
pas.

### 4.4 — 02 · L'architecture — comment il est organisé

Les quatre nombres, chacun accompagné de sa ligne d'explication :

- **7 rubriques** — des domaines d'action, nommés par des verbes.
- **28 compétences** — quatre par rubrique.
- **3 fils transversaux** — ils traversent les sept rubriques.
- **4 niveaux** appliqués aux 31 entrées, soit **124 descripteurs observables**.

Puis `RubricMap`, inchangé. Puis `LevelCards` et la règle d'or de calibrage : les
niveaux relèvent de l'architecture, leur place est ici et non trois sections plus
bas.

Appel à l'action vers `/referentiel`.

### 4.5 — 03 · Une entrée — à quoi ressemble une compétence

Section neuve, et cœur de la refonte.

Un fac-similé annoté d'une entrée réelle : **1.2 — Évaluer la fiabilité et
détecter la manipulation**, choisie parce que son objet est immédiatement
intelligible sans connaître le référentiel.

Le fac-similé porte le code, le titre, la rubrique d'appartenance avec sa teinte,
la définition, puis **le même point de compétence à deux niveaux opposés** —
Découverte et Expertise — chacun avec son descripteur et sa preuve d'évaluation.
Le contraste entre les deux extrêmes explique la gradation mieux que les quatre
niveaux affichés à la suite.

Trois annotations nomment les parties de l'objet :

- le **code** est stable et citable ;
- le **descripteur** énonce ce que la personne est capable de faire ;
- la **preuve d'évaluation** dit comment on le vérifie.

Un lien mène à la fiche complète de la compétence.

En quinze secondes, un lecteur qui n'a jamais ouvert un référentiel de
compétences sait ce qu'est une entrée, ce qu'est un descripteur observable, et ce
que « quatre niveaux » recouvre concrètement.

### 4.6 — 04 · Portée et limites

Les quatre paires existantes, conservées dans leur principe.

La section est renommée : « Ce que CréaComp est, ce qu'il n'est pas » devient
**« Portée et limites »**, l'énoncé standard d'un cadre de référence. Déplacée
après l'exposition de l'objet, elle ne creuse plus de vide : elle borne quelque
chose de déjà posé.

Les corps de texte sont resserrés pour ne plus recouvrir les principes P1 à P3 de
`/cadre` ni le § `notPrescriptive` de `/utiliser`. La page d'accueil énonce la
limite ; les autres pages la motivent.

### 4.7 Pourquoi ce cadre

Section non numérotée : c'est une orientation, pas une étape du parcours.

Trois à quatre phrases neuves, écrites pour la page d'accueil, disant pourquoi ce
cadre existe. Elles sont accompagnées du schéma de la chaîne créative — amont,
fabrication, aval — conservé tel quel : c'est la figure la plus parlante du site.
Un lien mène à `/cadre`.

Le bloc « balance attention → intention » est retiré de la page d'accueil. Il
figure mot pour mot sur `/cadre` § `intention`.

### 4.8 Usages, puis Citer et réutiliser

Les deux sections finales sont conservées et allégées. Elles annoncent `/utiliser`
au lieu d'en résumer le contenu.

## 5. Le spécimen — modèle et rendu

Nouveau composant `src/components/Specimen.astro`.

```astro
<Specimen lang={lang} code="1.2" levels={['N1', 'N4']} />
```

Le composant lit `src/data/<langue>/framework.json`, y trouve l'entrée par son
`code`, et en rend `title`, `definition`, puis pour chaque niveau demandé
`levels[N].descriptor` et `levels[N].evidence`. Le nom et la posture du niveau
viennent de `site.levels`. La rubrique d'appartenance est résolue par `rubricId`,
ce qui donne la teinte d'accent.

**Aucun contenu n'est recopié.** Le spécimen ne peut pas diverger du référentiel,
et il suit automatiquement toute réextraction depuis le document source.

Les trois annotations, en revanche, sont du texte d'interface : elles vivent dans
`site.json` sous `home.specimen`, et sont traduites.

## 6. Impact sur les fichiers

| Fichier | Nature de l'intervention |
|---|---|
| `src/components/Specimen.astro` | nouveau — fac-similé annoté d'une entrée |
| `src/components/PageToc.astro` | nouveau — sommaire de page |
| `src/views/Home.astro` | réécrit — nouvelle séquence, en-têtes numérotés, styles des blocs neufs |
| `src/data/fr/site.json` | branche `home` refondue |
| `src/data/en/site.json` | branche `home` refondue, strictement parallèle |

`RubricMap.astro`, `LevelCards.astro`, `framework.json` et les trois autres pages
ne sont pas modifiés.

## 7. Contraintes à respecter

**Aucun attribut `style=` en ligne.** La politique de sécurité du contenu du site
fonctionne par empreintes et interdit le style en ligne. Le spécimen et le
sommaire passent par classes et attributs `data-*`, comme `stage[data-value]` le
fait déjà dans la page actuelle.

**Aucune valeur littérale.** Toute couleur, toute taille, tout espacement passe
par une variable du système, conformément au design system.

**Rien ne dépend de la seule couleur.** La teinte de rubrique du spécimen est
doublée par le code et le nom de la rubrique en toutes lettres.

**Parité des deux langues.** Toute clé ajoutée à `fr/site.json` est ajoutée à
`en/site.json` dans le même mouvement. Le spécimen anglais lit l'entrée `1.2` du
`framework.json` anglais.

**Terminologie.** « littératie numérique créative », dans cet ordre. Aucune
correspondance avec DigComp ou EntreComp n'est introduite : ces cadres sont une
inspiration et un complément, jamais une tutelle.

## 8. Hors périmètre

Les pages `/cadre`, `/referentiel`, `/utiliser` et `/contact` ne sont pas
retouchées. Les textes qui quittent la page d'accueil existent déjà sur ces pages
et n'ont pas à y être réécrits.

L'ajout des éclairages et de leur bibliographie, spécifié le 17 août 2026, est un
chantier distinct et sans interaction avec celui-ci.
