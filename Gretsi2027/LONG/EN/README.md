# English version — 51 slides

English translation of [`../main.tex`](../main.tex): same Inria theme, same
figures, same 51 slides, same bibliography and the same `[n]` numbering. The
only intended difference is the language.

Like the French version, this deck is meant for **general use** — seminar,
course, invited talk: no conference name and no date anywhere on the slides.

`make` produces `GRETSI2027_Semantic_Segmentation_Remote_Sensing_LONG.pdf`
**in the parent folder**, next to the French PDF. Requirements and a note on
the engine: see the [README one level up](../../README.md#compilation).

## What the folder holds

```
LONG/EN/
├── main.tex           the talk (11 sections, 51 slides)
│                   (the built PDF lands in ../, beside the French one)
├── references.bib     79 entries — the French .bib, English comments, same order
├── speaker-notes.md   what to say, slide by slide
├── imgs/, theme/      the same figures and the same theme as the French version
├── latexmkrc          TEXINPUTS → theme/, pdfLaTeX
└── Makefile           `make` / `make clean`
```

## What changes, besides the words

- `\usepackage[english]{babel}`, so biblatex writes `In:`, `and`, `1st ed.`
  instead of `In :`, `et`, `1re éd.`, and the French thin space before `:` `;`
  `?` `!` disappears.
- `\thankyou` becomes *Thank you for your attention.*, the table of contents is
  *Outline*, and the five boxes of the running-thread frieze (`\filrouge`) are
  in English.
- French guillemets become `\enquote{...}`; where English simply does not
  quote (`« transformers »`, `« poivre et sel »`), the quotes are dropped.
- `references.bib` keeps the French title of the source paper, as one does for
  a work published in French. The `\NoAutoSpacing` wrapper around the HAL URL
  is gone: that macro belongs to babel-french.
- The French version loads `fontenc`/`lmodern` to get proper French guillemets;
  English needs neither, so this deck stays on Computer Modern. Add
  `\usepackage[T1]{fontenc}\usepackage{lmodern}` if you want the two decks to
  use exactly the same font.

Everything else — macros, layout, column widths, figure sizes, citation keys —
is identical to the French file.

## Checks run on the built PDF

| | result |
|---|---|
| slides | 51, as in the French version |
| figures | the same number on every one of the 51 slides |
| overfull boxes | 14 hbox / 13 vbox — exactly the French profile, so the English text adds none |
| text outside the frame | none |
| body colliding with the bottom reference band | none (the tightest slide, 10, has slightly more clearance than the French) |
| French left in the source | none, outside proper nouns and the paper's own title |

## Translation

Produced by machine translation under a shared glossary, then checked chunk by
chunk against the French (structure, citation keys, emphasis, terminology) and
harmonized across the whole deck. **It has not been proofread by a native
speaker**: before the talk, a human pass over the slide titles and the
highlighted phrases is worth the time.
