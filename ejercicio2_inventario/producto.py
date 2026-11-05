class Producto:
    """Producto del inventario con su nivel de stock."""

    def __init__(self, codigo, nombre, cantidad):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.estado = self.clasificar()

    def clasificar(self):
        if self.cantidad < 10:
            return "crítico"
        elif self.cantidad <= 50:
            return "bajo stock"
        else:
            return "suficiente"

    def __str__(self):
        return f"[{self.codigo}] {self.nombre} - {self.cantidad} unidades"
