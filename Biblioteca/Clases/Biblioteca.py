class Biblioteca:
    def  __init__(self, run, direccion, rs):
        self.run = run
        self.direccion = direccion
        self.rs = rs

    def mostrar_run(self):
        return self.run

    def mostrar_direccion(self):
        return self.direccion

    def mostrar_rs(self):
        return self.rs
