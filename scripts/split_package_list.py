#!/usr/bin/env python3

import sys
import os
from collections import defaultdict

CATEGORIES = '''
B | base         | basic CLI tools
M | multimedia   | photo/video/audio tools
H | hardware     | tools for embedded development (microcontrollers, etc)
D | development  | development tools
P | python       | python tools and libraries
R | r            | R tools and libraries
G | gui          | basic GUI tools
T | tex          | LaTeX stuff
F | fonts        | fonts
N | network      | networking tools
S | special      | specialized tools for various needs
? | unsorted     | stuff where I don't know what it is
# | misc         | stuff that I'm not sure about
'''

def parse_categories(cat_list):
    categories = {}
    for line in cat_list.splitlines():
        if len(line) < 2:
            continue
        letter, suffix, description = map(lambda x: x.strip(" \n"), line.split("|"))
        categories[letter] = suffix
    return categories

def sort_package_list(file_path):
    categories = parse_categories(CATEGORIES)
    packages = defaultdict(list)
    file_name = os.path.basename(file_path)
    file_base, extension = os.path.splitext(file_name)
    with open(file_path, "r") as fd:
        for line in fd:
            try:
                letter, package = map(lambda x: x.strip(" \n"), line.split(" "))
            except ValueError:
                print("malformed line: " + line, file=sys.stderr)
                continue
            if letter in categories.keys():
                packages[categories[letter]].append(package)
            else:
                print("Unknown letter: " + line, file=sys.stderr)

        for suffix, package_list in packages.items():
            print("Writing %s: " % suffix, end="")
            with open(file_base + "-" + suffix + extension, "w") as fd:
                fd.write(", ".join(package_list))
                fd.write("\n")
            print("done (%d packages)" % len(package_list))

if __name__ == "__main__":
    sort_package_list(sys.argv[1])
