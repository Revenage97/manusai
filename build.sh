#!/bin/bash

# Build script for Render deployment
echo "Running build script..."

# Install dependencies
pip install -r requirements.txt

# Run migrations
cd inventory_dashboard
python manage.py migrate

# Create media directories
mkdir -p media/uploads media/backups

echo "Build completed successfully!"
