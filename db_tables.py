from sqlite3 import connect
from db import get_db,close_db

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

def create_tables2():
  connect_db=get_db()
  try:
      connect_db.execute("""CREATE TABLE order(
        meal TEXT NOT NULL,
       address TEXT NOT NULL,
       amount INTEGER
   );""")

  except:
    print("table 2 already exists")
    connect_db.commit()
    close_db(connect_db)

create_tables2()


def create_tables3():
  connect_db=get_db()
  try:
      connect_db.execute("""CREATE TABLE menu(
        pizza_name TEXT NOT NULL,
        size TEXT,
        price INTEGER,

   );""")

  except:
    print("table 3 already exists")
    connect_db.commit()
    close_db(connect_db)

create_tables3()