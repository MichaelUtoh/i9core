#!/usr/bin/env bash
# ezit on error

set -o errexit

pip install

python manage.py collectstatic --no-input
python manage.py migrate