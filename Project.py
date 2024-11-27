from datetime import date, datetime
import sqlite3
import os

#Notes Class
class Notes:
     #We create the constructor with parameters
    def __init__(self, title : str,description : str, date: date, userid: int) -> None:
         #Atributos
        self.title       = title
        self.description = description
        self.date        = date.today()
        self.userid      = userid
        
        
    def search_notes(self):
        con = sqlite3.connect("BD_Projecto.db", timeout=10)
        cur = con.cursor()
        res = cur.execute("SELECT Title, Description, Date FROM Notes")
        notes = res.fetchall() 
        print(notes)    
        con.close()
        
    def search_notes_id(self, id):
        con = sqlite3.connect("BD_Projecto.db", timeout=10)
        cur = con.cursor()
        res = cur.execute("SELECT Title, Description, Date FROM Notes WHERE IdN = ?", (id,))
        note = res.fetchone() 
        if note:
            print("Nota encontrada")
            print(note)
        else:
            print("No se encontró ninguna nota con ese ID.")
        con.close()

        
    def create_note(self):
        con = sqlite3.connect("BD_Projecto.db", timeout=10)
        cur = con.cursor()
        cur.execute("INSERT INTO Notes (Title, Description, Date) VALUES (?,?,?)",( self.title, self.description))
        con.commit()
        con.close()
        
        
    def delete_notes(self, id):
        con = sqlite3.connect("BD_Projecto.db", timeout=10)
        cur = con.cursor()
        res = cur.execute("DELETE FROM Notes WHERE IdN = ?", (id,))
        con.commit()
        if cur.rowcount > 0:
            print("Nota eliminada.")
        else:
            print("No se encontró ninguna nota con ese ID.")
        con.close()

    def edit_note(self, id, new_title, new_description):
        con = sqlite3.connect("BD_Projecto.db", timeout=10)
        cur = con.cursor()
        cur.execute("UPDATE Notes SET Title = ?, Description = ? WHERE IdN = ?", (new_title, new_description, id))
        con.commit()
        if cur.rowcount > 0:
            print("Nota actualizada.")
        else:
            print("No se encontró ninguna nota con ese ID.")
        con.close()


#Entering data to register a user
title_u = input("Enter title: ")
description_u = input("Enter description: ")
user_u = input("Enter Id: ")
#End of data to register user

#Object
notes1 = Notes(
    title       = title_u,
    description = description_u,
    date=date.today(),
    userid=user_u
)

#Testing Notes functions
#notes1.create_note()
#notes1.search_notes()
#notes1.search_notes_id(user_u)
#notes1.delete_notes(user_u)
#notes1.edit_note(user_u, title_u, description_u)


#User Class

class User:
    def __init__(self, name : str, gmail: str, password : str) -> None:
        self.name     = name
        self.gmail    = gmail
        self.password = password
        self.my_notes = []
        
    #Methods
    
    def register_user(self):
        #This function allows you to save to the DB
        con = sqlite3.connect("BD_Projecto.db", timeout=10)
        cur = con.cursor()
        cur.execute("INSERT INTO User (Name, Gmail, Password) VALUES (?,?,?)",( self.name, self.gmail , self.password))
        con.commit()
        con.close()     
    
    def delete_user(self,id):
        con = sqlite3.connect("BD_Projecto.db", timeout=10)
        cur = con.cursor()
        res = cur.execute("DELETE FROM User WHERE IdU = ?", (id,))
        con.commit()
        if cur.rowcount > 0:
            print("Usuario eliminado.")
        else:
            print("No se encontró ningun usuario con ese ID.")
        con.close()
        


#Entering data to register a user
name_u = input("Enter Username: ")
gmail_u = input("Enter User Gmail: ")
password_u = input("Enter User Password: ")
#End of data to register user

#Object
user=User(
    name     = name_u,
    gmail    = gmail_u,
    password = password_u
)

#Testing User functions

#user.register_user()
#user.delete_user(user_u)

