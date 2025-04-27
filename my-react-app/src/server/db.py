import psycopg2

connection = psycopg2.connect(
    dbname="CSE412Project",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432"
)

curs = connection.cursor()

curs.execute("SELECT * FROM user_data")

results = curs.fetchall()

for r in results:
    print(r)
