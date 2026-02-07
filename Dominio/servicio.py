# Integrantes:
# - HERNANDEZ AMADA
# - SOLIS BRIGGITTE
# - CARRERA EDUARDO
# - ZAMBRANO KELY

from abc import ABC, abstractmethod
from Dominio.cliente import Cliente
from Dominio.libro import Libro


class Servicio(ABC):
    """
    Superclase abstracta para servicios de la biblioteca.
    Usa composición con Cliente y Libro.
    """

    def __init__(self, id_servicio: str, precio: float, descripcion: str,
                 cliente: Cliente, libro: Libro):
        self._id_servicio = id_servicio
        self._precio = precio
        self._descripcion = descripcion
        self._cliente = cliente
        self._libro = libro

    @property
    def id_servicio(self):
        return self._id_servicio
    @id_servicio.setter
    def id_servicio(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("id_servicio debe ser string no vacío")
        self._id_servicio = value.strip()

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("precio debe ser número >= 0")
        self._precio = float(value)

    @property
    def descripcion(self):
        return self._descripcion
    @descripcion.setter
    def descripcion(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("descripcion No debe estar vacío")
        self._descripcion = value.strip()

    @property
    def cliente(self):
        return self._cliente
    @cliente.setter
    def cliente(self, value):
        if not isinstance(value, Cliente):
            raise ValueError("Error Debe ser un Cliente")
        self._cliente = value

    @property
    def libro(self):
        return self._libro
    @libro.setter
    def libro(self, value):
        if not isinstance(value, Libro):
            raise ValueError("libro debe ser una instancia de Libro")
        self._libro = value

    @abstractmethod
    def calcular_costo(self):
        """Método abstracto para calcular el costo del servicio."""
        pass

    def calcular_costo_con_descuento(self):
        """Calcula el costo aplicando descuento si el cliente es socio."""
        costo_base = self.calcular_costo()
        return self.cliente.aplicar_descuento(costo_base)

    def mostrar_info(self):
        return (f"Servicio(id={self.id_servicio}, "
                f"descripcion='{self.descripcion}', "
                f"precio_base={self.precio}, "
                f"cliente={self.cliente.nombre}, "
                f"libro='{self.libro.titulo}')")

    def __str__(self):
        return self.mostrar_info()