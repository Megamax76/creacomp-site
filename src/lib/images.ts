import type { ImageMetadata } from 'astro';
import credits from '../data/credits.json';

// Les images sont importées en bloc : leur clé est déterminée à l'exécution
// (« rubrique-3 », « fil-t2 »…), ce qu'un import statique ne permettrait pas.
const files = import.meta.glob<{ default: ImageMetadata }>('../assets/images/*.jpg', {
  eager: true,
});

export type Credit = (typeof credits)['items'][number];

export const creditSource = { name: credits.source, url: credits.sourceUrl };

export function image(key: string): ImageMetadata | undefined {
  return files[`../assets/images/${key}.jpg`]?.default;
}

export function credit(key: string): Credit | undefined {
  return credits.items.find((item) => item.key === key);
}

/** Tous les crédits, dans l'ordre d'apparition sur le site. */
export const allCredits = credits.items;
