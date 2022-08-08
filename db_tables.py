from sqlite3 import connect
from db import get_db,close_db

def Users():
    connect_db = get_db()
    try:
       connect_db.execute("""CREATE TABLE user (
                          email TEXT  NOT NULL, 
                          password TEXT NOT NULL,
                          name TEXT NOT NULL,
                          address TEXT NOT NULL
                        );""")
    except:

      print("table users already exists")
      connect_db.commit()
      close_db(connect_db)

Users()

def Make_Order() :
    connect_db = get_db()
    try:
      connect_db.execute("""CREATE TABLE orders (
                          name TEXT UNIQUE NOT NULL, 
                          size TEXT NOT NULL,
                          price INTEGER
                          amount INTEGER
                        );""")
    except:
      print("table orders already exists")
      connect_db.commit()
      close_db(connect_db)

Make_Order()

def menu() :
    connect_db = get_db()
    try:
      connect_db.execute("""CREATE TABLE menu (
                          name TEXT UNIQUE  NOT NULL, 
                          size TEXT NOT NULL,
                          price INTEGER
                        );""")
    except:
      print("table menu already exists")
      connect_db.commit()
      close_db(connect_db)

menu()


def branches():
    connect_db = get_db()
    try:
       connect_db.execute("""CREATE TABLE branch (
                          branch_name TEXT  NOT NULL, 
                          time TEXT NOT NULL,
                          hotline INTGER
                        );""")
    except:

      print("table branches already exists")
      connect_db.commit()
      close_db(connect_db)

branches()


