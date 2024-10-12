# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'RecipEase'
copyright = '2024, Ben Phillips'
author = 'Ben Phillips'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']

import os
import sys
import django

# Add the project path
sys.path.insert(0, os.path.abspath('../src'))

# Set the Django settings module (replace with your settings file)
os.environ['DJANGO_SETTINGS_MODULE'] = 'recipe_project.settings'

# Initialize Django
django.setup()

# Sphinx extensions
extensions = [
    'sphinx.ext.autodoc',        # Automatically documents your code
    'sphinx.ext.napoleon',       # Supports Google-style docstrings
    'sphinx.ext.viewcode',       # Adds links to the source code
    'sphinx.ext.todo',           # Includes TODOs in your docs
    'autoapi.extension',         # Automatically generates API docs
    'sphinx_autodoc_typehints',  # Adds type hints to the documentation
]

# AutoAPI configuration
autoapi_type = 'python'
autoapi_dirs = ['../src']  # Path to your Django app
