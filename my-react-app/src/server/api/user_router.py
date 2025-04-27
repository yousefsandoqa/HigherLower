import psycopg2
from psycopg2.extensions import connection
from server.database.db import get_db_connection
from fastapi import APIRouter, Depends, HTTPException, status
from server.api.users import get_users
from pydantic import BaseModel
from server.api.models import User

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.get("/", response_model=list[User])
def get_user_router(db_con: connection = Depends(get_db_connection)):
    return get_users(db_con)





