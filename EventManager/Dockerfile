FROM python:3.13.3

# download system packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

ENV DJANGO_SETTINGS_MODULE=EventManager.settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt
# RUN python manage.py collectstatic --noinput

COPY . /app/

CMD ["gunicorn", "EventManager.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--threads", "2", "--preload"]
