# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "monte carlo methods"
copyright = "2023, li weihua"
author = "li weihua"
release = "0.0.1"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_proof",
    "myst_parser",
    "sphinxcontrib.katex",
    "sphinx_copybutton",
]


import sphinxcontrib.katex as katex

latex_macros = r"""
    \def \Z  {\mathbb{Z}}
    \def \R  {\mathbb{R}}
    \def \P  {\mathbb{P}}
    \def \E  {\mathbb{E}}
    \def \x  {\mathbf{x}}
"""

# Translate LaTeX macros to KaTeX and add to options for HTML builder
katex_macros = katex.latex_defs_to_katex_macros(latex_macros)
katex_options = "macros: {" + katex_macros + "}"

# Add LaTeX macros for LATEX builder
latex_elements = {"preamble": latex_macros}

# Pre-rending not support latex macros,
# see https://github.com/hagenw/sphinxcontrib-katex/issues/65
# When this bug fixed, we can set this option to true.
katex_prerender = False


templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# TODO: 1. sphinx_rtd_theme conflict with sphinx-proof
#       2. sphinx_book_theme conflict with katex
# html_theme = "sphinx_rtd_theme"
# html_theme = "sphinx_book_theme"
html_theme = "alabaster"
html_static_path = ["_static"]
