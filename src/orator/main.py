import pyttsx3
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


# Models
class TextModel(BaseModel):
    text: str
    voice: Optional[str] = "default"


# Services
class TextService:
    def __init__(self):
        self.engine = pyttsx3.init()

    def to_speech(self, text: str, voice: str = "default"):
        self.engine.setProperty('voice', voice)
        self.engine.say(text)
        self.engine.runAndWait()
        return f"Text '{text}' has been spoken"


# Initialize service
text_service = TextService()


@app.post("/to_speech")
async def to_speech(text_model: TextModel):
    try:
        return text_service.to_speech(text_model.text, voice=text_model.voice)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.patch("/set_parameter")
async def set_parameter(parameter: str, value: str):
    return {"message": f"Parameter {parameter} set to {value}"}
