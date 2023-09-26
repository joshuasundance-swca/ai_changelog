FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

RUN adduser --uid 1000 --disabled-password --gecos '' appuser
USER 1000

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/home/appuser/.local/bin:$PATH"

WORKDIR /home/appuser/ai_changelog

RUN pip install --user --no-cache-dir --upgrade pip
COPY ./requirements.txt /home/appuser/ai_changelog/requirements.txt
RUN python -m pip install --user --no-cache-dir  --upgrade -r /home/appuser/ai_changelog/requirements.txt

COPY ./pyproject.toml /home/appuser/ai_changelog/pyproject.toml
COPY ./README.md /home/appuser/ai_changelog/README.md
COPY ./ai_changelog /home/appuser/ai_changelog/ai_changelog

RUN python -m pip install --user --no-cache-dir /home/appuser/ai_changelog

WORKDIR /home/appuser/

ENTRYPOINT ["ai_changelog"]
