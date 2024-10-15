from CLASE_productos_de_control import ProductoControl as pc

class Factura:
    def __init__(self):
        self._antibiotico = []
        self._producto_control = []

    @property
    def antibiotico(self):
        return self._antibiotico
    
    
    @antibiotico.setter
    def antibiotico(self,antibiotico):
        self._antibiotico.append(antibiotico)


    @property
    def producto_control(self):
        return self._producto_control
    

    @producto_control.setter
    def producto_control(self, producto_control):
        self._producto_control.append(producto_control)


    def asociar_producto_control(self, producto_control):
        self.producto_control = producto_control


    def asociar_antibiotico(self, antibiotico):
        self.antibiotico = antibiotico


    def realizar_venta(self, producto_control = None, antibiotico = None):
        if producto_control != None:
            self.asociar_producto_control(producto_control)
        if antibiotico != None:
            self.asociar_antibiotico(antibiotico)
