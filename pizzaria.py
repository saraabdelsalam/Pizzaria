from sqlite3 import connect
from unittest import result
from flask import redirect, request, url_for,flash
from flask import Flask
from flask import render_template
import db

app= Flask(__name__)
@app.route('/')
def home_page():

    return render_template('main.html')




@app.route('/Register',methods=['GET', 'POST'])
def Register():
    
    if request.method== 'POST':
        email=request.form['email']
        password= request.form['password']
        name= request.form['name']
        address=request.form['address']
        conn=db.get_db()
        conn.execute("""INSERT INTO user(email,password,name,address)Values('{email}','{password}','{name}',
            '{address}');  """)   
        conn.commit()
        return redirect(url_for('home_page'))    

    return render_template('register.html')    



@app.route('/menu_admin',methods=['GET', 'POST'])
def menu_admin():
    if request.method =="POST":
        name = request.form['name']
        size = request.form['size']
        price = request.form['price']
        connect= db.get_db()
        connect.execute(f""" INSERT INTO menu (name, size, price)
                             VALUES('{name}','{size}','{price}');""")
        connect.commit()
        db.close_db(connect)
        return redirect(url_for('menu'))
    return render_template('menu_admin.html')


@app.route('/menu')
def menu():
     connect= db.get_db().cursor()
     connect.execute('SELECT * FROM menu;')
     data= connect.fetchall()
     return render_template('menu.html',data = data)


@app.route('/branches',methods=['GET', 'POST'])
def branches_admin():
    if request.method =="POST" :
        branch_name = request.form['branch_name']
        time = request.form['time']
        hotline = request.form['hotline']
        connect= db.get_db()
        connect.execute(f""" INSERT INTO branch (branch_name,time ,hotline)
                             VALUES('{branch_name}','{time}','{hotline}');""")
        connect.commit()
        db.close_db(connect)
    return render_template('branches_admin.html')


@app.route('/search',methods=['GET','POST'])
def search():
       if request.method=="POST":
        search= request.form['search']
        con= db.get_db().cursor()
        con.execute(f"""SELECT * FROM branch WHERE branch_name='{search}';""")
        result=con.fetchall()
        db.close_db(con)
        
       return render_template('search.html',result=result )        



@app.route('/payment')
def payment():
    connect= db.get_db().cursor()
    connect.execute('SELECT * FROM orders')
    data= connect.fetchall()
    return render_template('payment.html',data=data)



@app.route('/make_order/<name>')
def make_order(name=None):
    
        conn= db.get_db().cursor()
        conn.execute(f"""SELECT * FROM menu WHERE name='{name}';""")
        result=conn.fetchall()
        db.close_db(conn)
        
        return render_template('MakeOrder.html',result=result) 


