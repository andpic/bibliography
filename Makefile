# LaTeX Makefile
all: clean biblist 

.PHONY: clean
clean:
	rm	-f \
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

.PHONY: biblist
biblist:
	pdflatex -halt-on-error biblist.tex
	biber biblist
	pdflatex -halt-on-error biblist.tex
	pdflatex -halt-on-error biblist.tex

.PHONY: html
html:
	htlatex biblist.tex "xhtml_mathjax.cfg, charset=utf-8" " -cunihtf -utf8"
	biber biblist
	htlatex biblist.tex "xhtml_mathjax.cfg, charset=utf-8" " -cunihtf -utf8"

.PHONY: update
update: 
	pdflatex -halt-on-error -shell-escape $(FILE)

