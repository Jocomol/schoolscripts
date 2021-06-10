#!/usr/env/bin python3
import sys

try:
    filename = sys.argv[1]
    with open(filename, "w+") as file:
        title = "# " + filename.strip(".md").replace("_", " ")
        file.write(title)
except(IndexError):
    print("No filename was entered")
