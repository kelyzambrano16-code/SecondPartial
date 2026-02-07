# Integrantes:
# - HERNANDEZ AMADA
# - SOLIS BRIGGITTE
# - CARRERA EDUARDO
# - ZAMBRANO KELY

from PySide6.QtWidgets import QMainWindow, QMessageBox
from UI.vtnPrincipal import Ui_interfazui
from Datos.Servico_DAO import ServicioDAO
from Dominio.cliente import Cliente
from Dominio.libro import Libro


class ServicioServicio(QMainWindow):
    '''
    Clase que genera la lógica de los objetos servicio
    '''

    def __init__(self):
        super(ServicioServicio, self).__init__()
        self.ui = Ui_interfazui()
        self.ui.setupUi(self)

        # Conexión de botones
        self.ui.btnGuardar.clicked.connect(self.guardar)
        self.ui.btnLimpiar.clicked.connect(self.limpiar)
        self.ui.btnBuscar.clicked.connect(self.buscar)
        self.ui.btnCrear.clicked.connect(self.insertar)
        self.ui.btnActualizar.clicked.connect(self.actualizar)
        self.ui.btnEliminar.clicked.connect(self.eliminar)

    def validar_campos(self):
        if not self.ui.TxTConsulta.text().strip():
            QMessageBox.warning(self, "Validación", "El ID del Servicio es obligatorio")
            return False
        if not self.ui.TxTPrecio.text().strip():
            QMessageBox.warning(self, "Validación", "El Precio es obligatorio")
            return False
        if not self.ui.TxTDescripcion.text().strip():
            QMessageBox.warning(self, "Validación", "La Descripción es obligatoria")
            return False
        if not self.ui.TxTCodUsuario.text().strip():
            QMessageBox.warning(self, "Validación", "El ID de Usuario es obligatorio")
            return False
        if self.ui.comboBox.currentText() == "SELECCIONAR":
            QMessageBox.warning(self, "Validación", "Debe seleccionar si es Socio o no")
            return False
        if not self.ui.TxTTitulo.text().strip():
            QMessageBox.warning(self, "Validación", "El Título del Libro es obligatorio")
            return False
        if not self.ui.TxTAutor.text().strip():
            QMessageBox.warning(self, "Validación", "El Autor del Libro es obligatorio")
            return False
        try:
            float(self.ui.TxTPrecio.text().strip())
        except ValueError:
            QMessageBox.warning(self, "Validación", "El Precio debe ser un número válido")
            return False
        return True

    def crear_servicio_desde_formulario(self):
        try:
            # Crear objeto Cliente
            cliente = Cliente(
                id_cliente=self.ui.TxTCodUsuario.text().strip(),
                nombre="",  # No lo tenemos en el formulario
                es_socio=self.ui.comboBox.currentText()
            )
            libro = Libro(
                titulo=self.ui.TxTTitulo.text().strip(),
                autor=self.ui.TxTAutor.text().strip(),
                isbn="",  # No lo tenemos en el formulario
                disponible=True
            )
            servicio_data = {
                'id_servicio': self.ui.TxTConsulta.text().strip(),
                'precio': float(self.ui.TxTPrecio.text().strip()),
                'descripcion': self.ui.TxTDescripcion.text().strip(),
                'cliente': cliente,
                'libro': libro
            }

            return servicio_data
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al crear servicio: {str(e)}")
            return None

    def guardar(self):
        """Guarda un nuevo servicio en la base de datos"""
        if not self.validar_campos():
            return

        self.insertar()

    def limpiar(self):
        """Limpia todos los campos del formulario"""
        self.ui.TxTConsulta.clear()
        self.ui.TxTPrecio.clear()
        self.ui.TxTDescripcion.clear()
        self.ui.TxTCodUsuario.clear()
        self.ui.comboBox.setCurrentIndex(0)
        self.ui.TxTTitulo.clear()
        self.ui.TxTAutor.clear()
        self.ui.TxTConsulta.setFocus()

    def buscar(self):
        """Busca un servicio por su ID"""
        id_servicio = self.ui.TxTConsulta.text().strip()
        if not id_servicio:
            QMessageBox.warning(self, "Validación", "Ingrese un ID de Servicio para buscar")
            return
        try:
            resultado = ServicioDAO.seleccionar_servicio(id_servicio)
            if resultado:
                # Llenar los campos con los datos encontrados
                self.ui.TxTPrecio.setText(str(resultado['precio']))
                self.ui.TxTDescripcion.setText(resultado['descripcion'])
                self.ui.TxTCodUsuario.setText(resultado['cliente'].id_cliente)
                index = self.ui.comboBox.findText(resultado['cliente'].es_socio)
                if index >= 0:
                    self.ui.comboBox.setCurrentIndex(index)
                self.ui.TxTTitulo.setText(resultado['libro'].titulo)
                self.ui.TxTAutor.setText(resultado['libro'].autor)
                QMessageBox.information(self, "Búsqueda", "Servicio encontrado")
            else:
                QMessageBox.warning(self, "Búsqueda", "No se encontró ningún servicio con ese ID")
                self.limpiar()
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al buscar: {str(e)}")

    def insertar(self):
        if not self.validar_campos():
            return
        try:
            servicio_data = self.crear_servicio_desde_formulario()
            if not servicio_data:
                return
            class ServicioTemp:
                def __init__(self, data):
                    self.id_servicio = data['id_servicio']
                    self.precio = data['precio']
                    self.descripcion = data['descripcion']
                    self.cliente = data['cliente']
                    self.libro = data['libro']
            servicio = ServicioTemp(servicio_data)
            resultado = ServicioDAO.insertar_servicio(servicio)

            if resultado['ejecuto']:
                QMessageBox.information(self, "Éxito", resultado['mensaje'])
                self.limpiar()
            else:
                QMessageBox.warning(self, "Advertencia", resultado['mensaje'])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al insertar: {str(e)}")

    def actualizar(self):
        """Actualiza un servicio existente"""
        if not self.validar_campos():
            return
        try:
            servicio_data = self.crear_servicio_desde_formulario()
            if not servicio_data:
                return
            class ServicioTemp:
                def __init__(self, data):
                    self.id_servicio = data['id_servicio']
                    self.precio = data['precio']
                    self.descripcion = data['descripcion']
                    self.cliente = data['cliente']
                    self.libro = data['libro']
            servicio = ServicioTemp(servicio_data)
            resultado = ServicioDAO.actualizar_servicio(servicio)

            if resultado['ejecuto']:
                QMessageBox.information(self, "Éxito", resultado['mensaje'])
                self.limpiar()
            else:
                QMessageBox.warning(self, "Advertencia", resultado['mensaje'])
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error al actualizar: {str(e)}")

    def eliminar(self):
        id_servicio = self.ui.TxTConsulta.text().strip()

        if not id_servicio:
            QMessageBox.warning(self, "Validación", "Debe ingresar un ID de Servicio para eliminar")
            return
        respuesta = QMessageBox.question(
            self,
            "Confirmar Eliminación",
            f"¿Está seguro de eliminar el servicio con ID '{id_servicio}'?",
            QMessageBox.Yes | QMessageBox.No
        )
        if respuesta == QMessageBox.Yes:
            try:
                resultado = ServicioDAO.eliminar_servicio(id_servicio)

                if resultado['ejecuto']:
                    QMessageBox.information(self, "Éxito", resultado['mensaje'])
                    self.limpiar()
                else:
                    QMessageBox.warning(self, "Advertencia", resultado['mensaje'])
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Error al eliminar: {str(e)}")