# Albert
Swiss German Voice Assistant for Visually Impaired

Swiss German Voice Assistant for Visually Impaired
This project aims to develop a user-friendly voice assistant tailored specifically for the needs of visually impaired individuals. The assistant will support Swiss German to provide a better and more natural user experience. It is designed to simplify daily tasks and improve access to digital information for visually impaired users.

Features (MVP)
Speech Recognition: Supports Swiss German through adjustments and dialect mapping.
Speech Output: Responds in Swiss German using predefined phrases and Text-to-Speech (TTS) solutions.
Basic Commands:
Announce the current time and date.
Create reminders or simple notifications.
Provide weather updates or general information.
Future Enhancements
OCR Integration: Read text from printed or digital documents aloud.
Smart Home Control: Enable control of devices like lights or TVs.
Advanced Speech Models: Train a custom model for Swiss German (e.g., using Coqui TTS or Mozilla DeepSpeech).
Offline Functionality: Use local speech recognition models to ensure privacy.
Technology Stack
Programming Language: Python
Speech Recognition:
Google Speech-to-Text API (configured with de-CH for Swiss German).
Alternative: Mozilla DeepSpeech or Vosk for offline capabilities.
Speech Output:
gTTS or pyttsx3 for voice synthesis.
Hardware:
Microphone (e.g., USB microphone or ReSpeaker).
Speaker (external or built-in).
