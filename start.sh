#!/bin/bash

# Wait for PostgreSQL to start
echo "Waiting for PostgreSQL..."
while ! nc -z db 5432; do
  sleep 1
done
echo "PostgreSQL started"

# Run migrations and start the server
python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py runserver 0.0.0.0:3003
# gunucorn ajhome.wsgi --bind "0.0.0.0:${PORT:-8000}"

# Start Gunicorn server
exec gunicorn ajhome.wsgi:application \
    --bind 0.0.0.0:3003 \
    --workers 3