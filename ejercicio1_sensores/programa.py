from sensor import Sensor
from edificio import Edificio


class Programa:
    """Controla la entrada de datos y el flujo del programa."""

    @staticmethod
    def leer_entero(mensaje):
        while True:
            try:
                valor = int(input(mensaje))
                if valor >= 1:
                    return valor
                print("  Ingrese un número mayor o igual a 1.")
            except ValueError:
                print("  Entrada inválida. Ingrese un número entero.")

    @staticmethod
    def leer_decimal(mensaje):
        while True:
            try:
                return float(input(mensaje).replace(",", "."))
            except ValueError:
                print("  Entrada inválida. Ingrese un número.")

    def ejecutar(self):
        print("=== CONTROL DE SENSORES DE TEMPERATURA ===")
        edificio = Edificio()
        cantidad = self.leer_entero("Cantidad de sensores instalados: ")

        for i in range(1, cantidad + 1):
            temp = self.leer_decimal(f"Temperatura del sensor {i} (°C): ")
            sensor = Sensor(i, temp)
            edificio.agregar_sensor(sensor)
            print(f"  -> {sensor}")

        edificio.resumen()


if __name__ == "__main__":
    Programa().ejecutar()
