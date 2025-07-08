from IPython.terminal.prompts import Prompts, Token
from time import time, strftime, localtime
from traitlets import Unicode
from traitlets.config import Configurable
from prompt_toolkit.styles import Style, merge_styles

class CustomPrompt(Prompts):
    def in_prompt_tokens(self, cli=None):
        return [
            # (Token.PromptTime, strftime("[%H:%M:%S]\n", localtime())),
            (Token.PromptIn, 'In ['),
            (Token.PromptIn, str(self.shell.execution_count)),
            (Token.PromptIn, ']: '),
            (Token.PromptInArrow, ' '),
        ]

    def out_prompt_tokens(self):
        return [
            # (Token.PromptTime, strftime("[%H:%M:%S]\n", localtime())),
            (Token.PromptOut, 'Out ['),
            (Token.PromptOut, str(self.shell.execution_count)),
            (Token.PromptOut, ']: '),
            (Token.PromptOutArrow, ' '),
        ]

class VarWatcher(object):
    def __init__(self, ip):
        self.shell = ip
        self.t_pre = time()
        self.texc = 0
        self.prev_texc = 0

    def pre_execute(self):
        self.t_pre = time()

    def post_execute(self):
        self.prev_texc = self.texc
        self.texc = time() - self.t_pre

        print('[{}s]'.format('{}'.format(self.texc)[:7]) + " @ " + strftime("[%H:%M:%S]", localtime()))
        # Only add or update user namespace var if it is safe to do so
        if 'texc' not in self.shell.user_ns or \
                self.shell.user_ns['texc'] == self.prev_texc:
            self.shell.push({'texc': self.texc})
        else:
            pass

def setup_prompt(ip):

    ip.prompts = CustomPrompt(ip)

    vw = VarWatcher(ip)
    ip.events.register('pre_execute', vw.pre_execute)
    ip.events.register('post_execute', vw.post_execute)
