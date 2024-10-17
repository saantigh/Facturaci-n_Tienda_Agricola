# TEST Para realizar el DEBUG

from Modelo.cliente import Cliente
from Modelo.factura import Factura

def main():
    # Crear un cliente
    cliente = Cliente("Juan Pérez", "12345678")

    # Crear una factura
    factura1 = Factura()
    factura2 = Factura()

    # Asociar productos a la factura
    factura1.realizar_venta(producto_control="FertiGrow", antibiotico="Penicilina")
    factura2.realizar_venta(producto_control="Plaguicida")

    # Asociar facturas al cliente
    cliente.asociar_factura(factura1)
    cliente.asociar_factura(factura2)

    # Hacer debug para inspeccionar las composiciones
    import pdb; pdb.set_trace()

if __name__ == "__main__":
    main()