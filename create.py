import sqlite3
db = sqlite3.connect("data/data.db")
cur = db.cursor()
try:
    cur = db.execute("CREATE TABLE sensorlog(logid integer primary key autoincrement not null, sensorid integer, sensorvalue float, updatetime time)")
    cur = db.execute("CREATE TABLE sensorlist(sensorid integer primary key autoincrement not null, sensorname varchar(50), maxvalue integer, minvalue integer)")
    db.commit()
except:
    pass
cur.close()
db.close()