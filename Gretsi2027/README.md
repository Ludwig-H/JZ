# GRETSI 2027 — Segmentation sémantique en télédétection

Support de présentation (Beamer, thème Inria + logo Università di Genova) pour
l'article **« Segmentation Sémantique en Télédétection »** de Martina
**Pastorino**, Gabriele **Moser** et Josiane **Zerubia**.

> **État : préparation.** Le dossier contient l'article source, ses figures
> extraites, les logos et le thème Beamer. Les slides (`main.tex`) restent à
> écrire — voir [« À décider ensemble »](#à-décider-ensemble).

## Contenu du dossier

```
Gretsi2027/
├── TSI segmentation semantique paper + logo UniGE.zip   archive d'origine (intacte)
├── article/
│   ├── Martina_TSI_GRETSI_segmentation_semantique.pdf   l'article (18 p., 11 sections, 80 réf.)
│   └── texte-extrait.txt                                texte brut (pypdf), pour citer/rechercher
├── imgs/
│   ├── article/   les 7 figures de l'article, extraites en PNG (14 sous-images)
│   └── logos/     logos Università di Genova (versions horizontale et verticale, couleur)
├── theme/         thème Beamer Inria 2024
├── latexmkrc      TEXINPUTS → theme/, compilation LuaLaTeX
├── Makefile       `make` / `make clean`
└── main.tex       ← à écrire
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
make        # latexmk + LuaLaTeX
make clean
```

Prérequis : LuaLaTeX, `texlive-lang-french` (babel), et les paquets appelés par
le thème (`tikz`, `textpos`, `fmtcount`, `calc`, `ifdraft`). Les fontes Inria
Sans sont **optionnelles** : sans elles le thème émet un avertissement et
utilise la fonte sans-serif par défaut. Pour les activer, déposer
[`latex-inria-fonts`](https://gitlab.inria.fr/gabarits/latex-inria-fonts) à la
racine du dossier (le `latexmkrc` l'ajoute déjà à `TEXINPUTS`).

⚠️ Le thème référence ses images par des chemins **relatifs à la racine de
compilation** (`theme/imgs/...`) : compiler depuis `Gretsi2027/`, pas depuis
`theme/`.

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
  second logo : il faudra l'ajouter côté `main.tex` (p. ex. `textpos` en page de
  titre, à côté du bloc-marque), sans toucher à `theme/`.

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

Crédits à reporter sur les slides : Fig. 1 — jeu de données Zeebruges, IADF TC
IEEE GRSS, École royale militaire belge & ONERA ; Fig. 2 — [12] ; Fig. 3 —
[29] ; Fig. 5 — SPOT © CNES et [56] ; Fig. 6 — [61].

## À décider ensemble

- **Cadre exact de l'exposé** : GRETSI 2027 (tutoriel ? session invitée ?),
  durée, public — le nom de fichier de l'article mentionne « TSI » et
  « GRETSI », à confirmer.
- **Orateur / auteurs affichés** et affiliations (Inria, Università di Genova),
  donc placement du logo UniGe (page de titre seule, ou aussi en pied).
- **Langue** des slides (l'article est en français).
- **Découpage** : les 11 sections telles quelles, ou un regroupement en 4 actes
  (pixel → contexte → énergie/représentation → apprentissage) ?
- **Éléments à recréer en TikZ** plutôt qu'à reprendre en bitmap (typiquement la
  Fig. 3 des voisinages, et une frise chronologique 1970 → 2026).
- Reprise ou non du système de citations `\citb` / `\reffoot` de la soutenance
  (80 références dans l'article, à réduire fortement).
