from sqlite3 import connect
from db import get_db,close_db


def Make_Order() :
    connect_db = get_db()
    try:
      connect_db.execute("""CREATE TABLE orders (
                        name TEXT UNIQUE NOT NULL, 
                        size TEXT NOT NULL,
                        amount TEXT
                       );""")
    except:
      print("table orders already exists")
      connect_db.commit()
      close_db(connect_db)

Make_Order()


def create_tables():
  connect_db=get_db()
  try:
      connect_db.execute("""CREATE TABLE users(
        name TEXT NOT NULL,
  email TEXT NOT NULL,
  password TEXT NOT NULL,
  address TEXT NOT NULL
   );""")

  except:
    print("table 1 already exists")
    connect_db.commit()
    close_db(connect_db)

create_tables()