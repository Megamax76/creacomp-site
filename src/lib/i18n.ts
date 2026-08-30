import frSite from '../data/fr/site.json';
import enSite from '../data/en/site.json';
import frFramework from '../data/fr/framework.json';
import enFramework from '../data/en/framework.json';

export type Lang = 'fr' | 'en';
export type PageKey =
  | 'home'
  | 'framework'
  | 'foundations'
  | 'positioning'
  | 'use'
  | 'contact';

export const langs: Lang[] = ['fr', 'en'];

const sites = { fr: frSite, en: enSite } as const;
const frameworks = { fr: frFramework, en: enFramework } as const;

export type Site = (typeof sites)['fr'];
export type Framework = (typeof frameworks)['fr'];
export type Rubric = Framework['rubrics'][number];
export type Level = Site['levels'][number];

/** Une entrée du référentiel : compétence ou fil transversal, forme identique. */
export type Entry = {
  code: string;
  slug: string;
  title: string;
  subtitle?: string;
  definition: string;
  components: string[];
  levels: Record<string, { descriptor: string; evidence: string }>;
  rubricId?: number;
};

export const site = (lang: Lang): Site => sites[lang];
export const framework = (lang: Lang): Framework => frameworks[lang];

export const other = (lang: Lang): Lang => (lang === 'fr' ? 'en' : 'fr');

/** Préfixe de langue : le français occupe la racine, l'anglais vit sous /en. */
const prefix = (lang: Lang) => (lang === 'fr' ? '' : '/en');

/** Chemin d'une page principale, avec barre oblique finale. */
export function path(lang: Lang, page: PageKey): string {
  const segment = sites[lang].routes[page];
  return `${prefix(lang)}/${segment ? segment + '/' : ''}`;
}

/** Chemin d'une entrée du référentiel, à partir de son slug localisé. */
export function entryPath(lang: Lang, slug: string): string {
  return `${path(lang, 'framework')}${slug}/`;
}

/** Toutes les entrées, compétences puis fils, dans l'ordre du référentiel. */
export function entries(lang: Lang): Entry[] {
  const data = frameworks[lang];
  return [...data.competences, ...data.threads] as Entry[];
}

export function entryByCode(lang: Lang, code: string): Entry | undefined {
  return entries(lang).find((entry) => entry.code === code);
}

export function rubricById(lang: Lang, id: number): Rubric | undefined {
  return frameworks[lang].rubrics.find((rubric) => rubric.id === id);
}

/** Les quatre compétences d'une rubrique, dans l'ordre de leur code. */
export function competencesOf(lang: Lang, rubricId: number): Entry[] {
  return frameworks[lang].competences.filter(
    (competence) => competence.rubricId === rubricId,
  ) as Entry[];
}

/**
 * Chemin équivalent dans l'autre langue. Le code de la compétence est la clé
 * stable entre les deux versions : les slugs, eux, sont traduits. Le sélecteur
 * de langue mène donc toujours à la page correspondante, jamais à l'accueil.
 */
export function alternatePath(lang: Lang, page: PageKey, code?: string): string {
  const target = other(lang);
  if (page !== 'framework' || !code) return path(target, page);
  const twin = entryByCode(target, code);
  return twin ? entryPath(target, twin.slug) : path(target, 'framework');
}

/** Couleur d'accent : celle de la rubrique, ou le graphite des fils transversaux. */
export function accentOf(lang: Lang, entry: Entry): string {
  if (entry.rubricId === undefined) return 'graphite';
  return rubricById(lang, entry.rubricId)?.color ?? 'graphite';
}

/** Référence prête à copier pour une entrée donnée. */
export function citationOf(lang: Lang, entry: Entry): string {
  const meta = sites[lang].meta;
  const label = lang === 'fr' ? 'compétence' : 'competency';
  return `Hébert, M. (${meta.edition}). ${meta.name} ${meta.version} — ${meta.subtitle}, ${label} ${entry.code} « ${entry.title} ». ${meta.license}.`;
}
