import psycopg2
from psycopg2.extensions import connection
from fastapi import HTTPException
from typing import Any
from server.api.models import Player_Career
import random

def get_career(db_con: connection, stat: list[str]):
    curs = db_con.cursor()
    player = None
    sum_list = " + ".join(stat)

    try:
        query = f'''SELECT name, SUM({sum_list})
                    FROM career_stats 
                    JOIN player ON career_stats.p_index = player.p_index 
                    GROUP BY name;'''
        curs.execute(query)
        careers = curs.fetchall()

        count_query = '''SELECT COUNT(*) FROM career_stats'''
        curs.execute(count_query)
        count_res = curs.fetchall()
        count = count_res[0][0]

        rand = random.randint(1, count)

        r = careers[rand]

        player = Player_Career(name=r[0],
                               stat_name = sum_list,
                                stat = round(r[1],2))
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=str(err))

    return player
        

