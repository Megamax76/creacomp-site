/**
 * Réglages de déploiement du site CréaComp — le seul fichier à modifier
 * pour mettre le site en ligne. Il est lu à la fois par la configuration
 * d'Astro (URL canonique, plan du site) et par les pages (formulaire).
 */

/**
 * URL canonique du site, une fois le nom de domaine arrêté.
 * Exemple : 'https://creacomp.org' — sans barre oblique finale.
 *
 * Tant que la valeur est vide, le site se construit avec des chemins relatifs
 * et se déploie n'importe où ; le plan du site (sitemap.xml) et les URL
 * canoniques n'apparaissent qu'une fois cette adresse renseignée.
 */
export const siteUrl = 'https://creacomp.org';

/**
 * Identifiant du formulaire Formspree (https://formspree.io).
 * Créez un formulaire gratuit, copiez l'identifiant affiché dans son URL
 * (https://formspree.io/f/XXXXXXXX → « XXXXXXXX ») et collez-le ci-dessous.
 *
 * Tant que la valeur est vide, la page Contact affiche l'adresse e-mail
 * directe à la place du formulaire : le site reste utilisable en l'état.
 */
export const formspreeId = '';
