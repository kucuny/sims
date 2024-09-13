FROM python:3.12-slim-bookworm

RUN set -eux; \
    apt-get update \
    && apt-get upgrade -yq \
    && apt-get install --no-install-recommends -yq pkg-config build-essential procps libpq5 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && pip install poetry

COPY pyproject.toml /tmp/pyproject.toml

RUN cd /tmp \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

WORKDIR /app
