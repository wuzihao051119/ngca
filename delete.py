import sqlite3
db = sqlite3.connect('D:/ngca/data/data.db')
cur = db.cursor()
cur.execute("DELETE FROM sensorlog")
cur.execute("DELETE FROM sensorlist")
db.commit()
cur.close()
db.close()
print("Delete successfully.")