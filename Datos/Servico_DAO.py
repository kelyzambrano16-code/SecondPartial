from Datos.conexion import Conexion
from Dominio.cliente import Cliente
from Dominio.libro import Libro
import pyodbc as bd


class ServicioDAO:
    # Consultas SQL
    _INSERT = ("INSERT INTO Servicio (IDServicio, PrecioServicio, DescServicio, IDUsuario, Socio, Titulo, Autor) "
               "VALUES (?, ?, ?, ?, ?, ?, ?)")

    _UPDATE = ("UPDATE Servicio SET PrecioServicio=?, DescServicio=?, IDUsuario=?, Socio=?, Titulo=?, Autor=? "
               "WHERE IDServicio=?")

    _DELETE = "DELETE FROM Servicio WHERE IDServicio=?"

    _SELECT = "SELECT * FROM Servicio WHERE IDServicio=?"

    @classmethod
    def existe_id(cls, id_servicio):
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute("SELECT COUNT(*) FROM Servicio WHERE IDServicio=?", (id_servicio,))
                resultado = cursor.fetchone()
                return resultado[0] > 0
        except Exception as e:
            print(f"Error al validar existencia de ID: {e}")
            return False

    @classmethod
    def insertar_servicio(cls, servicio):
        try:
            if cls.existe_id(servicio.id_servicio):
                return {'ejecuto': False, 'mensaje': 'El ID de Servicio ya existe.'}

            try:
                with Conexion.obtenerCursor() as cursor:
                    datos = (
                        servicio.id_servicio,
                        servicio.precio,
                        servicio.descripcion,
                        servicio.cliente.id_cliente,
                        servicio.cliente.es_socio,
                        servicio.libro.titulo,
                        servicio.libro.autor
                    )
                    cursor.execute(cls._INSERT, datos)
                    Conexion.obtenerConexion().commit()
                    respuesta = cursor.rowcount
                    if respuesta == 1:
                        return {'ejecuto': True, 'mensaje': 'Se guardó con éxito.'}
                    else:
                        return {'ejecuto': False, 'mensaje': 'No se pudo guardar el servicio.'}
            except bd.IntegrityError as e_bb:
                print(f"Error en el servicio: {e_bb}")
                if 'IDServicio' in str(e_bb):
                    return {'ejecuto': False, 'mensaje': 'ID de Servicio ya existe.'}
                elif 'IDUsuario' in str(e_bb):
                    return {'ejecuto': False, 'mensaje': 'ID de Usuario no válido.'}
                else:
                    return {'ejecuto': False, 'mensaje': 'Error de integridad en la base de datos.'}
        except Exception as e:
            print(f"Error General: {e}")
            print(type(e))
            return {'ejecuto': False, 'mensaje': 'Error al guardar los datos, comunicarse con Sistemas.'}

    @classmethod
    def actualizar_servicio(cls, servicio):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (
                    servicio.precio,
                    servicio.descripcion,
                    servicio.cliente.id_cliente,
                    servicio.cliente.es_socio,
                    servicio.libro.titulo,
                    servicio.libro.autor,
                    servicio.id_servicio
                )
                cursor.execute(cls._UPDATE, datos)
                Conexion.obtenerConexion().commit()

                if cursor.rowcount > 0:
                    return {'ejecuto': True, 'mensaje': 'Servicio actualizado con éxito.'}
                else:
                    return {'ejecuto': False, 'mensaje': 'No se encontró el servicio para actualizar.'}
        except Exception as e:
            print(f"Error al actualizar: {e}")
            return {'ejecuto': False, 'mensaje': 'Error al actualizar los datos.'}

    @classmethod
    def eliminar_servicio(cls, id_servicio):
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._DELETE, (id_servicio,))
                Conexion.obtenerConexion().commit()

                if cursor.rowcount > 0:
                    return {'ejecuto': True, 'mensaje': 'Servicio eliminado correctamente.'}
                else:
                    return {'ejecuto': False, 'mensaje': 'El ID de servicio no existe.'}
        except Exception as e:
            print(f"Error al eliminar: {e}")
            return {'ejecuto': False, 'mensaje': 'Error al intentar eliminar el servicio.'}

    @classmethod
    def seleccionar_servicio(cls, id_servicio):
        try:
            with Conexion.obtenerCursor() as cursor:
                cursor.execute(cls._SELECT, (id_servicio,))
                registro = cursor.fetchone()

                if registro:
                    cliente = Cliente(
                        id_cliente=registro[3],
                        nombre="",
                        es_socio=registro[4]
                    )

                    libro = Libro(
                        titulo=registro[5],
                        autor=registro[6],
                        isbn="",
                        disponible=True
                    )

                    return {
                        'id_servicio': registro[0],
                        'precio': registro[1],
                        'descripcion': registro[2],
                        'cliente': cliente,
                        'libro': libro
                    }
                return None
        except Exception as e:
            print(f"Error al seleccionar: {e}")
            return None