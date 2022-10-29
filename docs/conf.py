from datetime import datetime


project = 'Random Profile Generator'
description = 'A random profile generator for testing purposes.'
copyright = '2022, Deeapk Raj'
author = 'Deeapk Raj'
release = '0.2.3'

extensions = [
    'sphinx.ext.autosectionlabel'
]

releases_github_path = "Py-Contributors/RandomProfileGenerator"

autosectionlabel_prefix_document = True

templates_path = ['_templates']
source_suffix = ".rst"
master_doc = "index"
year = datetime.now().year
copyright = "{} Deepak Raj".format(year)

html_theme = 'sphinx_rtd_theme'  # 'pydata_sphinx_theme' 'alabaster'

html_static_path = ['_static']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '.venv']
html_sidebars = { '**': ['globaltoc.html', 'relations.html', 'sourcelink.html', 'searchbox.html'] }