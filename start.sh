#!/bin/bash

echo "Starting collectstatic..."
python manage.py collectstatic --noinput

echo "Starting migrations..."
python manage.py migrate

echo "Starting Gunicorn..."
exec gunicorn uk.wsgi:application \
    --bind 0.0.0.0:${PORT:-8080} \
    --access-logfile - \
    --error-logfile - \
    --log-level debug \
    --timeout 120
