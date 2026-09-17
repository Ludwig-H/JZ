# Version longue — 51 planches

Support **à usage général** (≈ 45 min) : séminaire, cours, exposé invité. Il
suit les 11 sections de l'article, plus les crédits et la bibliographie en
annexe. Aucune mention de colloque ni de date sur les planches.

PDF, dans ce dossier :

- `GRETSI2027_Segmentation_Semantique_Teledetection_LONG.pdf` — les planches ;
- `GRETSI2027_Semantic_Segmentation_Remote_Sensing_LONG.pdf` — les planches en
  anglais, dont les sources sont dans [`EN/`](EN/) ;
- `Notes_Orateur_Segmentation_Semantique_Teledetection_LONG.pdf` — le support
  pour l'oral, version imprimable de [`notes-orateur.md`](notes-orateur.md) ;
- `Speaker_Notes_Semantic_Segmentation_Remote_Sensing_LONG.pdf` — le même en
  anglais.

État d'origine : [`reference/`](reference/) conserve le PDF envoyé par Martina
Pastorino le 11 septembre 2026, dont ce `main.tex` est issu — voir
[« Rapport au PDF de référence »](#rapport-au-pdf-de-référence).

## Contenu du dossier

```
LONG/
├── main.tex                    la présentation (11 sections, 51 planches)
├── *.pdf                       planches et supports pour l'oral, français et anglais
├── references.bib              79 entrées : les références de l'article + l'article lui-même
├── notes-orateur.md            support pour l'oral : ce qu'il y a à dire, planche par planche
├── rapport-complementaire.md   document d'accompagnement (déroulé, crédits, minutage)
├── reference/                  le PDF envoyé par Martina, tel quel
├── EN/                         la même présentation en anglais (voir EN/README.md)
├── imgs/article/               les 7 figures de l'article (14 sous-images)
├── imgs/logos/                 logos Università di Genova
├── theme/                      thème Beamer Inria 2024 (copie amont, non modifiée)
├── latexmkrc                   TEXINPUTS → theme/, compilation pdfLaTeX
└── Makefile                    `make` / `make clean`
```

Version anglaise : [`EN/`](EN/) — mêmes 51 planches, même thème, mêmes figures,
même numérotation bibliographique. Support pour l'oral :
[`notes-orateur.md`](notes-orateur.md) en français,
[`EN/speaker-notes.md`](EN/speaker-notes.md) en anglais.

`make` produit `GRETSI2027_Segmentation_Semantique_Teledetection_LONG.pdf`
(pdfLaTeX + biber). `make` depuis [`EN/`](EN/) dépose le PDF anglais dans ce
même dossier. Prérequis et remarques sur le moteur : voir le
[README du dossier parent](../README.md#compilation).

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

## Rapport au PDF de référence

Cette version **ne reproduit plus** le PDF de `reference/`, et c'est délibéré.
Deux changements l'en écartent :

1. **Plus aucune mention du GRETSI 2027.** Le support est prévu pour un usage
   générique : le sous-titre devient « D'après l'article de synthèse [1] », le
   pied de page affiche le titre court au lieu du colloque, et les métadonnées
   PDF suivent.
2. **Vraies guillemets françaises**, via `\usepackage[T1]{fontenc}` et
   `lmodern`. En OT1 — l'encodage par défaut — babel-french compose « et » avec
   les signes *mathématiques* ≪ et ≫ de la fonte CMSY, qui n'en ont ni le
   dessin ni la chasse. Le document passe donc de Computer Modern à Latin
   Modern : même dessin, encodage T1, guillemets corrects.

Le second point change les métriques de fonte, donc la concordance au centième
de point avec le PDF de Martina n'a plus d'objet.

**Ce qui n'a pas bougé**, vérifié planche par planche contre `reference/` :

| | résultat |
|---|---|
| planches | 51 / 51 |
| texte des planches, hors pied de page et page de titre | 7 103 mots, **identiques** — au seul détail près que les guillemets ont gagné l'espace fine qui leur revient |
| images | 119, aux mêmes emplacements (écart maximal 0,29 pt, dû aux métriques) |
| boîtes débordantes | 14 hbox / 13 vbox, comme avant — elles viennent du thème, pas du texte |
| corps contre le bandeau de références | la planche 10, tout juste limite auparavant, a gagné de la marge |

Le PDF d'origine reste dans `reference/` comme trace de l'état initial.

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

- **Durée réellement allouée** : le minutage vise 45 min ; pour 30 min, les
  planches 16, 28, 36 et 40 sont les candidates à la coupe — sinon la
  [version courte](../SHORT/) tient en ≈ 20 min.
- **Affiliations** : la page de titre annonce Josiane Zerubia (Centre Inria
  d'Université Côte d'Azur, équipe Ayana) comme oratrice, en collaboration avec
  Martina Pastorino et Gabriele Moser (Università di Genova, DITEN) —
  rattachements **à confirmer**. Logo UniGe en page de titre seule, ou aussi en
  pied de page ?
- **Contexte** : le pied de page affiche le titre court. Pour un colloque
  précis, il suffit d'y remettre son nom : `\date[Mon colloque 20XX]{}`.
- **Référence de l'article** : volume, numéro et pages restent à compléter à la
  parution dans `references.bib`.
- **Droits des figures 4 et 7** : elles ne portent aucune attribution dans
  l'article et sont donc créditées à l'article lui-même. À faire remonter si
  elles proviennent d'une source tierce.
