import psycopg2
from psycopg2.extensions import connection
from fastapi import HTTPException
from typing import Any
import random
from server.api.models import Stat_List, Stat_List_Teams_Year, Stat_List_Year, Player_Season
#from server.api.models import Player_Season

def get_player_season_stat(stat_year: Stat_List_Teams_Year, db_con: connection):
    curs = db_con.cursor()
    player = None
    sum = " + ".join(stat_year.stat)

    try:
        query = f'''SELECT player.name, SUM({sum})
                    FROM player_season 
                    JOIN player ON player_season.p_index = player.p_index 
                    JOIN team on team.t_idx = player_season.t_idx
                    WHERE year = '{stat_year.year}'
                      AND abr IN ({",".join(stat_year.teams)})
                    GROUP BY player.name;'''
        
        curs.execute(query)
        careers = curs.fetchall()

        count_query = f'''SELECT COUNT(*) FROM player_season WHERE year = '{stat_year.year}' '''
        curs.execute(count_query)
        count_res = curs.fetchall()
        count = count_res[0][0]

        rand = random.randint(1, count)

        r = careers[rand]

        player = Player_Season(name=r[0],
                               stat_name = sum,
                                stat = round(r[1],2), 
                                year = stat_year.year)
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=str(err))

    return player
