# Version courte — 24 planches

Version resserrée de l'exposé (≈ 20 min) : **6 sections** au lieu de 11,
20 planches d'exposé, pas de planche de section, pas de planche de crédits en
back-up, bibliographie réduite.

PDF, dans ce dossier :

- `GRETSI2027_Segmentation_Semantique_Teledetection_SHORT.pdf` — les planches ;
- `GRETSI2027_Semantic_Segmentation_Remote_Sensing_SHORT.pdf` — les planches en
  anglais, dont les sources sont dans [`EN/`](EN/) ;
- `Notes_Orateur_Segmentation_Semantique_Teledetection_SHORT.pdf` — le support
  pour l'oral, version imprimable de [`notes-orateur.md`](notes-orateur.md) ;
- `Speaker_Notes_Semantic_Segmentation_Remote_Sensing_SHORT.pdf` — le même en
  anglais.

État d'origine : [`reference/`](reference/) conserve le PDF envoyé par Martina
Pastorino le 11 septembre 2026, dont ce `main.tex` a été reconstruit par
rétro-ingénierie — voir [« Rapport au PDF de référence »](#rapport-au-pdf-de-référence).

## Contenu du dossier

```
SHORT/
├── main.tex          la présentation (6 sections, 24 planches)
├── *.pdf             planches et supports pour l'oral, français et anglais
├── references.bib    54 entrées, revues et conférences abrégées
├── notes-orateur.md  support pour l'oral : ce qu'il y a à dire, planche par planche
├── reference/        le PDF envoyé par Martina, tel quel
├── EN/               la même présentation en anglais (voir EN/README.md)
├── imgs/article/     les 7 figures de l'article (jeu complet ; 6 sont utilisées ici)
├── imgs/logos/       logos Università di Genova
├── theme/            thème Beamer Inria 2024 (copie amont, non modifiée)
├── latexmkrc         TEXINPUTS → theme/, compilation pdfLaTeX
└── Makefile          `make` / `make clean`
```

Version anglaise : [`EN/`](EN/) — mêmes 24 planches, même thème, mêmes figures,
même numérotation bibliographique ; la citation cassée de la planche 9 y est
corrigée. Support pour l'oral : [`notes-orateur.md`](notes-orateur.md) en
français, [`EN/speaker-notes.md`](EN/speaker-notes.md) en anglais.

`make` produit `GRETSI2027_Segmentation_Semantique_Teledetection_SHORT.pdf`
(pdfLaTeX + biber). `make` depuis [`EN/`](EN/) dépose le PDF anglais dans ce
même dossier. Prérequis et remarques sur le moteur : voir le
[README du dossier parent](../README.md#compilation).

## Déroulé

| # | Planche | Figure |
|---|---|---|
| 1 | Page de titre | — |
| 2 | Sommaire (une colonne) | — |
| | **1. Introduction** | |
| 3 | De l'image à la carte thématique | Fig. 1 (a)(b) |
| 4 | Ce qui distingue la télédétection | — |
| 5 | Fil directeur (`I : Ω → R^d`, puis `f : Ω → C`) | frise |
| | **2. Du pixel au contexte** | |
| 6 | Les premières approches : pixel à pixel | — |
| 7 | Deux limites : dimension et indépendance | Fig. 2 (b) |
| 8 | Méthodes discriminantes et d'ensemble | — |
| 9 | L'apport du contexte spatial | Fig. 2 (a)(b)(c) |
| | **3. Modèles markoviens et bayésiens** | |
| 10 | Les champs de Markov : première formalisation | — |
| 11 | Attache aux données + régularisation | Fig. 3 (a)(b) |
| 12 | Optimisation et usages des MRF | — |
| 13 | Des MRF aux CRF : un pont vers le profond | — |
| | **4. Représentations spectro-spatiales et variationnelles** | |
| 14 | Enrichir la représentation, pas seulement les étiquettes | — |
| 15 | Morphologie mathématique et profils multi-échelles | Fig. 4 (×3) |
| 16 | Méthodes variationnelles : régulariser la solution | — |
| | **5. Apprentissage profond et modèles de fondation** | |
| 17 | Apprendre profond (AlexNet, FCN, U-Net, DeepLab) | Fig. 6 |
| 18 | Transformers, auto-supervisé et modèles de fondation | Fig. 7 |
| | **6. Défis ouverts** | |
| 19 | Défis ouverts | — |
| 20 | Conclusion : une histoire non linéaire | frise |
| 21 | Merci de votre attention | — |
| 22–24 | Références (annexe, 54 entrées) | — |

La figure 5 (SPOT © CNES / segmentation variationnelle) n'est pas reprise dans
cette version ; elle reste disponible dans `imgs/article/`.

## Différences avec la [version longue](../LONG/)

- **Structure** : 6 sections au lieu de 11, regroupées (« Du pixel au
  contexte » fusionne les §2 à §5 de l'article ; « Représentations
  spectro-spatiales et variationnelles » fusionne les §7 et §8). Les sections
  ne sont pas introduites par une planche dédiée, et le sommaire tient sur une
  seule colonne.
- **Bibliographie** : 54 entrées au lieu de 79. 26 références non citées ont
  été retirées, une a été ajoutée (Xiao *et al.*, 2025, « Foundation Models for
  Remote Sensing and Earth Observation: A Survey », citée planche 18), et les
  noms de revues et de conférences sont **abrégés** (`IEEE Trans. Geosci.
  Remote Sens.`, `NeurIPS`, `ICLR`…). Les numéros `[n]` d'une version à l'autre
  ne se correspondent donc pas.
- **Annexes** : pas de planche « Crédits des figures ».
- **Mise en page** : macros identiques (`\hl`, `\refc`, `\legende`, `\credit`,
  `\biblio`, `\formulebox`, `\filrouge`, `\logounige`) et thème `theme/`
  inchangé.

## Rapport au PDF de référence

Cette version reproduisait le PDF de `reference/` glyphe pour glyphe. Elle ne
le fait plus : les **guillemets françaises** y ont été corrigées. En OT1 —
l'encodage par défaut — babel-french compose « et » avec les signes
*mathématiques* ≪ et ≫ de la fonte CMSY, qui n'en ont ni le dessin ni la
chasse. `\usepackage[T1]{fontenc}` et `lmodern` donnent les vraies guillemets ;
le document passe de Computer Modern à Latin Modern, même dessin, encodage T1.

Les métriques changent donc, et avec elles les quatre calages verticaux au
point près qui servaient uniquement à retomber sur le PDF de Martina (sommaire,
planches 17 et 18, largeur de la figure 7). Ils ont été retirés : le code est
revenu à sa forme naturelle.

**Ce qui n'a pas bougé**, vérifié planche par planche contre `reference/` :

| | résultat |
|---|---|
| planches | 24 / 24 |
| texte des planches | 3 918 mots, **identiques** — au seul détail près que les guillemets ont gagné l'espace fine qui leur revient |
| images | 62, aux mêmes emplacements (écart maximal 1,23 pt, dû aux métriques et au retrait des calages) |
| boîtes débordantes | 2 hbox / 2 vbox, une de moins qu'avant |
| texte hors cadre, collision avec le bandeau | aucune |

Le PDF d'origine reste dans `reference/` comme trace de l'état initial.

> **Défaut hérité, toujours là — planche 9.** Le bandeau de références du bas
> affiche `[haralick1985image] haralick1985image` : la planche cite une clé
> absente de `references.bib`. Conservé pour ne pas modifier le contenu d'une
> planche sans arbitrage. Deux façons de corriger, au choix : retirer la clé de
> la ligne `\biblio` de cette planche (elle n'est citée nulle part ailleurs), ou
> réintroduire l'entrée dans `references.bib` — mais cela décalerait tous les
> numéros `[n]` suivants. La [version anglaise](EN/) a, elle, retiré la clé.

## À vérifier

- **Planche 9** : la citation `[haralick1985image]` cassée (voir ci-dessus).
- La référence `[1]` (l'article) est datée de 2027 et renvoie, pour le lien, au
  rapport de recherche Inria RR-9631 de septembre 2026. Volume, numéro et pages
  restent à compléter à la parution.
- Planche 18 : « modèles de fondation **geospatiaux** » est sans accent dans le
  PDF d'origine, et conservé tel quel ici.
- Affiliations : même point ouvert que pour la
  [version longue](../LONG/README.md#à-décider-ensemble). Contrairement à elle,
  cette version reste celle du GRETSI 2027 : le sous-titre et le pied de page
  nomment le colloque.
