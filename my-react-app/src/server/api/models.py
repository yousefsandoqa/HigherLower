from pydantic import BaseModel

class User(BaseModel):
    index: int
    name: str
    score: int

class Player_Career(BaseModel):
    name: str
    years: int
    ppg: float
    rpg: float
    apg: float
    bpg: float
    spg: float