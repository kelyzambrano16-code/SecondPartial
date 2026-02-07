-Sistema de Gestión de Biblioteca - 2do Parcial POO
Descripción del Proyecto
Este proyecto consiste en una aplicación de escritorio desarrollada en Python para la gestión de libros y clientes de una biblioteca. Es la evolución del sistema del primer parcial, integrando ahora una Interfaz Gráfica de Usuario (UI) desarrollada con Qt Designer y persistencia de datos en una base de datos Oracle.

-Tecnologías Utilizadas
Interfaz Gráfica: PyQt6 (Archivos .ui y .py)
Base de Datos: Oracle Database (utilizando la librería cx_Oracle)

-Arquitectura del Proyecto (Capas)
El proyecto sigue la estructura recomendada para mantener el código organizado y escalable:
Capa de Dominio (cliente.py, libro.py): Contiene las clases base con sus atributos y métodos constructores.
Capa de Datos (conexion.py, Servico_DAO.py): Gestiona la conexión a Oracle y las sentencias SQL (Select, Insert, Update, Delete).
Capa de Servicio (servicio.py): Actúa como intermediario entre la UI y los datos, manejando la lógica de negocio.
Capa de UI (vtnPrincipal.py, interfaz.ui): Controla la ventana principal y los eventos de los botones.
Main (main.py): Punto de entrada que inicializa la aplicación.

-Funcionalidades CRUD Implementadas
El sistema permite realizar las siguientes operaciones sobre la entidad Libro:

Create (Guardar): Permite registrar nuevos libros validando que los campos no estén vacíos.

Read (Buscar): Implementa la búsqueda de libros por su ID para cargar la información en el formulario.

Update (Actualizar): Modifica los datos de un libro ya existente en la base de datos.

Delete (Eliminar): Elimina un registro de la base de datos tras la confirmación del usuario.

Limpiar: Botón para resetear los campos del formulario de manera rápida.

-Requisitos e Instalación
Instalar dependencias:
Bash
pip install PyQt6 cx_Oracle

-Configurar Base de Datos:
Ejecuta el script db.sql (incluido en el repositorio) para crear las tablas necesarias.
Configura tus credenciales en el archivo conexion.py.

👥 Integrantes
- HERNANDEZ AMADA
- SOLIS BRIGGITTE
- CARRERA EDUARDO
- ZAMBRANO KELY

-EVIDENCIA
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/8fe22b47-eb19-4893-8c3c-dd7c2cc1b3d7" />
