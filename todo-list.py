#!/usr/bin/env python3
from sys import exit

if __name__ != "__main__":
    print("This script cannot be required as a module.")
    print("It is a \"runner script\".")
    exit(1)

from sys import argv
from src import cli

cli( *argv[1:] )
