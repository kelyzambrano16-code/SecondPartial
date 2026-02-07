-- Script de creación de base de datos (db.sql)

-- 1. Tabla para la clase Libro (Entidad Principal)
CREATE TABLE LIBRO (
    ID_LIBRO NUMBER PRIMARY KEY,
    TITULO VARCHAR2(100) NOT NULL,
    AUTOR VARCHAR2(100),
    EDITORIAL VARCHAR2(100),
    ANIO_PUBLICACION NUMBER(4),
    ESTADO VARCHAR2(20) -- Ejemplo: Disponible, Prestado
);

-- 2. Tabla para la clase Cliente
CREATE TABLE CLIENTE (
    ID_CLIENTE NUMBER PRIMARY KEY,
    CEDULA VARCHAR2(10) UNIQUE NOT NULL,
    NOMBRE VARCHAR2(100) NOT NULL,
    APELLIDO VARCHAR2(100) NOT NULL,
    TELEFONO VARCHAR2(15),
    CORREO VARCHAR2(100)
);

-- Registros de prueba iniciales
INSERT INTO LIBRO (ID_LIBRO, TITULO, AUTOR, EDITORIAL, ANIO_PUBLICACION, ESTADO) 
VALUES (1, 'Cien años de soledad', 'Gabriel García Márquez', 'Editorial Sudamericana', 1967, 'Disponible');

COMMIT;