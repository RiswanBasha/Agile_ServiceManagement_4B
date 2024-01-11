#!/bin/bash

# Redirect output to a log file
exec > >(tee /tmp/build_files.log) 2>&1

# Activate the virtual environment
source venv/bin/activate   # Adjust the path based on your project structure

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Run collectstatic command
python manage.py collectstatic --noinput

