-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: TienditasCadena
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `area`
--

DROP TABLE IF EXISTS `area`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `area` (
  `id_area` int NOT NULL AUTO_INCREMENT,
  `nom_area` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id_area`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `area`
--

LOCK TABLES `area` WRITE;
/*!40000 ALTER TABLE `area` DISABLE KEYS */;
INSERT INTO `area` VALUES (1,'Lácteos'),(2,'Bebidas'),(3,'Latas'),(4,'Botanas'),(5,'Dulces'),(6,'Galletas');
/*!40000 ALTER TABLE `area` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ciudad`
--

DROP TABLE IF EXISTS `ciudad`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ciudad` (
  `id_ciu` int NOT NULL AUTO_INCREMENT,
  `nom_ciu` varchar(40) NOT NULL,
  `lada_ciu` int NOT NULL,
  PRIMARY KEY (`id_ciu`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ciudad`
--

LOCK TABLES `ciudad` WRITE;
/*!40000 ALTER TABLE `ciudad` DISABLE KEYS */;
INSERT INTO `ciudad` VALUES (1,'Zitácuaro',715),(2,'Aquila',313),(3,'La Piedad',352),(4,'Sahuayo',353),(5,'Santiago Tangamandapio',383),(6,'Cherán',423),(7,'Pátzcuaro',434),(8,'Zirahuén',434),(9,'Quiroga',454),(10,'Jungapeo',715),(15,'Nuevo San Juan Parangaricutiro',452),(18,'Jaripo',352),(19,'Tepalcatepec ',424),(20,'Yurécuaro',356),(21,'Morelia',443);
/*!40000 ALTER TABLE `ciudad` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `codigo`
--

DROP TABLE IF EXISTS `codigo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `codigo` (
  `cp_cod` int NOT NULL,
  `id_ciu` int NOT NULL,
  PRIMARY KEY (`cp_cod`),
  KEY `id_ciu` (`id_ciu`),
  CONSTRAINT `codigo_ibfk_1` FOREIGN KEY (`id_ciu`) REFERENCES `ciudad` (`id_ciu`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `codigo`
--

LOCK TABLES `codigo` WRITE;
/*!40000 ALTER TABLE `codigo` DISABLE KEYS */;
INSERT INTO `codigo` VALUES (61500,1),(60870,2),(59300,3),(59000,4),(59920,5),(60270,6),(16319,7),(61810,8),(58420,9),(61470,10),(60490,15),(78965,18);
/*!40000 ALTER TABLE `codigo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `colonia`
--

DROP TABLE IF EXISTS `colonia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `colonia` (
  `id_col` int NOT NULL AUTO_INCREMENT,
  `nom_col` varchar(60) NOT NULL,
  `cp_cod` int NOT NULL,
  PRIMARY KEY (`id_col`),
  KEY `cp_cod` (`cp_cod`),
  CONSTRAINT `colonia_ibfk_1` FOREIGN KEY (`cp_cod`) REFERENCES `codigo` (`cp_cod`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `colonia`
--

LOCK TABLES `colonia` WRITE;
/*!40000 ALTER TABLE `colonia` DISABLE KEYS */;
INSERT INTO `colonia` VALUES (1,'La Encarnación',61500),(2,'Rancho Agua Caliente',60870),(3,'Arroyo Delgado',59300),(4,'Alameda',59000),(5,'Camino Real',59920),(6,'Cruciro',60270),(7,'Jacarandas',16319),(8,'Zirahuén',61810),(9,'Kutzaro',58420),(10,'Agua Salada',61470),(11,'Jaripo',78965);
/*!40000 ALTER TABLE `colonia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contrato`
--

DROP TABLE IF EXISTS `contrato`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `contrato` (
  `id_con` int NOT NULL AUTO_INCREMENT,
  `fi_con` datetime NOT NULL,
  `ff_con` datetime NOT NULL,
  `puesto_con` varchar(45) DEFAULT NULL,
  `sueldo` float(8,2) DEFAULT NULL,
  `h1_con` time DEFAULT NULL,
  `hs_con` time DEFAULT NULL,
  `id_tie` int NOT NULL,
  `id_per` int NOT NULL,
  PRIMARY KEY (`id_con`),
  KEY `id_tie` (`id_tie`),
  KEY `id_per` (`id_per`),
  CONSTRAINT `contrato_ibfk_1` FOREIGN KEY (`id_tie`) REFERENCES `tienda` (`id_tie`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `contrato_ibfk_2` FOREIGN KEY (`id_per`) REFERENCES `persona` (`id_per`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contrato`
--

LOCK TABLES `contrato` WRITE;
/*!40000 ALTER TABLE `contrato` DISABLE KEYS */;
INSERT INTO `contrato` VALUES (1,'2018-06-12 00:00:00','2023-06-12 00:00:00','Gerente',8600.00,'08:00:00','18:00:00',1,4),(2,'2020-11-12 00:00:00','2023-11-12 00:00:00','mostrador',4500.00,'08:00:00','16:00:00',6,5),(3,'2022-04-12 00:00:00','2023-04-12 00:00:00','Mostrador',4500.00,'08:00:00','16:00:00',4,6),(4,'2022-12-12 00:00:00','2023-12-12 00:00:00','Gerente',5000.00,'09:00:00','18:00:00',5,7),(5,'2022-12-12 00:00:00','2023-12-12 00:00:00','Cajero',5000.00,'08:30:00','18:00:00',2,8);
/*!40000 ALTER TABLE `contrato` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dimension`
--

DROP TABLE IF EXISTS `dimension`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dimension` (
  `id_dimen` int NOT NULL AUTO_INCREMENT,
  `alto_dimen` float(8,3) DEFAULT NULL,
  `largo_dim` float(8,3) DEFAULT NULL,
  `ancho_dim` float(8,3) DEFAULT NULL,
  `umedida_dim` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id_dimen`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dimension`
--

LOCK TABLES `dimension` WRITE;
/*!40000 ALTER TABLE `dimension` DISABLE KEYS */;
INSERT INTO `dimension` VALUES (1,30.000,30.000,10.000,'cm'),(2,20.000,40.000,30.000,'cm'),(3,0.000,1.000,1.000,'m'),(4,10.000,20.000,20.000,'cm'),(5,3.000,20.000,15.000,'m'),(6,3.000,2.000,2.000,'m'),(7,3.000,1.000,2.000,'m'),(8,3.000,2.000,1.000,'m'),(9,3.000,27.000,5.000,'cm'),(10,36.000,10.000,12.000,'cm'),(11,2.000,3.000,1.000,'m'),(12,25.000,16.000,2.000,'cm'),(13,5.000,6.000,2.000,'m'),(14,2.000,5.000,6.000,'m'),(15,2.000,4.000,5.000,'m');
/*!40000 ALTER TABLE `dimension` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `empresa`
--

DROP TABLE IF EXISTS `empresa`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empresa` (
  `id_emp` int NOT NULL AUTO_INCREMENT,
  `nom_emp` varchar(40) NOT NULL,
  `tel_emp` varchar(11) NOT NULL,
  PRIMARY KEY (`id_emp`),
  CONSTRAINT `empresa_chk_1` CHECK ((not((`tel_emp` like _cp850'[a-z|A-Z]'))))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empresa`
--

LOCK TABLES `empresa` WRITE;
/*!40000 ALTER TABLE `empresa` DISABLE KEYS */;
INSERT INTO `empresa` VALUES (1,'Coca-Cola','1751489523'),(2,'Bimbo','5514245879'),(3,'Gamesa','551478965'),(4,'Barcel','3521238567'),(5,'Grupo Lala','5561234567'),(6,'Nestlé México	','5561234567');
/*!40000 ALTER TABLE `empresa` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `estante`
--

DROP TABLE IF EXISTS `estante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `estante` (
  `id_est` int NOT NULL AUTO_INCREMENT,
  `tipo_est` varchar(40) NOT NULL,
  `niveles_est` int NOT NULL,
  `id_dimen` int NOT NULL,
  `id_tienarea` int NOT NULL,
  PRIMARY KEY (`id_est`),
  KEY `id_dimen` (`id_dimen`),
  KEY `id_tienarea` (`id_tienarea`),
  CONSTRAINT `estante_ibfk_1` FOREIGN KEY (`id_dimen`) REFERENCES `dimension` (`id_dimen`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `estante_ibfk_2` FOREIGN KEY (`id_tienarea`) REFERENCES `tiendaarea` (`id_tienarea`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `estante`
--

LOCK TABLES `estante` WRITE;
/*!40000 ALTER TABLE `estante` DISABLE KEYS */;
INSERT INTO `estante` VALUES (1,'anaquel',5,11,1),(2,'anaquel',5,11,2),(3,'anaquel',5,11,3),(4,'anaquel',5,11,4),(5,'anaquel',5,11,6),(6,'Anaquel',5,8,1),(7,'Anaquel',5,8,1);
/*!40000 ALTER TABLE `estante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marca`
--

DROP TABLE IF EXISTS `marca`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `marca` (
  `id_mar` int NOT NULL AUTO_INCREMENT,
  `nom_mar` varchar(45) NOT NULL,
  `tipo_mar` varchar(40) NOT NULL,
  `id_emp` int NOT NULL,
  PRIMARY KEY (`id_mar`),
  KEY `id_emp` (`id_emp`),
  CONSTRAINT `marca_ibfk_1` FOREIGN KEY (`id_emp`) REFERENCES `empresa` (`id_emp`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marca`
--

LOCK TABLES `marca` WRITE;
/*!40000 ALTER TABLE `marca` DISABLE KEYS */;
INSERT INTO `marca` VALUES (1,'coca-cola','internacional',1),(2,'bimbo','nacional',2),(3,'Gamesa','local',3),(4,'Barcel','nacional',4),(5,'Marinela','nacional',2),(6,'Lala','Internacional',5),(7,'Nestlé','Nacional',6);
/*!40000 ALTER TABLE `marca` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `minmax`
--

DROP TABLE IF EXISTS `minmax`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `minmax` (
  `num_minmax` int NOT NULL AUTO_INCREMENT,
  `fecha_minmax` datetime NOT NULL,
  `min_minmax` int NOT NULL,
  `max_minmax` int NOT NULL,
  `codbar_pro` varchar(13) NOT NULL,
  `id_tie` int NOT NULL,
  PRIMARY KEY (`num_minmax`),
  KEY `codbar_pro` (`codbar_pro`),
  KEY `id_tie` (`id_tie`),
  CONSTRAINT `minmax_ibfk_1` FOREIGN KEY (`codbar_pro`) REFERENCES `producto` (`codbar_pro`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `minmax_ibfk_2` FOREIGN KEY (`id_tie`) REFERENCES `tienda` (`id_tie`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `minmax`
--

LOCK TABLES `minmax` WRITE;
/*!40000 ALTER TABLE `minmax` DISABLE KEYS */;
INSERT INTO `minmax` VALUES (1,'2022-05-21 00:00:00',20,50,'1234567891234',1);
/*!40000 ALTER TABLE `minmax` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `persona`
--

DROP TABLE IF EXISTS `persona`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `persona` (
  `id_per` int NOT NULL AUTO_INCREMENT,
  `ap_per` varchar(40) NOT NULL,
  `am_per` varchar(40) NOT NULL,
  `nom_per` varchar(40) NOT NULL,
  `genero_per` varchar(1) NOT NULL,
  `fnac_per` date NOT NULL,
  `tel_per` varchar(10) NOT NULL,
  `mail_per` varchar(50) NOT NULL,
  `edocivil_per` varchar(20) NOT NULL,
  `calle_per` varchar(45) NOT NULL,
  `num_per` int NOT NULL,
  `orientacion_per` set('norte','sur','poniente','oriente') DEFAULT NULL,
  `entrecalles_per` varchar(100) NOT NULL,
  `id_col` int NOT NULL,
  PRIMARY KEY (`id_per`),
  KEY `id_col` (`id_col`),
  CONSTRAINT `persona_ibfk_1` FOREIGN KEY (`id_col`) REFERENCES `colonia` (`id_col`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `persona_chk_1` CHECK ((not((`tel_per` like _utf8mb4'[a-z|A-Z]'))))
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `persona`
--

LOCK TABLES `persona` WRITE;
/*!40000 ALTER TABLE `persona` DISABLE KEYS */;
INSERT INTO `persona` VALUES (1,'González','Domínguez','Ana Rosa','F','1992-06-12','7151451478','anarosa@gmai.com','soltera','Av. Independencia',54,'norte','5 de mayo y Morelos',2),(2,'','Hernández','Ernesto Daniel','M','1982-12-02','4121057896','dansan@gmail.com','casado','Hidalgo',12,'sur','2 de mayo y Mercado',3),(3,'Arriaga','Rosas','Gilberto','M','2000-05-25','3321567854','gil05@hotmail.com','soltero','La Peña',17,'poniente','Corolines y Pañolandas',4),(4,'Mendoza','Resendiz','Esther','F','1974-11-14','3271478526','esther74@hotmail.com','casada','Ignacio Rayón',18,'oriente','Coss y Laureles',5),(5,'Arriaga','Salguero','Vanessa','F','1980-05-23','1757561234','arriaga02@hotmail.com','casada','Ignacio Rayon',41,'sur','Pañolandas y Laureles',4),(6,'Gutierrez','Marin','Aracelo','F','1995-08-08','7891478523','ara_marin@yahoo.com','Casado(a)','Saranghe',74,'norte','El éden y Almahara',6),(7,'Di','Angelo','Nico','M','1999-11-11','7151234569','nico_hell06@gmail.com','Soltero(a)','Half-blood',66,'sur','Shadow y Stigya',5),(8,'Benites','Suarez','Roberto','M','1995-12-12','4567894563','suarez_rob15@gmail.com','Casado(a)','Emiliano Zapata',45,'poniente','Benito Juarez y Niños Heroes',6);
/*!40000 ALTER TABLE `persona` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `preciovta`
--

DROP TABLE IF EXISTS `preciovta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `preciovta` (
  `id_pre` int NOT NULL AUTO_INCREMENT,
  `fecha_pre` datetime NOT NULL,
  `precio_pre` float(8,2) DEFAULT NULL,
  `codbar_pro` varchar(13) NOT NULL,
  PRIMARY KEY (`id_pre`),
  KEY `codbar_pro` (`codbar_pro`),
  CONSTRAINT `preciovta_ibfk_1` FOREIGN KEY (`codbar_pro`) REFERENCES `producto` (`codbar_pro`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `preciovta`
--

LOCK TABLES `preciovta` WRITE;
/*!40000 ALTER TABLE `preciovta` DISABLE KEYS */;
INSERT INTO `preciovta` VALUES (1,'2022-09-22 00:15:19',139.91,'1234567891234'),(4,'2022-10-03 22:15:30',3645.61,'4569871231456'),(5,'2022-10-03 22:23:01',3645.61,'4569871231456'),(6,'2022-10-03 23:04:40',182.27,'4569871231456');
/*!40000 ALTER TABLE `preciovta` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tr_espia` AFTER UPDATE ON `preciovta` FOR EACH ROW begin
insert into vigila values(null, now(), user(), old.precio_pre, new.precio_pre, old.codbar_pro);
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `producto`
--

DROP TABLE IF EXISTS `producto`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto` (
  `codbar_pro` varchar(13) NOT NULL,
  `nom_pro` varchar(50) DEFAULT NULL,
  `contenido_pro` float(8,2) DEFAULT NULL,
  `umedida_pro` varchar(3) DEFAULT NULL,
  `presentacion_pro` varchar(50) DEFAULT NULL,
  `id_mar` int NOT NULL,
  `id_dimen` int NOT NULL,
  PRIMARY KEY (`codbar_pro`),
  KEY `id_mar` (`id_mar`),
  KEY `id_dimen` (`id_dimen`),
  CONSTRAINT `producto_ibfk_1` FOREIGN KEY (`id_mar`) REFERENCES `marca` (`id_mar`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `producto_ibfk_2` FOREIGN KEY (`id_dimen`) REFERENCES `dimension` (`id_dimen`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto`
--

LOCK TABLES `producto` WRITE;
/*!40000 ALTER TABLE `producto` DISABLE KEYS */;
INSERT INTO `producto` VALUES ('1234567891234','Mini Barritas',184.00,'g','Bolsa de celofán',5,9),('1478523691478','Boing',500.00,'ml','Envase de cartón',1,1),('4569871231456','POP Karameladas',120.00,'g','Bolsa biodegradable',4,12),('9874561230787','Coca-Cola',3.00,'L','Botella de plástico retornable',1,9);
/*!40000 ALTER TABLE `producto` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `renglonresurtir`
--

DROP TABLE IF EXISTS `renglonresurtir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `renglonresurtir` (
  `num_renres` int NOT NULL AUTO_INCREMENT,
  `cant_renres` int NOT NULL,
  `fcad_renres` date NOT NULL,
  `ppu_renres` int NOT NULL,
  `baja_renres` int NOT NULL,
  `id_res` int NOT NULL,
  `codbar_pro` varchar(13) NOT NULL,
  PRIMARY KEY (`num_renres`),
  KEY `id_res` (`id_res`),
  KEY `codbar_pro` (`codbar_pro`),
  CONSTRAINT `renglonresurtir_ibfk_1` FOREIGN KEY (`id_res`) REFERENCES `resurtir` (`id_res`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `renglonresurtir_ibfk_2` FOREIGN KEY (`codbar_pro`) REFERENCES `producto` (`codbar_pro`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `renglonresurtir`
--

LOCK TABLES `renglonresurtir` WRITE;
/*!40000 ALTER TABLE `renglonresurtir` DISABLE KEYS */;
INSERT INTO `renglonresurtir` VALUES (1,5,'2025-04-14',17,0,1,'4569871231456'),(2,20,'2023-12-24',32,0,1,'1234567891234'),(3,5,'2025-04-15',20,3,1,'4569871231456'),(4,20,'2024-12-24',40,4,1,'1234567891234');
/*!40000 ALTER TABLE `renglonresurtir` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `renglonticket`
--

DROP TABLE IF EXISTS `renglonticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `renglonticket` (
  `id_rentic` int NOT NULL AUTO_INCREMENT,
  `cant_rentic` int DEFAULT NULL,
  `descuento_rentic` float(8,3) DEFAULT NULL,
  `id_pre` int NOT NULL,
  `id_tic` int NOT NULL,
  PRIMARY KEY (`id_rentic`),
  KEY `id_pre` (`id_pre`),
  KEY `id_tic` (`id_tic`),
  CONSTRAINT `renglonticket_ibfk_1` FOREIGN KEY (`id_pre`) REFERENCES `preciovta` (`id_pre`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `renglonticket_ibfk_2` FOREIGN KEY (`id_tic`) REFERENCES `ticket` (`id_tic`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `renglonticket`
--

LOCK TABLES `renglonticket` WRITE;
/*!40000 ALTER TABLE `renglonticket` DISABLE KEYS */;
INSERT INTO `renglonticket` VALUES (4,2,0.000,1,1);
/*!40000 ALTER TABLE `renglonticket` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `repestatus`
--

DROP TABLE IF EXISTS `repestatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `repestatus` (
  `id_repest` int NOT NULL AUTO_INCREMENT,
  `fecha_est` date NOT NULL,
  `estatus_est` set('activo','inactivo','suspendido') DEFAULT NULL,
  `id_tierep` int NOT NULL,
  PRIMARY KEY (`id_repest`),
  KEY `id_tierep` (`id_tierep`),
  CONSTRAINT `repestatus_ibfk_1` FOREIGN KEY (`id_tierep`) REFERENCES `tiendarep` (`id_tierep`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `repestatus`
--

LOCK TABLES `repestatus` WRITE;
/*!40000 ALTER TABLE `repestatus` DISABLE KEYS */;
INSERT INTO `repestatus` VALUES (1,'2022-11-27','activo',1),(2,'2022-11-20','inactivo',1);
/*!40000 ALTER TABLE `repestatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `representante`
--

DROP TABLE IF EXISTS `representante`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `representante` (
  `id_rep` int NOT NULL AUTO_INCREMENT,
  `id_emp` int NOT NULL,
  `id_per` int NOT NULL,
  PRIMARY KEY (`id_rep`),
  KEY `id_emp` (`id_emp`),
  KEY `id_per` (`id_per`),
  CONSTRAINT `representante_ibfk_1` FOREIGN KEY (`id_emp`) REFERENCES `empresa` (`id_emp`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `representante_ibfk_2` FOREIGN KEY (`id_per`) REFERENCES `persona` (`id_per`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `representante`
--

LOCK TABLES `representante` WRITE;
/*!40000 ALTER TABLE `representante` DISABLE KEYS */;
INSERT INTO `representante` VALUES (1,1,3);
/*!40000 ALTER TABLE `representante` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `resurtir`
--

DROP TABLE IF EXISTS `resurtir`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `resurtir` (
  `id_res` int NOT NULL AUTO_INCREMENT,
  `fecha_res` datetime NOT NULL,
  `total_res` float(8,2) NOT NULL,
  `id_tierep` int NOT NULL,
  PRIMARY KEY (`id_res`),
  KEY `id_tierep` (`id_tierep`),
  CONSTRAINT `resurtir_ibfk_1` FOREIGN KEY (`id_tierep`) REFERENCES `tiendarep` (`id_tierep`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `resurtir`
--

LOCK TABLES `resurtir` WRITE;
/*!40000 ALTER TABLE `resurtir` DISABLE KEYS */;
INSERT INTO `resurtir` VALUES (1,'2022-08-22 00:00:00',10000.00,1);
/*!40000 ALTER TABLE `resurtir` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ticket`
--

DROP TABLE IF EXISTS `ticket`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ticket` (
  `id_tic` int NOT NULL AUTO_INCREMENT,
  `fecha_tic` datetime DEFAULT NULL,
  `total_tic` float(8,2) DEFAULT NULL,
  `id_con` int NOT NULL,
  `id_tie` int NOT NULL,
  PRIMARY KEY (`id_tic`),
  KEY `id_con` (`id_con`),
  KEY `id_tie` (`id_tie`),
  CONSTRAINT `ticket_ibfk_1` FOREIGN KEY (`id_con`) REFERENCES `contrato` (`id_con`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `ticket_ibfk_2` FOREIGN KEY (`id_tie`) REFERENCES `tienda` (`id_tie`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ticket`
--

LOCK TABLES `ticket` WRITE;
/*!40000 ALTER TABLE `ticket` DISABLE KEYS */;
INSERT INTO `ticket` VALUES (1,'2022-08-22 00:14:19',112.50,1,1),(2,'2022-12-12 09:22:39',2400.00,1,1);
/*!40000 ALTER TABLE `ticket` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = cp850 */ ;
/*!50003 SET character_set_results = cp850 */ ;
/*!50003 SET collation_connection  = cp850_general_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `tr_verificacionFecha2` BEFORE INSERT ON `ticket` FOR EACH ROW begin

if(new.fecha_tic <> now())
then
SIGNAL SQLSTATE VALUE '45000' set message_text = 'Fecha invalida';
end if;
end */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `tienda`
--

DROP TABLE IF EXISTS `tienda`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tienda` (
  `id_tie` int NOT NULL AUTO_INCREMENT,
  `calle_tie` varchar(45) NOT NULL,
  `num_tie` int NOT NULL,
  `orientacio_tie` set('Norte','sur','poniente','oriente') DEFAULT NULL,
  `entrecalles_tie` varchar(100) NOT NULL,
  `tel_tie` varchar(11) NOT NULL,
  `id_col` int NOT NULL,
  `id_dimen` int NOT NULL,
  PRIMARY KEY (`id_tie`),
  KEY `id_col` (`id_col`),
  KEY `id_dimen` (`id_dimen`),
  CONSTRAINT `tienda_ibfk_1` FOREIGN KEY (`id_col`) REFERENCES `colonia` (`id_col`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `tienda_ibfk_2` FOREIGN KEY (`id_dimen`) REFERENCES `dimension` (`id_dimen`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `tienda_chk_1` CHECK ((not((`tel_tie` like _cp850'[a-z|A-Z]'))))
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tienda`
--

LOCK TABLES `tienda` WRITE;
/*!40000 ALTER TABLE `tienda` DISABLE KEYS */;
INSERT INTO `tienda` VALUES (1,'Independencia',42,'Norte','I. Zaragoza y Emiliano Zapata','7151054489',2,5),(2,'Revolucion',20,'sur','Agustín de Iturbide y Degollado','3134567896',3,5),(3,'5 de mayo',12,'poniente','16 de septiembre y Miguel Hidalgo','3521234567',2,5),(4,'Plutarco Elías Calles',24,'Norte','Emiliano Zapata y Jose Ma. Coss','7154567852',2,5),(5,'Francisco I. Madero',14,'oriente','Benito Juárez y Josefa Ortíz de Domínguez','4548952741',10,5),(6,'Emilio Garcia',5,'poniente','Quirino y Cortés','7781472563',4,5);
/*!40000 ALTER TABLE `tienda` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tiendaarea`
--

DROP TABLE IF EXISTS `tiendaarea`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tiendaarea` (
  `id_tienarea` int NOT NULL AUTO_INCREMENT,
  `id_dimen` int NOT NULL,
  `id_area` int NOT NULL,
  `id_tiesec` int NOT NULL,
  PRIMARY KEY (`id_tienarea`),
  KEY `id_dimen` (`id_dimen`),
  KEY `id_area` (`id_area`),
  KEY `id_tiesec` (`id_tiesec`),
  CONSTRAINT `tiendaarea_ibfk_1` FOREIGN KEY (`id_dimen`) REFERENCES `dimension` (`id_dimen`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `tiendaarea_ibfk_2` FOREIGN KEY (`id_area`) REFERENCES `area` (`id_area`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `tiendaarea_ibfk_3` FOREIGN KEY (`id_tiesec`) REFERENCES `tiendaseccion` (`id_tiesec`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tiendaarea`
--

LOCK TABLES `tiendaarea` WRITE;
/*!40000 ALTER TABLE `tiendaarea` DISABLE KEYS */;
INSERT INTO `tiendaarea` VALUES (1,6,1,1),(2,6,2,2),(3,6,4,4),(4,6,5,5),(5,6,6,6),(6,6,6,1);
/*!40000 ALTER TABLE `tiendaarea` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tiendarep`
--

DROP TABLE IF EXISTS `tiendarep`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tiendarep` (
  `id_tierep` int NOT NULL AUTO_INCREMENT,
  `fecha_tierep` date NOT NULL,
  `id_rep` int NOT NULL,
  `id_tie` int NOT NULL,
  PRIMARY KEY (`id_tierep`),
  KEY `id_rep` (`id_rep`),
  KEY `id_tie` (`id_tie`),
  CONSTRAINT `tiendarep_ibfk_1` FOREIGN KEY (`id_rep`) REFERENCES `representante` (`id_rep`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `tiendarep_ibfk_2` FOREIGN KEY (`id_tie`) REFERENCES `tienda` (`id_tie`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tiendarep`
--

LOCK TABLES `tiendarep` WRITE;
/*!40000 ALTER TABLE `tiendarep` DISABLE KEYS */;
INSERT INTO `tiendarep` VALUES (1,'2022-09-25',1,1);
/*!40000 ALTER TABLE `tiendarep` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tiendaseccion`
--

DROP TABLE IF EXISTS `tiendaseccion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tiendaseccion` (
  `id_tiesec` int NOT NULL AUTO_INCREMENT,
  `tipo_tiesec` set('almacen','venta','mostrador') DEFAULT NULL,
  `id_tie` int NOT NULL,
  `id_dimen` int NOT NULL,
  PRIMARY KEY (`id_tiesec`),
  KEY `id_tie` (`id_tie`),
  KEY `id_dimen` (`id_dimen`),
  CONSTRAINT `tiendaseccion_ibfk_1` FOREIGN KEY (`id_tie`) REFERENCES `tienda` (`id_tie`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `tiendaseccion_ibfk_2` FOREIGN KEY (`id_dimen`) REFERENCES `dimension` (`id_dimen`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tiendaseccion`
--

LOCK TABLES `tiendaseccion` WRITE;
/*!40000 ALTER TABLE `tiendaseccion` DISABLE KEYS */;
INSERT INTO `tiendaseccion` VALUES (1,'almacen',1,6),(2,'almacen',2,6),(3,'almacen',3,6),(4,'almacen',4,6),(5,'venta',2,6),(6,'venta',3,6),(7,'venta',4,6),(8,'mostrador',1,5),(9,'mostrador',2,5),(10,'mostrador',3,5);
/*!40000 ALTER TABLE `tiendaseccion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ubicarprod`
--

DROP TABLE IF EXISTS `ubicarprod`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ubicarprod` (
  `num_ubipro` int NOT NULL AUTO_INCREMENT,
  `cant_ubipro` int NOT NULL,
  `baja_ubipro` int NOT NULL,
  `id_est` int NOT NULL,
  `num_renres` int NOT NULL,
  PRIMARY KEY (`num_ubipro`),
  KEY `id_est` (`id_est`),
  KEY `num_renres` (`num_renres`),
  CONSTRAINT `ubicarprod_ibfk_1` FOREIGN KEY (`id_est`) REFERENCES `estante` (`id_est`) ON DELETE RESTRICT ON UPDATE CASCADE,
  CONSTRAINT `ubicarprod_ibfk_2` FOREIGN KEY (`num_renres`) REFERENCES `renglonresurtir` (`num_renres`) ON DELETE RESTRICT ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ubicarprod`
--

LOCK TABLES `ubicarprod` WRITE;
/*!40000 ALTER TABLE `ubicarprod` DISABLE KEYS */;
INSERT INTO `ubicarprod` VALUES (1,5,0,5,1),(2,20,0,3,2);
/*!40000 ALTER TABLE `ubicarprod` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary view structure for view `vexistencia`
--

DROP TABLE IF EXISTS `vexistencia`;
/*!50001 DROP VIEW IF EXISTS `vexistencia`*/;
SET @saved_cs_client     = @@character_set_client;
/*!50503 SET character_set_client = utf8mb4 */;
/*!50001 CREATE VIEW `vexistencia` AS SELECT 
 1 AS `codbar_pro`,
 1 AS `nom_pro`,
 1 AS `contenido_pro`,
 1 AS `umedida_pro`,
 1 AS `presentacion_pro`,
 1 AS `nom_mar`,
 1 AS `sum(baja_renres)`*/;
SET character_set_client = @saved_cs_client;

--
-- Final view structure for view `vexistencia`
--

/*!50001 DROP VIEW IF EXISTS `vexistencia`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = cp850 */;
/*!50001 SET character_set_results     = cp850 */;
/*!50001 SET collation_connection      = cp850_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`root`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `vexistencia` AS select `p`.`codbar_pro` AS `codbar_pro`,`p`.`nom_pro` AS `nom_pro`,`p`.`contenido_pro` AS `contenido_pro`,`p`.`umedida_pro` AS `umedida_pro`,`p`.`presentacion_pro` AS `presentacion_pro`,`m`.`nom_mar` AS `nom_mar`,sum(`rr`.`baja_renres`) AS `sum(baja_renres)` from ((`producto` `p` join `marca` `m` on((`p`.`id_mar` = `m`.`id_mar`))) join `renglonresurtir` `rr` on((`p`.`codbar_pro` = `rr`.`codbar_pro`))) group by `p`.`codbar_pro` */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-12-13 16:58:20
