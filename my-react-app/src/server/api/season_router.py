import psycopg2
from psycopg2.extensions import connection
from server.database.db import get_db_connection
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from server.api.models import Stat_List_Teams_Year, Stat_List_Year, Player_Season
from server.api.season import get_player_season_stat
#from server.api.models import Player_Season

router = APIRouter(
    prefix='/season',
    tags=['season']
)

@router.post("/stat_year/", response_model=Player_Season)
def get_player_season_router(stat: Stat_List_Year, db_con: connection = Depends(get_db_connection)):
    return get_player_season_stat(stat, db_con)