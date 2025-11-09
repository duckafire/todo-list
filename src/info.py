PROGRAM = {
    "name":    "todo-list",
    "version": "v0.0.0",
    "license": {
        "name": "GPL3",
        "year": "2025", # 2025-20XX
    },
    "author": {
        "alias":   "DuckAfire",
        "contact": "<https://duckafire.gitlab.io>",
    }
}

def name():
    return PROGRAM["name"]

def version():
    return PROGRAM["version"]

def header():
    # foo | vX.Y.Z | bar2.0
    return f'{PROGRAM["name"]} | ' + \
           f'{PROGRAM["version"]} | ' + \
           f'{PROGRAM["license"]["name"]}'

def copyright():
    # foo Copyright (C) 20XX-20YY fooauthor <fooauthor.foo.bar>
    return f'{PROGRAM["name"]}\n' + \
           f'Copyright (C) ' + \
           f'{PROGRAM["license"]["year"]} ' + \
           f'{PROGRAM["author"]["alias"]} ' + \
           f'{PROGRAM["author"]["contact"]}'

__all__ = ["name", "version", "header", "copyright"]
