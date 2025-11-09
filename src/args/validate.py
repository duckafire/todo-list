from .       import flags, help_info as info
from ..      import options
from ..print import display

# they are invalid when used out
# from the 1st argument position
INVALID_INFO_FLAGS = (
    flags.HELP,
    flags.LICENSE,
    flags.VERSION,
)

def is_flag(arg, flags):
    EXTEN_F = flags[0]
    SHORT_F = (flags[1] if len(flags) == 2 else EXTEN_F[0])

    ARG_LEN = len(arg)

    return (ARG_LEN > 1 and SHORT_F == arg[1:]) \
        or (ARG_LEN > 2 and EXTEN_F == arg[2:])

def info_flags(arg):
    if is_flag(arg, flags.HELP):
        info.help()

    if is_flag(arg, flags.LICENSE):
        info.license()

    if is_flag(arg, flags.VERSION):
        info.version()

def invalid_process_flag(arg):
    for flag in INVALID_INFO_FLAGS:
        if is_flag(arg, flag):
            display.error(f"Invalid use of flag: '{flag}'\n")

def process_flags(*argv):
    if len(argv) == 0:
        return

    for arg in argv:
        invalid_process_flag(arg)

        if is_flag(arg, flags.REPLACE):
            options.set(flags.REPLACE, arg)

        elif is_flag(arg, flags.VERBOSE):
            options.set(flags.VERBOSE, arg)

        else:
            display.error(f"Invalid flag: '{arg}'\n")

def validate(*argv):
    if len(argv) == 0:
        info.default()

    info_flags(argv[0])
    process_flags(*argv)

    if options.get(flags.VERBOSE):
        display.message( options.str(flags.REPLACE) )
        display.message( options.str(flags.VERBOSE) )

__all__ = ["validate"]
