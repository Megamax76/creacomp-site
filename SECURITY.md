# Sécurité

## Signaler une faille

**N'ouvrez pas d'issue publique pour une faille de sécurité.**

Écrivez à **maxime.hebert76@gmail.com** avec, si possible : ce que vous avez
observé, comment le reproduire, et ce qu'un attaquant pourrait en tirer.
Vous recevrez un accusé de réception sous quelques jours.

GitHub permet aussi le
[signalement privé](https://github.com/Megamax76/creacomp-site/security/advisories/new),
qui est le canal à préférer si vous avez un compte.

Ce projet n'a ni programme de prime, ni budget : les signalements sont traités
par une seule personne, sur son temps. Les correctifs sont publiés dès qu'ils
sont prêts, et les contributeurs sont crédités s'ils le souhaitent.

## Versions concernées

Seule la version en ligne sur [creacomp.org](https://creacomp.org), construite
depuis `main`, est maintenue. Il n'y a pas de branches de support.

## Le modèle de menace, en clair

Le site est **entièrement statique** : aucun serveur applicatif, aucune base de
données, aucune session, aucun cookie, aucun compte, aucune donnée saisie par un
visiteur — sauf, si le formulaire de contact est activé, ce qu'un visiteur y
écrit, qui part directement chez Formspree.

Les classes de failles habituelles — injection SQL, exécution de code à
distance, contournement d'authentification, élévation de privilèges — **n'ont
pas de prise** : il n'y a rien qui les exécuterait. La surface réelle se réduit
à deux choses : ce que le site charge chez le visiteur, et ce qui le construit.

### Ce que le site charge

- **Aucune requête vers un tiers.** Polices et photographies sont
  auto-hébergées. Le site n'embarque aucun script tiers, aucun traceur, aucune
  balise analytique, et ne pose aucun cookie. Vérifiable :
  `grep -roE 'src="https?://' dist/` ne renvoie rien.
- **Politique de sécurité du contenu à empreintes SHA-256**, générée à la
  construction par Astro et partant de `default-src 'none'`. Les scripts et
  feuilles de style sont autorisés par leur empreinte, jamais par
  `unsafe-inline` : un script injecté dans le HTML ne s'exécuterait pas.
- **`connect-src` et `form-action` restent à `'none'`** tant que `formspreeId`
  est vide dans `site.config.mjs`. Le renseigner ouvre la politique pour le seul
  domaine `formspree.io`, automatiquement.

### Ce qui construit le site

C'est là que se situe le risque réel d'un site statique — la chaîne
d'approvisionnement :

- **Actions épinglées à une empreinte de commit**, jamais à une étiquette : une
  étiquette comme `v5` peut être redirigée vers un autre code par qui publie
  l'action, une empreinte non.
- **`npm ci`**, qui installe exactement ce que décrit `package-lock.json` et
  refuse de s'en écarter.
- **Droits minimaux** : `contents: read` au niveau du workflow ; seul le job de
  publication reçoit `pages: write`. Le jeton n'est pas persisté pendant la
  construction (`persist-credentials: false`).
- **Dependabot** surveille npm et les actions ; **l'analyse de secrets** et la
  **protection à la poussée** sont actives sur le dépôt.

`npm audit` doit rester à **zéro vulnérabilité**. C'est la vérification à faire
avant de fusionner toute montée de version.

## Limites connues, assumées

**GitHub Pages n'admet aucun en-tête HTTP personnalisé.** Deux protections sont
donc hors d'atteinte tant que le site y est hébergé :

- **`frame-ancestors`** — les navigateurs l'ignorent dans une balise `<meta>`.
  Le site peut donc être encadré dans une iframe par un tiers. Pour un site de
  documentation sans connexion ni action à détourner, l'impact est négligeable :
  il n'y a aucun clic à détourner.
- **`X-Content-Type-Options: nosniff`** — indisponible pour la même raison.

Sur un hébergeur acceptant les en-têtes (Netlify, Cloudflare Pages), ajouter ces
deux en-têtes suffit à combler l'écart. Rien d'autre n'est à changer.

**L'adresse de contact est publiée en clair** sur la page Contact, et sera
moissonnée par des robots. C'est un choix assumé : une page de contact sans
adresse ne contacte personne. Elle est isolée dans `site.config.mjs` pour qu'une
adresse de fonction puisse s'y substituer en une ligne.

## Contrainte à connaître avant de contribuer

La politique de sécurité du contenu **interdit les attributs `style=` en
ligne** — et les bloque *silencieusement* : le style ne s'applique pas, mais la
construction réussit et rien ne signale l'erreur.

Passez par une classe ou un attribut de données ciblé en CSS. Après toute
modification visuelle, reconstruisez et vérifiez que la console du navigateur
est **vide** au chargement : c'est le seul signal fiable.
