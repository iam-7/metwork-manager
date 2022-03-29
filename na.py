from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import mysql.connector,db
import user_management,inventory_mgt,devconf

# Database SetUp
mydb = mysql.connector.connect(
  host="localhost",
  user="guru",
  passwd="Dominus@5",
  database="network_manager"
)
#
 
app = Flask(__name__)
 
@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template("dashboard.html")


@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route("/login", methods=['POST'])
def login():
    user_form = request.form['username']
    pass_form = request.form['pass']
    session['logged_in'] = True
    return user_management.userlogin(user_form,pass_form)


@app.route('/adduser',methods=['POST','GET'])
def adduser():
        if not session.get('logged_in'):
                return render_template('login.html')
        else:
                if request.method == 'GET':
                        return render_template('register.html')
                else:
                        user_form = request.form['user']
                        user_email = request.form['email']
                        return user_management.createUser(user_form,user_email)

@app.route('/resetpassword',methods=['POST','GET'])
def passreset():
        if request.method == 'GET':
                return render_template('password-reset.html')
        else:
                oldpass = request.form['oldpass']
                email = request.form['email']
                newpass = request.form['newpass']
                passrep = request.form['passrep']
                user_pass = db.getuser(email)
                print(user_pass)
                if oldpass == user_pass[0][0]:
                        if newpass == passrep:
                                return user_management.resetpassword(email,newpass)
                        else:
                                return render_template('password-reset.html',message='Password does not match',id=0)
                else:
                        return render_template('password-reset.html',message='Password entered for user is Incorrect',id=0)

                

pin = 1111
reset_email = ''
@app.route('/forgot_password',methods=['POST','GET'])
def forgotpassword():
        if request.method == 'GET':
                return render_template('forgot-password.html')
        else:
                email = request.form['email']
                global reset_email
                reset_email = email 
                global pin
                pin = user_management.forgotpassword(email)
                return render_template('pin-verification.html')

@app.route('/pinverify',methods=['POST'])
def verifypin():
        print(pin)
        form_pin = int(request.form['pin'])
        print(form_pin)
        if pin == form_pin:
                return render_template('new-password.html')
        else:
                return render_template('pin-verification.html')

@app.route('/newpassword',methods=['POST'])
def newpass():
        password = request.form['pass']
        return user_management.resetpassword(reset_email,password)

@app.route('/changepassword',methods=['POST'])
def changepass():
        password = request.form['newpass']
        email = request.form['email']
        return user_management.resetpassword(email,password)

@app.route('/inventory',methods=['POST','GET'])
def inventory():
        
        if not session.get('logged_in'):
                return render_template('login.html')
        else:
                if request.method == 'GET':
                        removed=0
                        return inventory_mgt.showdev(removed)

@app.route('/adddevice',methods=['POST','GET'])
def add_device():
        if request.method == 'GET':
                return render_template('add-device.html')
        else:
                hostname = request.form['host']
                ip = request.form['ip']
                devtype = request.form['device']
                return inventory_mgt.adddevice(hostname,ip,devtype)

@app.route('/check_status',methods=['POST','GET'])
def checkstatus():
        if request.method == 'POST':
                ip = request.form['ip']
                return inventory_mgt.check_status(ip)

@app.route('/removedevice',methods=['POST'])
def remove():
        return inventory_mgt.removedevice(request.form['ip'])

@app.route('/users')
def user():
        return user_management.listusers()

@app.route('/backupall',methods=['POST'])
def backupall():
        user = request.form['user']
        pwd = request.form['pass']
        return inventory_mgt.getconfig(user,pwd)

@app.route('/showconfig',methods=['POST'])
def showconfig():
        host = request.form['host']
        return devconf.shconfig(host)






if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=4000)
