class Sensor:
    """Sensor de temperatura instalado en una habitación."""

    def __init__(self, numero, temperatura):
        self.numero = numero
        self.temperatura = temperatura
        self.categoria = ""
        self.accion = ""
        self.evaluar()

    def evaluar(self):
        if self.temperatura < 18:
            self.categoria = "fría"
            self.accion = "Se enciende la calefacción"
        elif self.temperatura <= 25:
            self.categoria = "óptima"
            self.accion = "Sin acción"
        else:
            self.categoria = "caliente"
            self.accion = "Se activa el aire acondicionado"

    def __str__(self):
        return (f"Sensor {self.numero}: {self.temperatura:.1f}°C -> "
                f"{self.categoria.upper()} | {self.accion}")
