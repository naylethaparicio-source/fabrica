class Curso:
    """Colección de estudiantes y resumen estadístico del curso."""

    def __init__(self):
        self.estudiantes = []

    def agregar_estudiante(self, estudiante):
        self.estudiantes.append(estudiante)

    def resultados(self):
        print("\n===== RESULTADOS INDIVIDUALES =====")
        for e in self.estudiantes:
            print(e)

    def estadisticas(self):
        total = len(self.estudiantes)
        promedios = [e.promedio for e in self.estudiantes]
        mejor = max(self.estudiantes, key=lambda e: e.promedio)
        peor = min(self.estudiantes, key=lambda e: e.promedio)

        conteo = {"reprobado": 0, "regular": 0, "bueno": 0, "excelente": 0}
        for e in self.estudiantes:
            conteo[e.categoria] += 1

        aprobados = total - conteo["reprobado"]

        print("\n===== RESUMEN ESTADÍSTICO DEL CURSO =====")
        print(f"Total de estudiantes: {total}")
        print(f"Promedio general del curso: {sum(promedios) / total:.2f}")
        print(f"Mejor promedio: {mejor.nombre} ({mejor.promedio:.2f})")
        print(f"Menor promedio: {peor.nombre} ({peor.promedio:.2f})")
        print(f"Porcentaje de aprobación: {aprobados / total * 100:.1f}%")
        print("Distribución por categoría:")
        for categoria, cant in conteo.items():
            print(f"   {categoria.capitalize():<10}: {cant}")
