class Estudiante:
    """Estudiante con sus 4 calificaciones del periodo."""

    def __init__(self, nombre, notas):
        self.nombre = nombre
        self.notas = notas
        self.promedio = sum(notas) / len(notas)
        self.categoria = self.clasificar()

    def clasificar(self):
        # Condicionales anidadas
        if self.promedio < 3.0:
            return "reprobado"
        else:
            if self.promedio < 4.0:
                return "regular"
            else:
                if self.promedio <= 4.5:
                    return "bueno"
                else:
                    return "excelente"

    def __str__(self):
        notas = ", ".join(f"{n:.1f}" for n in self.notas)
        return (f"{self.nombre}: notas [{notas}] | promedio {self.promedio:.2f} "
                f"-> {self.categoria.upper()}")
