# Integrantes:
# - HERNANDEZ AMADA
# - SOLIS BRIGGITTE
# - CARRERA EDUARDO
# - ZAMBRANO KELY
import sys

from Servicio.servicio import ServicioServicio

from PySide6.QtWidgets import QApplication

app = QApplication()
vtn_principal = ServicioServicio()
vtn_principal.show()
sys.exit(app.exec())