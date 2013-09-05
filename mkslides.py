"""
Custom slide converter to use a local copy of reveal.js.

Credit to Damian Avila (http://www.damian.oquanta.info/)

Source: http://nbviewer.ipython.org/urls/gist.github.com/damianavila/5970218/raw/1e84a3fcc714b58384b8d0261075d496ba221430/using_local_reveal.ipynb
"""
from IPython.nbconvert.exporters import SlidesExporter
from IPython.config import Config
from IPython.nbformat import current as nbformat

infile = "qualificacao.ipynb"
outfile = "slides/index.html"
notebook = open(infile).read()
notebook_json = nbformat.reads_json(notebook)
# This is the config object I talked before, in the 'url_prefix',
# you can set you proper location of your local reveal.js library,
# i.e. if the reveal.js is located in the same directory as your
# your_slideshow.reveal.html, then set 'url_prefix':'reveal.js'.
c = Config({
    'RevealHelpTransformer':{
        'enabled':True,
        'url_prefix':'reveal.js',
    },})
exportHtml = SlidesExporter(config=c)
(body,resources) = exportHtml.from_notebook_node(notebook_json)
open(outfile, 'w').write(body.encode('utf-8'))
