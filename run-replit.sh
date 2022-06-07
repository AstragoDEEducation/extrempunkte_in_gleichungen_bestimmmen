#!/bin/sh

# update and install dependencies
poetry update

echo "========== Main Program ==========\n"

poetry run python3 ./main.py