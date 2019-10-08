import sqlite3 

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    """
    conn = None
    conn = sqlite3.connect(db_file)
 
    return conn

def total_rows(conn):
    """
    Query total number of rows
    """
    curs = conn.cursor()
    curs.execute("select count(*) from buddymove_holidayiq;")
 
    rows = curs.fetchall()
 
    for row in rows:
        print(row)

def at_least_a_hunnid(conn):
    """
    Query total number of users who reviewed at least 100 in nature and shopping categories
    """
    curs = conn.cursor()
    curs.execute("select count(*) from buddymove_holidayiq where nature >= 100 and shopping >= 100;")
 
    rows = curs.fetchall()
 
    for row in rows:
        print(row)

def avg_score(conn):
    """
    Query average score for each categories
    """
    curs = conn.cursor()
    curs.execute("select round(avg(sports), 2), round(avg(religious), 2), round(avg(nature), 2), round(avg(theatre), 2), round(avg(shopping), 2), round(avg(picnic), 2) from buddymove_holidayiq;")
 
    rows = curs.fetchall()
 
    for row in rows:
        print(row)

def main():
    database = r"buddymove_holidayiq.sqlite3"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Total rows (reviews)")
        total_rows(conn)

    with conn:
        print("1. Total number of users who reviewed at least 100 in nature and shopping categories")
        at_least_a_hunnid(conn)

    with conn:
        print("1. Average score for each categories")
        avg_score(conn)


if __name__ == '__main__':
    main()
