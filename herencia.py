# class Rectangulo:
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura
    
#     def area(self):
#         return self.base * self.altura


# class Cuadrado(Rectangulo): # Se le define la superclase entre parentesis. La clase cuadrado extiende a Rectangulo
#     '''
#     super nos permite obtener una referencia directa de la superclase, se obtiene la referencia al rectangulo y podemos llamar a su constructor. Siempre que se inicializa una subclase se debe inicializar tambien las superclases
#     '''
#     def __init__(self, lado):
#         super().__init__(lado, lado)



# if __name__ == '__main__':
#     rectangulo = Rectangulo(base=3, altura=4)
#     print(rectangulo.area())

#     cuadrado = Cuadrado(lado=5)
#     print(cuadrado.area()) # Podemos ejecutar el método area sin haberlo definido, se está heredando el método area de la superclase rectangulo


# Se creará una jerarquia de administrador y empleado de una tienda

class Admin:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad= edad
    
    def vender(self):
        print(f"{self.nombre} puede vender en la tienda y tiene {self.edad} años")
    
    def abrirTienda(self):
        print(f"{self.nombre} puede abrir la tienda y tiene {self.edad} años")


class Empleado(Admin):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)

if __name__ == '__main__':
    persona1 = Admin('Jose', 25)
    persona1.vender()
    persona1.abrirTienda()

    persona2 = Empleado('Daniel', 19)
    persona2.vender()
    persona2.abrirTienda()