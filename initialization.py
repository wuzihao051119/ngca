import sqlite3
db = sqlite3.connect('data/data.db')
cur = db.cursor()
sensornumber = int(input("请输入增加的传感器数量: "))
for i in range(sensornumber):
    try:    
        sensorname = input("请输入sensorname: ")
        maxvalue = int(input("请输入maxvalue: "))
        minvalue = int(input("请输入minvalue: "))
    except:
        continue
    try:
        cur.execute("INSERT INTO sensorlist(sensorname, maxvalue, minvalue) VALUES(?, ?, ?)", (sensorname, maxvalue, minvalue))
        db.commit()
    except:
        pass
cur.close()
db.close()