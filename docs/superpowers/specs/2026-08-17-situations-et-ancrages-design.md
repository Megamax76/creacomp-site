# CréaComp — Éclairages · Spécification de conception

Date : 2026-08-17
Auteur du référentiel : Maxime Hébert
Licence du contenu : CC BY-SA 4.0

## 1. Objet

Doter chacune des 31 entrées du référentiel (28 compétences, 3 fils transversaux)
d'un **éclairage** : un texte court qui présente la compétence, montre ce qu'elle
recouvre dans le monde réel, et adosse ce propos à des travaux vérifiés.

Le référentiel ne comporte aujourd'hui aucune bibliographie. L'ajouter fait
passer CréaComp de « document raisonné » à « document adossé à la littérature ».
C'est un gain de crédibilité et un engagement : chaque référence doit tenir devant
un lecteur qui la vérifie.

## 2. Contrainte décisive — l'emplacement des données

`scripts/extract-framework.py` **régénère** `src/data/fr/framework.json` depuis
`DCLIC_V7_Referentiel.docx`. Le script ouvre la cible en écriture et y écrit une
charge utile reconstruite : il ne relit pas l'existant et ne fusionne rien.

> Des champs ajoutés à la main dans `framework.json` seraient **silencieusement
> détruits** à la première réextraction — potentiellement après des semaines
> d'écriture et de vérification.

**Décision : le nouveau contenu vit dans un fichier distinct**,
`src/data/<langue>/eclairages.json`, apparié au référentiel par le `code`
(`1.1`, `T2`…) — la même clé stable qui apparie déjà le français et l'anglais.
`extract-framework.py` n'est pas modifié, et le cycle de mise à jour depuis le
Word reste intact.

## 3. Modèle de données

```jsonc
{
  "2.1": {
    "texte": [
      "Premier paragraphe…",
      "Second paragraphe…"
    ],
    "sources": [
      {
        "authors": "Eslami, M. et al.",
        "year": 2015,
        "work": "« I always assumed that I wasn't really that close to [her] » : Reasoning about invisible algorithms in news feeds",
        "venue": "CHI '15",
        "locator": "153–162",
        "url": "https://dl.acm.org/doi/10.1145/2702123.2702556",
        "checked": "2026-08-17"
      }
    ]
  }
}
```

**Ce qui se traduit et ce qui ne se traduit pas.** `texte` est rédigé dans chaque
langue — ce n'est pas une traduction mot à mot mais le même propos redit. En
revanche `authors`, `year`, `work`, `venue`, `locator` et `url` sont **identiques
dans les deux fichiers** : traduire le titre d'un travail le rendrait
introuvable, ce que la compétence 1.1 interdit précisément d'accepter.

## 4. Affichage

L'éclairage ouvre la colonne principale, avant le bloc « Définition ». Les
sources se placent dessous, en petit corps, sous la forme brève
« Auteur, revue, année ». La référence complète (volume, pages, URL) est
disponible mais n'encombre pas la lecture.

Un seul bloc, présent sur toutes les entrées : il n'y a plus de section qui
apparaît ou disparaît selon les pages, donc plus de problème d'inégalité entre
les compétences bien et mal documentées.

## 5. Protocole de vérification

Règle première : **aucune référence n'est produite de mémoire.**

1. Chaque référence est retrouvée sur un enregistrement primaire — page de
   l'éditeur, DOI, site de la revue. Ni agrégateur, ni résumé, ni notice de
   seconde main.
2. L'URL de vérification et la date sont enregistrées (`url`, `checked`).
3. Auteur, année, titre, volume et pages sont recopiés depuis cet
   enregistrement, jamais reconstitués.
4. **Une référence qui ne se vérifie pas est retirée, pas atténuée.** Ni
   « probablement », ni « voir aussi ».
5. Aucun chiffre n'est cité sans sa source. Un chiffre trouvé dans une reprise
   de presse est remonté jusqu'à l'étude ; s'il ne s'y trouve pas, il est écarté.
6. La portée d'un résultat est dite avec lui. « Dans une étude menée auprès de
   quarante utilisateurs » et non « 62 % des internautes ».
7. Une formule est attribuée à qui l'a écrite. Exemple traité : « quand une
   mesure devient une cible, elle cesse d'être une bonne mesure » est de
   Strathern (1997) reformulant Goodhart, et non de Goodhart.

Ce protocole n'est pas une précaution de rédaction : la compétence 1.1 demande de
« remonter systématiquement à l'information primaire » et le fil Discerner exige
une création « loyale et non manipulatoire ». Une bibliographie approximative
contredirait le référentiel dans son propre texte.

## 6. Règles d'écriture

**Forme.** Deux paragraphes, environ 120 à 140 mots. Pas de titre interne.

**Registre.** Compréhensible sans formation académique. Aucun terme technique
dans le corps du texte : les concepts sont dits en français courant, les noms
propres et les revues renvoyés en note. L'entrée se fait par une phrase que
n'importe qui comprend, jamais par le vocabulaire du domaine.

**Portée.** Généraliste. Une compétence concerne aussi bien celui qui consomme
des contenus que celui qui en produit, et le texte le montre quand c'est vrai.
On garde de la hauteur : le texte explique ce que la compétence fait au monde,
pas comment l'exercer.

**Analyse.** L'angle retenu doit apprendre quelque chose à quelqu'un qui connaît
déjà le sujet. La lecture attendue est écartée au profit de ce que les travaux
disent réellement.

**Anecdote.** Admise, jamais dominante — une illustration à l'intérieur du
propos, pas le propos lui-même. Elle est vérifiée au même titre qu'un chiffre.

**Style.** Pas de phrase-choc décorative. La chute, si elle existe, est le
contenu analytique lui-même, énoncé simplement.

## 7. Périmètre

**Compris :** 31 éclairages × 2 langues ; `eclairages.json` FR et EN ; le rendu
dans `Competence.astro` ; la documentation du fichier dans le README, section
« Modifier le contenu ».

**Exclu :** toute modification de `extract-framework.py` ou de `framework.json` ;
toute page de bibliographie générale ; tout éclairage sur les pages autres que
les entrées du référentiel.

## 8. État d'avancement

| Rubrique | Éclairages | État |
|---|---|---|
| 1 · S'informer | 1.1 – 1.4 | rédigés, sources vérifiées |
| 2 · Analyser | 2.1 – 2.4 | rédigés, sources vérifiées |
| 3 · Créer | 3.1 – 3.4 | à faire |
| 4 · Faire | 4.1 – 4.4 | à faire |
| 5 · Collaborer | 5.1 – 5.4 | à faire |
| 6 · Entreprendre | 6.1 – 6.4 | à faire |
| 7 · Rentabiliser | 7.1 – 7.3 | à faire |
| 7 · Rentabiliser | 7.4 | rédigé, sources vérifiées |
| Fils | T1 – T3 | à faire |

Version anglaise : à faire intégralement, après validation du français.

## 9. Risque identifié

La littérature est inégale selon les compétences. « Comprendre les algorithmes »
ou « Économie des plateformes » sont abondamment documentés ; « Prendre des
risques et rebondir » ou « Gérer ressources et priorités » le sont beaucoup moins
en contexte créateur. Sur ces entrées, deux issues sont acceptables : un ancrage
dans une littérature voisine solide, explicitement située, ou l'aveu qu'aucun
chiffre fiable n'existe. Fabriquer une référence plausible n'en est pas une.

## 10. Point ouvert

`extract-framework.py` porte un chemin absolu en dur
(`/Users/maximehebert/CreaComp Site/src/data/fr/framework.json`), ce qui lie le
script à une machine. Sans effet sur ce chantier, à traiter séparément.
