import psycopg2
from psycopg2.extensions import connection
from fastapi import HTTPException
from typing import Any
from server.api.models import Player_Career
import random

def get_career(db_con: connection):
    curs = db_con.cursor()
    player = None

    try:
        query = '''SELECT name, years_played, ppg, rpg, apg, bpg, spg 
                    FROM career_stats 
                    JOIN player ON career_stats.p_index = player.p_index'''
        curs.execute(query)
        careers = curs.fetchall()

        count_query = '''SELECT COUNT(*) FROM career_stats'''
        curs.execute(count_query)
        count_res = curs.fetchall()
        count = count_res[0][0]

        rand = random.randint(1, count)

        r = careers[rand]

        player = Player_Career(name=r[0],
                                years=r[1],
                                ppg=round(r[2], 2),  
                                rpg=round(r[3], 2),
                                apg=round(r[4], 2),
                                bpg=round(r[5], 2),
                                spg=round(r[6], 2))
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=str(err))

    return player
        

