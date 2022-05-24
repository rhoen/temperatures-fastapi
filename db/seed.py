import sqlite3
import datetime
con = sqlite3.connect("temperature_development.db")
cur = con.cursor()


# cur.execute('''
#     INSERT INTO devices ('name')
#     VALUES ('test device');
# ''')
# con.commit()
# cur.execute('''
#     SELECT id FROM devices WHERE name is 'test device'
# ''')
# test = cur.fetchone()
# id = test[0]
id = 2
readings = [
    (id, 82.4, datetime.datetime.now().replace(microsecond=0).isoformat()),
    (id, 81.4, datetime.datetime.now().replace(microsecond=0).isoformat()),
    (id, 80.8, datetime.datetime.now().replace(microsecond=0).isoformat())
]
con.executemany('''
    INSERT INTO readings ('device_id', 'temperature', 'created_at')
    VALUES (?, ?, ?)
''', readings)
con.commit()

con.close()
