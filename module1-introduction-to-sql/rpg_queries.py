import sqlite3

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    """
    conn = None
    conn = sqlite3.connect(db_file)
 
    return conn

def total_characters(conn):
    """
    Query total number of distinct characters
    """
    curs = conn.cursor()
    curs.execute("select distinct count(character_id) as number_of_character from charactercreator_character;")
 
    rows = curs.fetchall()
 
    for row in rows:
        print(row)

def total_subclasses(conn):
    """
    Query total number of unique subclass
    """
    curs = conn.cursor()
    curs.execute("SELECT count(*) FROM sqlite_master where type = 'table' and name like 'charactercreator%' and name != 'charactercreator_character' and name != 'charactercreator_character_inventory';")

    rows = curs.fetchall()
 
    for row in rows:
        print(row)

def total_items(conn):
    """
    Query total number of items
    """
    curs = conn.cursor()
    curs.execute("select count(*) from armory_item;")

    rows = curs.fetchall()
 
    for row in rows:
        print(row)

def total_weapons(conn):
    """
    Query total number of weapons
    """
    curs = conn.cursor()
    curs.execute("select count(distinct item_ptr_id) from armory_weapon;")

    rows = curs.fetchall()
 
    for row in rows:
        print(row)

def total_non_weapons(conn):
    """
    Query total number of non-weapons
    """
    curs = conn.cursor()
    curs.execute("select (count(distinct item_id) - count(distinct item_ptr_id)) as non_weapons from armory_item left join armory_weapon on item_id = item_ptr_id;")

    rows = curs.fetchall()
 
    for row in rows:
        print(row)

def total_ipc(conn):
    """
    Query total number of items per character
    """
    curs = conn.cursor()
    curs.execute("select count(item_id) as item_per_character from charactercreator_character_inventory group by character_id limit 20")

    rows = curs.fetchall()
 
    for row in rows:
        print(row)

def total_wpc(conn):
    """
    Query total number of weapons per character
    """
    curs = conn.cursor()
    curs.execute("select count(item_ptr_id) as weapons_per_character from charactercreator_character_inventory join armory_weapon on item_id = item_ptr_id group by character_id limit 20;")

    rows = curs.fetchall()
 
    for row in rows:
        print(row)


# def avg_ipc(conn):
#     """
#     Query average number of items per character
#     """
#     curs = conn.cursor()
#     curs.execute("")

#     rows = curs.fetchall()
 
#     for row in rows:
#         print(row)

# def avg_wpc(conn):
#     """
#     Query average number of weapons per character
#     """
#     curs = conn.cursor()
#     curs.execute("")

#     rows = curs.fetchall()
 
#     for row in rows:
#         print(row)

def main():
    database = r"rpg_db.sqlite3"
 
    # create a database connection
    conn = create_connection(database)
    with conn:
        print("1. Total characters")
        total_characters(conn)

    with conn:
        print("2. Total subclasses")
        total_subclasses(conn)

    with conn:
        print("3. Total items")
        total_items(conn)

    with conn:
        print("4. Total weapons")
        total_weapons(conn)

    with conn:
        print("5. Total non-weapons")
        total_non_weapons(conn)

    with conn:
        print("6. Total items per character")
        total_ipc(conn)

    with conn:
        print("7. Total weapons per character")
        total_wpc(conn)
    
    # with conn:
    #     print("8. Average items per character")
    #     avg_ipc(conn)

    # with conn:
    #     print("9. Average weapons per character")
    #     avg_wpc(conn)

if __name__ == '__main__':
    main()
