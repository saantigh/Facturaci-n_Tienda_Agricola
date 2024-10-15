import unittest
from Modelo.clase_factura import Factura as factura
from Modelo.clase_antibioticos import Antibiotico as antibiotico
from Modelo.producto_fertilizante import ControlFertilizantes as producto_fertilizante
from Modelo.producto_plagas import ControlPlagas as producto_plaga
from Modelo.clase_cliente import Cliente as cliente
from Modelo.CLASE_productos_de_control import ProductoControl as pc


class TestCliente(unittest.TestCase):
    def setup(self):
        self.factura_1 = factura.Factura()
        self.factura_2 = factura.Factura()

        self.c = cliente.Cliente("santiago gonzales","10243580")
        self.ant_1 = antibiotico.Antibiotico("anti_1", "10ml", "bovino", "120000")
        self.ant_2 = antibiotico.Antibiotico("anti_2", "8ml", "caprino", "100000")
        self.pc_plaga = producto_plaga.ControlPlagas("Plaga X", "ICA124", "8", "20000")
        self.pc_fertilizante = producto_fertilizante.ControlFertilizantes("UREA", "ICA7028", "15", "60000")

    def test_cliente_tiene_varias_facturas_asociadas(self):
        self.factura_1.asociar_antibiotico(self.ant_1)
        self.factura_1.asociar_antibiotico(self.ant_2)
        self.factura_1.asociar_producto_control(self.pc_plaga)
        self.factura_1.asociar_producto_control(self.pc_fertilizante)

        self.factura_2.asociar_antibiotico(self.ant_1)
        self.factura_2.asociar_antibiotico(self.ant_2)
        self.factura_2.asociar_producto_control(self.pc_plaga)
        self.factura_2.asociar_producto_control(self.pc_fertilizante)

        self.c.asociar_factura(self.factura_1)
        self.c.asociar_factura(self.factura_2)

        self.assertEqual(2, len(self.c.factura), "Cliente no tiene facturas asociadas")

if __name__ == "__main__":  
    unittest.main()
