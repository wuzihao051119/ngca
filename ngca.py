import datetime
import json
import sqlite3
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from flask import Flask, render_template, request

DATABASE = 'D:/ngca/data/data.db'
app = Flask(__name__)
@app.route("/")
def hello():
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    cur.execute("SELECT * FROM sensorlog WHERE sensorid = 1")
    data = cur.fetchall()
    cur.close()
    db.close()
    if data ==[]:
        return render_template('view.html', data = [], temp = "没有数据")
    else:
        temp1 = data[len(data) - 1]
        temp = temp1[2]
        return render_template('view.html', data = data, temp = temp)
@app.route("/input", methods = ['POST', 'GET'])
def add_data():
    if request.method == 'POST':
        sensorid = int(request.form.get('id'))
        sensorvalue = float(request.form.get('val'))
    else:
        sensorid = int(request.args.get('id'))
        sensorvalue = float(request.args.get('val'))
    nowtime = datetime.datetime.now()
    nowtime = nowtime.strftime('%Y-%m-%d %H:%M:%S')
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    try:
        cur.execute("INSERT INTO sensorlog(sensorid, sensorvalue, updatetime) VALUES(?, ?, ?)", (sensorid, sensorvalue, nowtime))
        db.commit()
        cur.execute("SELECT * FROM sensorlist where sensorid = ?", (sensorid,))
        rv = cur.fetchall()
    except:
        return 'Error'
    cur.close()
    db.close()
    maxrv = rv[0][2]
    minrv = rv[0][3]
    if sensorvalue > maxrv or sensorvalue < minrv:
        return '1'
    else:
        return '0'
@app.route("/get", methods = ['POST', 'GET'])
def get_data():
    if request.method == 'POST':
        sensorid = int(request.form.get('id'))
    else:
        sensorid = int(request.args.get('id'))
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    try:
        cur.execute("SELECT * FROM sensorlog where sensorid = ?", (sensorid,))
        data = cur.fetchall()
    except:
        return
    cur.close()
    db.close()
@app.route("/view", methods = ['POST', 'GET'])
def view_data():
    if request.method == 'POST':
        sensorid = int(request.form.get('id'))
    else:
        sensorid = int(request.args.get('id'))
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    try:
        cur.execute("SELECT * FROM sensorlog where sensorid = ?", (sensorid,))
        data = cur.fetchall()
    except:
        return
    cur.close()
    db.close()
    time=[]
    temperature=[]
    for item in data:
        temperature.append(item[2])
        time.append(item[3][11:19])
    font = FontProperties(fname = "C:/Windows/Fonts/simsun.ttc", size = 15)
    plt.plot(time, temperature)
    plt.xlabel(time)
    plt.ylabel(temperature)
    plt.title(str(sensorid) + "号传感器")
    plt.savefig("static/image/image.jpg", dpi = 200, format = "jpg")
    return render_template("image.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8080, debug = True)
