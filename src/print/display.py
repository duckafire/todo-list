from sys import exit

from .      import shell_colors as scolors
from ..     import info, options
from ..args import flags

def verbose_info(color):
    if not options.get(flags.VERBOSE):
        return None

    filename = None
    lineno   = None

    try:
        filename = __file__
    except NameError:
        filename = "???.?"

    try:
        lineno = __line__
    except NameError:
        lineno = "??"

    print(color, f"Line: {lineno}, File: {filename}", scolors.END)

def display(color, tag, *args):
    color    = color.upper()
    boldc    = getattr(scolors, "BOLD_" + color)
    regularc = getattr(scolors, color)

    verbose_info(regularc)
    print(f"{boldc}[{info.name()}: {tag}]{scolors.END}{regularc}", *args)
    print(scolors.END)

def message(*args):
    display("white", "message", *args)

def warning(*args):
    display("yellow", "warning", *args)

def error(*args):
    display("red", "error", *args)
    exit(1)

def verbose(*args):
    if options.get(flags.VERBOSE):
        display("white", "verbose", *args)

__all__ = ["message", "warning", "error", "verbose"]
