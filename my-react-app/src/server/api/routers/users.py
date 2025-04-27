import psycopg2
from psycopg2.extensions import connection
from fastapi import HTTPException
from typing import Any
from server.api.models import User

def get_users(db_con: connection):
    curs = db_con.cursor()
    users = []

    try:
        query = '''SELECT * FROM user_data'''
        curs.execute(query)
        results = curs.fetchall()
        for r in results:
            user = User(index=r[0], name=r[1], score=r[2])
            users.append(user)
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=str(err))

    return users
        

