import sqlite3
db = sqlite3.connect('D:/ngca/data/data.db')
cur = db.cursor()
sensornumber = int(input("请输入增加的传感器数量: "))
for i in range(sensornumber):   
    sensorname = input("请输入sensorname: ")
    maxvalue = int(input("请输入maxvalue: "))
    minvalue = int(input("请输入minvalue: "))
    try:
        cur.execute("INSERT INTO sensorlist(sensorname, maxvalue, minvalue) VALUES('%s', %d, %d)" % (sensorname, maxvalue, minvalue))
        db.commit()
    except:
        pass
cur.close()
db.close()