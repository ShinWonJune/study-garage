import sqlite3

conn = sqlite3.connect('./resource/database.db')

c=conn.cursor()

#데이터 수정1

c.execute("UPDATE users SET username = ? WHERE id = ?",('niceman',4))
conn.commit()


conn.close()
#row 