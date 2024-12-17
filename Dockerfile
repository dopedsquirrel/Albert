# Verwende ein Python-3.9-Image
FROM python:3.9

# Installiere die Vosk-Python-Bibliothek
RUN pip install vosk

# Arbeitsverzeichnis setzen
WORKDIR /app

# Kopiere das Python-Skript und die Modelle
COPY . /app

# Lade das deutsche Modell herunter
RUN apt-get update && apt-get install -y wget unzip \
    && wget https://alphacephei.com/vosk/models/vosk-model-small-de-0.15.zip \
    && unzip vosk-model-small-de-0.15.zip && mv vosk-model-small-de-0.15 model

# Starte das Python-Skript
CMD ["python", "recognize.py"]
