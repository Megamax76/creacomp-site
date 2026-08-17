<!--
Merci de contribuer. Ce gabarit sert à ce que la relecture aille droit au but.
Supprimez les sections qui ne s'appliquent pas — un correctif de coquille n'a
pas besoin de tout remplir.
-->

## Ce que ça change

<!-- En deux phrases. Le pourquoi compte plus que le quoi : le diff dit déjà le quoi. -->

## Nature

- [ ] Contenu du référentiel (descripteurs, définitions, composantes)
- [ ] Traduction
- [ ] Textes éditoriaux du site
- [ ] Code du site (composants, styles, mise en page)
- [ ] Outillage, configuration, documentation

Issue liée : <!-- #123, ou « aucune » -->

## Vérifications

<!-- Rien de tout cela n'est automatisé hors construction : merci de l'avoir fait tourner. -->

- [ ] `npx astro check` — 0 erreur
- [ ] `npm run build` — 73 pages, aucun avertissement
- [ ] `npm audit` — 0 vulnérabilité
- [ ] `npm run preview`, puis site ouvert et **console vide au chargement**

## Si vous avez touché au contenu du référentiel

- [ ] Les champs `code` sont inchangés — ou modifiés **dans les deux langues**
- [ ] Les descripteurs restent **observables** (« Est capable de… »), pas des
      énoncés d'intention

## Si vous avez touché au rendu

- [ ] **Aucun attribut `style=` en ligne** — la politique de sécurité du contenu
      les bloque en silence, sans casser la construction
- [ ] Vérifié en thème **clair et sombre**
- [ ] Navigation clavier intacte

## Captures

<!-- Pour tout changement visible. Avant / après si possible. -->
