import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))


from CRUD.crud import CRUD
from CRUD.CRUDAntibiotico import CRUDAntibiotico
from CRUD.CRUDCliente import CRUDCLiente
from CRUD.CRUDFertilizante import CRUDFertilizantes
from CRUD.CRUDPlagas import CRUDPlagas
from CRUD.CRUDFacturas import CRUDFacturas

plagas_stock = CRUDPlagas.create()
fertilizantes_stock = CRUDFertilizantes.create()
factura = 
