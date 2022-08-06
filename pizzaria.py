from sqlite3 import connect
from unittest import result
from flask import redirect, request, url_for
from flask import Flask
from flask import render_template
import db

app= Flask(__name__)

@app.route('/home')
def home_page():

    return render_template('main.html')


@app.route('/Register')
def Register():

   return render_template('register.html')    

@app.route('/menu',methods=['GET', 'POST'])
def menu():
    #if request.method=="POST":
        # # pizza_name = request.form['pizza_name']
        # # size= request.form['size']
        # # price= request.form['price']
        # connect= db.get_db()
        # connect.execute(f"""INSERT INTO menu(pizza_name,size,price)VALUES('chicken ranch', 'large', 140);""")
        # connect.commit()
        # db.close_db(connect)
        # conn= db.get_db()
        # conn.execute('SELECT * FROM menu')
        # data= conn.fetchone()
    #return render_template('menu.html', data=data)
    return render_template('menu.html')

@app.route('/pick_your_order')
def pick_your_order():
    return render_template()         


@app.route('/payment')
def payment():
    render_template()    