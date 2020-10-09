from flask import Flask, render_template, request
import mysql.connector
import os

app=Flask(__name__, static_folder='assets')

conn=mysql.connector.connect(host="remotemysql.com", user="mYM5R3a4Nk", password="63d9k8viAd", database="mYM5R3a4Nk" )
cursor=conn.cursor()

@app.route('/')
def index ():
    return render_template('index.html')


@app.route('/signup')
def about ():
    return render_template('signup.html')

@app.route('/notif')
def notif():
    return render_template('notif.html')

@app.route('/index_validation', methods=['post'])
def index_validation():
    userid=request.form.get('userid')
    password=request.form.get('password')
    cursor.execute("""SELECT * FROM `user`WHERE `userid` LIKE '{}' AND `password` LIKE '{}' """.format(userid,password))
    user=cursor.fetchall()

    if len(user)>0:
        return render_template('notif.html')
    else:
        return render_template('index.html')

    return user


    return "The email is {} and the password is {}".format(userid,password)

@app.route('/add_user', methods=['post'])
def add_user():
    name=request.form.get('uname')
    email=request.form.get('uemail')
    userid=request.form.get('uuserid')
    password=request.form.get('upassword')

    cursor.execute("""INSERT INTO `user`(`name`, `email`, `userid`, `password`)VALUES
    ('{}', '{}', '{}', '{}')""".format(name,email,userid,password))
    conn.commit()

    return "User registered succesfully"

if __name__=="__main__":

    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, threaded=True)

    app.run(debug=True)

   