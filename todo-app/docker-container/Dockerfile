FROM alpine:3.23 AS build

WORKDIR /todo-app
COPY static tempates app.py database.py requirements.txt schema.sql /todo-app/

RUN set -e && \
    apk add --no-cache python3 py3-pip python3-dev build-base && \
    python3 -m venv /path/to/venv && \
    source /path/to/venv/bin/activate && \ 
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    python app.py
