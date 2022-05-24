import sqlite3

# setup db connection
def con():
    con = sqlite3.connect("db/temperature_development.db")
    con.row_factory = sqlite3.Row
    return con
