class Biblioteca:
    def  __init__(self, run, direccion, rs):
        """Constructor de la clase Biblioteca"""
        self.run = run
        self.direccion = direccion
        self.rs = rs

    def mostrar_run(self):
        """Muestra el run de la biblioteca"""
        return self.run

    def mostrar_direccion(self):
        """muestra la dirección de la biblioteca"""
        return self.direccion

    def mostrar_rs(self):
        """muestra la razon social de la biblioteca"""
        return self.rs
