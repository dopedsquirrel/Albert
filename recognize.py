from vosk import Model, KaldiRecognizer
import wave
import json

# Pfade zu Modell und Audio-Datei
MODEL_PATH = "model"
AUDIO_PATH = "albert-message-converted.wav"

def transcribe_audio(model_path, audio_path):
    print("Lade Vosk-Modell...")
    model = Model(model_path)
    recognizer = KaldiRecognizer(model, 16000)  # 16 kHz Samplingrate
    
    print("Verarbeite Audio-Datei...")
    wf = wave.open(audio_path, "rb")
    
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        recognizer.AcceptWaveform(data)

        if "hallo albert" in json.loads(recognizer)["text"].lower():
            print("Aktivierungswort erkannt: Hallo Albert!")

    
    result = recognizer.FinalResult()
    print("Transkription abgeschlossen:")
    print(json.loads(result)["text"])

if __name__ == "__main__":
    transcribe_audio(MODEL_PATH, AUDIO_PATH)
