# Clase Empleado

class Empleado:

    def __init__(self, nombre, cargo, edad, turno, codigo):
        self.nombre = nombre
        self.cargo = cargo
        self.edad = edad
        self.turno = turno
        self.codigo = codigo

    # ---------- getters ----------
    def get_nombre(self):
        return self.nombre

    def get_cargo(self):
        return self.cargo

    def get_edad(self):
        return self.edad

    def get_turno(self):
        return self.turno

    def get_codigo(self):
        return self.codigo

    # ---------- setters ----------
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_cargo(self, cargo):
        self.cargo = cargo

    def set_edad(self, edad):
        self.edad = edad

    def set_turno(self, turno):
        self.turno = turno

    def set_codigo(self, codigo):
        self.codigo = codigo

    # ---------- toString ----------
    def __str__(self):
        return ("Empleado: " + self.nombre +
                ", cargo " + self.cargo +
                ", edad " + str(self.edad) +
                ", turno " + self.turno +
                ", codigo " + str(self.codigo))


# prueba rapida
if __name__ == "__main__":
    e = Empleado("Carlos", "Operador", 30, "mañana", 101)
    print(e)
