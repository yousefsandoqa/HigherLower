from pydantic import BaseModel

class User(BaseModel):
    index: int
    name: str
    score: int

class Stat_List(BaseModel):
    stat: list[str]

class Player_Career(BaseModel):
    name: str
    stat_name: str
    stat: float

class Player_Season(BaseModel):
    name: str
    stat_name: str
    stat: float
    year: str


class Stat_List(BaseModel):
    stat: list[str]

class Stat_List_Year(BaseModel):
    stat: list[str]
    year: str

class Stat_List_Teams_Year(BaseModel):
    stat: list[str]
    teams: list[str]
    year: str
