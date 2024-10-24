class UI:
    def mostrar_menu_principal(self):
        print("BIENVENIDO AL SISTEMA GESTOR DE FACTURACION AGRICOLA\n\n")
        print("Digite la opción que desea realizar\n")
        print("1) Agregar cliente a la base de datos\n2) Buscar cliente y listar todas sus facturas\n3) Eliminar cliente de la base de datos\n 4) Vender producto a un cliente\n\n")

    def interfaz_agregar_cliente(self):
        print("Digite la informacion del cliente que desea ingresar: \n")
        nombre_cliente = str(input("Digite el nombre completo del cliente: "))
        cedula_cliente = str(input("Digite la cedula del cliente: "))
        return nombre_cliente,cedula_cliente
    
