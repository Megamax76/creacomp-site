import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { siteUrl, web3formsKey } from './site.config.mjs';

// Le site ne charge rien de l'extérieur : la politique de sécurité du contenu
// part donc de `default-src 'none'` et ne rouvre que le strict nécessaire.
// Astro y ajoute lui-même `script-src` et `style-src` avec les empreintes
// SHA-256 de ses scripts : aucun script étranger ne peut s'exécuter.
// Le formulaire de contact est le seul point où le site parle à l'extérieur,
// et seulement une fois Web3Forms configuré : la politique s'ouvre alors juste
// pour son relais, et reste close tant qu'il ne l'est pas. Sans clé, le
// formulaire bascule sur le logiciel de messagerie du visiteur, qui relève du
// navigateur et non d'une requête réseau : rien à autoriser de ce côté.
const relay = web3formsKey.trim() ? 'https://api.web3forms.com' : null;

// Tant qu'aucun nom de domaine n'est arrêté, le site se construit avec des
// chemins relatifs et se déploie n'importe où. Renseigner `siteUrl` dans
// site.config.mjs active les URL canoniques et le plan du site.
export default defineConfig({
  ...(siteUrl ? { site: siteUrl } : {}),
  trailingSlash: 'always',
  build: { format: 'directory' },
  compressHTML: true,
  integrations: siteUrl ? [sitemap({ i18n: { defaultLocale: 'fr', locales: { fr: 'fr-FR', en: 'en-GB' } } })] : [],
  i18n: {
    defaultLocale: 'fr',
    locales: ['fr', 'en'],
    routing: { prefixDefaultLocale: false },
  },
  security: {
    csp: {
      algorithm: 'SHA-256',
      directives: [
        "default-src 'none'",
        "img-src 'self'",
        // Astro intègre les sous-ensembles de polices en `data:` dans le CSS ;
        // sans cette autorisation, le site s'affiche en polices de substitution.
        "font-src 'self' data:",
        `connect-src ${relay ?? "'none'"}`,
        // Sans relais, `form-action 'self'` laisse l'envoi sans JavaScript
        // recharger la page plutôt que d'être bloqué net par la politique.
        `form-action ${relay ?? "'self'"}`,
        "base-uri 'none'",
        "object-src 'none'",
        // `frame-ancestors` est délibérément absent : les navigateurs
        // l'ignorent dans une balise <meta>, et GitHub Pages ne permet pas
        // d'en-têtes HTTP. La déclarer ne protégerait de rien et afficherait
        // une erreur à chaque visite. Sur un hébergeur acceptant les en-têtes,
        // ajouter `frame-ancestors 'none'` et `X-Content-Type-Options: nosniff`.
      ],
    },
  },
});
