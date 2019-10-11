import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')

curs = conn.cursor()

create_demo_table = """
    CREATE TABLE demo_data (
        s VARCHAR(1),
        x INT,
        y INT
    );
"""

curs.execute(create_demo_table)

insert_data = """
    INSERT INTO demo_data 
    (s, x, y)
    VALUES ('g', 3, 9);"""

insert_data2 = """
    INSERT INTO demo_data 
    (s, x, y)
    VALUES ('v', 5, 7);"""

insert_data3 = """
    INSERT INTO demo_data 
    (s, x, y)
    VALUES ('f', 8, 7);"""

curs.execute(insert_data)
curs.execute(insert_data2)
curs.execute(insert_data3)
curs.close()
conn.commit()
