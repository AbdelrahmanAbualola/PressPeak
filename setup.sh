#!/bin/bash
sudo apt update && sudo apt upgrade -y

# Install the latest version of Python 3.x (Replace 3.x with the specific version if needed)
sudo apt install python3 python3-pip -y

# Verify Python version
python3 --version

# Upgrade pip to the latest version for Python 3
python3 -m pip install --upgrade pip

python -m spacy download en_core_web_md
