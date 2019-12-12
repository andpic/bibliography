# LaTeX Makefile
all: clean pdf 

BASENAME=bibliography
TEXNAME=$(BASENAME).tex
BIBNAME=$(BASENAME).bib
RM=rm -f

.PHONY: clean
clean:
	$(RM) \
		*.acn \
		*.acr \
		*.alg \
		*.aux \
		*.bbl \
		*.bcf \
		*.blg \
		*-blx.bib \
		*.fdb_latexmk \
		*.fls \
		*.glg \
		*.glo \
		*.gls \
		*.idx \
		*.ind \
		*.ilg \
		*.lof \
		*.loa \
		*.lol \
		*.log \
		*.lot \
		*.run.xml \
		*.toc \
		*.out \
		*.xdy

.PHONY: pdf
pdf:
	pdflatex -halt-on-error $(TEXNAME)
	biber $(BASENAME)
	pdflatex -halt-on-error $(TEXNAME)
	pdflatex -halt-on-error $(TEXNAME)

.PHONY: html
html:
	htlatex $(TEXNAME) "xhtml_mathjax.cfg, charset=utf-8" " -cunihtf -utf8"
	biber $(BASENAME)
	htlatex $(TEXNAME) "xhtml_mathjax.cfg, charset=utf-8" " -cunihtf -utf8"

