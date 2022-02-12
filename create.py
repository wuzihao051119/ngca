import sqlite3
db = sqlite3.connect("D:/ngca/data/data.db")
cur = db.cursor()
try:
    cur = db.execute("CREATE TABLE sensorlog(logid int, sensorid int, sensorvalue real, updatetime text)")
    cur = db.execute("CREATE TABLE sensorlist(sensorid int, sensorname text, maxvalue int, minvalue int)")
except:
    pass
cur.close()
db.close()