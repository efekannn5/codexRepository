import speech_recognition as sr
import pyttsx3


class SpeechRecognizer:
    """Handle speech-to-text operations."""

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self) -> str:
        """Listen via microphone and return recognized text.

        Returns empty string if no speech is detected.
        """
        with sr.Microphone() as source:
            audio = self.recognizer.listen(source)

        try:
            return self.recognizer.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""


class SpeechSynthesizer:
    """Handle text-to-speech output."""

    def __init__(self):
        self.engine = pyttsx3.init()

    def say(self, text: str) -> None:
        self.engine.say(text)
        self.engine.runAndWait()
