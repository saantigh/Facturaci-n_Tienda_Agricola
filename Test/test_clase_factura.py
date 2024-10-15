import unittest
from Modelo.clase_factura import Factura as factura
from Modelo.clase_antibioticos import Antibiotico
from Modelo.producto_fertilizante import ControlFertilizantes
from Modelo.producto_plagas import ControlPlagas


class TestFactura(unittest.TestCase):

    def setUp(self):
        """Inicializa los productos y una factura para las pruebas."""
        self.pc_plagas = ControlPlagas("Plaga X", "ICA124", "8", "20000", 20)
        self.pc_fertilizante = ControlFertilizantes("UREA", "ICA7028", "15", "60000", 15)
        self.ant_1 = Antibiotico("anti_1", "10ml", "bovino", 120000, 10)
        self.ant_2 = Antibiotico("anti_2", "8ml", "caprino", 100000, 8)
        self.factura = factura()

    

if __name__ == "__main__":
    unittest.main()


