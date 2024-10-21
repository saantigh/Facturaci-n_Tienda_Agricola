from Modelo.cliente import Cliente
from Modelo.factura import Factura

class CRUD:
    def __init__(self):
        self.clientes = []  # Lista para almacenar los clientes

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def buscar_por_cedula(self, cedula):
        # Buscar al cliente por la cédula
        for cliente in self.clientes:
            if cliente.cedula == cedula:
                print(f"Cliente encontrado: {cliente.nombre_cliente}")
                print("Facturas asociadas:")

                # Iterar sobre las facturas del cliente
                for factura in cliente.facturas:
                    print("Productos control:")
                    for producto in factura.producto_control:
                        print(f"- {producto.nombre_producto}")
                    
                    print("Antibióticos:")
                    for antibiotico in factura.antibiotico:
                        print(f"- {antibiotico.nombre_antibiotico}")

                return  # Salir de la función una vez encontrado el cliente

        # Si no se encontró el cliente
        print("Cliente no encontrado.")


def eliminar_cliente(self, cedula):
        # Buscar al cliente por la cédula y eliminarlo si se encuentra
        cliente_encontrado = self.buscar_por_cedula(cedula)
        if cliente_encontrado:
            self.clientes.remove(cliente_encontrado)
            print(f"Cliente con cédula {cedula} eliminado correctamente.")
        else:
            print(f"No se encontró ningún cliente con la cédula {cedula}.")