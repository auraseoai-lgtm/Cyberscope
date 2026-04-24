#!/bin/bash

echo "Installing Ethical Security Toolkit..."

pkg update -y
pkg install python -y
pip install requests dnspython

chmod +x main.py

echo "Done!"
echo "Run: python main.py"
