from .models.text_model import TextModel
import pyttsx3

class TextService:
    def __init__(self):
        self.engine = pyttsx3.init()

    def to_speech(self, text: str, voice: str = "default"):
        self.engine.setProperty('voice', voice)
        self.engine.say(text)
        self.engine.runAndWait()
        return f"Text '{text}' has been spoken"