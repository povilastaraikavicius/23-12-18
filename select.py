import sqlite3

conn = sqlite3.connect("zmones.db")
c = conn.cursor()


# with conn:
#     c.execute("SELECT * From draugai WHERE f_name='Povilas'")
#     print(c.fetchall())


with conn:
    c.execute("SELECT * From draugai WHERE l_name LIKE 'T%'")
    print(c.fetchone())
