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
 * Adresse affichée sur la page Contact.
 *
 * Elle est publiée en clair sur une page publique : elle sera moissonnée par
 * des robots et recevra du courrier indésirable. Préférez donc une adresse de
 * fonction sur votre propre domaine — `contact@creacomp.org` — redirigée vers
 * votre boîte personnelle : vous pourrez la filtrer ou la remplacer sans jamais
 * exposer votre adresse privée, et sans toucher au site.
 */
export const contactEmail = 'maxime.hebert76@gmail.com';

/**
 * Identifiant du formulaire Formspree (https://formspree.io).
 * Créez un formulaire gratuit, copiez l'identifiant affiché dans son URL
 * (https://formspree.io/f/XXXXXXXX → « XXXXXXXX ») et collez-le ci-dessous.
 *
 * Tant que la valeur est vide, la page Contact affiche l'adresse e-mail
 * directe à la place du formulaire : le site reste utilisable en l'état.
 */
export const formspreeId = '';
