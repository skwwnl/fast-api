from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "FastAPI Book Launch",
                "image": "http://~~~~image.png",
                "description": "We will be discussing ~",
                "tags": ["python", "fastapi"],
                "location": "Google Meet",
            }
        }
