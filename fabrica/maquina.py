# Clase Maquina (el brazo robotico)

class Maquina:

    def __init__(self, nombre, tipo, estado, cantidad_ventosas, potencia):
        self.nombre = nombre
        self.tipo = tipo
        self.estado = estado
        self.cantidad_ventosas = cantidad_ventosas
        self.potencia = potencia

    # ---------- getters ----------
    def get_nombre(self):
        return self.nombre

    def get_tipo(self):
        return self.tipo

    def get_estado(self):
        return self.estado

    def get_cantidad_ventosas(self):
        return self.cantidad_ventosas

    def get_potencia(self):
        return self.potencia

    # ---------- setters ----------
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_estado(self, estado):
        self.estado = estado

    def set_cantidad_ventosas(self, cantidad_ventosas):
        self.cantidad_ventosas = cantidad_ventosas

    def set_potencia(self, potencia):
        self.potencia = potencia

    # ---------- toString ----------
    def __str__(self):
        return ("Maquina: " + self.nombre +
                ", tipo " + self.tipo +
                ", estado " + self.estado +
                ", ventosas " + str(self.cantidad_ventosas) +
                ", potencia " + str(self.potencia) + " W")


# prueba rapida
if __name__ == "__main__":
    m = Maquina("Brazo 1", "brazo robotico", "activa", 4, 1500)
    print(m)
