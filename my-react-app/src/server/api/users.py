import psycopg2
from psycopg2.extensions import connection
from fastapi import HTTPException
from typing import Any
from server.api.models import User

#returns the top 5 performers at the game in descending order like a traditional leaderboard
def get_users(db_con: connection):
    curs = db_con.cursor()
    users = []

    try:
        query = '''SELECT * FROM user_data ORDER BY score DESC LIMIT 5'''
        curs.execute(query)
        results = curs.fetchall()
        for r in results:
            user = User(index=r[0], name=r[1], score=r[2])
            users.append(user)
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=str(err))

    return users

# adds a user to the game and updates the sciore with the game performance
def add_users(user: User, db_con: connection):
    curs = db_con.cursor()
    count_query = '''SELECT COUNT(*) FROM user_data'''
    curs.execute(count_query)
    count_res = curs.fetchall()
    count = count_res[0][0] + 1

    try: 
        check = '''SELECT * FROM user_data WHERE name = %s'''
        curs.execute(check, (user.name,))
        result = curs.fetchall()
        if(count - 1 >= 5):
            if(len(result) == 0):
                curs.execute('''SELECT index FROM user_data ORDER BY score ASC LIMIT 1''')
                index = curs.fetchall()
                index_num = index[0][0]
                curs.execute('''DELETE FROM user_data WHERE index = %s;''', (index_num,)) 
                curs.execute('''INSERT INTO user_data ("index", name, score) VALUES (%s, %s, %s);''', (index_num, user.name, user.score))
            else:
                curs.execute('''UPDATE user_data SET score = %s WHERE name = %s;''', (user.score, user.name))
        else:
            if(len(result) == 0):
                curs.execute('''INSERT INTO user_data ("index", name, score) VALUES (%s, %s, %s);''', (count, user.name, user.score))
            else:
                curs.execute('''UPDATE user_data SET score = %s WHERE name = %s;''', (user.score, user.name))
    
        db_con.commit()
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=str(err))
