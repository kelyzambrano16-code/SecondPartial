-- Script de creación de base de datos (db.sql)
create database Servicio
go

create table Servicio
(IDServicio varchar(3) primary key,
	PrecioServicio decimal(4, 2),
	DescServicio varchar(15),
	IDUsuario varchar(10),
	Socio varchar(11),
	Titulo varchar(60),
	Autor varchar(60))


-- Registros de prueba iniciales

select * from [dbo].[Servicio]