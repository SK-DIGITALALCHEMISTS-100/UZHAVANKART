FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .


CMD python manage.py collectstatic --noinput && \
    python manage.py migrate && \
    exec gunicorn uk.wsgi:application --bind 0.0.0.0:${PORT:-8080} --access-logfile - --error-logfile - --log-level debug --timeout 120
