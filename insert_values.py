import sqlite3

conn = sqlite3.connect("zmones.db")
c = conn.cursor()


with conn:
    c.execute(
        "INSERT INTO draugai VALUES ('andrius', 'Rutkauskas', 'd.rutkauskas@imone.lt')"
    )
    c.execute("INSERT INTO draugai VALUES ('Rimas', 'Radzevičius', 'RR@gmail.com')")
    c.execute("INSERT INTO draugai VALUES ('Povilas', 'Taraik', 'ptpppp@gmail.com')")
