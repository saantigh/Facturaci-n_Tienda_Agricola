import unittest
from Modelo.clase_factura import Factura as factura
from Modelo.clase_antibioticos import Antibiotico as antibiotico
from Modelo.producto_fertilizante import ControlFertilizantes as producto_fertilizante
from Modelo.producto_plagas import ControlPlagas as producto_plaga
from Modelo.CLASE_productos_de_control import ProductoControl as pc



class TestFactura(unittest.TestCase):

    def setUp(self):
        self.pc_plaga = producto_plaga("Plaga X", "ICA124", "8", "20000")
        self.pc_fertilizante = producto_fertilizante("UREA", "ICA7028", "15", "60000")
        self.fact = factura.Factura()

    def test_vende_varios_producto_control(self):
        self.fact.asociar_producto_control(self.pc_plaga)
        self.fact.asociar_producto_control(self.pc_fertilizante)

        self.assertEqual(2,len(self.fact.producto_control), "No se ha asociado producto control")

    def test_vende_varios_antibioticos(self):
        ant_1 = antibiotico.Antibiotico("anti_1", "10ml", "bovino", "120000")
        ant_2 = antibiotico.Antibiotico("anti_2", "8ml", "caprino", "100000")
        self.fact.asociar_antibiotico(ant_1)
        self.fact.asociar_antibiotico(ant_2)

        self.assertEqual(2,len(self.fact.antibiotico), "No se ha asociado antibiotico")


    def test_vende_varios_producto_control_antibioticos(self):
        ant_1 = antibiotico.Antibiotico("anti_1", "10ml", "bovino", "120000")
        ant_2 = antibiotico.Antibiotico("anti_2", "8ml", "caprino", "100000")
        pc_plaga = producto_plaga.ControlPlagas("Plaga X", "ICA124", "8", "20000")
        pc_fertilizante = producto_fertilizante.ControlFertilizantes("UREA", "ICA7028", "15", "60000")


        self.fact.asociar_producto_control(pc_plaga)
        self.fact.asociar_producto_control(pc_fertilizante)
        self.fact.asociar_antibiotico(ant_1)
        self.fact.asociar_antibiotico(ant_2)

        self.assertEqual(2,len(self.fact.antibiotico), "No se ha asociado antibiotico")
        self.assertEqual(2,len(self.fact.producto_control), "No se ha asociado antibiotico")


if __name__ == "__main__":  
    unittest.main()


