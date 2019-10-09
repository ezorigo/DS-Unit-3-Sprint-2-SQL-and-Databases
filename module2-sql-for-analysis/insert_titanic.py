"""
script that uses psycopg2 to connect to and upload the data from the csv
to ElephantSQL
"""

import psycopg2
import pandas as pd
import sqlite3


url = 'https://raw.githubusercontent.com/ezorigo/DS-Unit-3-Sprint-2-SQL-and-Databases/master/module2-sql-for-analysis/titanic.csv'
dbname = 'rswteizh'
user = 'rswteizh'
password = 'Cw1bOrPRH76txUjt_9Vk3E0yvflzP07Q'
host = 'salt.db.elephantsql.com'

pg_conn = psycopg2.connect(dbname = dbname, user = user, password = password, host = host)
pg_curs = pg_conn.cursor()

sl_conn = sqlite3.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()

df = pd.read_csv(url)
df.to_sql('titanic', sl_conn)

create_titanic_table = """
    CREATE TABLE titanic (
        index SERIAL PRIMARY KEY,
        Survived INT,
        Pclass INT,
        Name VARCHAR(100),
        Sex VARCHAR(10),
        Age FLOAT,
        "Siblings/Spouses Aboard" INT,
        "Parents/Children Aboard" INT,
        Fare FLOAT
    );
"""

pg_curs.execute(create_titanic_table)
passengers = sl_curs.execute('SELECT * FROM titanic;').fetchall()

for passenger in passengers:
    insert_passenger = """
        INSERT INTO titanic
        (index, Survived, Pclass, Name, Sex, Age, "Siblings/Spouses Aboard",
        "Parents/Children Aboard", Fare)
        VALUES """ + str(passenger[0:]) + ';'
    pg_curs.execute(insert_passenger)

pg_curs.close()
pg_conn.commit()

pg_curs = pg_conn.cursor()
pg_passengers = pg_curs.execute('SELECT * FROM titanic;').fetchall()

for passenger, pg_passenger in zip(passengers, pg_passengers):
    assert passenger == pg_passenger
