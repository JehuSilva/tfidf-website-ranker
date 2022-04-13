#!/bin/bash
echo "Unpacking model files..."
unzip app/models/models.zip -d app/models
unzip app/models/datasets.zip -d app/models
rm -r app/models/models.zip
rm -r app/models/datasets.zip
echo "Building python environment"
python3 -m venv venv
source venv/bin/activate
echo "Installing dependencies"
pip install -r requirements.txt