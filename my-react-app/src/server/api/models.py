from pydantic import BaseModel

class User(BaseModel):
    index: int
    name: str
    score: int

class Player_Career(BaseModel):
    name: str
    stat_name: str
    stat: float

class Stat_List(BaseModel):
    stat: list[str]