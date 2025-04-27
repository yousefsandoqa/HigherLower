import psycopg2

def get_db_connection():
    connection = psycopg2.connect(
        dbname="CSE412Project",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )
    try:
        yield connection
    finally:
        connection.close()