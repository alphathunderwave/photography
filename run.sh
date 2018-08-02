#!/usr/bin/env bash

# Don't modify unless you know what you're doing
export FLASK_APP="app/main.py"
export FLASK_DEBUG=1
# Create and activate the virtual environment
python3 -m venv venv
source ./venv/bin/activate
pip3 install -U setuptools

# Install the project into the virtual environment
python3 setup.py install

# Run the project
python3 -m flask run
