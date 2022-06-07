#!/bin/sh

# update and install dependencies
poetry update

# format main.py
poetry run autopep8 -i -a ./main.py

# print main program start
echo ""
echo "============ Main Program ============"
echo ""

# run main.py
poetry run python3 ./main.py