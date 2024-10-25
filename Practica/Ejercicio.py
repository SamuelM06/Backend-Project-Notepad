import os
os.system("cls")

class Estudiante:
    def __init__(self,nombre,edad,grado) -> None:
        self.nombre = nombre
        self.edad   = edad
        self.grado  = grado
    
    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando")

Nombre = input("Digite nombre: ")
Edad = int(input("Digite Edad: "))
Grado = int(input("Digite Grado: "))

Aprendiz = Estudiante(Nombre,Edad,Grado)

print(f""" 
      Nombre: {Aprendiz.nombre} \n
      Edad: {Aprendiz.edad}\n
      Grado: {Aprendiz.grado}\n
""")

while True:
    estudiar = input().lower()
    if estudiar == "estudiar":
        Aprendiz.estudiar()
        break   