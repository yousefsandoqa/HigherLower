import psycopg2
from psycopg2.extensions import connection
from fastapi import HTTPException
from typing import Any
import random
from server.api.models import Stat_List, Stat_List_Teams_Year, Stat_List_Team, Player_Season, Stat_List_Teams_Acc_Year, Player_Career
#from server.api.models import Player_Season

#Retrieves a random player using the specified year and team_list
def get_player_season_stat_team_year(stat_year: Stat_List_Teams_Year, db_con: connection):
    curs = db_con.cursor()
    player = None
    sum_list = " + ".join(stat_year.stat)

    team_list = [f"'{team}'" for team in stat_year.teams]
    team_list_joined = ", ".join(team_list)

    try:
        #Joins together player_season, player, and team to select a random player given the statistic, season, and team specified
        query = f'''SELECT player.name, SUM({sum_list})
                    FROM player_season 
                    JOIN player ON player_season.p_index = player.p_index 
                    JOIN team on player_season.t_index = team.t_index
                    WHERE player_season.year = '{stat_year.year}'
                    AND team.abr IN ({team_list_joined})
                    GROUP BY player.name;'''

        curs.execute(query)

        careers = curs.fetchall()

        count_query = f'''SELECT COUNT(*) FROM player_season 
                          JOIN team on player_season.t_index = team.t_index
                          WHERE year = '{stat_year.year}' AND team.abr IN ({team_list_joined})'''
        
        curs.execute(count_query)
        count_res = curs.fetchall()
        count = count_res[0][0]

        rand = random.randint(0, count)
        r = careers[rand]

        player = Player_Season(name=r[0],
                               stat_name = sum_list,
                                stat = round(r[1],2), 
                                year = stat_year.year)
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=str(err))

    return player

#Retrieves a random player using a specific team from any year
def get_player_season_stat_team(stat_year: Stat_List_Team, db_con: connection):
    curs = db_con.cursor()
    player = None
    sum_list = " + ".join(stat_year.stat)

    team_list = [f"'{team}'" for team in stat_year.teams]
    team_list_joined = ", ".join(team_list)

    try:
        #Joins together player_season, player, and team to select a random player given the statistic and team specified
        query = f'''SELECT player.name, SUM({sum_list}), player_season.year
                    FROM player_season 
                    JOIN player ON player_season.p_index = player.p_index 
                    JOIN team on player_season.t_index = team.t_index
                    WHERE team.abr IN ({team_list_joined})
                    GROUP BY player.name, player_season.year;'''

        curs.execute(query)

        careers = curs.fetchall()    

        count_query = f'''SELECT COUNT(*) FROM player_season 
                          JOIN team on player_season.t_index = team.t_index
                          WHERE team.abr IN ({team_list_joined})'''
        curs.execute(count_query)
        count_res = curs.fetchall()
        count = count_res[0][0]

        rand = random.randint(0, count)

        r = careers[rand]

        player = Player_Season(name=r[0],
                               stat_name = sum_list,
                                stat = round(r[1],2), 
                                year = r[2])
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=str(err))

    return player

#Retrieves a random player that has an accolade
def get_player_season_stat_team_acc_year(stat_year: Stat_List_Teams_Acc_Year, db_con: connection):
    curs = db_con.cursor()
    player = None
    sum_list = " + ".join(stat_year.stat)

    team_list = [f"'{team}'" for team in stat_year.teams]

    try:
        #Retrieves a random players ppg that has an accolade
        query = f'''SELECT player.name, player_season.ppg
                    FROM player_season
                    JOIN player ON player_season.p_index = player.p_index
                    JOIN team ON player_season.t_index = team.t_index
                    WHERE player.p_index IN (SELECT DISTINCT accolades.p_index FROM accolades WHERE accolades.year = player_season.year);
                    '''
        print(query)
        curs.execute(query)

        careers = curs.fetchall()

        count_query = f'''
            SELECT COUNT(*) FROM accolades
        '''
        curs.execute(count_query)
        count_res = curs.fetchall()
        count = count_res[0][0]
        print(f"COUNT: {count}")
        print(f"LEN(careers): {len(careers)}")
        rand = random.randint(1, count)

        r = careers[rand]

        player = Player_Career(name=r[0],
                               stat_name = sum_list,
                                stat = round(r[1],2))
    except psycopg2.Error as err:
        raise HTTPException(status_code=500, detail=str(err))

    return player