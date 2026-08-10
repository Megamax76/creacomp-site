import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { siteUrl } from './site.config.mjs';

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
});
