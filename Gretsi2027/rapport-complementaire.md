# Rapport complémentaire — session historique GRETSI 2027

**Segmentation sémantique en télédétection**
Josiane **Zerubia** (Centre Inria d'Université Côte d'Azur, équipe Ayana), en
collaboration avec Martina **Pastorino** et Gabriele **Moser** (Università di
Genova, DITEN).

Support : [`GRETSI2027_Segmentation_Semantique_Teledetection.pdf`](GRETSI2027_Segmentation_Semantique_Teledetection.pdf)
(51 planches : 45 pour l'exposé, puis 6 en annexe).
Source de l'exposé : [`article/Martina_TSI_GRETSI_segmentation_semantique.pdf`](article/Martina_TSI_GRETSI_segmentation_semantique.pdf).

Ce document accompagne les transparents. Il consigne ce que les planches, par
construction synthétiques, ne disent pas : le raisonnement du découpage, la
provenance et les droits de chaque illustration, la correspondance exacte avec
l'article, un minutage, et les points qui restent à arbitrer avant diffusion.

---

## 1. Cadrage

| | |
|---|---|
| Format | Session historique, GRETSI 2027 |
| Durée visée | ≈ 45 min d'exposé (+ questions) |
| Planches | 45 numérotées jusqu'au « Merci », + crédits + bibliographie en annexe |
| Langue | Français intégral (titres, légendes, crédits, bibliographie) |
| Gabarit | Thème Beamer Inria 2024 + logo Università di Genova en page de titre |
| Illustrations | **Exclusivement** les 7 figures de l'article (14 sous-images), toutes reprises |

Trois contraintes ont guidé la rédaction :

1. **Suivre la structure de l'article.** Les 11 sections de l'article deviennent
   les 11 sections de l'exposé, dans le même ordre, avec une planche de section
   numérotée (`01`… `11`) par section. Le sommaire de la planche 2 est donc
   littéralement la table des matières de l'article.
2. **Aller à l'essentiel.** Quatre à six items par planche, une idée par item,
   pas de paragraphe. Les formules ne sont conservées que lorsqu'elles portent
   l'argument (règle bayésienne, énergie markovienne, Mumford–Shah) et sont
   alors isolées dans un encadré au liseré rouge Inria.
3. **Créditer partout.** Chaque renvoi bibliographique apparaît **dans le corps
   de la planche** sous la forme `[n]` en gris ; chaque figure porte sa
   **légende** sous l'image et son **crédit / copyright** en pied de planche ;
   une planche d'annexe récapitule l'ensemble des crédits.

---

## 2. Le fil directeur

L'article annonce sa thèse en §1 et la reprend en §11 : l'histoire de la
segmentation sémantique en télédétection est celle d'une **intégration
progressive de niveaux croissants de contexte**, et non d'une marche linéaire
des classifieurs statistiques vers les réseaux profonds.

Cette thèse est matérialisée sur les transparents par une frise en cinq étapes
(commande `\filrouge` dans `main.tex`), affichée deux fois — planche 6, à la fin
de l'introduction, et planche 43, en ouverture de la conclusion :

| Étape | Contenu | Sections de l'article |
|---|---|---|
| Information spectrale locale | le pixel seul | §2, §3, §4 |
| Cohérence spatiale | les étiquettes voisines | §5, §6 |
| Frontières, régions, objets | la géométrie de la scène | §7, §8 |
| Représentations apprises | les descripteurs ne sont plus conçus | §9 |
| Représentations générales | transférables, multimodales | §10 |

Un second fil, plus discret, court dans les planches 22, 31, 32 et 43 : la
formule **attache aux données + régularisation**, commune aux champs de Markov
(§6), aux modèles variationnels (§8) et aux formulations sur graphes. L'article
la qualifie explicitement de « même principe » sous des expressions
différentes ; c'est le meilleur levier pour éviter que l'exposé ne se réduise à
un catalogue chronologique.

---

## 3. Déroulé, planche par planche

Minutage indicatif pour 45 minutes. Les planches de section (`§`) sont des
respirations de quelques secondes.

| # | Planche | Message central | Figure | Réf. citées |
|---|---|---|---|---|
| 1 | Page de titre | — | — | — |
| 2 | Sommaire | le plan de l'exposé est celui de l'article | — | — |
| | | | | **1 min 30** |
| 3 | § **01 Introduction** | | | |
| 4 | De l'image à la carte thématique | définition ; carte dense ≠ segmentation « bas niveau » | **Fig. 1 (a)(b)** | [1][2][3] |
| 5 | Ce qui distingue la télédétection | capteurs, résolutions, dates, modalités ; ce n'est pas une transposition de la vision par ordinateur | — | — |
| 6 | Formalisation et fil directeur | `I : Ω → ℝᵈ` puis `f : Ω → C` ; frise en 5 étapes | frise | — |
| | | | | **4 min** |
| 7 | § **02 Classification statistique pixel à pixel** | | | |
| 8 | Les premières approches (années 1970) | Landsat / SeaSat ; règle bayésienne ; MAP dit « MLC » | — | [4][5][6][1][2][3][7] |
| 9 | Deux limites structurelles | Hughes + indépendance des observations | — | [8] |
| 10 | L'effet « poivre et sel » | on passe de la classification spectrale à l'interprétation spatiale | **Fig. 2 (a)(b)** | [9][10][11][12] |
| | | | | **4 min** |
| 11 | § **03 Méthodes discriminantes et à noyaux** | | | |
| 12 | Estimer la frontière plutôt que la distribution | SVM, maximisation de la marge | — | [13][14] |
| 13 | Noyaux : la non-linéarité sans perdre la convexité | **la décision progresse, pas la représentation** | — | [15][16][17] |
| | | | | **3 min** |
| 14 | § **04 Méthodes d'ensemble** | | | |
| 15 | Forêts aléatoires | double aléa observations/variables ; importance des variables | — | [18][19][20] |
| 16 | Bilan de l'ère « pixel » | charnière : régulariser les étiquettes **ou** enrichir les descripteurs | — | — |
| | | | | **2 min 30** |
| 17 | § **05 Classification contextuelle** | | | |
| 18 | Trois niveaux de contexte | local / régional / global | — | [3][21][22][23][24][25][26] |
| 19 | L'apport mesurable du contexte | les étiquettes doivent être estimées conjointement | **Fig. 2 (a)(b)(c)** | [27][28][11][12] |
| | | | | **3 min 30** |
| 20 | § **06 Modèles markoviens et bayésiens** | | | |
| 21 | Les champs de Markov : la première formalisation | Markov ≡ Gibbs ; MAP ⇔ minimisation d'énergie | — | [9][10][29] |
| 22 | Attache aux données + régularisation | `U = U_d + β·U_r` ; rôle de β | **Fig. 3 (a)(b)** | [29] |
| 23 | Optimiser : un problème difficile | ICM, recuit simulé, Gibbs, coupes de graphes, loopy BP | — | [30][9][31][32][11][33][34] |
| 24 | Des MRF aux CRF | `P(Y|X)` direct ; couches différentiables | — | [35][36][37][38][39][40][41] |
| | | | | **6 min** |
| 25 | § **07 Méthodes spectro-spatiales** | | | |
| 26 | Enrichir la représentation, pas les étiquettes | la THR rend texture et forme aussi discriminantes que la radiométrie | — | [5][42] |
| 27 | Morphologie mathématique | érosion / dilatation | **Fig. 4 (×3)** | [21][43][44] |
| 28 | Profils morphologiques et profils d'attributs | multi-échelle ; unités-régions | — | [45][46][16][47][48][49][50] |
| | | | | **4 min** |
| 29 | § **08 Méthodes variationnelles** | | | |
| 30 | Segmenter en minimisant une énergie | contours actifs, forces internes / externes | — | [29][51][52][53] |
| 31 | La fonctionnelle de Mumford–Shah | trois termes, un principe | — | [51] |
| 32 | Robustesse numérique et applications | level sets, modèles régionaux ; **convergence des cadres** | **Fig. 5 (a)(b)** | [54][55][52] |
| | | | | **4 min 30** |
| 33 | § **09 Apprentissage profond** | | | |
| 34 | 2012 : la bascule | représentation et décision apprises conjointement | — | [57][58][59] |
| 35 | Prédiction dense : FCN et encodeur–décodeur | FCN, U-Net, connexions de saut | **Fig. 6** | [60][62][63][64][65][61] |
| 36 | Contexte, échelles, modalités | ResNet, DeepLab/ASPP, FPN, multimodalité | — | [66][67][68][69][63][70] |
| 37 | Ce que l'apprentissage profond ne supprime pas | les notions sont reformulées ; trois limites | — | — |
| | | | | **5 min 30** |
| 38 | § **10 Transformers et modèles de fondation** | | | |
| 39 | L'attention en segmentation | dépendances longue portée ; Swin, SegFormer | — | [71][72][73][74] |
| 40 | Apprendre sans annotations | MAE ; archives abondantes / annotations rares | — | [75] |
| 41 | Modèles de fondation géospatiaux | généricité **et** coût énergétique | **Fig. 7** | [76][77][78][79][80] |
| | | | | **4 min** |
| 42 | § **11 Conclusion** | | | |
| 43 | Une histoire non linéaire | convergence de traditions ; rappel de la frise | frise | — |
| 44 | Défis ouverts | six défis + positionnement du domaine | — | — |
| | | | | **2 min 30** |
| 45 | Merci | planche de remerciement du thème | — | — |
| 46 | Crédits des figures | annexe | — | — |
| 47–51 | Références | annexe, 80 entrées | — | — |

*(Les numéros `[n]` de cette colonne sont ceux de l'article ; voir §6 pour la
correspondance avec ceux imprimés sur les planches.)*

---

## 4. Correspondance avec les sections de l'article

Les titres de section des transparents sont raccourcis pour tenir en gros corps
sur la planche de section ; le contenu et l'ordre sont ceux de l'article.

| § | Titre de l'article | Titre sur les transparents |
|---|---|---|
| 1 | Introduction | Introduction |
| 2 | Classification statistique : les premières approches pixel à pixel | Classification statistique pixel à pixel |
| 3 | Méthodes discriminantes et méthodes à noyaux | Méthodes discriminantes et à noyaux |
| 4 | Méthodes d'ensemble | Méthodes d'ensemble |
| 5 | Classification contextuelle et premiers modèles spatiaux | Classification contextuelle |
| 6 | Modèles markoviens et bayésiens | Modèles markoviens et bayésiens |
| 7 | Méthodes spectro-spatiales | Méthodes spectro-spatiales |
| 8 | Méthodes variationnelles et modèles énergétiques | Méthodes variationnelles |
| 9 | Apprentissage profond et segmentation sémantique | Apprentissage profond |
| 10 | Transformers et modèles de fondation | Transformers et modèles de fondation |
| 11 | Conclusion | Conclusion |

---

## 5. Figures : emplacement, légendes et droits

Les 7 figures de l'article — soit 14 sous-images — sont **toutes** reprises,
extraites du PDF sans recompression (`imgs/article/`). Aucune illustration
extérieure à l'article n'a été introduite ; les deux seuls éléments graphiques
ajoutés sont la frise du fil directeur et les encadrés de formules, qui sont des
éléments de structure et non des illustrations.

| Figure | Sous-images | Planche(s) | Crédit / copyright porté sur la planche |
|---|---|---|---|
| 1 | (a) image aérienne, (b) carte de segmentation | 4 | Jeu de données *Zeebruges*, publié par le comité technique d'analyse d'image et de fusion de données (IADF) de l'IEEE GRSS ; images et vérité terrain fournies par l'Académie royale militaire belge et l'ONERA — Laboratoire aérospatial français |
| 2 | (a) IKONOS, (b) pixel à pixel, (c) contextuelle | 10 *(a, b)* et 19 *(a, b, c)* | Image IKONOS, 4 m, 3 bandes, composition en fausses couleurs (infrarouge voisin, rouge, bleu) ; cartes de segmentation d'après [12] |
| 3 | (a) voisinage 1ᵉʳ ordre, (b) 2ᵈ ordre (+ cliques) | 22 | D'après [29] |
| 4 | érosion, image originale RVB, dilatation | 27 | Figure de l'article (aucune source tierce indiquée) |
| 5 | (a) SPOT, (b) segmentation variationnelle | 32 | Image satellitaire SPOT **© CNES** ; carte obtenue par la méthode variationnelle de [52] |
| 6 | architecture FCN | 35 | Base ISPRS *2D Semantic Labeling Challenge* (Potsdam) ; d'après [61] |
| 7 | principe d'un modèle de fondation géospatial | 41 | Figure de l'article (aucune source tierce indiquée) |

**Mécanique retenue.** Sous chaque image, une légende courte en gris
(`\legende`) identifie la sous-figure — « (a) image aérienne », « érosion »…
En pied de planche, au-dessus du filet, la ligne de crédit (`\sourcefoot`) suit
systématiquement le même patron : **légende factuelle + copyright + référence
bibliographique** `[n]`, sans renvoi en clair au numéro de figure de l'article.
Le renvoi vers l'article source `[80]` y figure sur chaque planche illustrée.
La planche 46 récapitule les sept crédits, précédés de la référence complète de
l'article.

**Point de vigilance.** Les figures 4 et 7 ne portent aucune attribution dans
l'article. Si elles proviennent d'une source tierce, il faut la faire remonter
avant diffusion ; en l'état, elles sont créditées à l'article lui-même. La
mention SPOT © CNES de la figure 5 doit être conservée telle quelle.

---

## 6. Citations et numérotation

- Les renvois apparaissent **dans le corps des planches** sous la forme `[n]`
  en gris (commande `\refc`), et sous forme développée dans les lignes de
  crédit (`\cite`).
- La bibliographie complète est imprimée en annexe (planches 47 à 51),
  `\nocite{*}` étant placé en tête de document pour que la numérotation suive
  l'ordre du fichier `references.bib`, lui-même calé sur l'ordre de l'article.
- **L'article source est lui-même référencé**, sous la clé
  `pastorino2026segmentation` : M. Pastorino, G. Moser, J. Zerubia,
  « Segmentation sémantique en télédétection », *Traitement du Signal et des
  Images* (TSI), GRETSI, décembre 2026. Il est saisi en fin de `.bib` et porte
  donc le numéro **[80]** ; volume, numéro et pages restent à compléter à la
  parution. Il est cité sur la page de titre, sur le sommaire, sur chaque
  planche illustrée et sur la planche de crédits.
- **Décalage à connaître** : l'article numérote deux fois la même référence
  (Samson *et al.*, 2000, en [52] **et** en [56]). Le fichier `.bib` ne la
  contient qu'une fois, sous la clé `samson2000variational`. Par conséquent :

  | Numéros dans l'article | Numéros sur les planches |
  |---|---|
  | [1] … [55] | identiques |
  | [56] | fusionné avec [52] |
  | [57] … [80] | [56] … [79] |
  | *(l'article lui-même)* | [80] |

  Chaque entrée de `references.bib` porte en commentaire son numéro d'origine
  (`% [nn]`), ce qui permet de retrouver la correspondance à tout moment.
- Le fichier `.bib` a été relu automatiquement contre la liste de références du
  PDF : année et premier auteur des 79 entrées reprises concordent.

---

## 7. Choix éditoriaux

**Ce qui a été conservé de l'article.** Les 11 sections et leur ordre ; les
cinq formules qui portent un argument (vecteur d'observations et règle
bayésienne §2, MAP markovien et énergie §6, Mumford–Shah §8) ; les 80 références
(79 entrées après fusion du doublon, plus l'article lui-même) ; les 7 figures ; les formulations
tranchées de l'article — « le problème cesse d'être une classification spectrale
pour devenir un problème d'interprétation spatiale », « différentes expressions
d'un même principe », « les modèles de fondation ne constituent pas une rupture
complète ».

**Ce qui a été ajouté.** Deux planches de synthèse sans équivalent direct dans
l'article, destinées à tenir le rythme de la session :

- planche 16, « Bilan de l'ère *pixel* » — pose explicitement l'alternative qui
  organise la suite (régulariser les étiquettes / enrichir les descripteurs) ;
- planche 37, « Ce que l'apprentissage profond ne supprime pas » — reformule le
  paragraphe de §9 sur la continuité conceptuelle, en le transformant en point
  d'appui pour la transition vers §10.

La frise du fil directeur (planches 6 et 43) traduit graphiquement la thèse
énoncée en §1 et §11.

**Ce qui a été volontairement laissé de côté.** Le détail des jeux de données ;
les développements sur les processus ponctuels marqués, mentionnés en §11 de
l'article mais non traités dans son corps ; l'énumération exhaustive des
applications par capteur. Rien de tout cela n'est nécessaire au fil directeur ;
tout est disponible dans l'article pour les questions.

**Densité.** Aucune planche ne dépasse six items de premier niveau. Les items de
second niveau ne servent qu'à énumérer (limites, forces, niveaux de contexte).
Les mises en évidence en rouge Inria portent sur les **termes techniques
structurants**, jamais sur des phrases entières : elles doivent rester lisibles
comme une trame de l'exposé si l'on parcourt la planche du regard.

---

## 8. Notes pour l'oral

- **Planche 9 → 10.** Les deux limites (Hughes, indépendance) sont énoncées
  avant l'image ; la figure 2 (a)–(b) sert de preuve visuelle. Laisser le temps
  de voir le bruit poivre et sel avant de commenter.
- **Planche 13.** Point de bascule du premier tiers : les SVM améliorent la
  *fonction de décision*, pas la *représentation*. C'est ce qui justifie que
  §5–§6 et §7 partent dans deux directions différentes.
- **Planche 19.** Même image qu'en planche 10, avec la carte contextuelle en
  plus. La répétition est délibérée : elle rend l'apport du contexte
  immédiatement lisible.
- **Planche 22.** L'unique équation à faire vraiment ressentir : `β` est le
  curseur entre fidélité et régularité. Tout le reste de l'exposé s'y raccroche.
- **Planche 32.** Dernière planche du bloc « modèles explicites ». C'est là
  qu'on annonce que bayésien, markovien, variationnel et graphes disent la même
  chose — puis on enchaîne sur l'apprentissage profond.
- **Planche 41.** Ne pas éluder le coût : l'article insiste sur l'empreinte
  environnementale et l'accessibilité des modèles de fondation pour la
  communauté scientifique. C'est un point d'accroche naturel pour les questions.
- **Questions probables** : place des CRF dans les architectures actuelles
  (planche 24) ; validation et généralisation géographique (planche 44) ;
  articulation entre modèles de fondation et modèles physiques du capteur.

---

## 9. Points à valider avant diffusion

1. **Affiliations** de la page de titre, en particulier le rattachement de
   Martina Pastorino (indiquée avec Gabriele Moser à l'Università di Genova,
   DITEN).
2. **Date exacte** de la session : le pied de page affiche « GRETSI 2027 »
   (`\date[…]{…}` dans `main.tex`).
3. **Droits des figures 4 et 7**, sans attribution dans l'article (cf. §5).
4. **Durée réelle** allouée à la session : le minutage du §3 vise 45 minutes.
   Pour 30 minutes, les candidates à la coupe sont les planches 16, 28, 36 et
   40, sans casser le fil directeur.
5. **Système de citations** : `biblatex` numérique et bibliographie complète en
   annexe, ou passage au système `\citb` / `\reffoot` de la soutenance de thèse
   (label court entre crochets et référence développée en bas de la planche de
   première citation).

---

## 10. Reproduire le document

```bash
cd Gretsi2027
make          # latexmk + LuaLaTeX + biber
make clean
```

Prérequis : LuaLaTeX, `biber`, `texlive-lang-french`, `biblatex`, `csquotes`,
`tikz`, `textpos`, `fmtcount`, `ifdraft`. Testé avec TeX Live 2023
(biblatex 3.19 / biber 2.19). Compiler depuis `Gretsi2027/` : le thème appelle
ses images par des chemins relatifs (`theme/imgs/…`).

Commandes maison définies dans `main.tex` : `\hl` (mise en évidence rouge
Inria), `\refc` (renvoi `[n]` en gris), `\legende` (légende sous figure),
`\sourcefoot` (crédit en pied de planche), `\formulebox` (encadré de formule),
`\filrouge` (frise du fil directeur), `\logounige` (logo Università di Genova).
Le dossier `theme/` reste identique à l'amont et n'a pas été modifié.
