FROM alpine:3.23 

WORKDIR /todo-app
COPY static templates app.py database.py requirements.txt schema.sql /todo-app/

RUN set -e && \
    apk add --no-cache python3 py3-pip python3-dev build-base && \
    cd /todo-app && \
    python3 -m venv /path/to/venv && \
    source /path/to/venv/bin/activate && \ 
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    deactivate && \
    echo "#!/bin/bash \
     cd /todo-app \
     python3 -m venv /path/to/venv \
     source /path/to/venv/bin/activate \ 
     python app.py"> start.sh && chmod +x start.sh
CMD ["./start.sh"]