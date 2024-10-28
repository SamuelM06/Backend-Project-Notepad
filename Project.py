from datetime import date
import sqlite3
import os



#Clase Notas
class Notes:
     #Creo el constructor y paso los parametros
    def __init__(self, title = str,description = str, date= date) -> None:
         #Atributos
        self.title       = title
        self.description = description
        self.date        = date.today()
        
    def search_notes(self):
        #Falta logica
        print("")
    
    def obtener_descripcion_por_titulo(self, title):
        #Recibe el titulo, busca la nota y devuelve la descripcion
        return title
    



#Clase Usuarios

class User:
    def __init__(self, name = str, gmail= str, password = str) -> None:
        self.name     = name
        self.gmail    = gmail
        self.password = password
        self.mis_notas = []
        
        
    #Metodos        
    def create_password(self):
        pass
    
    def create_note(self):
        #Pedir al usuario los datos de la nota
        title_u= input("Digite titulo: ")
        description_u= input("Digite descripcion: ")
        #Fin ingreso de datos
        #Instancia
        mi_nota = Notes(
            title = title_u,
            description = description_u,
            user_id = self.id 
        )
        
        self.mis_notas.append(mi_nota)
    
    def edit_note(self,descripcion):
        pass
        #Sql
        
    def delete_notes(self):
        pass
        #sql
    
    def save_notes(self):
        #Esta funcion permite guardar en la DB
        con = sqlite3.connect("BD_Projecto.db")
        cur = con.cursor()
        cur.execute("INSERT INTO User (Name, Gmail, Password) VALUES (?,?,?)",( self.name, self.gmail , self.password))
        con.commit()





user=User(
    name="Eliecer Daza",
    gmail="Eliecerdaza@gmail.com",
    password="987654321"
)
user.save_notes()

#Ingreso de datos para registrar un usuario
"""
    name =input("Digite Nombre de Usuario: ")
    gmail =input("Digite Gmail de Usuario: ")
    password =input("Digite password de Usuario: ")
"""