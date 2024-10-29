from datetime import date, datetime
import sqlite3
import os



#Notes Class
class Notes:
     #Creo el constructor y paso los parametros
    def __init__(self, title = str,description = str, date= date) -> None:
         #Atributos
        self.title       = title
        self.description = description
        self.date        = date.today()
        
    def search_notes(self):
        #logical fault
        print("")
    
    def obtener_descripcion_por_titulo(self, title):
        #Receives the title, finds the note and returns the description
        return title
    
        
    def create_note(self):
        con = sqlite3.connect("BD_Projecto.db", timeout=10)
        cur = con.cursor()
        today_date = datetime.now().strftime("%Y-%m-%d")
        cur.execute("INSERT INTO Notes (Title, Description, Date) VALUES (?,?,?)",( self.title, self.description, today_date))
        con.commit()
        con.close()

#Entering data to register a user
title_u = input("Enter title: ")
description_u = input("Enter description: ")
#End of data to register user

#Object
notes1 = Notes(
    title       = title_u,
    description = description_u
)

notes1.create_note()


#User Class

class User:
    def __init__(self, name = str, gmail= str, password = str) -> None:
        self.name     = name
        self.gmail    = gmail
        self.password = password
        self.my_notes = []
        
        
    #Methods
    def create_password(self):
        pass
      
    
    def edit_note(self,descripcion):
        pass
        #Sql
        
    def delete_notes(self):
        pass
        #sql
    
    def register_user(self):
        #This function allows you to save to the DB
        con = sqlite3.connect("BD_Projecto.db", timeout=10)
        cur = con.cursor()
        cur.execute("INSERT INTO User (Name, Gmail, Password) VALUES (?,?,?)",( self.name, self.gmail , self.password))
        con.commit()
        con.close()     
    
    def delete_user(self):
        pass


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


user.register_user()