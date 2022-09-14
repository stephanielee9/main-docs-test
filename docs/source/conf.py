# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html


# -- General Setup -----------------------------------------------------------
from typing import List

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Test'
copyright = '2022, SLee'
author = 'SLee'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # "nbsphinx",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.mathjax",  # math rendering in html
    "sphinx.ext.napoleon",
]

# since our notebooks can involve network I/O (or even costing $), we don't want them to be
# run every time we build the docs. Instead, just use the pre-executed outputs.
nbsphinx_execute = "never"

# In addition, we set the mathjax path to v3, which allows \ket{} (and other commands) to render
mathjax_path = "https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"
autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = []

# Using `modules` in index.rst gets the first package and ignores additional included packages.
# Listing out modules explicitly causes building docs to throw error looking for `modules.rst`,
# so add to excluded search patterns as per suggestion here: https://stackoverflow.com/a/15438962
exclude_patterns: List[str] = ["modules.rst"]


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
