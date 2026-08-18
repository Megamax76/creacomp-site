// Les réglages de déploiement vivent à la racine, dans site.config.mjs, afin
// d'être partagés avec astro.config.mjs. Ce module n'en est que le relais typé.
export { siteUrl, web3formsKey, contactEmail } from '../site.config.mjs';
