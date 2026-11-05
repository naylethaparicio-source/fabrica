from estudiante import Estudiante
from curso import Curso


class Programa:
    """Controla la entrada de datos y el flujo del programa."""

    NUM_NOTAS = 4

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
    def leer_nota(mensaje):
        while True:
            try:
                nota = float(input(mensaje).replace(",", "."))
                if 0 <= nota <= 5:
                    return nota
                print("  La nota debe estar entre 0.0 y 5.0.")
            except ValueError:
                print("  Entrada inválida. Ingrese un número.")

    @staticmethod
    def leer_texto(mensaje):
        while True:
            texto = input(mensaje).strip()
            if texto:
                return texto
            print("  Este campo no puede estar vacío.")

    def ejecutar(self):
        print("=== CALCULADORA DE CALIFICACIONES ACADÉMICAS ===")
        curso = Curso()
        cantidad = self.leer_entero("Número de estudiantes del curso: ")

        for i in range(1, cantidad + 1):
            print(f"\nEstudiante {i}:")
            nombre = self.leer_texto("  Nombre: ")
            notas = []
            for n in range(1, self.NUM_NOTAS + 1):
                notas.append(self.leer_nota(f"  Calificación {n} (0.0 - 5.0): "))
            curso.agregar_estudiante(Estudiante(nombre, notas))

        curso.resultados()
        curso.estadisticas()


if __name__ == "__main__":
    Programa().ejecutar()
