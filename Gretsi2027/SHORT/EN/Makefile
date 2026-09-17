PDFNAME = GRETSI2027_Semantic_Segmentation_Remote_Sensing_SHORT.pdf
JOBNAME = GRETSI2027_Semantic_Segmentation_Remote_Sensing_SHORT

all: $(PDFNAME)

$(PDFNAME): main.tex
	latexmk -jobname=$(JOBNAME) main.tex

clean:
	latexmk -jobname=$(JOBNAME) -C
	@rm -f $(JOBNAME).nav $(JOBNAME).snm

.PHONY: all clean
