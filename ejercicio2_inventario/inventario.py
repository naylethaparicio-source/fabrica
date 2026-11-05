class Inventario:
    """Colección de productos y generación del reporte consolidado."""

    TITULOS = {
        "crítico": "CRÍTICO (reabastecimiento urgente, < 10 unidades)",
        "bajo stock": "BAJO STOCK (10 a 50 unidades)",
        "suficiente": "SUFICIENTE (> 50 unidades)",
    }

    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def reporte(self):
        print("\n===== REPORTE CONSOLIDADO DE INVENTARIO =====")
        for estado, titulo in self.TITULOS.items():
            grupo = [p for p in self.productos if p.estado == estado]
            print(f"\n{titulo} - {len(grupo)} producto(s)")
            if grupo:
                for p in grupo:
                    print(f"   • {p}")
            else:
                print("   (ninguno)")
        print(f"\nTotal de productos: {len(self.productos)}")
