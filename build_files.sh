#!/bin/bash

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Run collectstatic command
python manage.py collectstatic
