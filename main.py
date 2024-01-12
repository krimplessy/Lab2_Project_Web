import sqlite3
import pandas as pd

con = sqlite3.connect("BeautySalon.sqlite")

f_damp = open('BeautySalon.db','r')
damp = f_damp.read()
f_damp.close()

con.executescript(damp)
con.commit()

cursor = con.cursor()

cursor.execute("SELECT * FROM specialization")
print(cursor.fetchall())

cursor.execute("SELECT * FROM client")
print(cursor.fetchall())

cursor.execute("SELECT * FROM master")
print(cursor.fetchall())

cursor.execute("SELECT * FROM service")
print(cursor.fetchall())

cursor.execute("SELECT * FROM timetable")
print(cursor.fetchall())

cursor.execute("SELECT * FROM timetable_date")
print(cursor.fetchall())

cursor.execute("SELECT * FROM record")
print(cursor.fetchall())

con.close()