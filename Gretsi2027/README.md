# GRETSI 2027 — Segmentation sémantique en télédétection

Supports de présentation (Beamer, thème Inria + logo Università di Genova) pour
l'article **« Segmentation Sémantique en Télédétection »** de Martina
**Pastorino**, Gabriele **Moser** et Josiane **Zerubia**
([Inria RR-9631](https://inria.hal.science/hal-05742224), à paraître dans
*Traitement du Signal et des Images*, GRETSI).

Deux versions, chacune dans son propre sous-dossier, complète et compilable
indépendamment :

| Dossier | Planches | Format | Structure |
|---|---|---|---|
| [`LONG/`](LONG/) | **51** | session historique, ≈ 45 min | 11 sections (celles de l'article), planches de section numérotées, bibliographie (79 réf.) et crédits des figures en annexe |
| [`SHORT/`](SHORT/) | **24** | exposé resserré, ≈ 20 min | 6 sections, pas de planche de section, bibliographie réduite (54 réf., revues abrégées) |

Les deux dossiers sont issus d'une **reconstruction** des PDF envoyés par
Martina Pastorino le 11 septembre 2026 ; ces PDF sont conservés tels quels dans
`LONG/reference/` et `SHORT/reference/`. Chaque `main.tex` **reproduit son PDF
de référence à l'identique** : mêmes fontes, mêmes césures, mêmes positions de
texte et d'images (écart maximal relevé : 0,1 point sur 75 planches). Voir la
section « Fidélité au PDF de référence » de chaque sous-dossier.

```
Gretsi2027/
├── LONG/      la version longue  (main.tex, references.bib, theme/, imgs/, reference/)
├── SHORT/     la version courte  (idem)
└── article/   l'article source (PDF) et son texte extrait
```

## Compilation

Dans l'un ou l'autre sous-dossier :

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
compilation** (`theme/imgs/...`) : compiler depuis `LONG/` ou `SHORT/`, pas
depuis `theme/`.

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
  non recompressées. Les deux sous-dossiers en contiennent le jeu complet, même
  si la version courte n'en utilise qu'une partie.
- Les logos Università di Genova (`imgs/logos/`) proviennent de l'archive
  fournie avec l'article.
