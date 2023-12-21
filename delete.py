import sqlite3

conn = sqlite3.connect("zmones.db")
c = conn.cursor()


with conn:
    c.execute("DELETE from draugai WHERE f_name='andrius'")
