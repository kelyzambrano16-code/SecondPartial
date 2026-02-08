USE [master]
GO
/* For security reasons the login is created disabled and with a random password. */
/****** Object:  Login [##MS_PolicyEventProcessingLogin##]    Script Date: 8/2/2026 11:11:01 ******/
CREATE LOGIN [##MS_PolicyEventProcessingLogin##] WITH PASSWORD=N'vxissK8GeeUZptcN/6CrodUKZYuf+ERUVs4v8NNofVg=', DEFAULT_DATABASE=[master], DEFAULT_LANGUAGE=[us_english], CHECK_EXPIRATION=OFF, CHECK_POLICY=ON
GO
ALTER LOGIN [##MS_PolicyEventProcessingLogin##] DISABLE
GO
/* For security reasons the login is created disabled and with a random password. */
/****** Object:  Login [##MS_PolicyTsqlExecutionLogin##]    Script Date: 8/2/2026 11:11:01 ******/
CREATE LOGIN [##MS_PolicyTsqlExecutionLogin##] WITH PASSWORD=N'mWzF1ITlDaRg4XyLRisvv8Yy5E0ggOGD0s6fqvFnzds=', DEFAULT_DATABASE=[master], DEFAULT_LANGUAGE=[us_english], CHECK_EXPIRATION=OFF, CHECK_POLICY=ON
GO
ALTER LOGIN [##MS_PolicyTsqlExecutionLogin##] DISABLE
GO
/****** Object:  Login [DESKTOP-0SEUBDP\SOPORTE TH]    Script Date: 8/2/2026 11:11:01 ******/
CREATE LOGIN [DESKTOP-0SEUBDP\SOPORTE TH] FROM WINDOWS WITH DEFAULT_DATABASE=[master], DEFAULT_LANGUAGE=[us_english]
GO
/****** Object:  Login [NT AUTHORITY\SYSTEM]    Script Date: 8/2/2026 11:11:01 ******/
CREATE LOGIN [NT AUTHORITY\SYSTEM] FROM WINDOWS WITH DEFAULT_DATABASE=[master], DEFAULT_LANGUAGE=[us_english]
GO
/****** Object:  Login [NT Service\MSSQL$SQLZAMBRANOK]    Script Date: 8/2/2026 11:11:01 ******/
CREATE LOGIN [NT Service\MSSQL$SQLZAMBRANOK] FROM WINDOWS WITH DEFAULT_DATABASE=[master], DEFAULT_LANGUAGE=[us_english]
GO
/****** Object:  Login [NT SERVICE\SQLAgent$SQLZAMBRANOK]    Script Date: 8/2/2026 11:11:01 ******/
CREATE LOGIN [NT SERVICE\SQLAgent$SQLZAMBRANOK] FROM WINDOWS WITH DEFAULT_DATABASE=[master], DEFAULT_LANGUAGE=[us_english]
GO
/****** Object:  Login [NT SERVICE\SQLTELEMETRY$SQLZAMBRANOK]    Script Date: 8/2/2026 11:11:01 ******/
CREATE LOGIN [NT SERVICE\SQLTELEMETRY$SQLZAMBRANOK] FROM WINDOWS WITH DEFAULT_DATABASE=[master], DEFAULT_LANGUAGE=[us_english]
GO
/****** Object:  Login [NT SERVICE\SQLWriter]    Script Date: 8/2/2026 11:11:01 ******/
CREATE LOGIN [NT SERVICE\SQLWriter] FROM WINDOWS WITH DEFAULT_DATABASE=[master], DEFAULT_LANGUAGE=[us_english]
GO
/****** Object:  Login [NT SERVICE\Winmgmt]    Script Date: 8/2/2026 11:11:01 ******/
CREATE LOGIN [NT SERVICE\Winmgmt] FROM WINDOWS WITH DEFAULT_DATABASE=[master], DEFAULT_LANGUAGE=[us_english]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [DESKTOP-0SEUBDP\SOPORTE TH]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [NT Service\MSSQL$SQLZAMBRANOK]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [NT SERVICE\SQLAgent$SQLZAMBRANOK]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [NT SERVICE\SQLWriter]
GO
ALTER SERVER ROLE [sysadmin] ADD MEMBER [NT SERVICE\Winmgmt]
GO
USE [Servicio]
GO
-- _SERVIDOR = r'DESKTOP-0SEUBDP\SQLZAMBRANOK'
--    _BBDD = 'Servicio'
--    _USUARIO = 'SA'
--    _PASSWORD = 'sa'
/****** Object:  Table [dbo].[Servicio]    Script Date: 8/2/2026 11:11:01 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Servicio](
	[IDServicio] [varchar](3) NOT NULL,
	[PrecioServicio] [decimal](4, 2) NOT NULL,
	[DescServicio] [varchar](15) NOT NULL,
	[IDUsuario] [varchar](10) NOT NULL,
	[Socio] [varchar](11) NOT NULL,
	[Titulo] [varchar](60) NOT NULL,
	[Autor] [varchar](60) NOT NULL,
 CONSTRAINT [PK__Servicio__3CCE7416D1300880] PRIMARY KEY CLUSTERED 
(
	[IDServicio] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
INSERT [dbo].[Servicio] ([IDServicio], [PrecioServicio], [DescServicio], [IDUsuario], [Socio], [Titulo], [Autor]) VALUES (N'001', CAST(2.75 AS Decimal(4, 2)), N'Préstamo', N'0986327867', N'SI', N'Cien Años de Seriedad', N'Serio Benedetti')
GO
INSERT [dbo].[Servicio] ([IDServicio], [PrecioServicio], [DescServicio], [IDUsuario], [Socio], [Titulo], [Autor]) VALUES (N'022', CAST(2.90 AS Decimal(4, 2)), N'Préstamo', N'0987654321', N'NO', N'Don Quitoje de la Seriedad', N'Miguel de Seriedad')
GO
INSERT [dbo].[Servicio] ([IDServicio], [PrecioServicio], [DescServicio], [IDUsuario], [Socio], [Titulo], [Autor]) VALUES (N'023', CAST(2.75 AS Decimal(4, 2)), N'Préstamo', N'0986327867', N'SI', N'Cien Años de Seriedad', N'Serio Benedetti')
GO
INSERT [dbo].[Servicio] ([IDServicio], [PrecioServicio], [DescServicio], [IDUsuario], [Socio], [Titulo], [Autor]) VALUES (N'024', CAST(1.75 AS Decimal(4, 2)), N'Venta', N'0950171587', N'NO', N'La Odisea', N'Homero')
GO
INSERT [dbo].[Servicio] ([IDServicio], [PrecioServicio], [DescServicio], [IDUsuario], [Socio], [Titulo], [Autor]) VALUES (N'200', CAST(11.00 AS Decimal(4, 2)), N'Reposición', N'0987676375', N'SI', N'La Odisea', N'Homero')
GO
INSERT [dbo].[Servicio] ([IDServicio], [PrecioServicio], [DescServicio], [IDUsuario], [Socio], [Titulo], [Autor]) VALUES (N'222', CAST(50.00 AS Decimal(4, 2)), N'Venta', N'1454223423', N'SI', N'Caperucita la Seria', N'Serio Desconocido')
GO
INSERT [dbo].[Servicio] ([IDServicio], [PrecioServicio], [DescServicio], [IDUsuario], [Socio], [Titulo], [Autor]) VALUES (N'555', CAST(3.11 AS Decimal(4, 2)), N'Préstamo', N'0956774829', N'SI', N'Harry Potter y la Seriedad', N'J.K Seriedad')
GO
