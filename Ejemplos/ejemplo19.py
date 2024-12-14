class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
    
    def trabajar(self):
        print("Puedo trabajar")
        
persona1 = Persona("Benito", "Esono", 20)

print(persona1.nombre)