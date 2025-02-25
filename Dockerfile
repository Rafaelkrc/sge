FROM python:3.12-slim

WORKDIR /sge

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt update -y \
    && apt install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    wait-for-it \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN set -ex && \
    pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
