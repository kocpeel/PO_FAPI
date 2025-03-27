from pydantic import BaseModel
from typing import Optional


class TextModel(BaseModel):
    text: str
    voice: Optional[str] = "default"
