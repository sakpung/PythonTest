import sqlite3

conn = sqlite3.connect('coachdata.sqlite')
try:
    cursor = conn.cursor()
#    cursor.execute('')

finally:
    conn.close()