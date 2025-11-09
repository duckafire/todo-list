from .print import display

list = {
    "replace": False,
    "verbose": False,
}

def is_valid(flag, flag_value = False, arg = None):
    if arg == None:
        arg = flag[0]

    if flag[0] not in list:
        display.error(f"Invalid flag: '{arg}'\n")

    if flag_value:
        return list[ flag[0] ]

    # flag name
    return flag[0]

def set(flag, arg):
    FLAG = is_valid(flag, False, arg)

    if list[ FLAG ]:
        display.error(f"Flag already used: '{arg}'\n")

    list[ FLAG ] = True

def get(flag):
    return is_valid(flag, True)

def str(flag):
    FLAG = is_valid(flag)
    return FLAG + ": " + ("ON" if list[ FLAG ] else "OFF")

__all__ = ["get", "set", "str"]
