#!/bin/bash

# Check if the venv folder exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

echo "Activating virtual environment..."
source venv/bin/activate

# Check if the installed flag exists in the virtual environment
if [ ! -f "venv/installed" ]; then
    if [ -f "requirements.txt" ]; then
        echo "Installing wheel for faster installation..."
        pip3 install wheel
        echo "Installing dependencies..."
        pip3 install -r requirements.txt
        touch venv/installed
    else
        echo "requirements.txt not found, skipping dependency installation."
    fi
else
    echo "Dependencies already installed, skipping installation."
fi

if [ ! -f ".env" ]; then
    echo "Copying configuration file..."
    cp .env-example .env
else
    echo "Skipping .env copying."
fi

echo "Starting the bot..."
python3 main.py

echo "Done."
echo "PLEASE EDIT THE .ENV FILE"
