class Libro:
    def __init__(self, titulo, id_autor, isbn, editorial,):
        """el init (constructor) inicia la clase y declara los atributos de cada clase"""
        self.titulo = titulo
        self.id_autor = id_autor
        self.isbn = isbn
        self.editorial = editorial
    
    def obt_titulo(self):
        """obtiene el titulo del libro"""
        return self.titulo

    def obt_id_autor(self):
        """obtiene el id del autor del libro"""
        return self.id_autor

    def obt_isbn(self):
        """obtiene el isbn del libro"""
        return self.isbn

    def obt_editorial(self):
        """obtiene la editorial del libro"""
        return self.editorial