from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from .events import Event


class User(BaseModel):
    email: str
    password: str
    username: str
    events: Optional[List[Event]] = Field(default=[])

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fast@sss.com",
                "password": "qwe123",
                "username": "strafds",
                "events": [],
            }
        }


class UserSignIn(BaseModel):
    email: EmailStr
    password: str

    class Config:
        json_schema_extra = {
            "example": {
                "email": "fast@sss.com",
                "username": "strafds",
                "events": [],
            }
        }
