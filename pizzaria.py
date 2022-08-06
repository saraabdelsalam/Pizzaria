from sqlite3 import connect
from unittest import result
from flask import redirect, request, url_for
from flask import Flask
from flask import render_template
#import db

app= Flask(__name__)

@app.route('/home')
def home_page():

    return render_template('main.html')


@app.route('/Register')
def register():

   return render_template('register.html')    