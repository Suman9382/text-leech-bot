FROM python:3.9.7-slim-buster

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends gcc libffi-dev ffmpeg aria2 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/

COPY requirements.txt /app/

RUN pip3 install --no-cache-dir --upgrade --requirement requirements.txt

COPY . /app/

CMD ["python3", "modules/main.py"]
