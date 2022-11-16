
class Automovil:
    def __init__(self, modelo, marca, color): # Constructors
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'En reposo' # Variable privada
        self._motor = Motor(cilindros=4) # Variable privada. None es que no hay ningun valor

    def acelerar(self, tipo='despacio'):
        if tipo == 'rapida':
            self._motor.inyecta_gasolina(10)
        else:
            self._motor.inyecta_gasolina(3)
        self._estado = 'En movimiento'


class Motor:
    def __init__(self, cilindros, tipo='gasolina'): # tipo tiene un default keyword o parametro por defecto
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0 # Variable privada

    def inyecta_gasolina(self, cantidad):
        pass


class SistemaElectrico:
    def __init__(self, luces, voltaje=5):
        self.luces = luces
        self.voltaje = voltaje

    def encenderLuces(self, cantidad):
        pass