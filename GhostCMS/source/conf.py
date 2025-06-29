# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

#import sphinx_simplepdf

project = 'Getting CMS Up & Running'
copyright = '2025, Alexander B.'
author = 'Alexander B.'
release = '06-2025'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.mathjax",
    "sphinx.ext.imgmath",
    "sphinx_simplepdf",
    #"sphinx_simplepdf",
]

templates_path = ['_templates']
include_patterns = ['*.rst', '*.md']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'classic'
html_static_path = ['_static']

# -- Options for simplepdf output --------------------------------------------
simplepdf_css = '_static/simplepdf_alex.css'
simplepdf_coverpage = True
simplepdf_toc_depth = 3
simplepdf_title = 'Getting CMS Up & Running'
simplepdf_author = 'Alexander B.'
simplepdf_file_name = 'cms-setup-guide.pdf'
simplepdf_vars = {
    'primary': "#1A961A",
    'secondary': "#379683",
    'cover': "#FFFFFF",
    'links': "#790000",
    'bottom-center-content': '"Getting CMS Up & Running"',
    'bottom-right-content': '"Alexander B."',
}
