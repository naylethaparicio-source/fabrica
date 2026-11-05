# Clase Carro

class Carro:

    def __init__(self, marca, modelo, color, placa, velocidad):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.placa = placa
        self.velocidad = velocidad

    # ---------- getters ----------
    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_color(self):
        return self.color

    def get_placa(self):
        return self.placa

    def get_velocidad(self):
        return self.velocidad

    # ---------- setters ----------
    def set_marca(self, marca):
        self.marca = marca

    def set_modelo(self, modelo):
        self.modelo = modelo

    def set_color(self, color):
        self.color = color

    def set_placa(self, placa):
        self.placa = placa

    def set_velocidad(self, velocidad):
        self.velocidad = velocidad

    # ---------- toString ----------
    def __str__(self):
        return ("Carro: " + self.marca + " " + self.modelo +
                ", color " + self.color +
                ", placa " + self.placa +
                ", velocidad " + str(self.velocidad) + " km/h")

    # ---------- métodos de funcionamiento ----------
    def encender(self):
        print("El carro " + self.placa + " esta encendido")

    def apagar(self):
        if self.velocidad == 0:
            print("El carro " + self.placa + " se apago")
        else:
            print("Primero hay que frenar para apagar el carro")

    def acelerar(self, cantidad):
        self.velocidad = self.velocidad + cantidad
        print("Acelerando... velocidad: " + str(self.velocidad) + " km/h")

    def frenar(self, cantidad):
        self.velocidad = self.velocidad - cantidad
        if self.velocidad < 0:
            self.velocidad = 0
        print("Frenando... velocidad: " + str(self.velocidad) + " km/h")

    def girar(self, direccion):
        print("El carro esta girando a la " + direccion)


# prueba rapida
if __name__ == "__main__":
    c = Carro("Mazda", "3", "rojo", "ABC123", 0)
    print(c)
    c.encender()
    c.acelerar(40)
    c.girar("derecha")
    c.frenar(40)
    c.apagar()
