PDFNAME = GRETSI2027_Segmentation_Semantique_Teledetection.pdf
JOBNAME = GRETSI2027_Segmentation_Semantique_Teledetection

all: $(PDFNAME)

$(PDFNAME): main.tex
	latexmk -jobname=$(JOBNAME) main.tex

clean:
	latexmk -jobname=$(JOBNAME) -C
	@rm -f $(JOBNAME).nav $(JOBNAME).snm

.PHONY: all clean
