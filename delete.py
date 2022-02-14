import sqlite3
db = sqlite3.connect('data/data.db')
cur = db.cursor()
try:
    cur.execute("DELETE FROM sensorlog")
    cur.execute("DELETE FROM sensorlist")
    db.commit()
except:
    pass
cur.close()
db.close()