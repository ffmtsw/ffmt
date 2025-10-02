project = "FFMT"
author = "Cesar Daniel Castro, Maria Kamila Diaz, Philip Hering, Andreas Junge"
release = "0.0"
language = "en"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
# html_theme = "furo"
# html_theme_options = {
#    "light_logo": "_static/ffmt-logo.png",
#    "dark_logo": "_static/ffmt-logo.png",
#    "light_css_variables": {
#        "color-brand-primary": "#0aa",
#        "color-brand-content": "#0aa",
#    },
#    "dark_css_variables": {
#        "color-brand-primary": "#5fd",   # más claro en dark
#        "color-brand-content": "#5fd",
#    },
#}

html_title = "FFMT"
html_static_path = ["_static"]
html_logo = "_static/images/general/logo_ffmt.png"
html_favicon = "_static/images/general/logo_ffmt.png"
html_css_files = ["custom.css"]

source_suffix = [".md", ".rst"]
myst_enable_extensions = ["colon_fence", "deflist", "fieldlist", "tasklist"]

html_theme_options = {
    "logo_only": True,                  
    "collapse_navigation": False,
    "navigation_depth": 4,
}

