#!/bin/bash
echo "applying migrations"
python3 manage.py makemigrations
python3 manage.py migrate

echo "starting project....."
python3 manage.py runserver 0.0.0.0:8000
