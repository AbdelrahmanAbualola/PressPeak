#!/bin/bash

# Update package list and upgrade system packages
sudo apt update && sudo apt upgrade -y

# Install Python 3 and pip if not installed
sudo apt install python3 python3-pip -y

# Upgrade pip
python3 -m pip install --upgrade pip

# Verify Python version
python3 --version

python -m pip install spacy

# Create the models directory if it doesn't exist
mkdir -p /home/user/dir/pages/models

# Set the custom download location
export SPACY_DOWNLOAD_LOCATION=/home/user/dir/pages/models

python -m spacy download en_core_web_md
