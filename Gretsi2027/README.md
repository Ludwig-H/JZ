# GRETSI 2027 — Segmentation sémantique en télédétection

Support de présentation (Beamer, thème Inria + logo Università di Genova) pour
l'article **« Segmentation Sémantique en Télédétection »** de Martina
**Pastorino**, Gabriele **Moser** et Josiane **Zerubia**.

> **État : présentation rédigée.** 45 planches pour une session historique
> (≈ 45 min), suivant les 11 sections de l'article, plus les crédits et la
> bibliographie en annexe. Voir le
> [rapport complémentaire](rapport-complementaire.md) pour le déroulé planche
> par planche et [« À décider ensemble »](#à-décider-ensemble) pour ce qui
> reste à arbitrer.

## Contenu du dossier

```
Gretsi2027/
├── main.tex                                             la présentation (11 sections, 45 planches)
├── rapport-complementaire.md                            document d'accompagnement (déroulé, crédits, minutage)
├── references.bib                                       80 entrées : les références de l'article + l'article lui-même
├── GRETSI2027_Segmentation_Semantique_Teledetection.pdf le PDF compilé (51 planches)
├── TSI segmentation semantique paper + logo UniGE.zip   archive d'origine (intacte)
├── article/
│   ├── Martina_TSI_GRETSI_segmentation_semantique.pdf   l'article (18 p., 11 sections, 80 réf.)
│   └── texte-extrait.txt                                texte brut (pypdf), pour citer/rechercher
├── imgs/
│   ├── article/   les 7 figures de l'article, extraites en PNG (14 sous-images)
│   └── logos/     logos Università di Genova (versions horizontale et verticale, couleur)
├── theme/         thème Beamer Inria 2024
├── latexmkrc      TEXINPUTS → theme/, compilation LuaLaTeX
└── Makefile       `make` / `make clean`
```

### Provenance

- L'archive `.zip` provient du dépôt `Ludwig-H/JZ` (elle a simplement été
  déplacée ici) ; son contenu a été décompressé et rangé dans `article/` et
  `imgs/logos/`.
- Le thème `theme/` est copié tel quel depuis
  [`Ludwig-H/Manuscrit-de-th-se`](https://github.com/Ludwig-H/Manuscrit-de-th-se/tree/main/Soutenance/soutenance/theme)
  (`Soutenance/soutenance/theme`), sans modification, pour rester alignable sur
  l'amont.
- Les figures de `imgs/article/` ont été extraites du PDF avec `pypdf` puis
  renommées d'après les légendes ; ce sont les images d'origine, non
  recompressées.

## Compilation

```bash
make        # latexmk + LuaLaTeX + biber → GRETSI2027_Segmentation_Semantique_Teledetection.pdf
make clean
```

Prérequis : LuaLaTeX, `biber`, `texlive-lang-french` (babel), `biblatex`,
`csquotes`, et les paquets appelés par le thème (`tikz`, `textpos`, `fmtcount`,
`calc`, `ifdraft`). Testé avec TeX Live 2023 (biblatex 3.19 / biber 2.19). Les fontes Inria
Sans sont **optionnelles** : sans elles le thème émet un avertissement et
utilise la fonte sans-serif par défaut. Pour les activer, déposer
[`latex-inria-fonts`](https://gitlab.inria.fr/gabarits/latex-inria-fonts) à la
racine du dossier (le `latexmkrc` l'ajoute déjà à `TEXINPUTS`).

⚠️ Le thème référence ses images par des chemins **relatifs à la racine de
compilation** (`theme/imgs/...`) : compiler depuis `Gretsi2027/`, pas depuis
`theme/`.

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

### `references.bib`

**80 entrées.** En tête, **l'article dont est tirée la présentation**, sous la
clé `pastorino2026segmentation` :

> M. Pastorino, G. Moser, J. Zerubia, « Segmentation sémantique en
> télédétection », *Traitement du Signal et des Images* (TSI), GRETSI,
> décembre 2026. *(volume, numéro et pages à compléter à la parution.)*

Il porte donc le numéro `[1]`, et c'est la seule référence à l'article
originel : elle figure sur la page de titre et dans la bibliographie, nulle
part ailleurs.

Viennent ensuite les 80 références de l'article, dans son ordre, chacune
précédée d'un commentaire `% [nn]` rappelant son numéro d'origine, ramenées à
79 parce que la référence Samson *et al.* (2000) y est numérotée deux fois
([52] et [56]) et n'est saisie qu'une fois, sous la clé
`samson2000variational`. La correspondance est donc :

| Numéros dans l'article | Numéros sur les planches |
|---|---|
| *(l'article lui-même)* | `[1]` |
| `[1]` … `[55]` | `[2]` … `[56]` |
| `[56]` | fusionné avec `[52]`, soit `[53]` |
| `[57]` … `[80]` | `[57]` … `[80]` |

Le fichier a été relu automatiquement contre la liste de références de
l'article (année et premier auteur de chaque entrée).

## Ressources graphiques disponibles

### Couleurs du thème (`beamercolorthemeinria.sty`)

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

| § | Thème | Points clés | Figures |
|---|---|---|---|
| 1 | Introduction | définition, spécificités de la télédétection (capteurs, résolutions, dates, modalités), formalisation `I`/`f` | Fig. 1 — Zeebruges (IADF IEEE GRSS) |
| 2 | Classification statistique pixel à pixel | Landsat / SeaSat (années 1970), règle bayésienne, MAP ≡ « MLC », phénomène de Hughes [8], hypothèse d'indépendance → effet poivre et sel | Fig. 2 |
| 3 | Méthodes discriminantes et à noyaux | SVM [13, 14], astuce du noyau [15], noyaux géospatiaux [16, 17] — améliorent la frontière de décision, restent pixel à pixel | — |
| 4 | Méthodes d'ensemble | Random Forests [18], applications multi/hyperspectrales [19, 20] — même limite spatiale | — |
| 5 | Classification contextuelle | contexte **local** [21, 22] / **régional** (→ OBIA [23]) / **global** ; hiérarchie qui structure toute la suite | Fig. 2 (a→c) |
| 6 | Modèles markoviens et bayésiens | MRF ≡ Gibbs, MAP, énergie `U = U_d + β·U_r` ; ICM, recuit simulé [30], échantillonneur de Gibbs [9], graph cuts [31], loopy BP [32] ; CRF [35], fully-connected [36], CRF-as-RNN [37] ; travaux Pastorino/Moser/Serpico/Zerubia [38–41] | Fig. 3 — voisinages d'ordre 1 et 2 + cliques |
| 7 | Méthodes spectro-spatiales | textures [21], morphologie mathématique [43, 44], EMP [45], profils d'attributs [46], SVM + profils [47], réduction de dimension et fusion [48, 49], unités-régions [50] — on enrichit **les descripteurs**, pas les étiquettes | Fig. 4 — érosion / original / dilatation |
| 8 | Méthodes variationnelles | contours actifs [53], **Mumford–Shah** (éq. 6) [51], level sets [54], Chan–Vese [55], modèle unifié classification/restauration [52, 56] | Fig. 5 — SPOT © CNES |
| 9 | Apprentissage profond | AlexNet 2012 [57], transfert [58, 59], **FCN** [60], **U-Net** [62], ResNet [66], DeepLab / ASPP [67, 68], FPN [69], multimodal [63, 70] ; limites : annotations denses coûteuses, généralisation inter-capteurs, longue portée | Fig. 6 — FCN sur ISPRS Potsdam, d'après [61] |
| 10 | Transformers et modèles de fondation | attention [71], ViT [72], Swin [73], SegFormer [74], MAE auto-supervisé [75], **GFM** [76–80] (AlphaEarth, SatMAE, Prithvi, SAM) ; coût de pré-entraînement et empreinte environnementale | Fig. 7 — principe d'un GFM |
| 11 | Conclusion | pas une trajectoire linéaire mais la convergence de plusieurs traditions ; défis ouverts : généralisation géographique, rareté des annotations, fusion optique/RSO/LiDAR, temporalité, interprétabilité, robustesse opérationnelle | — |

**Idée transversale à exploiter dans les slides** : MRF, modèles
variationnels et formulations sur graphes sont « différentes expressions d'un
même principe » — un terme d'**attache aux données** plus une
**régularisation** spatiale ou géométrique (§8) — principe que l'apprentissage
profond ne supprime pas mais reformule (§9).

### Inventaire des figures extraites

| Fichier (`imgs/article/`) | Figure | Contenu |
|---|---|---|
| `fig1a_zeebruges_image_aerienne.png` | 1 (a) | image aérienne Zeebruges |
| `fig1b_zeebruges_carte_segmentation.png` | 1 (b) | carte de segmentation (building / car / road / grass / tree) |
| `fig2a_ikonos_fausses_couleurs.png` | 2 (a) | IKONOS 4 m, composition fausses couleurs PIR-R-B |
| `fig2b_classification_pixel_a_pixel.png` | 2 (b) | carte pixel à pixel (bruitée) |
| `fig2c_classification_contextuelle.png` | 2 (c) | carte contextuelle [12] |
| `fig3a_voisinage_ordre1_cliques.png` | 3 (a) | voisinage du 1ᵉʳ ordre et ses cliques |
| `fig3b_voisinage_ordre2_cliques.png` | 3 (b) | voisinage du 2ᵈ ordre et ses cliques |
| `fig4a_erosion.png` | 4 (g.) | érosion |
| `fig4b_image_originale_rvb.png` | 4 (c.) | image satellite RVB originale |
| `fig4c_dilatation.png` | 4 (d.) | dilatation |
| `fig5a_spot_cnes.png` | 5 (a) | image SPOT © CNES |
| `fig5b_segmentation_variationnelle.png` | 5 (b) | segmentation variationnelle [56] |
| `fig6_fcn_potsdam.png` | 6 | architecture FCN, ISPRS Potsdam [61] |
| `fig7_modele_fondation_geospatial.png` | 7 | principe d'un modèle de fondation géospatial |

Crédits portés sur les planches, centrés sous les sous-légendes, sous la forme
*légende + copyright + référence* : jeu de données Zeebruges (comité technique
IADF de l'IEEE GRSS, Académie royale militaire belge & ONERA) ; cartes IKONOS
[12] ; voisinages [29] ; image SPOT © CNES et segmentation [52] ; architecture
FCN [61]. Les figures 4 et 7 ne portent aucune attribution dans l'article.

## À décider ensemble

- **Cadre exact** : session historique du GRETSI 2027 — durée réellement allouée
  (le minutage vise 45 min ; pour 30 min, les planches 16, 28, 36 et 40 sont les
  candidates à la coupe).
- **Affiliations** : la page de titre annonce Josiane Zerubia (Centre Inria
  d'Université Côte d'Azur, équipe Ayana) comme oratrice, en collaboration avec
  Martina Pastorino et Gabriele Moser (Università di Genova, DITEN) —
  rattachements **à confirmer**. Logo UniGe en page de titre seule, ou aussi en
  pied de page ?
- **Date exacte** de l'exposé : le pied de page affiche « GRETSI 2027 »
  (`\date[…]{…}`).
- **Droits des figures 4 et 7** : elles ne portent aucune attribution dans
  l'article et sont donc créditées à l'article lui-même. À faire remonter si
  elles proviennent d'une source tierce.
- **Citations** : garder `biblatex` (numéros `[n]` et bibliographie complète en
  annexe), ou reprendre le système `\citb` / `\reffoot` de la soutenance
  (label court entre crochets + référence en bas de la planche de première
  citation) ?
