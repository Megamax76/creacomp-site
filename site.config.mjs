/**
 * Réglages de déploiement du site CréaComp — le seul fichier à modifier
 * pour mettre le site en ligne. Il est lu à la fois par la configuration
 * d'Astro (URL canonique, plan du site, politique de sécurité) et par les
 * pages (formulaire de contact).
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
 * Adresse affichée sur la page Contact, et destination du formulaire.
 *
 * Elle est publiée en clair sur une page publique : elle sera moissonnée par
 * des robots et recevra du courrier indésirable. C'est donc une adresse de
 * fonction sur le domaine du site, redirigée vers la boîte personnelle de
 * l'auteur : elle peut être filtrée, mise en quarantaine ou remplacée sans
 * jamais exposer l'adresse privée, et sans toucher au site.
 *
 * La redirection se règle chez le bureau d'enregistrement du domaine ; aucune
 * trace n'en subsiste ici. Ne jamais remettre d'adresse personnelle à sa place.
 */
export const contactEmail = 'contact@creacomp.org';

/**
 * Clé d'accès Web3Forms (https://web3forms.com), le relais qui transforme
 * l'envoi du formulaire en courrier électronique. Un site statique n'a pas
 * de serveur : sans relais, un formulaire ne peut arriver nulle part.
 *
 * Pour l'obtenir : entrer `contactEmail` ci-dessus sur web3forms.com, valider,
 * et relever la clé reçue par courrier à cette même adresse. Aucun compte,
 * aucun mot de passe. Coller la clé ci-dessous.
 *
 * Cette clé est publique par construction : elle voyage dans le HTML de la
 * page, et ne donne rien d'autre que le droit d'écrire à `contactEmail`.
 * Elle ne relaie que vers cette adresse, jamais vers une autre. La révoquer
 * ou la remplacer se fait depuis le courriel d'activation de Web3Forms.
 *
 * Tant que la valeur est vide, le formulaire reste affiché mais bascule en
 * mode dégradé : le bouton prépare le message dans le logiciel de messagerie
 * du visiteur au lieu de l'envoyer. La page n'est jamais une impasse.
 */
export const web3formsKey = '6a466224-46c8-4419-8832-ffce68648103';
