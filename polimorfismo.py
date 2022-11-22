
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def avanza(self):
        print("Estoy caminando...")
    

class Ciclista(Persona):
    def __init__(self, nombre):
        super().__init__(nombre) # Ya hay referencia a la super clase con super
    
    def avanza(self):
        print('Moviendome en mi bicicleta')
    # Se puede compartir el nombre directamente sin tenerlo que declarar adentro de la instancia de ciclista. Aquí ya se pone en acción el polimorfismo

def main():
    persona = Persona('David')
    persona.avanza()

    ciclista = Ciclista('Daniel')
    ciclista.avanza()


if __name__ == '__main__':
    main()