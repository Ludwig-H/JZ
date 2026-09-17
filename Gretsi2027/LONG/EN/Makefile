PDFNAME = GRETSI2027_Semantic_Segmentation_Remote_Sensing_LONG.pdf
JOBNAME = GRETSI2027_Semantic_Segmentation_Remote_Sensing_LONG
# Le PDF compilé est déposé dans le dossier de la version française, à côté du sien.
OUTDIR  = ..

all: $(OUTDIR)/$(PDFNAME)

$(OUTDIR)/$(PDFNAME): main.tex references.bib
	latexmk -jobname=$(JOBNAME) main.tex
	@mv -f $(PDFNAME) $(OUTDIR)/$(PDFNAME)

clean:
	latexmk -jobname=$(JOBNAME) -C
	@rm -f $(JOBNAME).nav $(JOBNAME).snm $(OUTDIR)/$(PDFNAME)

.PHONY: all clean
