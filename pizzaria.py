from sqlite3 import connect
from unittest import result
from flask import redirect, request, url_for
from flask import Flask
from flask import render_template
import db 

app= Flask(__name__)

@app.route('/')
def home_page():

    return render_template('main.html')


@app.route('/Register', methods=['GET','POST'])
def Register():
    if request.method=="POST":
        name = request.form['name']
        email= request.form['email']
        password= request.form['password']
        address= request.form['address']
        connect= db.get_db()
        connect.execute(f"""INSERT INTO users(name,email,password,address)VALUES('{name}', '{email}', '{password}','{address}');""")
        connect.commit()
        db.close_db(connect)
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

@app.route('/make_order', methods=['GET', 'POST'])
def make_order():
    if request.method =="POST" :
        name = request.form['dish_name']
        size = request.form['size']
        amount = request.form['amount']
        connect= db.get_db()
        connect.execute(f""" INSERT INTO orders (dish_name, size, amount)
                             VALUES('{name}','{size}','{amount}');""")
        connect.commit()
        db.close_db(connect)
    return render_template('MakeOrder.html')       


@app.route('/payment')
def payment():
    render_template()    