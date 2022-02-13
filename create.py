import sqlite3
db = sqlite3.connect("D:/ngca/data/data.db")
cur = db.cursor()
try:
    cur = db.execute("CREATE TABLE sensorlog(logid integer primary key autoincrement, sensorid integer, sensorvalue float, updatetime time)")
    cur = db.execute("CREATE TABLE sensorlist(sensorid integer primary key autoincrement, sensorname varchar(50), maxvalue integer, minvalue integer)")
    db.commit()
except:
    pass
cur.close()
db.close()