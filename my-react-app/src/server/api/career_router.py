import psycopg2
from psycopg2.extensions import connection
from server.database.db import get_db_connection
from fastapi import APIRouter, Depends, HTTPException, status
from server.api.careers import get_career
from pydantic import BaseModel
from server.api.models import Player_Career

router = APIRouter(
    prefix='/career',
    tags=['career']
)

@router.get("/", response_model=Player_Career)
def get_career_router(db_con: connection = Depends(get_db_connection)):
    return get_career(db_con)