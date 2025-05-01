import psycopg2
from psycopg2.extensions import connection
from server.database.db import get_db_connection
from fastapi import APIRouter, Depends, HTTPException, status
from server.api.users import get_users, add_users
from pydantic import BaseModel
from server.api.models import User

router = APIRouter(
    prefix='/user',
    tags=['user']
)

@router.get("/", response_model=list[User])
def get_user_router(db_con: connection = Depends(get_db_connection)):
    return get_users(db_con)

#need to add a post for adding users to the leaderboard

@router.post("/add/")
async def add_new_user(user: User, db_con: connection = Depends(get_db_connection)):
    add_users(user, db_con)
    return {"message": "User added successfully"}