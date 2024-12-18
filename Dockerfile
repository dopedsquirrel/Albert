# Verwende ein Python-3.9-Image
FROM python:3.9

# Label für die Dokumentation
LABEL maintainer="dopedsquirrel"

# Arbeitsverzeichnis setzen
WORKDIR /app

# Systemabhängigkeiten installieren
RUN apt-get update && apt-get install -y \
    alsa-utils \            
    portaudio19-dev \       
    python3-dev \           
    gcc \ 
    git \                  
    libasound2-dev && \    
    rm -rf /var/lib/apt/lists/* 

# Installiere Python-Bibliotheken
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere das Python-Skript und die Modelle
COPY . /app

# Lade das deutsche Modell herunter
RUN apt-get update && apt-get install -y wget unzip \
    && wget https://alphacephei.com/vosk/models/vosk-model-small-de-0.15.zip \
    && unzip vosk-model-small-de-0.15.zip && mv vosk-model-small-de-0.15 model

# Starte das Python-Skript
CMD ["python", "recognize.py"]
