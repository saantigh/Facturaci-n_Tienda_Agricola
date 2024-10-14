from CLASE_productos_de_control import ProductoControl

class ControlPlagas(ProductoControl):
    def __init__(self, nombre_producto: str, registro_ica: str, frecuencia_aplicacion: int, precio: float, periodo_carencia: int):
        super().__init__(nombre_producto, registro_ica, frecuencia_aplicacion, precio)
        self._periodo_carencia = periodo_carencia

    # Propiedad para periodo de carencia
    @property
    def periodo_carencia(self):
        return self._periodo_carencia

    @periodo_carencia.setter
    def periodo_carencia(self, periodo_carencia):
        if periodo_carencia > 0:
            self._periodo_carencia = periodo_carencia
        else:
            raise ValueError("El periodo de carencia debe ser un valor positivo.")
