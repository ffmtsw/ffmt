project = "FFMT"
author = "Cesar Daniel Castro, Maria Kamila Diaz, Philip Hering, Andreas Junge"
release = "0.0"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
]

# Usar Inkscape como backend (más estable que cairosvg en RTD)
svg2pdf_converter = "inkscape"

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_title = "FFMT"
html_static_path = ["_static"]
html_css_files = ["custom.css"]

source_suffix = [".md", ".rst"]
myst_enable_extensions = ["colon_fence", "deflist", "fieldlist", "tasklist"]

# (Opcional) mejora de navegación en el menú lateral
html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
}
