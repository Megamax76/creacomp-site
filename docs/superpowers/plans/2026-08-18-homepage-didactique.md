# Refonte didactique de la page d'accueil — plan d'implémentation

> **Pour les agents :** SOUS-SKILL REQUISE — utiliser superpowers:subagent-driven-development (recommandé) ou superpowers:executing-plans pour dérouler ce plan tâche par tâche. Les étapes emploient la syntaxe à cases (`- [ ]`).

**But :** remplacer la page d'accueil, qui résume le site, par une page qui l'introduit — un parcours numéroté en quatre temps, un fac-similé d'entrée réelle, et zéro texte dupliqué avec les autres pages.

**Architecture :** deux composants Astro neufs (`Specimen`, `PageToc`), une refonte de la branche `home` des deux fichiers de langue, et une réécriture de `src/views/Home.astro`. Le spécimen lit `framework.json` : aucun contenu du référentiel n'est recopié.

**Pile technique :** Astro 7, composants `.astro` à styles scopés, données en JSON par langue, système de style à variables CSS (`src/styles/global.css`).

**Spécification de référence :** [`docs/superpowers/specs/2026-08-18-homepage-didactique-design.md`](../specs/2026-08-18-homepage-didactique-design.md)

---

## Note sur la vérification

Le dépôt ne comporte aucun harnais de test, et ce plan n'en introduit pas : ce
serait un chantier distinct, sans rapport avec la refonte demandée. La boucle
« test rouge → code → test vert » est donc remplacée par une boucle équivalente
et réellement exécutable :

```bash
npx astro check && npm run build
```

`astro check` valide les types des props et des accès aux données ; `astro build`
échoue si un composant lève à la construction. Les deux composants neufs lèvent
volontairement une erreur explicite quand une donnée manque (code d'entrée
inconnu, niveau absent) : c'est ce qui rend la vérification par construction
significative plutôt que décorative.

La tâche 6 ajoute les contrôles de rendu que la construction ne peut pas faire :
les deux langues, le thème sombre, la largeur mobile, la console du navigateur.

---

## Structure des fichiers

| Fichier | Responsabilité |
|---|---|
| `src/components/Specimen.astro` | **créé** — rend le fac-similé d'une entrée du référentiel, lue dans `framework.json` par son code. Ne connaît ni la page d'accueil ni les annotations. |
| `src/components/PageToc.astro` | **créé** — rend un sommaire d'ancres. Générique : ne connaît que `label` et `items`. |
| `src/data/fr/site.json` | **modifié** — branche `home` refondue. |
| `src/data/en/site.json` | **modifié** — branche `home` refondue, strictement parallèle. |
| `src/views/Home.astro` | **réécrit** — séquence, en-têtes numérotés, styles des blocs neufs. |

`RubricMap.astro`, `LevelCards.astro`, `Base.astro`, `i18n.ts` et les quatre
fichiers `framework.json` ne sont pas touchés. `entryByCode`, `rubricById`,
`entryPath` et `accentOf` existent déjà dans `src/lib/i18n.ts` et couvrent tout
le besoin du spécimen.

**Règle de nommage :** les *clés* JSON sont en anglais dans les deux langues —
c'est du code, lu par les composants. Seules les *valeurs* sont traduites. Les
identifiants d'ancre, eux, sont localisés, conformément à l'usage déjà en place
(`#perimetre` en français, `#scope` en anglais sur la page « Le cadre »).

**Règle de forme :** tous les objets d'un même tableau JSON ont exactement les
mêmes clés. Un objet du tableau `toc.items` sans clé `num` produirait un type
union et ferait échouer `astro check` ; les entrées non numérotées portent donc
`"num": ""`.

---

## Tâche 1 : les données

**Fichiers :**
- Modifier : `src/data/fr/site.json` — branche `home`
- Modifier : `src/data/en/site.json` — branche `home`

> **Corrigé à l'exécution.** Cette tâche était annoncée comme additive : elle ne
> l'est pas. Remplacer `hero` et `why` en bloc retire `hero.eyebrow` et
> `why.shift`, que l'ancien `Home.astro` lit encore — `astro check` remonte 11
> erreurs de type. Les données et la page doivent atterrir **ensemble** : dérouler
> les tâches 1 à 4 avant de construire, et ne vérifier qu'à la fin de la tâche 4.
> L'étape 4 ci-dessous est donc à ignorer telle qu'écrite.

Les clés `warning`, `map` et `levels` restent en place jusqu'à la tâche 5, où
elles sont retirées une fois plus personne pour les lire.

- [ ] **Étape 1 : remplacer la branche `home` de `src/data/fr/site.json`**

Remplacer intégralement la valeur de la clé `"home"` par l'objet ci-dessous.
Les clés `warning`, `map`, `levels` et l'ancien `why` disparaissent de cet
objet : leur contenu est redistribué dans `scope`, `architecture` et `why`.
Les clés `audiences` et `closing` sont conservées, avec un `id` ajouté et des
corps resserrés.

```json
"home": {
  "hero": {
    "title": "Le référentiel de compétences pour l'ère des créateurs",
    "lead": "CréaComp cartographie la littératie numérique créative : l'ensemble des savoirs qui permettent de recevoir de façon critique, comprendre, imaginer, fabriquer, diffuser et valoriser dans les environnements numériques.",
    "primaryCta": "Explorer les 31 entrées",
    "secondaryCta": "Comprendre le cadre"
  },
  "toc": {
    "label": "Sur cette page",
    "items": [
      { "id": "objet", "num": "01", "label": "L'objet" },
      { "id": "architecture", "num": "02", "label": "L'architecture" },
      { "id": "entree", "num": "03", "label": "Une entrée" },
      { "id": "portee", "num": "04", "label": "Portée et limites" },
      { "id": "pourquoi", "num": "", "label": "Pourquoi ce cadre" },
      { "id": "usages", "num": "", "label": "Usages" },
      { "id": "citer", "num": "", "label": "Citer et réutiliser" }
    ]
  },
  "object": {
    "id": "objet",
    "num": "01",
    "eyebrow": "L'objet",
    "title": "Ce que le référentiel décrit",
    "lead": "La définition tient en une phrase, mais elle recouvre six capacités distinctes. Les voici séparées : c'est sur elles que le référentiel est bâti.",
    "verbsLabel": "Six capacités",
    "verbs": [
      "Recevoir de façon critique",
      "Comprendre",
      "Imaginer",
      "Fabriquer",
      "Diffuser",
      "Valoriser"
    ],
    "note": "CréaComp en est la cartographie. Il ne dit pas comment enseigner ces capacités : il dit comment les reconnaître."
  },
  "architecture": {
    "id": "architecture",
    "num": "02",
    "eyebrow": "L'architecture",
    "title": "Comment le référentiel est organisé",
    "lead": "Quatre nombres suffisent à en décrire la charpente. Chacun désigne une chose précise.",
    "counts": [
      { "value": "7", "unit": "rubriques", "body": "Des domaines d'action, nommés par des verbes." },
      { "value": "28", "unit": "compétences", "body": "Quatre par rubrique." },
      { "value": "3", "unit": "fils transversaux", "body": "Ils traversent les sept rubriques." },
      { "value": "124", "unit": "descripteurs observables", "body": "Quatre niveaux appliqués à chacune des 31 entrées." }
    ],
    "mapTitle": "Sept rubriques d'action",
    "mapLead": "Chaque rubrique regroupe quatre compétences. Survolez-en une pour en découvrir le contenu.",
    "levelsTitle": "Quatre niveaux — des postures, non des âges",
    "levelsLead": "Les mêmes quatre niveaux s'appliquent identiquement aux trente et une entrées : c'est ce qui donne au référentiel sa cohérence interne. Les repères scolaires sont indicatifs.",
    "goldenRule": "Règle d'or de calibrage : tout descripteur de niveau Découverte est atteignable par un collégien équipé d'un simple smartphone. Aucun ne présuppose de matériel professionnel, d'audience existante ou d'activité établie.",
    "cta": "Ouvrir le référentiel complet"
  },
  "specimen": {
    "id": "entree",
    "num": "03",
    "eyebrow": "Une entrée",
    "title": "À quoi ressemble une compétence",
    "lead": "Voici une entrée réelle, dépliée à ses deux extrémités. Les trente autres ont exactement la même forme.",
    "code": "1.2",
    "levels": ["N1", "N4"],
    "annotationsLabel": "Comment lire cette fiche",
    "annotations": [
      {
        "term": "Le code",
        "body": "Stable d'une édition à l'autre et d'une langue à l'autre. C'est lui qu'on cite, jamais le titre."
      },
      {
        "term": "Le descripteur",
        "body": "Énonce ce que la personne est capable de faire, en termes vérifiables par un évaluateur tiers."
      },
      {
        "term": "La preuve d'évaluation",
        "body": "Dit comment on le vérifie : par un artefact réel, jamais par un questionnaire."
      }
    ]
  },
  "scope": {
    "id": "portee",
    "num": "04",
    "eyebrow": "Portée et limites",
    "title": "Ce que le référentiel fait, et ce qu'il ne fait pas",
    "lead": "Quatre bornes, énoncées comme des choix et non comme des réserves.",
    "pairs": [
      {
        "is": "Une cartographie",
        "isNot": "Pas un programme de formation",
        "body": "Il décrit des savoirs et permet de les évaluer. Il ne prescrit ni parcours, ni méthode, ni contenu."
      },
      {
        "is": "Un territoire où chacun dessine son profil",
        "isNot": "Pas un socle que tout le monde devrait maîtriser",
        "body": "Ni hiérarchie entre les rubriques, ni ordre imposé de progression. Nul n'est censé tout maîtriser."
      },
      {
        "is": "Des preuves de création",
        "isNot": "Pas de questionnaire, pas de note globale",
        "body": "Une compétence se valide par un artefact réel, accompagné d'une analyse réflexive."
      },
      {
        "is": "Des capacités de jugement",
        "isNot": "Pas une liste de logiciels",
        "body": "Aucun descripteur ne nomme un outil. Les outils se renouvellent ; le jugement demeure."
      }
    ],
    "cta": "Lire les sept principes directeurs"
  },
  "why": {
    "id": "pourquoi",
    "eyebrow": "Pourquoi ce cadre",
    "title": "La valeur a changé de place",
    "body": [
      "L'intelligence artificielle générative a effondré le coût de la production : un texte correct, un visuel propre, une vidéo montée deviennent universellement accessibles. Ce qui se banalise se dévalue, et la valeur se déplace vers les deux extrémités de la chaîne créative.",
      "Aucun cadre existant ne décrivait ces deux extrémités ensemble. C'est la raison d'être de CréaComp, et la clé de lecture qui explique pourquoi ses rubriques d'amont et d'aval pèsent autant que la fabrication elle-même."
    ],
    "caption": "Où se loge la valeur dans la chaîne créative",
    "stages": [
      {
        "label": "En amont",
        "name": "Le regard",
        "body": "Savoir quoi créer, pourquoi, avec quel point de vue.",
        "value": "high",
        "rubrics": "S'informer · Analyser · Créer"
      },
      {
        "label": "Au milieu",
        "name": "La fabrication",
        "body": "Produire une forme correcte. Coût effondré, valeur diluée.",
        "value": "low",
        "rubrics": "Faire"
      },
      {
        "label": "En aval",
        "name": "La relation",
        "body": "La confiance, la communauté, les actifs que l'on possède.",
        "value": "high",
        "rubrics": "Collaborer · Entreprendre · Rentabiliser"
      }
    ],
    "cta": "Lire les fondements du référentiel"
  },
  "audiences": {
    "id": "usages",
    "eyebrow": "Usages",
    "title": "À qui ce référentiel sert-il ?",
    "items": [
      {
        "name": "Enseignants",
        "body": "Adosser une progression à des descripteurs observables plutôt qu'à des intentions, du collège au supérieur."
      },
      {
        "name": "Organismes de formation",
        "body": "Construire une offre lisible, alignée sur un cadre public, et l'évaluer par des preuves de création."
      },
      {
        "name": "Créateurs et indépendants",
        "body": "Situer sa pratique sur une carte et repérer ses angles morts."
      },
      {
        "name": "Institutions et chercheurs",
        "body": "Disposer d'un cadre ouvert, daté et citable, pour outiller des politiques publiques ou des travaux de recherche."
      }
    ],
    "cta": "Comment utiliser le référentiel"
  },
  "closing": {
    "id": "citer",
    "title": "Un bien commun",
    "body": "CréaComp est publié sous licence Creative Commons Attribution – Partage dans les mêmes conditions 4.0. Vous pouvez le reprendre, le traduire, l'adapter et l'intégrer à vos propres dispositifs, à condition d'en citer l'origine et de partager vos adaptations aux mêmes conditions.",
    "primaryCta": "Utiliser & citer",
    "secondaryCta": "Écrire à l'auteur"
  }
}
```

- [ ] **Étape 2 : remplacer la branche `home` de `src/data/en/site.json`**

Mêmes clés, exactement, valeurs en anglais.

```json
"home": {
  "hero": {
    "title": "The competency framework for the creator era",
    "lead": "CréaComp maps digital creative literacy: the body of knowledge that allows a person to critically receive, understand, imagine, make, publish and capitalise on content and projects in digital environments.",
    "primaryCta": "Explore the 31 entries",
    "secondaryCta": "Understand the foundations"
  },
  "toc": {
    "label": "On this page",
    "items": [
      { "id": "object", "num": "01", "label": "The object" },
      { "id": "architecture", "num": "02", "label": "The architecture" },
      { "id": "entry", "num": "03", "label": "One entry" },
      { "id": "scope", "num": "04", "label": "Scope and limits" },
      { "id": "why", "num": "", "label": "Why this framework" },
      { "id": "uses", "num": "", "label": "Uses" },
      { "id": "cite", "num": "", "label": "Use and cite" }
    ]
  },
  "object": {
    "id": "object",
    "num": "01",
    "eyebrow": "The object",
    "title": "What the framework describes",
    "lead": "The definition fits in a single sentence, but it covers six distinct capacities. Here they are, set apart: they are what the framework is built on.",
    "verbsLabel": "Six capacities",
    "verbs": [
      "Critically receive",
      "Understand",
      "Imagine",
      "Make",
      "Publish",
      "Capitalise on"
    ],
    "note": "CréaComp maps them. It does not say how to teach these capacities: it says how to recognise them."
  },
  "architecture": {
    "id": "architecture",
    "num": "02",
    "eyebrow": "The architecture",
    "title": "How the framework is organised",
    "lead": "Four numbers describe its whole structure. Each one names something precise.",
    "counts": [
      { "value": "7", "unit": "domains", "body": "Fields of action, named with verbs." },
      { "value": "28", "unit": "competencies", "body": "Four per domain." },
      { "value": "3", "unit": "transversal threads", "body": "They run through all seven domains." },
      { "value": "124", "unit": "observable descriptors", "body": "Four levels applied to each of the 31 entries." }
    ],
    "mapTitle": "Seven domains of action",
    "mapLead": "Each domain gathers four competencies. Hover one to reveal what it contains.",
    "levelsTitle": "Four levels — postures, not ages",
    "levelsLead": "The same four levels apply identically to all thirty-one entries, and that is what gives the framework its internal coherence. The educational landmarks are indicative only.",
    "goldenRule": "Calibration golden rule: every Discovery-level descriptor is achievable by a lower-secondary student equipped with nothing more than a smartphone. None presupposes professional equipment, an existing audience or an established activity.",
    "cta": "Open the full framework"
  },
  "specimen": {
    "id": "entry",
    "num": "03",
    "eyebrow": "One entry",
    "title": "What a competency looks like",
    "lead": "Here is a real entry, unfolded at both ends. The other thirty have exactly the same shape.",
    "code": "1.2",
    "levels": ["N1", "N4"],
    "annotationsLabel": "How to read this entry",
    "annotations": [
      {
        "term": "The code",
        "body": "Stable across editions and across languages. It is what you cite — never the title."
      },
      {
        "term": "The descriptor",
        "body": "States what the person is able to do, in terms a third-party assessor can verify."
      },
      {
        "term": "The evidence",
        "body": "States how it is verified: through a real artefact, never through a questionnaire."
      }
    ]
  },
  "scope": {
    "id": "scope",
    "num": "04",
    "eyebrow": "Scope and limits",
    "title": "What the framework does, and what it does not",
    "lead": "Four boundaries, stated as choices rather than as caveats.",
    "pairs": [
      {
        "is": "A map",
        "isNot": "Not a curriculum",
        "body": "It describes knowledge and makes it assessable. It prescribes no pathway, no method and no content."
      },
      {
        "is": "A territory where each person draws their own profile",
        "isNot": "Not a baseline everyone must master",
        "body": "No hierarchy between domains, no imposed order of progression. Nobody is expected to master the whole."
      },
      {
        "is": "Evidence of creation",
        "isNot": "No quizzes, no overall grade",
        "body": "A competency is validated through a real artefact, together with a short reflective analysis."
      },
      {
        "is": "Capacities of judgement",
        "isNot": "Not a list of software",
        "body": "No descriptor names a tool. Tools are replaced; judgement remains."
      }
    ],
    "cta": "Read the seven guiding principles"
  },
  "why": {
    "id": "why",
    "eyebrow": "Why this framework",
    "title": "Value has moved",
    "body": [
      "Generative artificial intelligence has collapsed the cost of production: a competent text, a clean visual, an edited video are becoming universally accessible. What becomes ordinary loses its value, and value moves towards both ends of the creative chain.",
      "No existing framework described those two ends together. That is why CréaComp exists, and it is the reading key that explains why its upstream and downstream domains weigh as much as making itself."
    ],
    "caption": "Where value sits along the creative chain",
    "stages": [
      {
        "label": "Upstream",
        "name": "The eye",
        "body": "Knowing what to create, why, and from which point of view.",
        "value": "high",
        "rubrics": "Gather · Analyse · Create"
      },
      {
        "label": "Midstream",
        "name": "Making",
        "body": "Producing a correct form. Cost collapsed, value diluted.",
        "value": "low",
        "rubrics": "Make"
      },
      {
        "label": "Downstream",
        "name": "The relationship",
        "body": "Trust, community, and the assets you actually own.",
        "value": "high",
        "rubrics": "Collaborate · Venture · Monetise"
      }
    ],
    "cta": "Read the foundations of the framework"
  },
  "audiences": {
    "id": "uses",
    "eyebrow": "Uses",
    "title": "Who is this framework for?",
    "items": [
      {
        "name": "Teachers",
        "body": "Anchor a progression in observable descriptors rather than in intentions, from lower secondary to higher education."
      },
      {
        "name": "Training providers",
        "body": "Build a legible offer aligned with a public framework, and assess it through evidence of creation."
      },
      {
        "name": "Creators and freelancers",
        "body": "Locate your practice on a map and identify your blind spots."
      },
      {
        "name": "Institutions and researchers",
        "body": "Work from an open, dated and citable framework, to support public policy or research."
      }
    ],
    "cta": "How to use the framework"
  },
  "closing": {
    "id": "cite",
    "title": "A common good",
    "body": "CréaComp is published under a Creative Commons Attribution–ShareAlike 4.0 licence. You may reuse it, translate it, adapt it and embed it in your own programmes, provided you credit its origin and share your adaptations under the same terms.",
    "primaryCta": "Use & cite",
    "secondaryCta": "Write to the author"
  }
}
```

- [ ] **Étape 3 : vérifier que les deux fichiers portent exactement les mêmes clés**

```bash
cd "/Users/maximehebert/CreaComp Site" && python3 - <<'PY'
import json
def shape(o, p=''):
    if isinstance(o, dict):
        out = set()
        for k, v in o.items():
            out.add(p + '/' + k)
            out |= shape(v, p + '/' + k)
        return out
    if isinstance(o, list) and o:
        return shape(o[0], p + '[]')
    return set()
fr = json.load(open('src/data/fr/site.json'))['home']
en = json.load(open('src/data/en/site.json'))['home']
a, b = shape(fr), shape(en)
print('FR seul :', sorted(a - b))
print('EN seul :', sorted(b - a))
print('OK' if a == b else 'DIVERGENCE')
PY
```

Attendu : `FR seul : []`, `EN seul : []`, `OK`.

- [ ] **Étape 4 : ~~vérifier que le site construit toujours~~ — supprimée**

Voir l'avertissement en tête de tâche : à ce stade la construction échoue
nécessairement. Enchaîner les tâches 2, 3 et 4, et construire à la fin de la
tâche 4.

- [ ] **Étape 5 : ~~commit~~ — reporté à la fin de la tâche 4**

Les données seules ne construisent pas ; elles sont commitées avec la page.
Message de référence, conservé pour mémoire :

```bash
# NE PAS EXÉCUTER SEUL — voir tâche 4, étape 6
git commit -m "Refond les données de la page d'accueil

Les nouvelles clés cohabitent avec les anciennes : la page ne change pas
encore. Le sommaire, l'objet, l'architecture, le spécimen et la portée
entrent ; la balance attention-intention sort, elle figure mot pour mot
sur la page « Le cadre ». Le chapô de l'en-tête est conservé tel quel :
la section 01 ne redéfinit pas, elle déplie ses six verbes."
```

---

## Tâche 2 : le composant `Specimen`

**Fichiers :**
- Créer : `src/components/Specimen.astro`

Le composant rend le fac-similé d'une entrée du référentiel. Il ne connaît ni la
page d'accueil, ni les annotations qui l'entourent : il reçoit un code et une
liste de niveaux, et rend ce que `framework.json` contient. C'est ce qui garantit
qu'il ne peut jamais diverger du référentiel.

- [ ] **Étape 1 : écrire le composant**

Créer `src/components/Specimen.astro` avec exactement ce contenu :

```astro
---
import { entryByCode, rubricById, entryPath, site, type Lang } from '../lib/i18n';

interface Props {
  lang: Lang;
  /** Code de l'entrée à exposer, par exemple « 1.2 ». */
  code: string;
  /** Niveaux à déplier, dans l'ordre d'affichage. */
  levels: string[];
}

const { lang, code, levels } = Astro.props;
const s = site(lang);

// Le spécimen est lu dans le référentiel, jamais recopié : une donnée absente
// est une erreur de construction, pas une case vide à l'écran.
const entry = entryByCode(lang, code);
if (!entry) {
  throw new Error(`Specimen : aucune entrée ne porte le code « ${code} » en ${lang}.`);
}

const rubric = entry.rubricId === undefined ? undefined : rubricById(lang, entry.rubricId);
const accent = rubric?.color ?? 'graphite';

const shown = levels.map((id) => {
  const level = s.levels.find((candidate) => candidate.id === id);
  const content = entry.levels[id];
  if (!level || !content) {
    throw new Error(`Specimen : le niveau « ${id} » est introuvable pour l'entrée ${code} en ${lang}.`);
  }
  return { id, name: level.name, descriptor: content.descriptor, evidence: content.evidence };
});
---

<figure class="specimen" data-accent={accent}>
  <div class="specimen__head">
    <p class="specimen__stamp">
      <span class="specimen__code">{entry.code}</span>
      {rubric && <span class="specimen__rubric">{rubric.title}</span>}
    </p>
    <h3 class="specimen__title">{entry.title}</h3>
    <p class="specimen__definition">{entry.definition}</p>
  </div>

  <ol class="specimen__levels">
    {
      shown.map((level) => (
        <li class="specimen__level">
          <p class="specimen__level-head">
            <span class="specimen__level-code">{level.id}</span>
            <span class="specimen__level-name">{level.name}</span>
          </p>
          <dl class="specimen__fields">
            <dt>{s.ui.descriptor}</dt>
            <dd class="specimen__descriptor">{level.descriptor}</dd>
            <dt>{s.ui.evidence}</dt>
            <dd class="specimen__evidence">{level.evidence}</dd>
          </dl>
        </li>
      ))
    }
  </ol>

  <figcaption class="specimen__foot">
    <a class="specimen__link" href={entryPath(lang, entry.slug)}>
      {s.ui.readMore}
      <span class="specimen__arrow" aria-hidden="true">→</span>
    </a>
  </figcaption>
</figure>

<style>
  .specimen {
    margin: 0;
    border: 1px solid var(--rule);
    border-radius: var(--radius);
    background: var(--paper-raised);
    overflow: hidden;
  }

  .specimen__head {
    padding: 1.5rem 1.5rem 1.6rem;
    border-bottom: 1px solid var(--rule);
  }

  /* Le code et la rubrique portent la teinte ; le nom de la rubrique est écrit
     en toutes lettres pour que rien ne dépende de la seule couleur. */
  .specimen__stamp {
    display: flex;
    flex-wrap: wrap;
    align-items: baseline;
    gap: 0.6rem;
    font-family: var(--font-mono);
    font-size: 0.68rem;
    letter-spacing: 0.13em;
    text-transform: uppercase;
  }
  .specimen__code {
    padding: 0.18rem 0.45rem;
    border: 1px solid var(--accent-edge);
    border-radius: 3px;
    background: var(--accent-wash);
    color: var(--accent);
    font-weight: 600;
    letter-spacing: 0.08em;
  }
  .specimen__rubric { color: var(--ink-faint); }

  .specimen__title {
    margin-top: 0.85rem;
    font-size: var(--step-2);
    letter-spacing: -0.018em;
    text-wrap: balance;
  }

  .specimen__definition {
    margin-top: 0.7rem;
    font-size: 0.92rem;
    line-height: 1.6;
    color: var(--ink-soft);
  }

  .specimen__levels {
    display: grid;
    gap: 1px;
    background: var(--rule);
    list-style: none;
  }
  @media (min-width: 46rem) {
    .specimen__levels { grid-template-columns: repeat(2, 1fr); }
  }

  .specimen__level {
    padding: 1.3rem 1.5rem 1.5rem;
    background: var(--paper-raised);
  }

  .specimen__level-head {
    display: flex;
    align-items: baseline;
    gap: 0.55rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid var(--rule);
  }
  .specimen__level-code {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.14em;
    color: var(--accent);
  }
  .specimen__level-name {
    font-family: var(--font-display);
    font-variation-settings: 'SOFT' 30, 'WONK' 1, 'opsz' 20;
    font-size: 1.08rem;
    letter-spacing: -0.012em;
  }

  .specimen__fields { margin: 0; }
  .specimen__fields dt {
    margin-top: 1rem;
    font-family: var(--font-mono);
    font-size: 0.62rem;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    color: var(--ink-faint);
  }
  .specimen__fields dd {
    margin: 0.35rem 0 0;
    font-size: 0.9rem;
    line-height: 1.6;
  }
  .specimen__descriptor { color: var(--ink); }
  .specimen__evidence { color: var(--ink-soft); }

  .specimen__foot {
    padding: 1rem 1.5rem 1.1rem;
    border-top: 1px solid var(--rule);
    background: var(--paper-sunken);
  }
  .specimen__link {
    font-family: var(--font-mono);
    font-size: 0.72rem;
    letter-spacing: 0.06em;
    color: var(--accent);
    text-decoration: none;
  }
  .specimen__link:hover { text-decoration: underline; }
  .specimen__arrow { margin-left: 0.4rem; }
</style>
```

- [ ] **Étape 2 : vérifier que le composant compile**

```bash
cd "/Users/maximehebert/CreaComp Site" && npx astro check
```

Attendu : `0 errors`. Le composant n'est encore monté nulle part ; cette étape ne
valide que ses types et ses accès aux données.

- [ ] **Étape 3 : vérifier que les gardes lèvent bien**

Prouver que les deux `throw` fonctionnent, plutôt que de les supposer. Monter
temporairement le composant avec un code inexistant à la fin de `Home.astro`,
juste avant `</Base>` :

```astro
<Specimen lang={lang} code="9.9" levels={['N1']} />
```

en ajoutant l'import en tête de fichier :

```astro
import Specimen from '../components/Specimen.astro';
```

puis :

```bash
cd "/Users/maximehebert/CreaComp Site" && npm run build
```

Attendu : la construction **échoue** avec `Specimen : aucune entrée ne porte le
code « 9.9 » en fr.`

Retirer ensuite la ligne `<Specimen …>` et l'import, et vérifier que la
construction repasse :

```bash
cd "/Users/maximehebert/CreaComp Site" && npm run build
```

Attendu : `Complete!`

- [ ] **Étape 4 : commit**

```bash
cd "/Users/maximehebert/CreaComp Site" && git add src/components/Specimen.astro && git commit -m "Ajoute le composant du spécimen d'entrée

Il lit l'entrée dans framework.json par son code et déplie les niveaux
demandés. Rien n'est recopié : le spécimen ne peut pas diverger du
référentiel, et une donnée manquante casse la construction."
```

---

## Tâche 3 : le composant `PageToc`

**Fichiers :**
- Créer : `src/components/PageToc.astro`

Composant générique : il ne connaît que son intitulé et sa liste d'ancres. Il
n'enveloppe pas son contenu dans `.wrap` — c'est la page qui décide de sa
largeur.

- [ ] **Étape 1 : écrire le composant**

Créer `src/components/PageToc.astro` avec exactement ce contenu :

```astro
---
interface Item {
  href: string;
  /** Numéro d'étape, ou chaîne vide pour une section non numérotée. */
  num: string;
  label: string;
}

interface Props {
  label: string;
  items: Item[];
}

const { label, items } = Astro.props;
---

<nav class="toc" aria-label={label}>
  <p class="toc__label">{label}</p>
  <ol class="toc__items">
    {
      items.map((item) => (
        <li class="toc__item">
          <a class="toc__link" href={item.href}>
            {item.num && (
              <span class="toc__num" aria-hidden="true">
                {item.num}
              </span>
            )}
            <span class="toc__text">{item.label}</span>
          </a>
        </li>
      ))
    }
  </ol>
</nav>

<style>
  .toc {
    display: grid;
    gap: 0.9rem;
    padding: 1.1rem 0 1.2rem;
    border-top: 1px solid var(--rule);
    border-bottom: 1px solid var(--rule);
  }
  @media (min-width: 60rem) {
    .toc {
      grid-template-columns: auto 1fr;
      align-items: baseline;
      gap: 2rem;
    }
  }

  .toc__label {
    font-family: var(--font-mono);
    font-size: 0.66rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--ink-faint);
  }

  .toc__items {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem 1.5rem;
    list-style: none;
  }

  .toc__link {
    display: inline-flex;
    align-items: baseline;
    gap: 0.4rem;
    font-size: 0.84rem;
    color: var(--ink-soft);
    text-decoration: none;
  }
  .toc__link:hover { color: var(--accent); }
  .toc__link:hover .toc__text { text-decoration: underline; }

  .toc__num {
    font-family: var(--font-mono);
    font-size: 0.66rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    color: var(--accent);
  }
</style>
```

- [ ] **Étape 2 : vérifier que le composant compile**

```bash
cd "/Users/maximehebert/CreaComp Site" && npx astro check && npm run build
```

Attendu : `0 errors`, puis `Complete!`.

- [ ] **Étape 3 : commit**

```bash
cd "/Users/maximehebert/CreaComp Site" && git add src/components/PageToc.astro && git commit -m "Ajoute le sommaire de page

Composant générique : un intitulé, des ancres, un numéro facultatif.
Il ne fixe pas sa largeur, la page s'en charge."
```

---

## Tâche 4 : la réécriture de la page

**Fichiers :**
- Réécrire : `src/views/Home.astro`

C'est la tâche qui met la nouvelle page en service. Le fichier est remplacé
intégralement par le contenu ci-dessous.

Ce qui est **conservé tel quel** du fichier actuel : le bloc `hero` et ses styles,
la figure `curve` avec ses `stage` et leurs styles, la grille `audiences`, le bloc
`closing`, et la grille des paires (renommée `pairs` au lieu de `warning`).

Ce qui **disparaît** : la liste `hero__counts` (remontée en 02, expliquée), le
surtitre du hero (absorbé par la ligne d'identité), et tout le bloc `shift` — la
balance attention / intention, qui figure mot pour mot sur la page « Le cadre ».

- [ ] **Étape 1 : remplacer intégralement `src/views/Home.astro`**

```astro
---
import { Image } from 'astro:assets';
import Base from '../layouts/Base.astro';
import RubricMap from '../components/RubricMap.astro';
import LevelCards from '../components/LevelCards.astro';
import PageToc from '../components/PageToc.astro';
import Specimen from '../components/Specimen.astro';
import { site, path, type Lang } from '../lib/i18n';
import { image, credit, creditSource } from '../lib/images';

interface Props {
  lang: Lang;
}

const { lang } = Astro.props;
const s = site(lang);
const home = s.home;

// La carte d'identité du document remplace les compteurs : c'est le repère
// qu'attend un lecteur institutionnel, et il se déduit entièrement des méta.
const identity = `${s.meta.versionLabel} · ${s.meta.author} · ${s.meta.license}`;

const tocItems = home.toc.items.map((item) => ({
  href: `#${item.id}`,
  num: item.num,
  label: item.label,
}));

// Les principes directeurs portent une ancre localisée : « principes » en
// français, « principles » en anglais. On la lit plutôt que de la deviner.
const principlesHref = `${path(lang, 'foundations')}#${s.foundations.principles.id}`;

const heroImage = image('hero');
const heroCredit = credit('hero');
const heroAlt =
  lang === 'fr'
    ? "Deux silhouettes à contre-jour : une main tend un filtre devant l'objectif d'un photographe, dans des faisceaux bleus et magenta."
    : "Two silhouettes against the light: a hand holds a filter in front of a photographer's lens, in blue and magenta beams.";
---

<Base lang={lang} page="home">
  <!-- En-tête du document -->
  <section class="hero">
    <div class="wrap hero__inner">
      <div class="hero__text">
        <h1 class="hero__title">{home.hero.title}</h1>
        <p class="hero__lead">{home.hero.lead}</p>

        <div class="hero__actions">
          <a class="btn" href={path(lang, 'framework')}>
            {home.hero.primaryCta}
            <span class="btn__arrow" aria-hidden="true">→</span>
          </a>
          <a class="btn btn--ghost" href={path(lang, 'foundations')}>{home.hero.secondaryCta}</a>
        </div>

        <p class="hero__identity">{identity}</p>
      </div>

      {
        heroImage && (
          <figure class="hero__figure">
            <div class="hero__frame">
              <Image
                src={heroImage}
                alt={heroAlt}
                widths={[420, 640, 900]}
                sizes="(max-width: 62rem) 100vw, 34vw"
                loading="eager"
                fetchpriority="high"
              />
            </div>
            {heroCredit && (
              <figcaption class="credit-line">
                <a href={heroCredit.authorUrl} rel="noopener noreferrer" target="_blank">
                  {heroCredit.author}
                </a>
                <span aria-hidden="true"> · </span>
                <a href={creditSource.url} rel="noopener noreferrer" target="_blank">
                  {creditSource.name}
                </a>
              </figcaption>
            )}
          </figure>
        )
      }
    </div>
  </section>

  <!-- Sommaire de page -->
  <div class="wrap">
    <PageToc label={home.toc.label} items={tocItems} />
  </div>

  <!-- 01 · L'objet -->
  <section class="section" id={home.object.id}>
    <div class="wrap">
      <p class="eyebrow">
        <span class="step">{home.object.num}</span>
        {home.object.eyebrow}
      </p>
      <h2 class="title-2">{home.object.title}</h2>
      <p class="lead section__lead">{home.object.lead}</p>

      <p class="verbs__label">{home.object.verbsLabel}</p>
      <ul class="verbs">
        {home.object.verbs.map((verb) => <li class="verb">{verb}</li>)}
      </ul>

      <p class="object__note">{home.object.note}</p>
    </div>
  </section>

  <!-- 02 · L'architecture -->
  <section class="section section--sunken section--ruled" id={home.architecture.id}>
    <div class="wrap">
      <p class="eyebrow">
        <span class="step">{home.architecture.num}</span>
        {home.architecture.eyebrow}
      </p>
      <h2 class="title-2">{home.architecture.title}</h2>
      <p class="lead section__lead">{home.architecture.lead}</p>

      <ul class="tally">
        {
          home.architecture.counts.map((count) => (
            <li class="tally__item">
              <p class="tally__value">{count.value}</p>
              <p class="tally__unit">{count.unit}</p>
              <p class="tally__body">{count.body}</p>
            </li>
          ))
        }
      </ul>

      <div class="block">
        <h3 class="title-3">{home.architecture.mapTitle}</h3>
        <p class="block__lead">{home.architecture.mapLead}</p>
        <RubricMap lang={lang} />
      </div>

      <div class="block">
        <h3 class="title-3">{home.architecture.levelsTitle}</h3>
        <p class="block__lead">{home.architecture.levelsLead}</p>
        <LevelCards lang={lang} />
        <p class="rule-gold">{home.architecture.goldenRule}</p>
      </div>

      <p class="block__cta">
        <a class="btn" href={path(lang, 'framework')}>
          {home.architecture.cta}
          <span class="btn__arrow" aria-hidden="true">→</span>
        </a>
      </p>
    </div>
  </section>

  <!-- 03 · Une entrée -->
  <section class="section" id={home.specimen.id}>
    <div class="wrap">
      <p class="eyebrow">
        <span class="step">{home.specimen.num}</span>
        {home.specimen.eyebrow}
      </p>
      <h2 class="title-2">{home.specimen.title}</h2>
      <p class="lead section__lead">{home.specimen.lead}</p>

      <div class="sample">
        <Specimen lang={lang} code={home.specimen.code} levels={home.specimen.levels} />

        <aside class="notes">
          <p class="notes__label">{home.specimen.annotationsLabel}</p>
          <dl class="notes__list">
            {
              home.specimen.annotations.map((note) => (
                <div class="note">
                  <dt class="note__term">{note.term}</dt>
                  <dd class="note__body">{note.body}</dd>
                </div>
              ))
            }
          </dl>
        </aside>
      </div>
    </div>
  </section>

  <!-- 04 · Portée et limites -->
  <section class="section section--sunken section--ruled" id={home.scope.id}>
    <div class="wrap">
      <p class="eyebrow">
        <span class="step">{home.scope.num}</span>
        {home.scope.eyebrow}
      </p>
      <h2 class="title-2">{home.scope.title}</h2>
      <p class="lead section__lead">{home.scope.lead}</p>

      <ul class="pairs">
        {
          home.scope.pairs.map((pair) => (
            <li class="pair">
              <p class="pair__is">{pair.is}</p>
              <p class="pair__isnot">{pair.isNot}</p>
              <p class="pair__body">{pair.body}</p>
            </li>
          ))
        }
      </ul>

      <p class="block__cta">
        <a class="btn btn--ghost" href={principlesHref}>
          {home.scope.cta}
          <span class="btn__arrow" aria-hidden="true">→</span>
        </a>
      </p>
    </div>
  </section>

  <!-- Pourquoi ce cadre -->
  <section class="section" id={home.why.id}>
    <div class="wrap">
      <p class="eyebrow">{home.why.eyebrow}</p>
      <h2 class="title-2 why__title">{home.why.title}</h2>

      <div class="chain">
        <div class="chain__text prose">
          {home.why.body.map((paragraph) => <p>{paragraph}</p>)}
          <p class="block__cta">
            <a class="btn btn--ghost" href={path(lang, 'foundations')}>
              {home.why.cta}
              <span class="btn__arrow" aria-hidden="true">→</span>
            </a>
          </p>
        </div>

        <figure class="curve">
          <figcaption class="curve__caption">{home.why.caption}</figcaption>
          <ol class="curve__stages">
            {
              home.why.stages.map((stage) => (
                <li class="stage" data-value={stage.value}>
                  <div class="stage__bar" aria-hidden="true">
                    <span class="stage__fill" />
                  </div>
                  <p class="stage__label">{stage.label}</p>
                  <p class="stage__name">{stage.name}</p>
                  <p class="stage__body">{stage.body}</p>
                  <p class="stage__rubrics">{stage.rubrics}</p>
                </li>
              ))
            }
          </ol>
        </figure>
      </div>
    </div>
  </section>

  <!-- Usages -->
  <section class="section section--sunken section--ruled" id={home.audiences.id}>
    <div class="wrap">
      <p class="eyebrow">{home.audiences.eyebrow}</p>
      <h2 class="title-2">{home.audiences.title}</h2>
      <ul class="audiences">
        {
          home.audiences.items.map((item, index) => (
            <li class="audience">
              <p class="audience__index" aria-hidden="true">
                {String(index + 1).padStart(2, '0')}
              </p>
              <h3 class="audience__name">{item.name}</h3>
              <p class="audience__body">{item.body}</p>
            </li>
          ))
        }
      </ul>
      <p class="audiences__cta">
        <a class="btn btn--ghost" href={path(lang, 'use')}>
          {home.audiences.cta}
          <span class="btn__arrow" aria-hidden="true">→</span>
        </a>
      </p>
    </div>
  </section>

  <!-- Citer et réutiliser -->
  <section class="section closing" id={home.closing.id}>
    <div class="wrap closing__inner">
      <h2 class="title-2">{home.closing.title}</h2>
      <p class="closing__body">{home.closing.body}</p>
      <div class="closing__actions">
        <a class="btn" href={path(lang, 'use')}>{home.closing.primaryCta}</a>
        <a class="btn btn--ghost" href={path(lang, 'contact')}>{home.closing.secondaryCta}</a>
      </div>
    </div>
  </section>
</Base>

<style>
  /* --- Hero ----------------------------------------------------------------- */

  .hero {
    position: relative;
    padding-block: clamp(3.5rem, 11vw, 8.5rem) clamp(3rem, 8vw, 6rem);
    overflow: hidden;
  }
  /* Trame typographique discrète : une grille d'imprimeur, à peine perceptible. */
  .hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image:
      linear-gradient(to right, var(--rule) 1px, transparent 1px),
      linear-gradient(to bottom, var(--rule) 1px, transparent 1px);
    background-size: clamp(3rem, 8vw, 6rem) clamp(3rem, 8vw, 6rem);
    opacity: 0.42;
    mask-image: radial-gradient(115% 85% at 78% 8%, #000 0%, transparent 68%);
    pointer-events: none;
  }

  .hero__inner {
    position: relative;
    display: grid;
    gap: clamp(2rem, 5vw, 3.5rem);
    align-items: center;
  }
  @media (min-width: 62rem) {
    .hero__inner { grid-template-columns: minmax(0, 1.15fr) minmax(0, 0.85fr); }
  }

  .hero__figure { margin: 0; }
  .hero__frame {
    overflow: hidden;
    border-radius: var(--radius);
    aspect-ratio: 4 / 5;
    background: var(--paper-sunken);
  }
  @media (max-width: 62rem) {
    .hero__frame { aspect-ratio: 16 / 9; }
  }
  /* La photographie garde sa couleur, mais assagie : elle doit s'accorder au
     papier et aux encres des rubriques sans virer à l'illustration. */
  .hero__frame :global(img) {
    width: 100%;
    height: 100%;
    object-fit: cover;
    /* Le cadre vertical taille dans une photographie horizontale : le point
       d'ancrage est décalé vers la droite pour garder le photographe entier —
       chapeau, appareil, mains — sans perdre le faisceau de lumière. */
    object-position: 62% center;
    filter: saturate(0.62) contrast(1.04);
  }

  .hero__title {
    font-size: var(--step-5);
    font-variation-settings: 'SOFT' 30, 'WONK' 1, 'opsz' 144;
    font-weight: 400;
    letter-spacing: -0.032em;
    max-width: 17ch;
  }

  .hero__lead {
    margin-top: clamp(1.5rem, 3vw, 2.2rem);
    max-width: 46rem;
    font-size: var(--step-1);
    line-height: 1.55;
    color: var(--ink-soft);
  }

  .hero__actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    margin-top: clamp(1.8rem, 3.5vw, 2.6rem);
  }

  /* La carte d'identité du document : version, édition, auteur, licence. */
  .hero__identity {
    margin-top: clamp(1.8rem, 3.5vw, 2.6rem);
    padding-top: 1.2rem;
    border-top: 1px solid var(--rule);
    font-family: var(--font-mono);
    font-size: 0.72rem;
    letter-spacing: 0.05em;
    color: var(--ink-faint);
  }

  .credit-line {
    margin-top: 0.55rem;
    text-align: right;
    font-family: var(--font-mono);
    font-size: 0.64rem;
    letter-spacing: 0.08em;
    color: var(--ink-faint);
  }
  .credit-line a { color: inherit; text-decoration: none; }
  .credit-line a:hover { color: var(--accent); text-decoration: underline; }

  /* --- En-têtes de section --------------------------------------------------- */

  /* Le numéro d'étape rend la progression visible sans quitter le registre
     documentaire : c'est la même convention que les principes P1–P7. */
  .step {
    display: inline-block;
    margin-right: 0.6rem;
    padding-right: 0.6rem;
    border-right: 1px solid var(--accent-edge);
    font-weight: 700;
  }

  .section__lead { margin: 0.9rem 0 clamp(1.8rem, 4vw, 2.6rem); max-width: 46rem; }

  .block { margin-top: clamp(2.6rem, 6vw, 4rem); }
  .block__lead {
    margin: 0.7rem 0 clamp(1.4rem, 3vw, 2rem);
    max-width: 46rem;
    font-size: 1rem;
    line-height: 1.6;
    color: var(--ink-soft);
  }
  .block__cta { margin-top: 2.2rem; }

  /* --- 01 · L'objet ----------------------------------------------------------- */

  .verbs__label {
    font-family: var(--font-mono);
    font-size: 0.66rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--ink-faint);
  }

  /* Les six verbes étaient noyés dans une phrase de quarante mots. Dépliés,
     ils se lisent d'un coup d'œil : c'est tout le gain de la section. */
  .verbs {
    display: flex;
    flex-wrap: wrap;
    gap: 0.6rem;
    list-style: none;
    margin-top: 0.9rem;
  }
  .verb {
    padding: 0.5rem 0.95rem;
    border: 1px solid var(--accent-edge);
    border-radius: var(--radius);
    background: var(--accent-wash);
    font-family: var(--font-display);
    font-variation-settings: 'SOFT' 30, 'WONK' 1, 'opsz' 20;
    font-size: 1.02rem;
    letter-spacing: -0.01em;
    color: var(--ink);
  }

  .object__note {
    margin-top: clamp(1.8rem, 4vw, 2.6rem);
    padding-left: 1.3rem;
    border-left: 3px solid var(--accent);
    font-size: 0.95rem;
    line-height: 1.6;
    color: var(--ink-soft);
    max-width: 46rem;
  }

  /* --- 02 · L'architecture ---------------------------------------------------- */

  /* Chaque nombre porte son unité et son explication : un chiffre expliqué
     vaut mieux que cinq chiffres alignés. */
  .tally {
    display: grid;
    gap: 1px;
    grid-template-columns: repeat(auto-fit, minmax(13rem, 1fr));
    list-style: none;
    background: var(--rule);
    border: 1px solid var(--rule);
    border-radius: var(--radius);
    overflow: hidden;
  }
  .tally__item {
    background: var(--paper-raised);
    padding: 1.4rem 1.4rem 1.6rem;
  }
  .tally__value {
    font-family: var(--font-display);
    font-variation-settings: 'SOFT' 30, 'WONK' 1, 'opsz' 60;
    font-size: 2.4rem;
    line-height: 1;
    letter-spacing: -0.03em;
    color: var(--accent);
  }
  .tally__unit {
    margin-top: 0.4rem;
    font-family: var(--font-mono);
    font-size: 0.68rem;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    color: var(--ink-faint);
  }
  .tally__body {
    margin-top: 0.8rem;
    padding-top: 0.8rem;
    border-top: 1px solid var(--rule);
    font-size: 0.88rem;
    line-height: 1.55;
    color: var(--ink-soft);
  }

  .rule-gold {
    margin-top: 1.6rem;
    padding: 1.05rem 1.3rem;
    border-left: 3px solid var(--accent);
    background: var(--accent-wash);
    font-size: 0.92rem;
    line-height: 1.6;
    color: var(--ink-soft);
    max-width: 54rem;
  }

  /* --- 03 · Une entrée -------------------------------------------------------- */

  .sample {
    display: grid;
    gap: clamp(1.6rem, 4vw, 2.6rem);
    align-items: start;
  }
  @media (min-width: 64rem) {
    .sample { grid-template-columns: minmax(0, 1.9fr) minmax(0, 1fr); }
  }

  .notes__label {
    font-family: var(--font-mono);
    font-size: 0.66rem;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--ink-faint);
  }
  .notes__list { margin: 1rem 0 0; display: grid; gap: 1.2rem; }
  .note__term {
    font-family: var(--font-display);
    font-variation-settings: 'SOFT' 20, 'WONK' 1, 'opsz' 20;
    font-size: 1.02rem;
    font-weight: 600;
    letter-spacing: -0.012em;
    color: var(--accent);
  }
  .note__body {
    margin: 0.35rem 0 0;
    font-size: 0.88rem;
    line-height: 1.6;
    color: var(--ink-soft);
  }

  /* --- 04 · Portée et limites ------------------------------------------------- */

  .pairs {
    display: grid;
    gap: 1px;
    grid-template-columns: repeat(auto-fit, minmax(16rem, 1fr));
    list-style: none;
    background: var(--rule);
    border: 1px solid var(--rule);
    border-radius: var(--radius);
    overflow: hidden;
  }
  .pair {
    background: var(--paper-raised);
    padding: 1.6rem 1.5rem 1.8rem;
  }
  .pair__is {
    font-family: var(--font-display);
    font-variation-settings: 'SOFT' 20, 'WONK' 1, 'opsz' 24;
    font-size: 1.16rem;
    font-weight: 600;
    line-height: 1.25;
    letter-spacing: -0.012em;
    color: var(--accent);
    text-wrap: balance;
  }
  .pair__isnot {
    display: flex;
    align-items: baseline;
    gap: 0.45rem;
    margin-top: 0.55rem;
    font-size: 0.86rem;
    color: var(--ink-faint);
  }
  .pair__isnot::before {
    content: '';
    flex: none;
    width: 0.85rem;
    height: 1px;
    background: var(--ink-faint);
    transform: translateY(-0.28em);
  }
  .pair__body {
    margin-top: 1rem;
    padding-top: 1rem;
    border-top: 1px solid var(--rule);
    font-size: 0.9rem;
    line-height: 1.6;
    color: var(--ink-soft);
  }

  /* --- Pourquoi ce cadre ------------------------------------------------------ */

  .why__title { max-width: 20ch; }

  .chain {
    display: grid;
    gap: clamp(2rem, 5vw, 4rem);
    align-items: start;
    margin-top: clamp(2.2rem, 5vw, 3.5rem);
  }
  @media (min-width: 60rem) {
    .chain { grid-template-columns: 1fr 1.35fr; }
  }

  .curve {
    margin: 0;
    border: 1px solid var(--rule);
    border-radius: var(--radius);
    background: var(--paper-raised);
    overflow: hidden;
  }
  .curve__caption {
    padding: 0.9rem 1.3rem;
    border-bottom: 1px solid var(--rule);
    font-family: var(--font-mono);
    font-size: 0.68rem;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    color: var(--ink-faint);
  }
  .curve__stages {
    display: grid;
    gap: 1px;
    background: var(--rule);
    list-style: none;
  }
  @media (min-width: 46rem) {
    .curve__stages { grid-template-columns: repeat(3, 1fr); }
  }

  .stage {
    background: var(--paper-raised);
    padding: 1.3rem 1.25rem 1.5rem;
    display: grid;
    align-content: start;
    gap: 0.3rem;
  }
  .stage__bar {
    height: 4.5rem;
    display: flex;
    align-items: flex-end;
    margin-bottom: 1rem;
    border-bottom: 1px solid var(--rule);
  }
  .stage__fill {
    display: block;
    width: 100%;
    border-radius: 2px 2px 0 0;
    background: var(--accent);
  }
  .stage[data-value='high'] .stage__fill { height: 100%; }
  .stage[data-value='low'] .stage__fill {
    height: 22%;
    background: var(--rule-strong);
  }

  .stage__label {
    font-family: var(--font-mono);
    font-size: 0.65rem;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    color: var(--ink-faint);
  }
  .stage__name {
    font-family: var(--font-display);
    font-variation-settings: 'SOFT' 30, 'WONK' 1, 'opsz' 30;
    font-size: 1.3rem;
    font-weight: 500;
    letter-spacing: -0.015em;
  }
  .stage[data-value='low'] .stage__name { color: var(--ink-faint); }
  .stage__body {
    margin-top: 0.3rem;
    font-size: 0.875rem;
    line-height: 1.55;
    color: var(--ink-soft);
  }
  .stage__rubrics {
    margin-top: 0.75rem;
    padding-top: 0.7rem;
    border-top: 1px solid var(--rule);
    font-family: var(--font-mono);
    font-size: 0.66rem;
    letter-spacing: 0.05em;
    color: var(--ink-faint);
  }

  /* --- Usages ------------------------------------------------------------------ */

  .audiences {
    display: grid;
    gap: 1px;
    grid-template-columns: repeat(auto-fit, minmax(15rem, 1fr));
    list-style: none;
    margin-top: clamp(1.8rem, 4vw, 2.8rem);
    background: var(--rule);
    border-top: 1px solid var(--rule);
    border-bottom: 1px solid var(--rule);
  }
  .audience {
    background: var(--paper-sunken);
    padding: 1.6rem 1.4rem 1.8rem;
  }
  .audience__index {
    font-family: var(--font-mono);
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.1em;
    color: var(--accent);
  }
  .audience__name {
    margin-top: 0.5rem;
    font-size: 1.22rem;
    letter-spacing: -0.012em;
  }
  .audience__body {
    margin-top: 0.6rem;
    font-size: 0.9rem;
    line-height: 1.6;
    color: var(--ink-soft);
  }
  .audiences__cta { margin-top: 2rem; }

  /* --- Citer et réutiliser ------------------------------------------------------ */

  .closing__inner {
    max-width: 46rem;
    text-align: center;
    margin-inline: auto;
  }
  .closing__body {
    margin-top: 1.1rem;
    font-size: var(--step-1);
    line-height: 1.55;
    color: var(--ink-soft);
  }
  .closing__actions {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    justify-content: center;
    margin-top: 2rem;
  }
</style>
```

- [ ] **Étape 2 : construire**

```bash
cd "/Users/maximehebert/CreaComp Site" && npx astro check && npm run build
```

Attendu : `0 errors`, puis `Complete!`.

Si `astro check` signale une erreur de type sur `home.toc.items`, c'est que les
sept objets du tableau ne portent pas tous la clé `num` : reprendre l'étape 1 de
la tâche 1 et ajouter `"num": ""` aux entrées non numérotées.

- [ ] **Étape 3 : vérifier que les ancres du sommaire pointent sur quelque chose**

Chaque `href` du sommaire doit correspondre à un `id` présent dans la page
construite. Le contrôle est mécanique, il n'y a pas de raison de le faire à l'œil :

```bash
cd "/Users/maximehebert/CreaComp Site" && python3 - <<'PY'
import re, sys
ok = True
for page, label in (('dist/index.html', 'fr'), ('dist/en/index.html', 'en')):
    html = open(page, encoding='utf-8').read()
    ids = set(re.findall(r'\sid="([^"]+)"', html))
    nav = re.search(r'<nav class="toc".*?</nav>', html, re.S)
    if not nav:
        print(f'{label} : sommaire absent'); ok = False; continue
    anchors = re.findall(r'href="#([^"]+)"', nav.group(0))
    missing = [a for a in anchors if a not in ids]
    print(f'{label} : {len(anchors)} ancres, manquantes = {missing}')
    if missing or len(anchors) != 7:
        ok = False
print('OK' if ok else 'ÉCHEC')
PY
```

Attendu : `fr : 7 ancres, manquantes = []`, `en : 7 ancres, manquantes = []`, `OK`.

- [ ] **Étape 4 : vérifier que le spécimen est bien rendu dans les deux langues**

```bash
cd "/Users/maximehebert/CreaComp Site" && grep -c "specimen__descriptor" dist/index.html dist/en/index.html && grep -o "Est capable d'expliquer pourquoi un contenu peut être faux[^<]*" dist/index.html && grep -o "Is able to train others in information assessment[^<]*" dist/en/index.html
```

Attendu : `dist/index.html:1`, `dist/en/index.html:1`, puis les deux descripteurs
affichés en clair. C'est la preuve que le spécimen lit bien `framework.json` dans
chaque langue, et non un texte recopié.

- [ ] **Étape 5 : vérifier qu'aucun style en ligne n'a été introduit**

La politique de sécurité du contenu du site fonctionne par empreintes : un seul
attribut `style=` rendrait la page inutilisable en production.

```bash
cd "/Users/maximehebert/CreaComp Site" && grep -c 'style="' dist/index.html dist/en/index.html
```

Attendu : `0` pour les deux fichiers. (`grep -c` renvoie un code de sortie 1
quand il ne trouve rien : c'est le résultat souhaité ici.)

- [ ] **Étape 6 : commit**

```bash
cd "/Users/maximehebert/CreaComp Site" && git add src/views/Home.astro && git commit -m "Réécrit la page d'accueil en parcours guidé

La page introduit le référentiel au lieu de le résumer : sommaire, puis
l'objet, l'architecture, une entrée en fac-similé, la portée et les
limites. Les compteurs quittent l'en-tête pour l'architecture, où chaque
nombre est expliqué ; la balance attention-intention sort, elle vit sur
la page « Le cadre »."
```

---

## Tâche 5 : le nettoyage des données orphelines

**Fichiers :**
- Modifier : `src/data/fr/site.json`
- Modifier : `src/data/en/site.json`

La tâche 1 a laissé les anciennes clés en place pour que la page continue de
construire. Elles ne servent plus à rien depuis la tâche 4.

**Attention :** `s.counts` reste employé par `src/components/Footer.astro:55`.
Cette clé **ne doit pas** être retirée.

- [ ] **Étape 1 : lister ce qui n'est plus lu**

```bash
cd "/Users/maximehebert/CreaComp Site" && for k in hero.eyebrow warning map levels audiences closing why object architecture specimen scope toc; do printf '%-22s %s\n' "$k" "$(grep -ro "home\.${k%%.*}" src --include='*.astro' | wc -l | tr -d ' ')"; done
```

Attendu : `warning`, `map` et `levels` renvoient `0` — plus aucun composant ne les
lit. Toutes les autres renvoient au moins `1`.

- [ ] **Étape 2 : retirer les clés orphelines des deux fichiers**

Dans `src/data/fr/site.json` **et** `src/data/en/site.json`, supprimer de l'objet
`home` les trois clés devenues inutiles :

- `home.warning` — son contenu vit désormais dans `home.scope`
- `home.map` — ses intitulés vivent dans `home.architecture.mapTitle` / `mapLead` / `cta`
- `home.levels` — ses intitulés vivent dans `home.architecture.levelsTitle` / `levelsLead` / `goldenRule`

Ne rien retirer d'autre. En particulier, `counts`, `ui`, `levels` **à la racine**
(le tableau des quatre niveaux) et `meta` sont tous encore lus.

- [ ] **Étape 3 : revérifier la parité des deux langues**

```bash
cd "/Users/maximehebert/CreaComp Site" && python3 - <<'PY'
import json
def shape(o, p=''):
    if isinstance(o, dict):
        out = set()
        for k, v in o.items():
            out.add(p + '/' + k)
            out |= shape(v, p + '/' + k)
        return out
    if isinstance(o, list) and o:
        return shape(o[0], p + '[]')
    return set()
fr = json.load(open('src/data/fr/site.json'))['home']
en = json.load(open('src/data/en/site.json'))['home']
a, b = shape(fr), shape(en)
print('FR seul :', sorted(a - b))
print('EN seul :', sorted(b - a))
print('clés de premier niveau :', sorted(fr))
print('OK' if a == b else 'DIVERGENCE')
PY
```

Attendu : aucune divergence, et `clés de premier niveau : ['architecture',
'audiences', 'closing', 'hero', 'object', 'scope', 'specimen', 'toc', 'why']`.

- [ ] **Étape 4 : construire**

```bash
cd "/Users/maximehebert/CreaComp Site" && npx astro check && npm run build
```

Attendu : `0 errors`, puis `Complete!`.

- [ ] **Étape 5 : commit**

```bash
cd "/Users/maximehebert/CreaComp Site" && git add src/data/fr/site.json src/data/en/site.json && git commit -m "Retire les clés d'accueil devenues orphelines

warning, map et levels ne sont plus lus depuis la réécriture de la page.
counts reste : le pied de page s'en sert encore."
```

---

## Tâche 6 : la vérification de rendu

Aucun fichier modifié. Cette tâche constate ce que la construction ne peut pas
constater. Elle se déroule dans le navigateur intégré, jamais en demandant à
l'auteur de regarder à notre place.

- [ ] **Étape 1 : démarrer le serveur de développement**

Utiliser l'outil `preview_start` avec `{ "name": "creacomp" }` — jamais `npm run
dev` dans un terminal.

- [ ] **Étape 2 : contrôler la page française**

Naviguer sur `http://localhost:4321/`, puis lire la page avec `read_page`.

Vérifier point par point :

- l'en-tête ne contient plus la liste des cinq compteurs ;
- l'en-tête ne contient plus le surtitre « CréaComp 1.0 — édition 2026 » **au-dessus** du titre, et porte bien la ligne d'identité « CréaComp 1.0 — édition 2026 · Maxime Hébert · CC BY-SA 4.0 » **sous les boutons** ;
- le sommaire liste sept entrées, dont quatre numérotées 01 à 04 ;
- les six verbes apparaissent comme six éléments distincts, non comme une phrase ;
- le spécimen affiche le code `1.2`, la rubrique en toutes lettres, et deux niveaux : `N1 Découverte` et `N4 Expertise` ;
- les trois annotations sont présentes ;
- la section « Portée et limites » se trouve **après** le spécimen, jamais avant ;
- la balance « Économie de l'attention / Économie de l'intention » a bien disparu.

- [ ] **Étape 3 : vérifier que les ancres fonctionnent réellement**

Cliquer successivement sur les sept liens du sommaire avec `computer`, et vérifier
après chacun que la position de défilement a changé :

```js
window.scrollY
```

Attendu : une valeur strictement croissante d'un lien au suivant, et non `0`.

- [ ] **Étape 4 : contrôler la console**

Utiliser `read_console_messages` avec `onlyErrors: true`.

Attendu : aucun message. Une erreur ici signale le plus souvent une image ou une
police manquante.

- [ ] **Étape 5 : contrôler la page anglaise**

Naviguer sur `http://localhost:4321/en/` et refaire l'étape 2 avec les intitulés
anglais : ligne d'identité `CréaComp 1.0 — 2026 edition · Maxime Hébert · CC
BY-SA 4.0`, spécimen `1.2 / GATHER`, niveaux `N1 Discovery` et `N4 Expertise`,
sommaire de sept entrées.

- [ ] **Étape 6 : contrôler le thème sombre**

`resize_window` avec `{ "preset": "desktop", "colorScheme": "dark" }`, recharger,
puis prendre une capture.

Vérifier que le spécimen, la grille des nombres et les six verbes restent lisibles :
le fond `--accent-wash` et la bordure `--accent-edge` sont calculés par
`color-mix` à partir de `--accent`, qui change de valeur en thème sombre. C'est
l'endroit le plus susceptible de manquer de contraste.

- [ ] **Étape 7 : contrôler la largeur mobile**

`resize_window` avec `{ "preset": "mobile" }`, recharger, puis prendre une capture.

Vérifier que le sommaire passe en pile sans déborder, que les deux niveaux du
spécimen s'empilent l'un sous l'autre, et qu'**aucun défilement horizontal** n'est
possible :

```js
document.documentElement.scrollWidth <= window.innerWidth
```

Attendu : `true`.

- [ ] **Étape 8 : livrer les captures**

Transmettre à l'auteur la capture claire, la capture sombre et la capture mobile
de la page française, avec la liste de ce qui a été vérifié. Ne pas lui demander
de contrôler quoi que ce soit qui aurait pu l'être ici.

---

## Auto-relecture du plan

**Couverture de la spécification.** Chaque section de la spec est portée par une
tâche : § 4.1 en-tête → tâches 1 et 4 ; § 4.2 sommaire → tâches 1, 3, 4 ; § 4.3
à § 4.8 → tâches 1 et 4 ; § 5 spécimen → tâches 1, 2, 4 ; § 6 fichiers → toutes ;
§ 7 contraintes → tâche 4 étape 5 (aucun style en ligne), tâche 1 étape 3 et
tâche 5 étape 3 (parité des langues), tâche 6 étape 6 (rien ne dépend de la seule
couleur, contrôlé en thème sombre). Le détail d'exactitude « 31 compétences →
31 entrées » relevé au § 4.1 est traité en tâche 1, dans `hero.primaryCta`.

**Absence de fantômes.** Aucun `TODO`, aucun « à compléter », aucune étape qui
décrive une intention sans montrer le code. Les deux composants et la page sont
donnés en entier.

**Cohérence des noms.** `home.object`, `home.architecture`, `home.specimen`,
`home.scope`, `home.why`, `home.audiences`, `home.closing`, `home.toc` : mêmes
clés en tâche 1 et en tâche 4. Les props `Specimen({ lang, code, levels })` et
`PageToc({ label, items })` sont déclarées en tâches 2 et 3 et appelées à
l'identique en tâche 4. Les classes CSS employées dans `Home.astro` — `.step`,
`.verbs`, `.tally`, `.sample`, `.notes`, `.pairs` — sont toutes définies dans le
bloc `<style>` du même fichier.

**Périmètre.** Cinq fichiers, deux créés, trois modifiés. Aucune autre page
touchée. Tenable en un seul plan.
