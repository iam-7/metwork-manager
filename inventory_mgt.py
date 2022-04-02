from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
import os
import mysql.connector
import user_management, app,notifications
import automation

# Database SetUp
mydb = mysql.connector.connect(
  host="localhost",
  user="guru",
  passwd="Dominus@5",
  database="network_manager"
)
#

def adddevice(host,ip,type):
    mycursor = mydb.cursor()
    cmd = "SELECT * FROM  inventory where ip = '{}' ".format(ip)
    mycursor.execute(cmd)
    result = mycursor.fetchall()
    if result:
        value = 'Device with '+ip+' Already exits'
        return render_template('add-device.html',message=value,id=0)
    else:
        sql = "INSERT INTO inventory (hostname, ip, devtype) VALUES ('{}', '{}', '{}')".format(host, ip, type)
        mycursor.execute(sql)
        mydb.commit()
        return render_template('add-device.html',message='Device added to inventory',id=1)

def showdev(removed):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM  inventory")
    result = mycursor.fetchall()
    device_status=list()
    print(result)
    for device in result:
      if status(device[1]):
        device_status.append(1)
      else:
        device_status.append(0)
        notifications.send_mail(device[1],device[2])


    if removed == 1:
      return render_template('inventory.html',data=zip(result,device_status),message='Device Removed',id=1)
    else:
      return render_template('inventory.html',data=zip(result,device_status))
     

def check_status(ip):
    
    response = os.system("ping -n 1 " + ip)
    if response == 0:
      return "<script>alert('up')</script>"
    else:
      return "<script>alert('Down')</script>"

def status(ip):
    response = 0 #os.system("ping -n 1 " + ip)
    print(response)
    if response == 0:
      return True
    return False

def removedevice(ip):
    mycursor = mydb.cursor()
    mycursor.execute("delete FROM inventory where ip = %s ",(ip,))
    mydb.commit()
    removed=1
    return showdev(removed)
        
def getconfig(username,password):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT ip FROM  inventory")
    device_inventory = mycursor.fetchall()
    for device in device_inventory:
      ip = device[0]
      automation.backupconfig(username,password,ip)
    return render_template('dashboard.html',message='Configuration backup done',id=1)


