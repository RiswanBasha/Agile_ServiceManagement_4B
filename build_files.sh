#!/bin/bash

# Redirect output to a log file
exec > >(tee /tmp/build_files.log) 2>&1

# Print some information for debugging
echo "Current Directory: $(pwd)"
echo "Python Version: $(python --version)"

# Activate the virtual environment based on the platform
if [ "$(expr substr $(uname -s) 1 5)" == "Linux" ]; then
    echo "Activating virtual environment for Linux..."
    source venv/bin/activate
elif [ "$(expr substr $(uname -s) 1 10)" == "MINGW32_NT" ]; then
    echo "Activating virtual environment for Windows..."
    venv/Scripts/activate
else
    echo "Unsupported platform: $(uname -s)"
    exit 1
fi

# Print some more information
echo "Activated virtual environment"
echo "Installing dependencies..."

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Print more information
echo "Installed dependencies"
echo "Running collectstatic command..."

# Run collectstatic command
python manage.py collectstatic --noinput
