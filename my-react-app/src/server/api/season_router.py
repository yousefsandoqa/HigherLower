import psycopg2
from psycopg2.extensions import connection
from server.database.db import get_db_connection
from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from server.api.models import Stat_List_Teams_Year, Stat_List_Team, Player_Season, Stat_List, Player_Career
from server.api.season import get_player_season_stat_team_year, get_player_season_stat_team, get_player_season_stat_team_acc_year
#from server.api.models import Player_Season

router = APIRouter(
    prefix='/season',
    tags=['season']
)

#1st Parameter of the function is input
#Input is a list of stats, a list of teams, a specific year
#Response_model is output
@router.post("/stat_team_year/", response_model=Player_Season)
def get_player_season_router(stat: Stat_List_Teams_Year, db_con: connection = Depends(get_db_connection)):
    return get_player_season_stat_team_year(stat, db_con)

#Input is a list of stats, and a list of teams
#If no teams or years are specified, use this call and pass in a list of all teams
@router.post("/stat_team/", response_model=Player_Season)
def get_player_season_router(stat: Stat_List_Team, db_con: connection = Depends(get_db_connection)):
    return get_player_season_stat_team(stat, db_con)

#Input is a list of stats, and a list of teams, accolade, and year
@router.post("/stat_accolades/", response_model=Player_Career)
def get_player_season_router(stat: Stat_List_Team, db_con: connection = Depends(get_db_connection)):
    return get_player_season_stat_team_acc_year(stat, db_con)