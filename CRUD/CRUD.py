class CRUD:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente) #Inicializa la lista de clientes en el sistema

    def buscar_por_cedula(self, cedula):
        for cliente in self.clientes:
            if cliente.cedula == cedula:
                return cliente
        return None

    def eliminar_cliente(self, cedula):
        cliente = self.buscar_por_cedula(cedula)
        if cliente is None:
            raise ValueError("No se puede eliminar, el cliente no existe.")
        self.clientes.remove(cliente)

    def asociar_factura(self, cliente, facturas):
        if cliente not in self.clientes:
            raise ValueError("El cliente no existe.") 
        cliente.facturas.extend(facturas)

