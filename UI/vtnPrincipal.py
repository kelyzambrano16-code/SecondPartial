# Integrantes:
# - HERNANDEZ AMADA
# - SOLIS BRIGGITTE
# - CARRERA EDUARDO
# - ZAMBRANO KELY

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_interfazui(object):
    def setupUi(self, interfazui):
        if not interfazui.objectName():
            interfazui.setObjectName(u"interfazui")
        interfazui.resize(502, 360)
        self.lblConsulta = QLabel(interfazui)
        self.lblConsulta.setObjectName(u"lblConsulta")
        self.lblConsulta.setGeometry(QRect(40, 40, 91, 16))
        self.TxTConsulta = QLineEdit(interfazui)
        self.TxTConsulta.setObjectName(u"TxTConsulta")
        self.TxTConsulta.setGeometry(QRect(170, 40, 121, 20))
        self.TxTConsulta.setMaxLength(3)
        self.btnBuscar = QPushButton(interfazui)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setGeometry(QRect(340, 40, 101, 23))
        self.btnCrear = QPushButton(interfazui)
        self.btnCrear.setObjectName(u"btnCrear")
        self.btnCrear.setGeometry(QRect(340, 80, 101, 23))
        self.btnActualizar = QPushButton(interfazui)
        self.btnActualizar.setObjectName(u"btnActualizar")
        self.btnActualizar.setGeometry(QRect(340, 120, 101, 23))
        self.btnEliminar = QPushButton(interfazui)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setGeometry(QRect(340, 160, 101, 23))
        self.btnGuardar = QPushButton(interfazui)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(340, 240, 101, 23))
        self.btnLimpiar = QPushButton(interfazui)
        self.btnLimpiar.setObjectName(u"btnLimpiar")
        self.btnLimpiar.setGeometry(QRect(340, 280, 101, 23))
        self.lblPrecio = QLabel(interfazui)
        self.lblPrecio.setObjectName(u"lblPrecio")
        self.lblPrecio.setGeometry(QRect(50, 80, 81, 21))
        self.TxTPrecio = QLineEdit(interfazui)
        self.TxTPrecio.setObjectName(u"TxTPrecio")
        self.TxTPrecio.setGeometry(QRect(170, 80, 121, 20))
        self.TxTPrecio.setMaxLength(4)
        self.lblDescripcion = QLabel(interfazui)
        self.lblDescripcion.setObjectName(u"lblDescripcion")
        self.lblDescripcion.setGeometry(QRect(30, 120, 111, 20))
        self.TxTDescripcion = QLineEdit(interfazui)
        self.TxTDescripcion.setObjectName(u"TxTDescripcion")
        self.TxTDescripcion.setGeometry(QRect(170, 120, 121, 20))
        self.TxTDescripcion.setMaxLength(15)
        self.lblCodUsuario = QLabel(interfazui)
        self.lblCodUsuario.setObjectName(u"lblCodUsuario")
        self.lblCodUsuario.setGeometry(QRect(70, 160, 61, 16))
        self.TxTCodUsuario = QLineEdit(interfazui)
        self.TxTCodUsuario.setObjectName(u"TxTCodUsuario")
        self.TxTCodUsuario.setGeometry(QRect(170, 160, 121, 20))
        self.TxTCodUsuario.setMaxLength(10)
        self.lblSocio = QLabel(interfazui)
        self.lblSocio.setObjectName(u"lblSocio")
        self.lblSocio.setGeometry(QRect(90, 200, 47, 20))
        self.lblTitulo = QLabel(interfazui)
        self.lblTitulo.setObjectName(u"lblTitulo")
        self.lblTitulo.setGeometry(QRect(50, 240, 91, 20))
        self.TxTTitulo = QLineEdit(interfazui)
        self.TxTTitulo.setObjectName(u"TxTTitulo")
        self.TxTTitulo.setGeometry(QRect(170, 240, 121, 20))
        self.TxTTitulo.setMaxLength(60)
        self.lblAutor = QLabel(interfazui)
        self.lblAutor.setObjectName(u"lblAutor")
        self.lblAutor.setGeometry(QRect(50, 280, 91, 20))
        self.TxTAutor = QLineEdit(interfazui)
        self.TxTAutor.setObjectName(u"TxTAutor")
        self.TxTAutor.setGeometry(QRect(170, 280, 121, 20))
        self.TxTAutor.setMaxLength(60)
        self.comboBox = QComboBox(interfazui)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(170, 200, 121, 22))

        self.retranslateUi(interfazui)

        QMetaObject.connectSlotsByName(interfazui)
    # setupUi

    def retranslateUi(self, interfazui):
        interfazui.setWindowTitle(QCoreApplication.translate("interfazui", u"Sistema de Consulta de Registros Bibliotecarios", None))
        self.lblConsulta.setText(QCoreApplication.translate("interfazui", u"Consulta Servicio", None))
        self.btnBuscar.setText(QCoreApplication.translate("interfazui", u"Buscar", None))
        self.btnCrear.setText(QCoreApplication.translate("interfazui", u"Nuevo Registro", None))
        self.btnActualizar.setText(QCoreApplication.translate("interfazui", u"Actualizar", None))
        self.btnEliminar.setText(QCoreApplication.translate("interfazui", u"Eliminar", None))
        self.btnGuardar.setText(QCoreApplication.translate("interfazui", u"Guardar", None))
        self.btnLimpiar.setText(QCoreApplication.translate("interfazui", u"Limpiar", None))
        self.lblPrecio.setText(QCoreApplication.translate("interfazui", u"Precio Servicio", None))
        self.lblDescripcion.setText(QCoreApplication.translate("interfazui", u"Descripci\u00f3n Servicio", None))
        self.lblCodUsuario.setText(QCoreApplication.translate("interfazui", u"ID Usuario", None))
        self.lblSocio.setText(QCoreApplication.translate("interfazui", u"Socio", None))
        self.lblTitulo.setText(QCoreApplication.translate("interfazui", u"T\u00edtulo del Libro", None))
        self.lblAutor.setText(QCoreApplication.translate("interfazui", u"Autor del Libro", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("interfazui", u"SELECCIONAR", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("interfazui", u"SI", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("interfazui", u"NO", None))

    # retranslateUi

