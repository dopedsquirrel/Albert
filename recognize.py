from vosk import Model, KaldiRecognizer
import wave
import json

# Pfade zu Modell und Audio-Datei
MODEL_PATH = "model"
AUDIO_PATH = "albert-message-converted.wav"

def load_model(model_path):
    """Lädt das Vosk-Modell."""
    print("Lade Vosk-Modell...")
    return Model(model_path)

def process_audio(audio_path, recognizer):
    """Verarbeitet die Audio-Datei und gibt die Transkription zurück."""
    print("Verarbeite Audio-Datei...")
    wf = wave.open(audio_path, "rb")

    while True:
        data = wf.readframes(4000)  # Lesen der Audiodaten in Blöcken
        if len(data) == 0:
            break
        recognizer.AcceptWaveform(data)  # Verarbeitet die Daten

    result = recognizer.FinalResult()
    return json.loads(result)

def check_activation_word(transcription, activation_word="hallo albert"):
    """Prüft, ob das Aktivierungswort in der Transkription enthalten ist."""
    if activation_word in transcription.lower():
        print(f"Aktivierungswort erkannt: {activation_word.capitalize()}!")
        return True
    return False

def transcribe_audio(model_path, audio_path):
    """Hauptlogik: Lädt Modell, verarbeitet Audio und prüft Aktivierungswort."""
    # Modell laden
    model = load_model(model_path)
    recognizer = KaldiRecognizer(model, 16000)  # 16 kHz Samplingrate

    # Audio verarbeiten
    transcription = process_audio(audio_path, recognizer)
    print("Transkription abgeschlossen:")
    print(transcription["text"])

    # Aktivierungswort prüfen
    if check_activation_word(transcription["text"]):
        print("Aktion ausführen...")
        # Hier kannst du weitere Aktionen hinzufügen
    else:
        print("Kein Aktivierungswort erkannt.")

if __name__ == "__main__":
    transcribe_audio(MODEL_PATH, AUDIO_PATH)
