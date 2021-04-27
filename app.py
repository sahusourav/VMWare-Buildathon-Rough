from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.secretkey = 'a'
app.config['MYSQL_HOST'] = "remotemysql.com"
app.config["MYSQL_USER"] = "n78u8LCcCJ"
app.config["MYSQL_PASSWORD"] = "OwOGqi6KgD"
app.config["MYSQL_DB"] = "n78u8LCcCJ"

mysql = MySQL(app)

@app.route('/')
def home():
    return render_template('apply.html')
    
@app.route('/uploaddata', methods = ["POST"])
def uploaddata():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        stream = request.form["stream"]
        address = request.form["address"]
        
        cursor = mysql.connect.cursor()
        cursor.execute('INSERT INTO newtable VALUES(NULL, % s, % s, % s, % s)', (name, email, stream, address))
        mysql.connection.commit()
        
        msg = "You've successfully got registered"
        
        return render_template('apply.html', msg = msg)
        
    
if __name__ == '__main__':
    app.run(debug = True)