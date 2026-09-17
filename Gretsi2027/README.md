# GRETSI 2027 — Segmentation sémantique en télédétection

Supports de présentation (Beamer, thème Inria + logo Università di Genova) pour
l'article **« Segmentation Sémantique en Télédétection »** de Martina
**Pastorino**, Gabriele **Moser** et Josiane **Zerubia**
([Inria RR-9631](https://inria.hal.science/hal-05742224), à paraître dans
*Traitement du Signal et des Images*, GRETSI).

**Quatre versions** — deux durées, deux langues — chacune dans son propre
dossier, complète et compilable indépendamment :

| Dossier | Langue | Planches | Format | Structure |
|---|---|---|---|---|
| [`LONG/`](LONG/) | français | **51** | session historique, ≈ 45 min | 11 sections (celles de l'article), planches de section numérotées, bibliographie (79 réf.) et crédits des figures en annexe |
| [`LONG/EN/`](LONG/EN/) | anglais | **51** | idem | traduction de `LONG/`, même thème, mêmes figures, même numérotation |
| [`SHORT/`](SHORT/) | français | **24** | exposé resserré, ≈ 20 min | 6 sections, pas de planche de section, bibliographie réduite (54 réf., revues abrégées) |
| [`SHORT/EN/`](SHORT/EN/) | anglais | **24** | idem | traduction de `SHORT/` |

Chaque version est accompagnée d'un **support pour l'oral** : ce qu'il y a à
dire, planche par planche, avec le minutage ([`LONG/notes-orateur.md`](LONG/notes-orateur.md),
[`SHORT/notes-orateur.md`](SHORT/notes-orateur.md),
[`LONG/EN/speaker-notes.md`](LONG/EN/speaker-notes.md),
[`SHORT/EN/speaker-notes.md`](SHORT/EN/speaker-notes.md)).

Les deux versions françaises sont issues d'une **reconstruction** des PDF
envoyés par Martina Pastorino le 11 septembre 2026 ; ces PDF sont conservés tels
quels dans `LONG/reference/` et `SHORT/reference/`. Chaque `main.tex` français
**reproduit son PDF de référence à l'identique** : mêmes fontes, mêmes césures,
mêmes positions de texte et d'images (écart maximal relevé : 0,1 point sur
75 planches). Voir la section « Fidélité au PDF de référence » de chaque
sous-dossier.

```
Gretsi2027/
├── LONG/      la version longue  (main.tex, references.bib, notes-orateur.md, theme/, imgs/, reference/)
│   └── EN/    la même, en anglais (main.tex, references.bib, speaker-notes.md, theme/, imgs/)
├── SHORT/     la version courte  (idem)
│   └── EN/
└── article/   l'article source (PDF) et son texte extrait
```

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
