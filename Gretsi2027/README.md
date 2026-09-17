# GRETSI 2027 — Segmentation sémantique en télédétection

Supports de présentation (Beamer, thème Inria + logo Università di Genova) pour
l'article **« Segmentation Sémantique en Télédétection »** de Martina
**Pastorino**, Gabriele **Moser** et Josiane **Zerubia**
([Inria RR-9631](https://inria.hal.science/hal-05742224), à paraître dans
*Traitement du Signal et des Images*, GRETSI).

**Quatre versions** — deux durées, deux langues — chacune dans son propre
dossier, complète et compilable indépendamment :

| Dossier | Langue | Planches | Destination | Structure |
|---|---|---|---|---|
| [`LONG/`](LONG/) | français | **51** | **usage général**, ≈ 45 min | 11 sections (celles de l'article), planches de section numérotées, bibliographie (79 réf.) et crédits des figures en annexe |
| [`LONG/EN/`](LONG/EN/) | anglais | **51** | idem | traduction de `LONG/`, même thème, mêmes figures, même numérotation |
| [`SHORT/`](SHORT/) | français | **24** | **GRETSI 2027**, ≈ 20 min | 6 sections, pas de planche de section, bibliographie réduite (54 réf., revues abrégées) |
| [`SHORT/EN/`](SHORT/EN/) | anglais | **24** | idem | traduction de `SHORT/` |

La **version longue est neutre** : aucune mention de colloque ni de date sur les
planches, son pied de page affiche le titre court. Elle se donne telle quelle en
séminaire, en cours ou en exposé invité. La **version courte reste celle du
GRETSI 2027**, dont elle porte le nom en sous-titre et en pied de page.

Chaque version est accompagnée d'un **support pour l'oral** : ce qu'il y a à
dire, planche par planche, avec le minutage ([`LONG/notes-orateur.md`](LONG/notes-orateur.md),
[`SHORT/notes-orateur.md`](SHORT/notes-orateur.md),
[`LONG/EN/speaker-notes.md`](LONG/EN/speaker-notes.md),
[`SHORT/EN/speaker-notes.md`](SHORT/EN/speaker-notes.md)).

Les deux versions françaises sont issues d'une **reconstruction** des PDF
envoyés par Martina Pastorino le 11 septembre 2026 ; ces PDF sont conservés tels
quels dans `LONG/reference/` et `SHORT/reference/`. Les sources s'en écartent
désormais **volontairement** — vraies guillemets françaises dans les deux, et
retrait de la mention du colloque dans la longue — mais le **texte des planches
reste identique, mot pour mot**. Voir la section « Rapport au PDF de référence »
de chaque sous-dossier.

> **Guillemets.** Les deux versions françaises chargent `[T1]{fontenc}` et
> `lmodern`. C'est indispensable : en OT1, l'encodage par défaut, babel-french
> compose « et » avec les signes *mathématiques* ≪ et ≫ de la fonte CMSY, qui
> n'en ont ni le dessin ni la chasse. Latin Modern reprend le dessin de Computer
> Modern et fournit T1 en Type 1. Les versions anglaises n'en ont pas besoin et
> restent sur Computer Modern.

```
Gretsi2027/
├── LONG/      la version longue  (main.tex, references.bib, notes-orateur.md, theme/, imgs/, reference/)
│   ├── *.pdf  les deux PDF compilés, français et anglais
│   └── EN/    la même, en anglais (main.tex, references.bib, speaker-notes.md, theme/, imgs/)
├── SHORT/     la version courte  (idem)
│   ├── *.pdf
│   └── EN/
└── article/   l'article source (PDF) et son texte extrait
```

Les quatre PDF compilés sont versionnés, et **ceux des versions anglaises sont
déposés à côté de leur version française** : `make` depuis `LONG/EN/` écrit dans
`LONG/`, `make` depuis `SHORT/EN/` écrit dans `SHORT/`.

## Compilation

Dans l'un quelconque des quatre dossiers :

```bash
make        # latexmk + pdfLaTeX + biber
make clean
```

Prérequis : **pdfLaTeX**, `biber`, `texlive-lang-french` (babel), `biblatex`,
`csquotes`, et les paquets appelés par le thème (`tikz`, `textpos`, `fmtcount`,
`calc`, `ifdraft`). Les fontes Inria Sans sont **optionnelles** : sans elles le
thème émet un avertissement et utilise la fonte sans-serif par défaut ; pour les
activer, déposer [`latex-inria-fonts`](https://gitlab.inria.fr/gabarits/latex-inria-fonts)
à la racine du sous-dossier (le `latexmkrc` l'ajoute déjà à `TEXINPUTS`).

⚠️ Le thème référence ses images par des chemins **relatifs à la racine de
compilation** (`theme/imgs/...`) : compiler depuis le dossier de la version
(`LONG/`, `LONG/EN/`, `SHORT/`, `SHORT/EN/`), pas depuis `theme/`.

> **Moteur.** Les deux projets compilent avec **pdfLaTeX**, le moteur utilisé
> pour les PDF de référence : c'est ce qui permet de les reproduire à
> l'identique, fontes Computer Modern comprises. **LuaLaTeX fonctionne aussi**
> (mêmes planches, même pagination, fontes Latin Modern) : il suffit de
> remplacer les deux dernières lignes du `latexmkrc` par `$pdf_mode = 4;`.
>
> Le thème teste la primitive `\draftmode`, que pdfTeX ne fournit que depuis
> TeX Live 2024 (auparavant `\pdfdraftmode`). Les deux `main.tex` définissent
> l'alias qui manque, si bien que le projet compile aussi avec des TeX Live
> plus anciens.

## Provenance

- Le thème `theme/` est copié tel quel depuis
  [`Ludwig-H/Manuscrit-de-th-se`](https://github.com/Ludwig-H/Manuscrit-de-th-se/tree/main/Soutenance/soutenance/theme)
  (`Soutenance/soutenance/theme`), sans modification.
- Les figures de `imgs/article/` ont été extraites du PDF de l'article avec
  `pypdf` puis renommées d'après les légendes ; ce sont les images d'origine,
  non recompressées. Les quatre dossiers en contiennent le jeu complet, même si
  la version courte n'en utilise qu'une partie.
- Les logos Università di Genova (`imgs/logos/`) proviennent de l'archive
  fournie avec l'article.
- Les deux versions anglaises ont été **traduites automatiquement** sous
  glossaire commun, puis relues morceau par morceau contre le français
  (structure LaTeX, clés de citation, mises en évidence, terminologie) et
  harmonisées sur l'ensemble du deck. Elles n'ont pas été relues par un
  anglophone : une passe humaine sur les titres de planche reste souhaitable
  avant diffusion.
