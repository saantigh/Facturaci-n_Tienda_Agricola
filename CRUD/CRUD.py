class CRUD:
    def __init__(self):
        self.clientes = []  # Lista de clientes

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def buscar_por_cedula(self, cedula):
        """Busca un cliente por su cédula."""
        for cliente in self.clientes:
            if cliente.cedula == cedula:
                return cliente
        return None

    def eliminar_cliente(self, cedula):
        """Elimina un cliente por cédula."""
        cliente = self.buscar_por_cedula(cedula)
        if cliente:
            self.clientes.remove(cliente)
            print(f"Cliente con cédula {cedula} eliminado correctamente.")
        else:
            print(f"No se encontró ningún cliente con la cédula {cedula}.")

    def asociar_factura(self, cliente, factura):
        """Asocia una factura a un cliente ya existente"""
        cliente.facturas = factura # Usa el método de cliente para agregar la factura
        print(f"Factura asociada correctamente al cliente {cliente.nombre_cliente}")
