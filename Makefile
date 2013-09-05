SLIDESDIR=slides
SLIDESNAME=index.html
SLIDES=$(SLIDESDIR)/$(SLIDESNAME)

$(SLIDES): mkslides.py qualificacao.ipynb $(SLIDESDIR)/custom.css
	python $<

serve: $(SLIDES)
	firefox http://localhost:8000/$(SLIDESAME) &
	cd $(SLIDESDIR); python -m SimpleHTTPServer 8000

