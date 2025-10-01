project = "FFMT Documentation"
author = "FFMT Team"
author = "Cesar Daniel Castro"
author = "Maria Kamila Diaz"
author = "Philip Hering"
author = "Andreas Junge"
release = "0.0"

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = []

html_theme = "sphinx_rtd_theme"
html_title = "FFMT"
html_static_path = ["_static"]

source_suffix = [".md", ".rst"]
myst_enable_extensions = ["colon_fence", "deflist", "fieldlist", "tasklist"]
