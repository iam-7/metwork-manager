'''import smtplib

gmail_user = 'guru.5798.r@gmail.com'  
gmail_password = 'Dominus@5'

sent_from = gmail_user  
to = ['guru.5798.r@gmail.com']  
subject = 'OMG Super Important Message'  
body = "Hey, what's up"

email_text = """\  
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
import random

pin = random.randint(999, 9999999)
print(pin)
import socket
import sys,os
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Create a TCP/IP socket
server_ip = input('Enter server IP : ')
rep = os.system('ping ' + server_ip)
if rep == 0:
    print('n n server is up n n')
else:
    print('server is down')
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="guru",
  passwd="Dominus@5",
  database="test"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM  guru")
result = mycursor.fetchall()
print(result)'''
import random
chars = 'zxcvbnmasSDFGHJKLQdfghjklqwerty!@#45678$%^&*uiopZXCVBNMAWERTYUIOP12390'
password = ''
for c in range(10):
    password+=random.choice(chars)
print(password)