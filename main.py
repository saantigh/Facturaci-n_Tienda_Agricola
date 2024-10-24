from Modelo.cliente import Cliente
from Modelo.factura import Factura
from CRUD.CRUD import CRUD

def main():
    # crear el crud
    crud = CRUD()
    # Crear un cliente
    cliente = Cliente("Juan Pérez", "12345678")

    # Agregar Cliente al CRUD
    crud.agregar_cliente(cliente)

    cliente2 = crud.buscar_por_cedula("12345678")

    nombre_cliente = cliente2.nombre_cliente
    print(nombre_cliente)

    # Crear una factura
    factura1 = Factura()
    factura2 = Factura()

    # Asociar productos a la factura
    factura1.realizar_venta(producto_control="FertiGrow", antibiotico="Penicilina")
    factura2.realizar_venta(producto_control="Plaguicida")

    # Asociar facturas al cliente
    crud.asociar_factura(cliente2,factura2)

    # Hacer debug para inspeccionar las composiciones
   # import pdb; pdb.set_trace()

if __name__ == "__main__":
    main()