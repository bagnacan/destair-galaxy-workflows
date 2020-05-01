#!/usr/bin/env python3

# Indent a Galaxy workflow.
# Takes a galaxy workflow as input, and creates a new file with a .indent
# extension.

# example:
# $ ./indent.py workflow.ga

import json
import yaml
import sys

with open(sys.argv[1], "r") as in_file:
    workflow = in_file.read()

    out_file = open(str(sys.argv[1] + ".indent"), "w")
    out_file.write(json.dumps(yaml.full_load(workflow), indent=4))
    out_file.close()
