# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add the root of the project (two levels up) to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# -- Project information ----------------------------------------------------
project = 'Stock Analysis API'
copyright = '2025, Ovidiu Suciu'
author = 'Ovidiu Suciu'
release = '1.0'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',       # Extract docstrings from modules
    'sphinx.ext.napoleon',      # Support for Google/NumPy-style docstrings
    'sphinx.ext.viewcode',      # Add source code links
    'myst_parser',              # Optional: Markdown support
]

# File types supported
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Template and static file paths
templates_path = ['_templates']
exclude_patterns = []

# Autodoc options
autodoc_default_options = {
    'members': True,
    'undoc-members': True,
    'show-inheritance': True,
}

# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False

# -- Options for HTML output -------------------------------------------------

# Use Read the Docs theme (recommended)
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
