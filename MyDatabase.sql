-- MySQL dump 10.13  Distrib 5.7.32, for Linux (x86_64)
--
-- Host: localhost    Database: SEMDB
-- ------------------------------------------------------
-- Server version	5.7.32-0ubuntu0.18.04.1

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
-- Table structure for table `demo`
--

DROP TABLE IF EXISTS `demo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `demo` (
  `email` varchar(24) NOT NULL,
  `password` varchar(24) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `demo`
--

LOCK TABLES `demo` WRITE;
/*!40000 ALTER TABLE `demo` DISABLE KEYS */;
INSERT INTO `demo` VALUES ('hello@exl.com','heelodasd'),('jitenada@fasj.com','duiasdasehaiwe'),('jitenada@adaa.com','JItenasdh@136468'),('jitenada@hmail.com','sadkjasgjdia56465'),('akash@chutiya.com','akash@chut'),('akash@chutiya.com','akash@chut'),('akash@chutiya.com','akash@chut'),('jitaena@das.com','new@pasdask1234'),('jite@ghmal.com','jhhyb@3423');
/*!40000 ALTER TABLE `demo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exp_category`
--

DROP TABLE IF EXISTS `exp_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exp_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `catName` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exp_category`
--

LOCK TABLES `exp_category` WRITE;
/*!40000 ALTER TABLE `exp_category` DISABLE KEYS */;
INSERT INTO `exp_category` VALUES (1,'Bills/Utilities'),(2,'Education'),(3,'EMI'),(4,'Entertainment'),(5,'Food & Drinks'),(6,'Grocery'),(7,'Health'),(8,'Insurance'),(9,'Investments'),(10,'Loan'),(11,'Air Tickets'),(12,'Beauty/Fitness'),(13,'Bike'),(14,'Books'),(15,'Breakfast'),(16,'Bus Fare'),(17,'Business'),(18,'Cable'),(19,'Car'),(20,'Cash Spend'),(21,'Cigarettes'),(22,'Clothes'),(23,'Coffee'),(24,'Cookies'),(25,'Courier'),(26,'Cycle'),(27,'Daily Care'),(28,'Dining'),(29,'Disco'),(30,'Donation'),(31,'Drinks'),(32,'Electricity'),(33,'Electronics'),(34,'Fast Food'),(35,'Flowers'),(36,'Games'),(37,'Petrol/Disel'),(38,'Gifts'),(39,'Jewellery'),(40,'Gym'),(41,'Health'),(42,'OYO'),(43,'Household'),(44,'Ice-cream'),(45,'Maid/Driver'),(46,'Maintenance'),(47,'Medical'),(48,'Miscellaneous'),(49,'Mutual Funds'),(50,'Office'),(51,'Pets'),(52,'Post Office'),(53,'Printing/Scanning'),(54,'Rent/Mortgage'),(55,'Salon'),(56,'Savings'),(57,'Shopping'),(58,'Stationery'),(59,'Stocks'),(60,'Tax'),(61,'Toys'),(62,'Transport'),(63,'Water');
/*!40000 ALTER TABLE `exp_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `expenses`
--

DROP TABLE IF EXISTS `expenses`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `expenses` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `UserId` int(11) NOT NULL,
  `expDate` date NOT NULL,
  `expCategory` int(11) NOT NULL,
  `expAmount` int(11) NOT NULL,
  `expDesc` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `UserId` (`UserId`),
  KEY `expCategory` (`expCategory`),
  CONSTRAINT `expenses_ibfk_1` FOREIGN KEY (`UserId`) REFERENCES `user` (`id`),
  CONSTRAINT `expenses_ibfk_2` FOREIGN KEY (`expCategory`) REFERENCES `exp_category` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expenses`
--

LOCK TABLES `expenses` WRITE;
/*!40000 ALTER TABLE `expenses` DISABLE KEYS */;
INSERT INTO `expenses` VALUES (1,2,'2021-01-27',59,15000,'Exide '),(2,2,'2021-01-31',57,450,'Shoes'),(3,2,'2021-01-30',57,1752,'Eyeglasses'),(4,2,'2021-01-28',3,1700,'Wrist Watch'),(5,2,'2021-01-20',56,2000,'Savings'),(6,2,'2021-01-27',6,75,'Milk'),(7,2,'2021-01-22',5,100,'Paneer Butter Masala'),(8,2,'2021-01-08',59,7000,'Stocks'),(9,2,'2021-01-01',23,174,'Coffee');
/*!40000 ALTER TABLE `expenses` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  `mobno` varchar(255) NOT NULL,
  `regdate` date NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Neeraj Yadav','neeraj@gmail.com','$2b$12$9lZYj9sZ89fGt979LdBgWOSpb5CzwINa4QDW2s7GmD2wKldXkuBDO','8445436985','2021-01-30'),(2,'JIten','jiten@gmail.com','sha256$DTjelTcU$b288905cc18cca13ce4064e235444fdfb68d9ab7405bc2f08a135d46e8aa623b','8446453858','2021-01-30');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-20 19:41:43
