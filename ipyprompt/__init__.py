from .prompt import setup_prompt
from .magic import prompt_theme

def load_ipython_extension(ip):
    setup_prompt(ip)
    ip.register_magic_function(prompt_theme, 'line')
