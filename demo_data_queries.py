import sqlite3

conn = sqlite3.connect('demo_data.sqlite3')
curs = conn.cursor()

print("1. " + str(curs.execute('SELECT COUNT(*) FROM demo_data;').fetchall()))
print("2. " + str(curs.execute('SELECT COUNT(*) FROM demo_data WHERE x >= 5 AND y >= 5;').fetchall()))
print("3. " + str(curs.execute('SELECT COUNT(DISTINCT y) FROM demo_data;').fetchall()))

curs.close()
conn.commit()
