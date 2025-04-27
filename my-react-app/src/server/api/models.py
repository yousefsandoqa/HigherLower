from pydantic import BaseModel

class User(BaseModel):
    index: int
    name: str
    score: int