# Clase Objeto (la pieza que levanta el brazo con las ventosas)

class Objeto:

    def __init__(self, nombre, material, peso, color, tamano):
        self.nombre = nombre
        self.material = material
        self.peso = peso
        self.color = color
        self.tamano = tamano

    # ---------- getters ----------
    def get_nombre(self):
        return self.nombre

    def get_material(self):
        return self.material

    def get_peso(self):
        return self.peso

    def get_color(self):
        return self.color

    def get_tamano(self):
        return self.tamano

    # ---------- setters ----------
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_material(self, material):
        self.material = material

    def set_peso(self, peso):
        self.peso = peso

    def set_color(self, color):
        self.color = color

    def set_tamano(self, tamano):
        self.tamano = tamano

    # ---------- toString ----------
    def __str__(self):
        return ("Objeto: " + self.nombre +
                ", material " + self.material +
                ", peso " + str(self.peso) + " kg" +
                ", color " + self.color +
                ", tamaño " + self.tamano)


# prueba rapida
if __name__ == "__main__":
    o = Objeto("Puerta", "metal", 12.5, "gris", "grande")
    print(o)
