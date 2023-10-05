-- MySQL dump 10.13  Distrib 5.5.57, for Win64 (AMD64)
--
-- Host: localhost    Database: air
-- ------------------------------------------------------
-- Server version	5.5.57

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `common2`
--

DROP TABLE IF EXISTS `common2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `common2` (
  `PNRNO` int(11) NOT NULL AUTO_INCREMENT,
  `PassengerName` varchar(30) DEFAULT NULL,
  `boarding` char(20) DEFAULT NULL,
  `destination` char(20) DEFAULT NULL,
  `date` char(30) DEFAULT NULL,
  `time` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`PNRNO`)
) ENGINE=InnoDB AUTO_INCREMENT=201 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `common2`
--

LOCK TABLES `common2` WRITE;
/*!40000 ALTER TABLE `common2` DISABLE KEYS */;
INSERT INTO `common2` VALUES (200,'Manvi Singh','Bangalore','New Delhi','23-03-2021','4:00 PM');
/*!40000 ALTER TABLE `common2` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `display`
--

DROP TABLE IF EXISTS `display`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `display` (
  `Boarding` char(20) DEFAULT NULL,
  `Destination` char(20) DEFAULT NULL,
  `Date` char(20) DEFAULT NULL,
  `Time` varchar(25) DEFAULT NULL,
  `Class` char(10) DEFAULT NULL,
  `Fare` varchar(30) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `display`
--

LOCK TABLES `display` WRITE;
/*!40000 ALTER TABLE `display` DISABLE KEYS */;
INSERT INTO `display` VALUES ('SRINAGAR','MUMBAI','20-03-2021','1:00','Economic','Rs.2500'),('SRINAGAR','BANGALORE','21-03-2021','4:00','Business','Rs.7500'),('SRINAGAR','NEW DELHI','22-03-2021','7:00','Economic','Rs.5500'),('SRINAGAR','chennai','23-03-2021','4:00','Economic','Rs.5800'),('MUMBAI','BANGALORE','24-03-2021','9:00',' Business','Rs.6700'),('MUMBAI','AHMEDABAD','25-03-2021','9:00','Economic','Rs.6000'),('MUMBAI','KOLKATA','21-03-2021','1:00','Economic','Rs6000'),('BANGALORE','CHENNAI','22-03-2021','7:00','Economic','Rs.5790'),('BANGALORE','AHEMDABAD','20-03-2021','4:00','Business','Rs.7564'),('BANGALORE','SRINAGAR','23-03-2021','1:00','Economic','Rs.6590'),('BANGALORE','KOLKATA','24-03-2021','1.00','Economic','Rs.5570'),('KOLKATA','MUMBAI','25-03-2021','1:00','Business','Rs.4598'),('KOLKATA','BANGALORE','21-03-2021','7.00','Economic','Rs.4500'),('KOLKATA','CHENNAI','22-03-2021','1:00','Business','Rs.5500'),('NEW DELHI','SHRINAGAR','23-03-2021','9:00','Economic','Rs.5040'),('NEW DELHI','BANGALORE','24-03-2021','1:00','Economic','Rs.5040'),('NEW DELHI','CHENNAI','25-03-2021','1:00','BUSINESS','Rs.8040'),('NEW DELHI','AHMEDABAD','20-03-2021','7:00','Economic','Rs.5040'),('NEW DELHI','KOLKATA','21-03-2021','4:00','Economic','Rs.5040'),('CHENNAI','NEW DELHI','22-03-2021','1:00','Business','Rs.6900'),('CHENNAI','MUMBAI','23-03-2021','9:00','Economic','Rs.6600'),('CHENNAI','KOLKATA','24-03-2021','7:00','Business','Rs.7600'),('CHENNAI','SHRINAGAR','25-03-2021','4:00','Economic','Rs.6600'),('CHENNAI','AHMEDABAD','20-03-2021','1:00','Economic','Rs.6600'),('Ahmedabad','Chennai','21-03-2021','7:00','Economic','Rs.5570'),('Ahmedabad','KOLKATA','22-03-2021','9:00','Business','Rs.9570'),('Ahmedabad','Mumbai','23-03-2021','1:00','Economic','Rs.4000'),('SRINAGAR','BANGALORE','25-03-2021','1:00','Business','Rs.10000'),('KOLKATA','Ahmedabad','23-03-2021','4:00','Economic','Rs.3500'),('Chennai','Bangalore','24-03-2021','9:00','Business','Rs.2500'),('Jaipur','Bangalore','20-03-2021','9:00','Business','Rs.2900'),('Jaipur','MUMBAI','24-03-2021','1:00','Economic','Rs.2800'),('Jaipur','NEW DELHI','22-03-2021','7:00','Economic','Rs.5500'),('Jaipur','Kolkata','22-03-2021','1:00','Economic','Rs.2800');
/*!40000 ALTER TABLE `display` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `economic2`
--

DROP TABLE IF EXISTS `economic2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `economic2` (
  `PNRNO` int(11) NOT NULL AUTO_INCREMENT,
  `PassengerName` varchar(30) DEFAULT NULL,
  `boarding` char(20) DEFAULT NULL,
  `destination` char(20) DEFAULT NULL,
  `date` char(30) DEFAULT NULL,
  `time` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`PNRNO`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `economic2`
--

LOCK TABLES `economic2` WRITE;
/*!40000 ALTER TABLE `economic2` DISABLE KEYS */;
INSERT INTO `economic2` VALUES (100,'kam',' Mumbai','Ahmedabad','22-03-2021','1:00 PM');
/*!40000 ALTER TABLE `economic2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-05 19:40:31
