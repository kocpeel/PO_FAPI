import pyttsx3
from ..models.text_model import TextModel


class TextService:
    def __init__(self):
        self.engine = pyttsx3.init()

    def to_speech(self, text_model: TextModel):
        self.engine.setProperty('voice', text_model.voice)
        self.engine.say(text_model.text)
        self.engine.runAndWait()
        return f"Text '{text_model.text}' has been spoken"
