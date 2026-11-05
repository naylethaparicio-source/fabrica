from producto import Producto
from inventario import Inventario


class Programa:
    """Controla la entrada de datos y el flujo del programa."""

    @staticmethod
    def leer_entero(mensaje, minimo):
        while True:
            try:
                valor = int(input(mensaje))
                if valor >= minimo:
                    return valor
                print(f"  Ingrese un número mayor o igual a {minimo}.")
            except ValueError:
                print("  Entrada inválida. Ingrese un número entero.")

    @staticmethod
    def leer_texto(mensaje):
        while True:
            texto = input(mensaje).strip()
            if texto:
                return texto
            print("  Este campo no puede estar vacío.")

    def ejecutar(self):
        print("=== GESTOR DE INVENTARIO DE SUPERMERCADO ===")
        inventario = Inventario()
        cantidad = self.leer_entero("Cantidad de productos en inventario: ", 1)

        for i in range(1, cantidad + 1):
            print(f"\nProducto {i}:")
            codigo = self.leer_texto("  Código: ")
            nombre = self.leer_texto("  Nombre: ")
            unidades = self.leer_entero("  Cantidad disponible: ", 0)
            inventario.agregar_producto(Producto(codigo, nombre, unidades))

        inventario.reporte()


if __name__ == "__main__":
    Programa().ejecutar()
