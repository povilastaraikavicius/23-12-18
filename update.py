import sqlite3

conn = sqlite3.connect("zmones.db")
c = conn.cursor()

with conn:
    c.execute(
        "UPDATE draugai SET email='naujas.email@aol.com' WHERE l_name='Radzevičius'"
    )
