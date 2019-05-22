Tworzenie dokuemntacji w sphinxie
======================================

Diagramy UML
+++++++++++++++++++++++++++



Paczka dla windowsa.
.. Graphviz_:  https://graphviz.gitlab.io/_pages/Download/Download_windows.html

config
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
    'sphinx.ext.graphviz',
    'sphinxcontrib.plantuml',
    "sphinx.ext.inheritance_diagram",
    'sphinx_automodapi.automodapi'
]



 easy_install sphinxcontrib-sdedit

Przykładowy diagram
.. graphviz::

   digraph foo {
      "bar" -> "baz";
   }

Generowanie diagramów #TODO
z jakiegoś dziwnego powodu kopiowanie poniższego -
 ustawianie ścieżki dziła i diagram się generuje; ale ustawienie jej jako zmiennej środowiskowej już nie działao o.Ó


SET SPHINXOPTS=-D graphviz_dot="C:\Program Files (x86)\Graphviz2.38\bin\dot.exe"
make html

pip install sphinxcontrib-plantuml

extensions = ['sphinxcontrib.plantuml']


Regardless of the existence of the GRAPHVIZ_DOT environment variable, the path to the Graphviz bin folder is apparently required to be in the PATH variable as well.