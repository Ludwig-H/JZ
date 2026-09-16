# Version courte — 24 planches

Version resserrée de l'exposé (≈ 20 min) : **6 sections** au lieu de 11,
20 planches d'exposé, pas de planche de section, pas de planche de crédits en
back-up, bibliographie réduite.

PDF de référence : [`reference/GRETSI_2027_Segmentation_sémantique_en_télédétection_SHORT.pdf`](reference/)
(Martina Pastorino, 11 septembre 2026). Le `main.tex` de ce dossier a été
reconstruit par rétro-ingénierie à partir de ce PDF — voir
[« Fidélité au PDF de référence »](#fidélité-au-pdf-de-référence).

## Contenu du dossier

```
SHORT/
├── main.tex          la présentation (6 sections, 24 planches)
├── references.bib    54 entrées, revues et conférences abrégées
├── reference/        le PDF envoyé par Martina, tel quel
├── imgs/article/     les 7 figures de l'article (jeu complet ; 6 sont utilisées ici)
├── imgs/logos/       logos Università di Genova
├── theme/            thème Beamer Inria 2024 (copie amont, non modifiée)
├── latexmkrc         TEXINPUTS → theme/, compilation pdfLaTeX
└── Makefile          `make` / `make clean`
```

`make` produit `GRETSI2027_Segmentation_Semantique_Teledetection_SHORT.pdf`
(pdfLaTeX + biber ; le PDF n'est pas versionné). Prérequis et remarques sur le
moteur : voir le [README du dossier parent](../README.md#compilation).

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

## Fidélité au PDF de référence

Le PDF produit par `make` et celui de `reference/` ont été comparés planche par
planche :

| | résultat |
|---|---|
| planches | 24 / 24 |
| fontes embarquées | 13, identiques |
| glyphes (caractère, fonte, corps, couleur, position) | 25 997 comparés, **aucun écart** de caractère, de fonte, de corps ni de couleur |
| lignes de texte | 456, identiques ; écart de position maximal **0,1 pt** |
| images | 62, écart de position et de taille **0,05 pt** |
| rendu 150 dpi | 0,09 % de pixels différents (anticrénelage) |

> **Défaut reproduit tel quel — planche 9.** Le bandeau de références du bas
> affiche `[haralick1985image] haralick1985image` : la planche cite une clé
> absente de `references.bib`. C'est ce qu'imprime le PDF de référence, donc
> c'est conservé. Deux façons de corriger, au choix : retirer la clé de la
> ligne `\biblio` de cette planche (elle n'est citée nulle part ailleurs), ou
> réintroduire l'entrée dans `references.bib` — mais cela décalerait tous les
> numéros `[n]` suivants. Un commentaire le rappelle dans `main.tex`.

Quelques réglages de `main.tex` ont été **calés numériquement** sur le PDF de
référence, faute de pouvoir deviner la valeur d'origine : la position verticale
du sommaire et des planches 17 et 18 (`\vspace*` de l'ordre du point) et la
largeur de la figure 7 (planche 18). Ils sont signalés par un commentaire.
Ce sont les seuls endroits où le code ne se lit pas naturellement.

## À vérifier

- **Planche 9** : la citation `[haralick1985image]` cassée (voir ci-dessus).
- La référence `[1]` (l'article) attend toujours volume, numéro et pages ; en
  l'état elle renvoie au rapport de recherche Inria RR-9631.
- Planche 18 : « modèles de fondation **geospatiaux** » est sans accent dans le
  PDF de référence, et reproduit tel quel ici.
- Affiliations et date exacte de l'exposé : mêmes points ouverts que pour la
  [version longue](../LONG/README.md#à-décider-ensemble).
