class Edificio:
    """Edificio que contiene los sensores y genera el resumen final."""

    def __init__(self):
        self.sensores = []

    def agregar_sensor(self, sensor):
        self.sensores.append(sensor)

    def resumen(self):
        conteo = {"fría": 0, "óptima": 0, "caliente": 0}
        for s in self.sensores:
            conteo[s.categoria] += 1

        print("\n===== RESUMEN DE TEMPERATURAS =====")
        print(f"Habitaciones frías (calefacción encendida):  {conteo['fría']}")
        print(f"Habitaciones óptimas (sin acción):           {conteo['óptima']}")
        print(f"Habitaciones calientes (aire acondicionado): {conteo['caliente']}")
        print(f"Total de habitaciones:                       {len(self.sensores)}")
