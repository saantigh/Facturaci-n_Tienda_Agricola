class ProductoControl:
    def __init__(self, nombre_producto: str, registro_ica: str, frecuencia_aplicacion: int, precio_producto: float):
        self._nombre_producto = nombre_producto
        self._registro_ica = registro_ica
        self._frecuencia_aplicacion = frecuencia_aplicacion  # En días
        self._precio_producto = precio_producto

    # Propiedad para nombre del producto
    @property
    def nombre_producto(self):
        return self._nombre_producto

    @nombre_producto.setter
    def nombre_producto(self, nombre_producto):
        if not nombre_producto.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        if not all(char.isalpha() or char.isspace() for char in nombre_producto):
            raise ValueError("El nombre del producto solo puede contener letras y espacios.")
        self._nombre_producto = nombre_producto

    # Propiedad para registro ICA
    @property
    def registro_ica(self):
        return self._registro_ica

    @registro_ica.setter
    def registro_ica(self, registro_ica):
        if len(registro_ica.strip()) > 0:
            self._registro_ica = registro_ica
        else:
            raise ValueError("El registro ICA no puede estar vacío.")

    # Propiedad para frecuencia de aplicación
    @property
    def frecuencia_aplicacion(self):
        return self._frecuencia_aplicacion

    @frecuencia_aplicacion.setter
    def frecuencia_aplicacion(self, frecuencia_aplicacion):
        if frecuencia_aplicacion > 0:
            self._frecuencia_aplicacion = frecuencia_aplicacion
        else:
            raise ValueError("La frecuencia de aplicación debe ser un valor positivo en días.")

    # Propiedad para precio
    @property
    def precio(self):
        return self._precio_producto

    @precio.setter
    def precio(self, precio):
        if precio > 0:
            self._precio_producto = precio
        else:
            raise ValueError("El precio debe ser un valor positivo.")


