from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort

def shconfig(host):
    filename = 'C:/new project/configurations/'+host+'.txt'

    with open(filename,"r") as config:
        content = config.read()
    return render_template('show-config.html',hostname=host,config=content)