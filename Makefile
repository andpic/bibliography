# LaTeX Makefile
all: clean pdf 

BASENAME=bibliography
TEXNAME=$(BASENAME).tex
BIBNAME=$(BASENAME).bib
HTMLNAME=$(BASENAME).html
MDNAME=$(BASENAME).md
HTLATEX_SETTINGS="html,charset=utf-8" " -cunihtf -utf8"
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
		*.xdy \
		*.4ct \
		*.4tc \
		*.css \
		*.dvi \
		*.html \
		*.idv \
		*.lg \
		*.tmp \
		*.xref \
		*.png

.PHONY: pdf
pdf:
	pdflatex -halt-on-error $(TEXNAME)
	biber $(BASENAME)
	pdflatex -halt-on-error $(TEXNAME)
	pdflatex -halt-on-error $(TEXNAME)

.PHONY: html
html:
	htlatex $(BASENAME) $(HTLATEX_SETTINGS)
	biber $(BASENAME)
	htlatex $(BASENAME) $(HTLATEX_SETTINGS)
	htlatex $(BASENAME) $(HTLATEX_SETTINGS)

.PHONY: md
md:
	make html
	pandoc $(HTMLNAME) -o $(MDNAME)

