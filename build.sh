#!/usr/bin/env bash

# Arrête le script en cas d'erreur
set -o errexit

# Installer les dépendances (si tu ne veux pas le faire dans le fichier Render)
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate

# Collecter les fichiers statiques
python manage.py collectstatic --noinput
