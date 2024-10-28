from flask import Flask, render_template
import pymysql

app = Flask(__name__)

connection = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='0000',
    db='kream',
    charset='utf8mb4'
)

cur = connection.cursor()
sql = "SELECT * FROM kream"
cur.execute(sql)

kream_data = cur.fetchall()

@app.route('/')
def index():
    return render_template('index.html', data_list=kream_data)

if __name__ == '__main__':
    app.run(debug=True, port=5500)