import psycopg2

def get_db_connection():
    connection = psycopg2.connect(
        dbname="CSE412Project", #Change dbname to whatever it is on your machine
        user="postgres",        #Change to the user you made db in
        password="postgres",    #Change to the user password
        host="localhost",
        port="5432"
    )
    try:
        yield connection
    finally:
        connection.close()