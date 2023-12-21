import sqlite3

conn = sqlite3.connect("zmones.db")
c = conn.cursor()

query = """
INSERT INTO draugai (f_name, l_name, email) 
VALUES ('andrius', 'Rutkauskas', 'd.rutkauskas@imone.lt');
"""

# ('Domantas', 'Rutkauskas', 'd.rutkauskas@imone.lt')
