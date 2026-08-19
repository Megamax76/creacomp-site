# Signature de courriel CreaComp

Quatre fichiers, et rien à installer :

| Fichier | Ce que c'est |
|---|---|
| `signature-fr.html` | Le bloc à coller, en français. Le cas courant. |
| `signature-en.html` | Le même, en anglais. |
| `signature.txt` | Repli en texte brut, pour les messages sans mise en forme. |
| `signature-marque.png` | La marque, 168 px. Copie de `public/signature-marque.png`. |
| `apercu.html` | Page de contrôle : les deux signatures, fond clair et fond sombre. |

---

## Ce qu'il faut changer avant de s'en servir

Trois endroits, pas davantage.

1. **La fonction**, ligne 2 du bloc — « Auteur et mainteneur du référentiel
   CreaComp ». C'est la formule que reprend le site (« conçu et maintenu par
   Maxime Hébert ») ; une autre fait l'affaire, à condition de tenir sur une
   ligne.
2. **Le téléphone**, facultatif : un motif commenté attend dans la ligne de
   contact. Le décommenter et remplacer le numéro suffit.
3. **Rien d'autre.** L'adresse est `contact@creacomp.org`, l'adresse de fonction
   déjà publiée sur le site — jamais l'adresse personnelle. C'est la raison
   d'être de la redirection décrite dans `site.config.mjs`.

---

## L'image

Le bloc pointe vers `https://creacomp.org/signature-marque.png`, servi depuis
`public/`. **Elle ne s'affichera qu'une fois le site en ligne** ; d'ici là le
destinataire verra le texte de remplacement « CreaComp ». Le reste de la
signature — le nom, les liens, le filet de six couleurs — ne dépend d'aucune
image et s'affiche partout, y compris chez les gens qui bloquent les images
distantes, ce que font beaucoup de messageries d'entreprise.

Pour la refabriquer après un changement de logo :

```bash
node scripts/logo/rasteriser.mjs   # régénère brand/
```

puis réexporter `creacomp-marque.svg` en 168 px vers `public/signature-marque.png`.

---

## Installation

**Gmail** — ouvrir `apercu.html` dans un navigateur, sélectionner la signature
d'un bord à l'autre, copier. Puis Paramètres → Général → Signature → coller.
Gmail conserve les styles en ligne ; ne pas coller le code source, il
l'afficherait tel quel.

**Apple Mail** — Réglages → Signatures, créer une signature vide, puis y coller
la sélection faite depuis `apercu.html`. Décocher « Toujours utiliser ma police
par défaut », sans quoi Mail écrase les polices du bloc.

**Outlook (web et bureau)** — même méthode : copier depuis le navigateur, coller
dans Fichier → Options → Courrier → Signatures. Outlook pour Windows rend le
HTML avec le moteur de Word : c'est pour lui que le bloc est en tableaux et non
en `flex`, et que les couleurs sont écrites en hexadécimal.

**Thunderbird** — Paramètres du compte → cocher « Utiliser HTML », puis coller
le contenu de `signature-fr.html` dans le champ, ou pointer le fichier
directement.

---

## Deux réserves, dites d'avance

**Le thème sombre.** Les messageries en thème sombre inversent le fond sans
prévenir. Le nom et le texte, écrits en `#1A1814` sur fond transparent, sont
alors ré-éclaircis par le client dans la plupart des cas ; la marque, elle, ne
change pas, et son C pétrole `#1B5068` perd du contraste sur fond très sombre.
Il n'existe pas de correctif portable : `prefers-color-scheme` n'est honoré ni
par Gmail ni par Outlook. La variante sombre `creacomp-marque-sombre.svg` existe
si l'usage réel se révèle majoritairement sombre.

**Les polices.** Fraunces, Archivo et JetBrains Mono ne se chargent pas dans un
courriel. Le bloc emploie les replis déclarés par le design system — Iowan Old
Style puis Georgia pour le nom, Helvetica puis Arial pour le texte, SF Mono puis
Consolas pour la ligne de licence. La signature reste de la même famille que le
site sans lui être identique ; c'est le maximum atteignable ici.
