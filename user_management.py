from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import mysql.connector
import smtplib,random

# Database SetUp
mydb = mysql.connector.connect(
  host="localhost",
  user="guru",
  passwd="Dominus@5",
  database="network_manager"
)
#


def userlogin(user_form,pass_form):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT username,password FROM  users where email = %s ",(user_form,))
    result = mycursor.fetchall()
    if result:
        if result[0][1] == pass_form:
            session['logged_in'] = True
            return render_template('dashboard.html')
        else:
            return render_template('login.html',message='Incorrect Password')
    else:
        return render_template('login.html',message='User not found')

def createUser(user_form,user_email):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM  users where email = %s ",(user_email,))
    result = mycursor.fetchall()
    if result:
        return render_template('register.html',message='User Already exits',id=0)
    else:
        user_pass = password_gen()
        sql = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        val = (user_form,user_email,user_pass)
        mycursor.execute(sql, val)
        mydb.commit()
        accconf(user_email,user_pass)
        return render_template('register.html',message='User added',id=1)    

def accconf(email,password):
    gmail_user = 'guru.5798.r@gmail.com'  
    gmail_password = 'Dominus@5'

    sent_from = gmail_user  
    to = [email]  
    subject = 'Account conformation'  
    body = """
    Your account has been created. You can Login to your network manager account
    Username : %s
    password : %s
    """ % (email,password)

    email_text = """  
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    return

def forgotpassword(email):
    pin = random.randint(999,999999)
    gmail_user = 'guru.5798.r@gmail.com'  
    gmail_password = 'Dominus@5'

    sent_from = gmail_user  
    to = [email]  
    subject = 'Password reset'  
    body = """
    Your secreat Pin to reset your password
                PIN : %s
    """ % (pin)

    email_text = """  
    From: %s  
    To: %s  
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()
    return pin

def resetpassword(email,password):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM  users where email = %s ",(email,))
    result = mycursor.fetchall()
    if result:
        sql = "update users set password = %s where email = %s"
        val = (password,email)
        mycursor.execute(sql, val)
        mydb.commit()
        return render_template('dashboard.html',message='Password Updated',id=1)
    else:
        return render_template('password-reset.html',message='User not found',id=0)
    
def password_gen():
    chars = 'zxcvbnmasSDFGHJKLQdfghjklqwerty!@#45678$%^&*uiopZXCVBNMAWERTYUIOP12390'
    password = ''
    for c in range(8):
        password+=random.choice(chars)
    return password

def listusers():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM  users")
    result = mycursor.fetchall()
    return render_template('users.html',data=result)