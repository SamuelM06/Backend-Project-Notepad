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
        
    def Search_Note(self):
        #Falta logica
        print("")
    
    def Obtener_descripcion_por_titulo(self, title):
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
    def Create_Password(self):
        pass
    
    def Create_Note(self):
        #Pedir al usuario los datos de la nota
        title_u= input("Digite titulo: ")
        description_u= input("Digite descripcion: ")
        #Fin ingreso de datos
        #Instancia
        mi_nota = Notes(
            title = title_u,
            description = description_u,
            user_id = self.id #De donde sale este id?
        )
        
        self.mis_notas.append(mi_nota)
    
    def edit_note(self,descripcion):
        pass
        #minuscualas
    def Delete_Notes(self):
        pass
    
    def Save_Notes(self):
        #Esta funcion permite guardar en la DB
        con = sqlite3.connect("BD_Projecto.db")
        cur = con.cursor()
        cur.execute("INSERT INTO User (Name, Gmail, Password) VALUES (?,?,?)",( self.name, self.gmail , self.password))
        con.commit()
        #Imprimir todas las tablas de la DB
        res = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
        print(res.fetchall())




user=User(
    name="Samuel Mena",
    gmail="Samuel123@gmail,com",
    password="123456"
)
user.Save_Notes()

#Ingreso de datos para registrar un usuario
"""
    name =input("Digite Nombre de Usuario: ")
    gmail =input("Digite Gmail de Usuario: ")
    password =input("Digite password de Usuario: ")
"""