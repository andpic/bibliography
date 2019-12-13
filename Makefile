# LaTeX Makefile
all: clean pdf 

DOC_NAME=bibliography
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
	pdflatex -halt-on-error $(DOC_NAME).tex
	biber $(DOC_NAME)
	pdflatex -halt-on-error $(DOC_NAME).tex
	pdflatex -halt-on-error $(DOC_NAME).tex

.PHONY: html
html:
	htlatex $(DOC_NAME) $(HTLATEX_SETTINGS)
	biber $(DOC_NAME)
	htlatex $(DOC_NAME) $(HTLATEX_SETTINGS)
	htlatex $(DOC_NAME) $(HTLATEX_SETTINGS)

.PHONY: md
md:
	make html
	pandoc $(DOC_NAME).html -o $(DOC_NAME).md

