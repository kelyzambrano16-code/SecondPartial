# Integrantes:
# - HERNANDEZ AMADA
# - SOLIS BRIGGITTE
# - CARRERA EDUARDO
# - ZAMBRANO KELY

class Cliente:
    """
    Representa un usuario de la biblioteca.
    """

    def __init__(self, id_cliente: str, nombre: str, es_socio: str):
        self._id_cliente = str(id_cliente)
        self._nombre = nombre.strip() if isinstance(nombre, str) else str(nombre)
        self.es_socio = es_socio

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, valor):
        valor_str = str(valor) if not isinstance(valor, str) else valor
        if not valor_str.strip():
            raise ValueError("La cédula no puede estar vacía")
        self._id_cliente = valor_str.strip()

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, v):
        if not isinstance(v, str) or not v.strip():
            raise ValueError("nombre no válido")
        self._nombre = v.strip()

    @property
    def es_socio(self):
        return self._es_socio

    @es_socio.setter
    def es_socio(self, nuevo_socio: str):
        if not isinstance(nuevo_socio, str):
            nuevo_socio = str(nuevo_socio)
        nuevo_socio = nuevo_socio.strip().upper()
        valores_validos = ["SELECCIONAR", "SI", "NO"]
        if nuevo_socio not in valores_validos:
            raise ValueError(f"es_socio debe ser uno de: {valores_validos}")
        self._es_socio = nuevo_socio

    def aplicar_descuento(self, monto: float) -> float:
        """
        Los socios tienen 20% de descuento sobre el costo del servicio.
        """
        if not isinstance(monto, (int, float)) or monto < 0:
            raise ValueError("monto no válido")
        if self.es_socio == "SI":
            return round(monto * 0.8, 2)
        return round(monto, 2)

    def __str__(self):
        return f"Cliente(id={self.id_cliente}, nombre='{self.nombre}', socio={self.es_socio})"


# Prueba
socio = Cliente(id_cliente=123, nombre="Leo", es_socio="SI")
print(socio.es_socio)
