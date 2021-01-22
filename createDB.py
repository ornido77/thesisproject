import sqlite3

conn = sqlite3.connect("patients")

c = conn.cursor()

c.execute(''' CREATE TABLE checkUp(
            ticket_id       INTEGER     PRIMARY KEY,
            full_name       TEXT(50)    NOT NULL,
            age             INTEGER     NOT NULL,
            address         TEXT(100)   NOT NULL,
            contact         INTEGER,
            time_in         DATETIME DEFAULT (datetime('now','localtime')
            )''')
c.execute("INSERT INTO CheckUp (full_name, age, address, contact) "
          "VALUES ('Miko Reyes', 35, 'Punturin', 4523523)")
c.execute("SELECT * FROM CheckUp")
print(c.fetchall())
conn.commit()
conn.close()