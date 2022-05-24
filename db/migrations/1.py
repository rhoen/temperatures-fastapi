import sqlite3
con = sqlite3.connect("temperature_development.db")
cur = con.cursor()

cur.execute('''
    CREATE TABLE devices(
        id integer,
        name text unique,
        primary key (id)
    );
''')

cur.execute('''
    CREATE TABLE readings(
        id integer,
        temperature real,
        device_id integer,
        created_at text,
        primary key (id)
    );
''')
