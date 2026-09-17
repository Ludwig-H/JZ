# English version — 24 slides

English translation of [`../main.tex`](../main.tex): same Inria theme, same
figures, same 24 slides, same bibliography and the same `[n]` numbering.

`make` produces `GRETSI2027_Semantic_Segmentation_Remote_Sensing_SHORT.pdf`
**in the parent folder**, next to the French PDF. Requirements and a note on
the engine: see the [README one level up](../../README.md#compilation).

## What the folder holds

```
SHORT/EN/
├── main.tex           the talk (6 sections, 24 slides)
│                   (the built PDF lands in ../, beside the French one)
├── references.bib     54 entries, journals and conferences abbreviated
├── speaker-notes.md   what to say, slide by slide
│                   (its PDF lands in ../ too — see ../../tools/notes-pdf.py)
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
  quote, the quotes are dropped.
- `references.bib` keeps the French title of the source paper. The
  `\NoAutoSpacing` wrapper around the HAL URL is gone: it belongs to
  babel-french.
- The French version loads `fontenc`/`lmodern` to get proper French guillemets;
  English needs neither, so this deck stays on Computer Modern. Add
  `\usepackage[T1]{fontenc}\usepackage{lmodern}` if you want the two decks to
  use exactly the same font.
- **Slide 9**: the broken `[haralick1985image]` citation of the French version
  is *fixed* here — the key is simply dropped from the `\biblio` line. The
  French version keeps it only because it has to reproduce Martina Pastorino's
  PDF exactly; this one has no such constraint.

Everything else — macros, layout, column widths, figure sizes, citation keys —
is identical to the French file, including the removal of the four
vertical-alignment calibrations that only served to match a reference PDF.

## Checks run on the built PDF

| | result |
|---|---|
| slides | 24, as in the French version |
| figures | the same number on every one of the 24 slides |
| overfull boxes | come from the theme, not from the text (the French version, now on Latin Modern, has 2 hbox / 2 vbox) |
| text outside the frame | none |
| body colliding with the bottom reference band | none |
| French left in the source | none, outside proper nouns and the paper's own title |

## Translation

Produced by machine translation under a shared glossary, then checked chunk by
chunk against the French (structure, citation keys, emphasis, terminology) and
harmonized across the whole deck. **It has not been proofread by a native
speaker**: before the talk, a human pass over the slide titles and the
highlighted phrases is worth the time.
