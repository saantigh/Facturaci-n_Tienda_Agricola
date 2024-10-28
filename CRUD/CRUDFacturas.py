from Modelo.factura import Factura 
import CRUDAntibiotico
import CRUDCliente
import CRUDFertilizante
import CRUDPlagas

class CRUDfacturas:
    @staticmethod
    def create():
        plagas_disponibles = CRUDPlagas()
        fertilizantes_disponibles = CRUDFertilizante()
        antibioticos_disponibles = CRUDAntibiotico()

        stock_plagas = plagas_disponibles.create()
        stock_fertilizantes = fertilizantes_disponibles.create()
        stock_antibioticos = antibioticos_disponibles.create()

        factura1=Factura()
        factura1.asociar_antibiotico(stock_antibioticos[0])
        factura1.asociar_producto_control(stock_plagas[0])
        factura1.asociar_producto_control(stock_fertilizantes[0])

        factura2=Factura()
        factura2.asociar_antibiotico(stock_antibioticos[0])
        factura2.asociar_producto_control(stock_plagas[1])
        factura2.asociar_producto_control(stock_fertilizantes[2])

        factura3=Factura()
        factura3.asociar_antibiotico(stock_antibioticos[4])
        factura3.asociar_producto_control(stock_plagas[3])
        factura3.asociar_producto_control(stock_fertilizantes[1])

        factura4=Factura()
        factura4.asociar_antibiotico(stock_antibioticos[4])
        factura4.asociar_antibiotico(stock_antibioticos[3])
        factura4.asociar_producto_control(stock_plagas[3])
        factura4.asociar_producto_control(stock_fertilizantes[3])

        factura5=Factura()
        factura5.asociar_producto_control(stock_plagas[4])

        return [factura1,factura2,factura3,factura4,factura5]
