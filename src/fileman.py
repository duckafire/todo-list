from os import path

from .      import options
from .args  import flags
from .print import display

def create_todo_list():

    display.verbose("Checking is the todo-list already exists...")
    if path.isfile("./todo-list.txt"):
        display.verbose("todo-list found.")

        if options.get(flags.REPLACE):
            display.verbose("The replacement flag was found.")
        else:
            display.error("The todo-list already exists")

    with open("./todo-list.txt", "w", encoding="utf-8") as file:
        pass

    display.verbose("todo-list created with successful!")

