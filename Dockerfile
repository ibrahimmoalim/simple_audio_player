FROM python:3.13.5-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir requirements.txt

COPY . .

RUN pip install pyinstaller

CMD [ "echo", "build complete"]