#!/bin/bash

################################################################################
# Virtual Environment Reset Script
# 
# Run this to rebuild the virtual environment.
################################################################################

# Config
VENV_DIR="__venv__/"

echo -n "Removing virtual environment at '${VENV_DIR}'..."
rm -rf $VENV_DIR
echo "Done!"

echo -n "Create new virtual environment at '${VENV_DIR}'..."
python3 -m venv $VENV_DIR
echo "Done!"

echo -n "Installing package in editable mode..."
$VENV_DIR/bin/pip install -e .[all]
echo "Done!"

echo "Virtual environment recreated. To activate the environment, run:"
echo "  source ${VENV_DIR}/bin/activate"