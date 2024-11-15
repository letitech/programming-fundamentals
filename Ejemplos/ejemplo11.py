class Libro:
    def __init__(self, titulo, autor, numero_paginas):
        self.atributo_titulo = titulo
        self.atributo_autor = autor
        self.atributo_numero_paginas = numero_paginas
        
class Biblioteca:
    def __init__(self):
        self.atributo_libro = list()
        
    def agregarLibro(self, libro):
        self.atributo_libro.append(libro)
    
    def agregarLibros(self, libros):
        self.atributo_libro += libros
        
    def obtenerLibros(self):
        for libro in self.atributo_libro:
            print(libro.atributo_titulo)
        
libro1 = Libro("Padre Rico Padre Pobre", "Robert T. Kiyosaki", 170)
libro2 = Libro("Cómo hacer amigo e influir sobre la gente", "Dale Carnegie", 300)
biblioteca = Biblioteca()
biblioteca.agregarLibro(libro1)
biblioteca.agregarLibro(libro2)