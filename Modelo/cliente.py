
class Cliente:
    def __init__(self, nombre_cliente: str, cedula: str):
        self._nombre_cliente = nombre_cliente
        self._cedula = cedula
        self._facturas = []  # Lista para almacenar las facturas del cliente

    @property
    def nombre_cliente(self):
        return self._nombre_cliente

    @nombre_cliente.setter
    def nombre_cliente(self, nombre_cliente):
        if len(nombre_cliente) >= 3:
            self._nombre_cliente = nombre_cliente
        else:
            raise ValueError("El nombre debe tener al menos 3 caracteres.")

    @property
    def cedula(self):
        return self._cedula

    @cedula.setter
    def cedula(self, cedula):
        if cedula.isdigit() and len(cedula) >= 7:
            self._cedula = cedula
        else:
            raise ValueError("La cédula debe ser numérica y tener al menos 7 dígitos.")
    
 
    @property
    def facturas(self):
        return self._facturas
    
    
    @facturas.setter
    def facturas(self, factura):
        self._facturas.append(factura)


    def asociar_factura(self, factura):
        self.facturas = factura