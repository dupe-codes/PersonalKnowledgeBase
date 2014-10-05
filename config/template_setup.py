"""
Setup for the jinja2 templating engine
"""

import jinja2
import os
from settings import TEMPLATE_PATH

# Tells jinja where to find templates and initializes the environment
TEMPLATE_ENV = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), TEMPLATE_PATH))
)
