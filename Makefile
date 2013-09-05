SLIDESDIR=slides
SLIDES=$(SLIDESDIR)/index.html

$(SLIDES): qualificacao.ipynb $(SLIDESDIR)/custom.css
	ipython nbconvert --to slides --stdout $< > $@

serve: $(SLIDES)
	firefox http://localhost:8000/$(SLIDES)?theme=night?transition=none &
	python -m SimpleHTTPServer 8000

