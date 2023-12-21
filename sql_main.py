import sqlite3

conn = sqlite3.connect("zmones.db")
c = conn.cursor()

vardas = input("Įveskite vardą: ")
with conn:
    c.execute("SELECT * From draugai WHERE f_name =?", (vardas,))
    res = c.fetchall()
if res:
    print(res)
else:
    print("nėra tokio vardo!")

