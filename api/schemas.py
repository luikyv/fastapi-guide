from typing import Optional
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    description: Optional[str] = None
    price: float

class User(BaseModel):
    username: str
    password: str