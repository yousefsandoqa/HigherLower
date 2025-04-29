import psycopg2
from psycopg2.extensions import connection
from server.database.db import get_db_connection
from fastapi import APIRouter, Depends, HTTPException, status
from server.api.users import get_users
from pydantic import BaseModel
#from server.api.models import Player_Season

router = APIRouter(
    prefix='/season',
    tags=['season']
)

#@router.get("/", response_model=Player_Season)
def get_player_season_router(db_con: connection = Depends(get_db_connection)):
    #return get_player_season(db_con)
    return