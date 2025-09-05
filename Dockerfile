# syntax=docker/dockerfile:1
FROM python:3.10-alpine
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers openssl-dev
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
EXPOSE 4433
COPY . .
CMD ["hypercorn", "--config", "hypercorn.toml", "main:app"]