from IPython.terminal.prompts import Token

classic = {
        Token.PromptIn: "fg:ansiblack bg:ansigreen",
        Token.PromptInArrow: "fg:ansigreen",
        Token.PromptOut: "fg:ansiblack bg:ansired",
        Token.PromptOutArrow: "fg:ansired",
        Token.PromptTime: "fg:ansigray",
        }

cool = {
        Token.PromptIn: "fg:ansiblack bg:ansiblue",
        Token.PromptInArrow: "fg:ansiblue",
        Token.PromptOut: "fg:ansiblack bg:ansimagenta",
        Token.PromptOutArrow: "fg:ansimagenta",
        Token.PromptTime: "fg:ansigray",
        }

THEMES = {
        "classic": classic,
        "cool": cool,
        }
