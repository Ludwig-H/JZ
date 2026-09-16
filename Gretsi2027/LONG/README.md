# Version longue — 51 planches

Support de la **session historique** du GRETSI 2027 (≈ 45 min), suivant les
11 sections de l'article, plus les crédits et la bibliographie en annexe.

PDF de référence : [`reference/GRETSI_2027_Segmentation_sémantique_en_télédétection_LONG.pdf`](reference/)
(Martina Pastorino, 11 septembre 2026). Le `main.tex` de ce dossier le
reproduit à l'identique — voir [« Fidélité au PDF de référence »](#fidélité-au-pdf-de-référence).

## Contenu du dossier

```
LONG/
├── main.tex                    la présentation (11 sections, 51 planches)
├── references.bib              79 entrées : les références de l'article + l'article lui-même
├── rapport-complementaire.md   document d'accompagnement (déroulé, crédits, minutage)
├── reference/                  le PDF envoyé par Martina, tel quel
├── imgs/article/               les 7 figures de l'article (14 sous-images)
├── imgs/logos/                 logos Università di Genova
├── theme/                      thème Beamer Inria 2024 (copie amont, non modifiée)
├── latexmkrc                   TEXINPUTS → theme/, compilation pdfLaTeX
└── Makefile                    `make` / `make clean`
```

`make` produit `GRETSI2027_Segmentation_Semantique_Teledetection_LONG.pdf`
(pdfLaTeX + biber ; le PDF n'est pas versionné). Prérequis et remarques sur le
moteur : voir le [README du dossier parent](../README.md#compilation).

## La présentation (`main.tex`)

51 planches : page de titre, sommaire, **11 sections** reprenant celles de
l'article (chacune ouverte par une planche de section numérotée `01`…`11`),
planche « Merci de votre attention » du thème, soit **45 planches d'exposé**,
puis en annexe la bibliographie complète et, en back-up, les crédits des
figures.

- **Illustrations** : les 7 figures de l'article, soit 14 sous-images, toutes
  reprises ; aucune image extérieure. Les deux seuls ajouts graphiques sont la
  frise du fil directeur (`\filrouge`) et les encadrés de formules
  (`\formulebox`).
- **Crédits** : légende courte sous chaque image (`\legende`), puis crédit et
  copyright **juste sous les sous-légendes** (`\credit`) ; les deux sont
  centrés. Une planche de back-up récapitule les sept crédits.
- **Citations** : renvois `[n]` en gris dans le corps des planches (`\refc`) et
  **texte complet des références citées, tout en bas de chaque planche**
  (`\biblio`, format compact) ; bibliographie complète en annexe. `\nocite{*}`
  est placé en tête de document pour que la numérotation suive l'ordre du
  `.bib`, donc celui de l'article.
- **Commandes maison** : `\hl` (mise en évidence rouge Inria), `\refc`,
  `\legende`, `\credit`, `\biblio`, `\formulebox`, `\filrouge`, `\logounige`
  (logo Università di Genova en page de titre). Le dossier `theme/` reste
  identique à l'amont, à ceci près que `\thankyou` est redéfini dans
  `main.tex` en « Merci de votre attention. ».

Le déroulé planche par planche, le minutage et les choix éditoriaux sont
consignés dans le [rapport complémentaire](rapport-complementaire.md).

## Fidélité au PDF de référence

Par rapport à l'état précédent du dépôt, le PDF envoyé par Martina comporte
**trois** modifications, reportées telles quelles dans les sources :

1. **Entrée `[1]`** (l'article lui-même) : la date « déc. 2026 » disparaît, au
   profit d'une note « *Also available as Inria RR-9631*
   <https://inria.hal.science/hal-05742224> (sept. 2026) ». Elle s'affiche en
   page de titre et dans la bibliographie.
2. **Référence retirée** : `li2014survey` (X. Li *et al.*, « A survey of
   semantic segmentation », arXiv:1412.7062, 2014), citée planche 18. La
   bibliographie passe de 80 à **79 entrées** et tous les numéros à partir de
   `[26]` sont décalés d'une unité.
3. **Planche 19** (« L'apport mesurable du contexte ») : les trois renvois sont
   réordonnés en `[12] [27] [28]` (Solberg d'abord).

**Vérification.** Le PDF produit par `make` et celui de `reference/` ont été
comparés planche par planche :

| | résultat |
|---|---|
| planches | 51 / 51 |
| fontes embarquées | 19, identiques |
| glyphes (caractère, fonte, corps, couleur, position) | 48 223 comparés, écart de position maximal **0,01 pt** |
| lignes de texte | 830, identiques |
| images | 119, écart de position et de taille **0,00 pt** |
| rendu 150 dpi | 0,09 % de pixels différents (anticrénelage) |

Seule exception, planche 31 : les accolades horizontales de la formule de
Mumford–Shah sont *dessinées* à l'identique, mais la table `ToUnicode` du PDF
les code différemment (`⏞⏟⏟⏞` chez Martina, `|{z}` ici). C'est une différence
de version de TeX Live — elle ne change que le copier-coller, pas l'affichage.

## `references.bib`

**79 entrées.** En tête, **l'article dont est tirée la présentation**, sous la
clé `pastorino2026segmentation`. Il porte donc le numéro `[1]`, et c'est la
seule référence à l'article originel : elle figure sur la page de titre et dans
la bibliographie, nulle part ailleurs.

Viennent ensuite les références de l'article, dans son ordre, chacune précédée
d'un commentaire `% [nn]` rappelant son numéro d'origine. Deux écarts avec
l'article :

- la référence Samson *et al.* (2000) y est numérotée deux fois ([52] et [56])
  et n'est saisie qu'une fois, sous la clé `samson2000variational` ;
- `li2014survey` a été retirée par Martina (voir ci-dessus).

Correspondance article → planches :

| Numéros dans l'article | Numéros sur les planches |
|---|---|
| *(l'article lui-même)* | `[1]` |
| `[1]` … `[24]` | `[2]` … `[25]` |
| `[25]` | *retirée* |
| `[26]` … `[55]` | `[26]` … `[55]` |
| `[56]` | fusionné avec `[52]`, soit `[52]` |
| `[57]` … `[80]` | `[56]` … `[79]` |

## Ressources graphiques disponibles

### Couleurs du thème (`theme/beamercolorthemeinria.sty`)

| Nom | Hex | | Nom | Hex |
|---|---|---|---|---|
| `inria-2024-rouge` | `#C9191E` | | `inria-2024-bleu-vert` | `#88CCAA` |
| `inria-2024-framboise` | `#A60F79` | | `inria-2024-gris-bleu` | `#384257` |
| `inria-2024-violet` | `#5D4B9A` | | `inria-2024-cactus` | `#608B37` |
| `inria-2024-bleu-nuit` | `#27348B` | | `inria-2024-vert-tendre` | `#95C11F` |
| `inria-2024-bleu-canard` | `#1067A3` | | `inria-2024-jaune` | `#FFCD1C` |
| `inria-2024-bleu-azur` | `#00A5CC` | | `inria-2024-orange` | `#DD8300` |
| | | | `inria-2024-sable` | `#E2D0AA` |

Alias fournis : `inria-rouge`/`rouge_inria`, `gris_fonce_inria`
(= `inria-2024-gris-bleu`), `gris_clair_inria`, `inria-noir`, `inria-blanc`.
`\usetheme{inria}` définit aussi `\barrecouleur` (filet dégradé),
`\titlelogo` (bloc-marque RF + Inria) et `\thankyou`.

### Logos

- Inria : dans `theme/imgs/` (`RF-INria_Bloc-marque.png` en page de titre,
  `Inria-logo-rouge.png` en pied de page) — géré par le thème.
- Università di Genova : `imgs/logos/logo_orizzontale_COLORE.png` (1915×485) et
  `logo_verticale_COLORE.png` (1017×865). Le thème Inria ne prévoit pas de
  second logo : la version horizontale est posée en page de titre par
  `\logounige` (défini dans `main.tex`), sans toucher à `theme/`.

## Carte de l'article

L'article est une **synthèse historique et méthodologique** : il retrace
l'évolution de la segmentation sémantique en télédétection comme une
*intégration progressive de niveaux croissants de contexte* — c'est le fil
directeur annoncé en §1 et repris en §11.

Formalisation commune : une image est `I : Ω → R^d` (Ω domaine spatial,
`d` variables : bandes pan/multi/hyperspectrales, polarisations RSO, LiDAR,
MNT, indices…) ; segmenter, c'est estimer `f : Ω → C`, `C` l'ensemble fini des
classes sémantiques.

| § | Thème | Figures |
|---|---|---|
| 1 | Introduction : définition, spécificités de la télédétection, formalisation `I`/`f` | Fig. 1 — Zeebruges (IADF IEEE GRSS) |
| 2 | Classification statistique pixel à pixel : règle bayésienne, MAP, phénomène de Hughes, effet poivre et sel | Fig. 2 |
| 3 | Méthodes discriminantes et à noyaux : SVM, astuce du noyau, noyaux géospatiaux | — |
| 4 | Méthodes d'ensemble : Random Forests, applications multi/hyperspectrales | — |
| 5 | Classification contextuelle : contexte local / régional (→ OBIA) / global | Fig. 2 (a→c) |
| 6 | Modèles markoviens et bayésiens : MRF ≡ Gibbs, `U = U_d + β·U_r`, ICM, recuit simulé, graph cuts, CRF | Fig. 3 — voisinages et cliques |
| 7 | Méthodes spectro-spatiales : textures, morphologie mathématique, EMP, profils d'attributs | Fig. 4 — érosion / original / dilatation |
| 8 | Méthodes variationnelles : contours actifs, Mumford–Shah, level sets, Chan–Vese | Fig. 5 — SPOT © CNES |
| 9 | Apprentissage profond : AlexNet, FCN, U-Net, ResNet, DeepLab / ASPP, FPN, multimodal | Fig. 6 — FCN sur ISPRS Potsdam |
| 10 | Transformers et modèles de fondation : attention, ViT, Swin, SegFormer, MAE, GFM | Fig. 7 — principe d'un GFM |
| 11 | Conclusion : convergence de plusieurs traditions ; défis ouverts | — |

**Idée transversale** : MRF, modèles variationnels et formulations sur graphes
sont « différentes expressions d'un même principe » — un terme d'**attache aux
données** plus une **régularisation** spatiale ou géométrique (§8) — principe
que l'apprentissage profond ne supprime pas mais reformule (§9).

### Inventaire des figures extraites

| Fichier (`imgs/article/`) | Figure | Contenu |
|---|---|---|
| `fig1a_zeebruges_image_aerienne.png` | 1 (a) | image aérienne Zeebruges |
| `fig1b_zeebruges_carte_segmentation.png` | 1 (b) | carte de segmentation |
| `fig2a_ikonos_fausses_couleurs.png` | 2 (a) | IKONOS 4 m, fausses couleurs PIR-R-B |
| `fig2b_classification_pixel_a_pixel.png` | 2 (b) | carte pixel à pixel (bruitée) |
| `fig2c_classification_contextuelle.png` | 2 (c) | carte contextuelle |
| `fig3a_voisinage_ordre1_cliques.png` | 3 (a) | voisinage du 1ᵉʳ ordre et ses cliques |
| `fig3b_voisinage_ordre2_cliques.png` | 3 (b) | voisinage du 2ᵈ ordre et ses cliques |
| `fig4a_erosion.png` | 4 (g.) | érosion |
| `fig4b_image_originale_rvb.png` | 4 (c.) | image satellite RVB originale |
| `fig4c_dilatation.png` | 4 (d.) | dilatation |
| `fig5a_spot_cnes.png` | 5 (a) | image SPOT © CNES |
| `fig5b_segmentation_variationnelle.png` | 5 (b) | segmentation variationnelle |
| `fig6_fcn_potsdam.png` | 6 | architecture FCN, ISPRS Potsdam |
| `fig7_modele_fondation_geospatial.png` | 7 | principe d'un modèle de fondation géospatial |

Crédits portés sur les planches, centrés sous les sous-légendes : jeu de
données Zeebruges (comité technique IADF de l'IEEE GRSS, Académie royale
militaire belge & ONERA) ; cartes IKONOS ; voisinages ; image SPOT © CNES et
segmentation ; architecture FCN. Les figures 4 et 7 ne portent aucune
attribution dans l'article.

## À décider ensemble

- **Cadre exact** : durée réellement allouée (le minutage vise 45 min ; pour
  30 min, les planches 16, 28, 36 et 40 sont les candidates à la coupe — sinon
  la [version courte](../SHORT/) tient en ≈ 20 min).
- **Affiliations** : la page de titre annonce Josiane Zerubia (Centre Inria
  d'Université Côte d'Azur, équipe Ayana) comme oratrice, en collaboration avec
  Martina Pastorino et Gabriele Moser (Università di Genova, DITEN) —
  rattachements **à confirmer**. Logo UniGe en page de titre seule, ou aussi en
  pied de page ?
- **Date exacte** de l'exposé : le pied de page affiche « GRETSI 2027 »
  (`\date[…]{…}`).
- **Référence de l'article** : volume, numéro et pages restent à compléter à la
  parution dans `references.bib`.
- **Droits des figures 4 et 7** : elles ne portent aucune attribution dans
  l'article et sont donc créditées à l'article lui-même. À faire remonter si
  elles proviennent d'une source tierce.
