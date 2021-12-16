import sqlite3

conn = sqlite3.connect("8_2_uzduotis_DB.db")
c = conn.cursor()

with conn:
    c.execute("CREATE TABLE IF NOT EXISTS paskaitos (pavadinimas TEXT, destytojas TEXT, trukme INTEGER)")

with conn:
    c.execute(f"""
    INSERT INTO paskaitos (pavadinimas, destytojas, trukme)
    VALUES
    ('Vadyba', 'Domantas', 40), 
    ('Python', 'Donatas', 80), 
    ('Java', 'Tomas', 80)
     """)

with conn:
    selection = c.execute("SELECT pavadinimas FROM paskaitos WHERE trukme > 50")
print(selection.fetchall())

# with conn:
#     c.execute("UPDATE paskaitos SET pavadinimas = 'Python programavimas' WHERE pavadinimas = 'Python'")
#     c.execute("DELETE FROM paskaitos WHERE destytojas = 'Tomas'")
#
# with conn:
#     selection = c.execute("SELECT * FROM paskaitos")
# print(selection.fetchall())
