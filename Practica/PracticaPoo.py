import os
os.system("cls")

#Clase Padre
class Personas:
    def __init__(self, nombre = str, edad = int, nacionalidad = str):
        self.nombre       = nombre
        self.edad         = edad
        self.nacionalidad = nacionalidad
        
    #Metodo
    def Saludar(self):
        print("Hola")
        
#Clase Hija
class Empleado(Personas):
    #Parametros de la clase padre y los que necesito
    def __init__(self, nombre = str, edad = int, nacionalidad = str, trabajo = str, salario = float): 
        super().__init__(nombre , edad, nacionalidad)
        self.trabajo = trabajo
        self.salario = salario
        
#Objeto
Empleado1 = Empleado(
    nombre="Samuel",
    edad=19,
    nacionalidad="Colombiano",
    trabajo="Python Developer",
    salario=1300000
)

class Estudiante(Personas):
    def __init__(self, nombre=str, edad=int, nacionalidad=str, grado = str):
        super().__init__(nombre, edad, nacionalidad)
        self.grado = grado
        
#Empleado1.Saludar()

aprendiz = Estudiante(
    nombre="Samuel Mena",
    edad=19,
    nacionalidad="Colombiano",
    grado="Aprendiz Sena"
)

print(f"El estudiante {aprendiz.nombre} tiene {aprendiz.edad}, y es: {aprendiz.grado}")
