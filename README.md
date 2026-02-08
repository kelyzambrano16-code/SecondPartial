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

LINK DE VIDEO CON EXPLICACION DE PROYECTO Y EJECUCION DEL MISMO 
https://drive.google.com/file/d/1cA9UjmN-bwylysDZ2A32rPPePd82IT94/view?usp=sharing

👥 Integrantes
- HERNANDEZ AMADA
- SOLIS BRIGGITTE
- CARRERA EDUARDO
- ZAMBRANO KELY

-EVIDENCIA
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/459ed4fc-4226-4849-bcb0-223665722918" />


- FUNCION READ
- <img width="1365" height="762" alt="image" src="https://github.com/user-attachments/assets/5457b879-633d-4fac-ac83-312bced1ab02" />
<img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/ca8abd00-aff8-484b-bfa0-4342f61dd6d9" />

  FUNCION INSERT
  <img width="1363" height="767" alt="image" src="https://github.com/user-attachments/assets/cbc894f1-e4bb-4ab0-9036-ed803a2e702d" />
  <img width="1365" height="762" alt="image" src="https://github.com/user-attachments/assets/eba07801-2aba-4349-aebb-7a3b1ce59c8e" />
  <img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/82605a6c-a6ed-41e4-8489-d096186bf4e2" />

- FUNCION UPDATE
   <img width="1365" height="764" alt="image" src="https://github.com/user-attachments/assets/0223e5d6-4bcc-4805-b885-68a0eabb4d9d" />
   <img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/db422168-14ba-4589-bb3a-c91120199233" />
   
- FUNCION DELETE
  <img width="1363" height="767" alt="image" src="https://github.com/user-attachments/assets/35c39e11-a0c9-4aa4-a96c-9aed7d09bc56" />
  <img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/22f3ebc0-fa88-4d20-9a21-746ce5975a3b" />
  <img width="1354" height="767" alt="image" src="https://github.com/user-attachments/assets/403cc2e2-cee9-443b-b4ea-707742958699" />
  <img width="1365" height="767" alt="image" src="https://github.com/user-attachments/assets/f4dc327b-7c81-4870-8d22-aba75aa2089c" />
- 



- 




