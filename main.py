import imp
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
import sqlite3
from sqlalchemy.sql import alias, select


meta=MetaData()


engine = create_engine('sqlite:///siteRe.db', echo=True)

users = Table('users', meta, Column('id', Integer, primary_key=True), 
Column('nom', String), Column('prenom', String), Column('departement', String), Column('mail', String), Column('id_amis', String) )
meta.create_all(engine)

amis = Table('amis', meta, Column('id', Integer, primary_key=True), 
Column('id_my', Integer), Column('id_ami', Integer), )
meta.create_all(engine)

# ins=users.insert()
# ins=users.insert().values(name='Ravi', lastname='Kapoor')
# conn = engine.connect()
# result = conn.execute(ins)


# s=users.select()
# conn = engine.connect()
# s=users.select().where(users.c.id>2)
# result=conn.execute(s)
# for row in result:
#  print (row)
def insert_into(nom, prenom, departement, mail):
  try:
    conn = sqlite3.connect('siteRe.db')
    cur = conn.cursor()
    print("Connexion réussie à SQLite")
    sql = "INSERT INTO users (nom, prenom, departement, mail) VALUES (?, ?, ?, ?)"
    value = (nom, prenom, departement, mail)
    cur.execute(sql, value)
    conn.commit()
    print("Enregistrement inséré avec succès dans la table users")
    cur.close()
    conn.close()
    print("Connexion SQLite est fermée")
  except sqlite3.Error as error:
    print("Erreur lors de l'insertion dans la table users", error)

def insert_ami(id_ami):
  try:
    conn = sqlite3.connect('siteRe.db')
    cur = conn.cursor()
    print("Connexion réussie à SQLite")
    sql = "INSERT INTO users (ami) VALUES (?)"
    value = (id_ami)
    cur.execute(sql, value)
    conn.commit()
    print("Enregistrement inséré avec succès dans la table users")
    cur.close()
    conn.close()
    print("Connexion SQLite est fermée")
  except sqlite3.Error as error:
    print("Erreur lors de l'insertion dans la table users", error)


id_ami="1"
insert_ami(id_ami)


nom="breil"
prenom="yoyo"
departement="azerty"
mail="breilkom@gmail.com"
insert_into(nom, prenom, departement, mail)
# insert_into('Breil', 'Paris')

# from sqlalchemy.orm import sessionmaker
# Session = sessionmaker(bind=engine)
# session = Session()
# c1 = users(name='Breil', address='bxl', 
# email='breilkom@gmail.com')
# session.add(c1)
# session.commit()

#selection des amis
def select(conn, priority):
    """
    Query tasks by priority
    :param conn: the Connection object
    :param priority:
    :return:
    """
    cur = conn.cursor()
    cur.execute("SELECT nom, prenom  FROM users WHERE departement=?")
    
    departement = "football"
    # departement = "tennis"
    # departement = "basket"

    rows = cur.fetchall()
    for row in rows:
        print(row)



