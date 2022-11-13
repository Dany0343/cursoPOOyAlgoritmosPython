class Coordenada:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distancia(self, otraCoordenada): # otraCoordenada es otra instancia de Coordenada
        # Para definir la distancia se utiliza el metodo euclidiano
        x_diff = (self.x - otraCoordenada.x) ** 2
        y_diff = (self.y - otraCoordenada.y) ** 2

        return (x_diff + y_diff) ** 0.5


if __name__ == '__main__':
    coord_1 = Coordenada(3, 30)
    coord_2 = Coordenada(4, 8)

    print(coord_1.distancia(coord_2))
    print(isinstance(coord_2, Coordenada)) # Método para saber si alguna de las coordenadas es instancia de Coordenada 