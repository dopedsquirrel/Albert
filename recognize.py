import pyaudio
import vosk
import json
import os

# Konfiguration
MODEL_PATH = "model"  # Pfad zum Vosk-Modell
AUDIO_PATH = "albert-message.wav"  # Pfad zur Weihnachtsnachricht
SAMPLE_RATE = 16000   # Abtastrate
CHUNK_SIZE = 4000     # Größe der Audio-Chunks

def main():
    # Lade das Vosk-Modell
    print("Lade Vosk-Modell...")
    model = vosk.Model(MODEL_PATH)

    # Initialisiere PyAudio
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=SAMPLE_RATE,
                    input=True,
                    frames_per_buffer=CHUNK_SIZE)
    stream.start_stream()

    # Initialisiere den Vosk-Recognizer
    recognizer = vosk.KaldiRecognizer(model, SAMPLE_RATE)

    print("Höre zu... (drücke STRG+C zum Beenden)")
    try:
        while True:
            # Lese Audio-Daten vom Mikrofon
            data = stream.read(CHUNK_SIZE, exception_on_overflow=False)
            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                print("Erkannt:", result["text"])

                # Überprüfe, ob das Aktivierungswort gesagt wurde
                if "hallo albert" in result["text"].lower():
                    print("Aktivierungswort erkannt: Hallo Albert!")

                    # Weihnachtsnachricht abspielen
                    play_audio(AUDIO_FILE)

    except KeyboardInterrupt:
        print("\nBeende...")
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()

if __name__ == "__main__":
    main()
