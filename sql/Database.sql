-- MySQL dump 10.13  Distrib 5.7.34, for Linux (x86_64)
--
-- Host: localhost    Database: SEMDB
-- ------------------------------------------------------
-- Server version	5.7.34-0ubuntu0.18.04.1

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
) ENGINE=InnoDB AUTO_INCREMENT=408 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `expenses`
--

LOCK TABLES `expenses` WRITE;
/*!40000 ALTER TABLE `expenses` DISABLE KEYS */;
INSERT INTO `expenses` VALUES (1,2,'2021-01-27',59,15000,'Exide '),(2,2,'2021-01-31',57,450,'Shoes'),(3,2,'2021-01-30',57,1752,'Eyeglasses'),(4,2,'2021-01-28',3,1700,'Wrist Watch'),(5,2,'2021-01-20',56,2000,'Savings'),(6,2,'2021-01-27',6,75,'Milk'),(7,2,'2021-01-22',5,100,'Paneer Butter Masala'),(8,2,'2021-01-08',59,7000,'Stocks'),(9,2,'2021-01-01',23,174,'Coffee'),(10,2,'2021-02-27',59,1000,'Exide '),(24,2,'2021-02-02',57,300,'T-Shirt'),(34,2,'2021-02-05',57,1552,'Contacts'),(35,2,'2021-02-18',40,800,'GYM Memebership'),(60,2,'2021-02-27',59,2000,'TATA '),(61,2,'2021-02-18',15,150,'Dosa'),(91,2,'2020-04-01',54,15000,'2 BHK Room Rent'),(92,2,'2020-04-02',6,3000,'Grocery Items'),(93,2,'2020-04-02',37,500,'Petrol'),(94,2,'2020-04-02',5,120,'Food And Beverages'),(95,2,'2020-04-05',1,860,'Light Bill(100 units)'),(96,2,'2020-04-05',1,900,'Wifi and phone recharge '),(97,2,'2020-04-06',22,1580,'Clothes Shopping'),(98,2,'2020-04-08',2,1000,'Tution fess'),(99,2,'2020-04-09',46,500,'Society Maintenance'),(100,2,'2020-04-10',45,1500,'Cook'),(101,2,'2020-04-11',40,3000,'Gym Membership 3 months '),(102,2,'2020-04-12',13,500,'Petrol after 1 week '),(103,2,'2020-04-13',47,300,'Fever and Cough'),(105,2,'2020-04-15',5,500,'Drinks '),(106,2,'2020-04-16',5,1200,'Dinner '),(107,2,'2020-04-17',1,2000,'Birthday '),(108,2,'2020-04-18',33,8000,'New home theater '),(109,2,'2020-04-19',55,300,'Personal Grooming (saloon)'),(110,2,'2020-04-20',44,100,'Ice cream '),(111,2,'2020-04-21',59,2500,'Investment '),(112,2,'2020-01-22',37,500,'Petrol after 3 week'),(113,2,'2020-04-23',60,3000,'Tax Bill'),(114,2,'2020-04-24',57,300,'Shopping  of home decorative items '),(115,2,'2020-06-25',23,150,'Coffee'),(116,2,'2020-04-25',24,100,'cookies'),(117,2,'2020-04-26',36,800,'Gaming Zone'),(118,2,'2020-04-27',11,6000,'Bussines Tour'),(119,2,'2020-04-28',56,5000,'Saving for future '),(120,2,'2020-04-29',28,1200,'Dinner'),(121,2,'2020-05-01',1,15000,'EMI'),(122,2,'2020-05-01',54,15000,'2 BHK Room Rent'),(123,2,'2020-05-02',37,500,'Petrol for 1st week '),(124,2,'2020-05-03',1,960,'Light Bill (110 units)'),(125,2,'2020-05-04',1,600,'Wifi Recharge'),(126,2,'2020-05-05',1,350,'Phone Recharge'),(127,2,'2020-05-06',2,5000,'School Fees(for lower standard classes) for 4 months '),(128,2,'2020-05-07',4,120,'Movie Day'),(129,2,'2020-05-08',37,500,'Petrol after 1 week'),(130,2,'2020-05-09',22,250,'Online Clothes Shopping'),(131,2,'2020-05-10',5,800,'Lunch'),(132,2,'2020-05-11',44,150,'Icecream'),(133,2,'2020-05-12',46,500,'Society Maintenance'),(134,2,'2020-05-13',15,120,'Morning Day'),(135,2,'2020-05-14',37,500,'Petrol after 3 week'),(136,2,'2020-05-15',30,500,'Donation for festival '),(137,2,'2020-05-16',19,650,'Cab Book ed for Bussines (2-3 days )'),(138,2,'2020-05-17',42,2360,'2 day stay at hotel(includes breakfast only )'),(139,2,'2020-05-18',28,300,'Dinner'),(140,2,'2020-05-19',31,100,'Drinks'),(141,2,'2020-05-20',14,350,'Books Purchased '),(142,2,'2020-05-21',1,101,'Data pack recharge because he was on bussiness tour '),(143,2,'2020-05-22',49,3000,'Investment'),(144,2,'2020-05-22',60,3000,'Tax Bill'),(145,2,'2020-05-23',45,1500,'Cook'),(146,2,'2020-05-24',55,120,'Personal Grooming (saloon)'),(147,2,'2020-05-25',4,120,'Movie Night'),(148,2,'2020-05-26',28,1200,'Dinner'),(149,2,'2020-05-27',1,150,'Water Bill (always at last date of month)'),(150,2,'2020-05-28',56,3000,'Saving for future (less saving bcz of bussines tour)'),(151,2,'2020-06-01',54,15000,'2 BHK Room Rent'),(152,2,'2020-06-02',1,680,'Light Bill (85 units) bcz in april he was on Bussiness Tour '),(153,2,'2020-06-03',1,600,'Wifi Recharge'),(154,2,'2020-06-04',1,350,'Phone Recharge'),(155,2,'2020-06-05',1,300,'TV Recharge'),(156,2,'2020-06-06',6,3000,'Grocery Items'),(157,2,'2020-06-07',46,500,'Society Maintenance'),(158,2,'2020-06-08',37,500,'Petrol after 1 week'),(159,2,'2020-06-09',36,300,'Game Zone'),(160,2,'2020-06-10',47,400,'Medical Case '),(161,2,'2020-06-11',7,600,'Fruits and Green Vegetables '),(162,2,'2020-06-12',19,330,'Cab Book (Because he was not able to drive bike)'),(163,2,'2020-06-13',15,100,'Breakfast'),(164,2,'2020-06-14',57,250,'Clothes Shopping'),(165,2,'2020-06-15',4,200,'Birthday'),(166,2,'2020-06-16',45,1500,'Cook'),(167,2,'2020-06-17',55,200,'Personal Grooming (saloon)'),(168,2,'2020-06-18',44,120,'Icecream'),(169,2,'2020-06-19',1,3000,'Investment'),(170,2,'2020-06-20',37,500,'petrol for 4 week '),(171,2,'2020-06-21',60,3000,'Tax Bill'),(172,2,'2020-06-22',20,1200,'Guest (extra food and vegetables)'),(173,2,'2020-06-23',28,2500,'Dinner with guest and famiy after long time '),(174,2,'2020-06-24',23,60,'Coffee'),(175,2,'2020-06-25',24,40,'cookies'),(176,2,'2020-06-26',1,170,'Water Bill (always at last date of month)'),(177,2,'2020-06-27',19,550,'Cab Book (For Guest)'),(178,2,'2020-06-28',2,1000,'Tution fess'),(179,2,'2020-06-29',8,500,'Insurance for medical '),(180,2,'2020-06-30',1,1000,'EMI '),(271,2,'2020-10-01',32,1100,'Electricity Bill'),(272,2,'2020-10-01',18,1500,'Cable Bills'),(273,2,'2020-10-02',37,500,'Bike Petrol'),(274,2,'2020-10-03',15,300,'Morning Breakfast'),(275,2,'2020-10-04',22,1800,'Clothes Shopping'),(276,2,'2020-10-05',36,800,'Game Zone'),(277,2,'2020-10-06',4,2000,'Movie'),(278,2,'2020-10-07',5,1200,'Lunch'),(279,2,'2020-10-08',14,1000,'Books Purchase'),(280,2,'2020-10-09',46,400,'Society Maintenance'),(281,2,'2020-10-10',5,500,'Drinks'),(282,2,'2020-10-10',5,1500,'Dinner'),(283,2,'2020-10-12',47,800,'Medical Bill'),(284,2,'2020-10-13',2,30000,'School Education'),(285,2,'2020-10-14',37,2000,'Car Diesel'),(286,2,'2020-10-15',1,10000,'House Bill'),(287,2,'2020-10-16',15,400,'Morning Breakfast'),(288,2,'2020-10-17',4,2000,'Birthday'),(289,2,'2020-10-19',36,200,'Game Zone'),(290,2,'2020-10-20',37,600,'Bike Petrol'),(291,2,'2020-10-21',5,1000,'Lunch'),(292,2,'2020-10-22',47,200,'Medical'),(293,2,'2020-10-23',44,200,'Ice-Cream'),(294,2,'2020-10-24',40,700,'Gym'),(295,2,'2020-10-25',22,200,'Clothes'),(296,2,'2020-10-26',5,1000,'Dinner'),(297,2,'2020-10-27',44,250,'Ice-Cream'),(298,2,'2020-10-28',15,300,'Breakfast'),(299,2,'2020-10-29',1,500,'Wifi bill'),(300,2,'2020-10-30',2,700,'Tution Fee'),(301,2,'2020-11-01',32,900,'Electricity Bill'),(302,2,'2020-11-01',18,1200,'Cable Bills'),(303,2,'2020-11-02',15,400,'Morning Breakfast'),(304,2,'2020-11-03',4,1000,'Movie'),(305,2,'2020-11-04',47,700,'Medical'),(306,2,'2020-11-05',22,300,'Clothes'),(307,2,'2020-11-06',44,200,'Ice-Cream'),(308,2,'2020-11-07',5,1000,'Lunch'),(309,2,'2020-11-08',36,300,'Game Zone'),(310,2,'2020-11-09',46,400,'Society Maintenance'),(311,2,'2020-11-10',37,600,'Bike Petrol'),(312,2,'2020-11-11',5,300,'Drinks'),(313,2,'2020-11-12',15,200,'Breakfast'),(314,2,'2020-11-14',14,1200,'Car Diesel'),(315,2,'2020-11-15',1,10000,'House Bill'),(316,2,'2020-11-16',5,1200,'Dinner'),(317,2,'2020-11-17',44,400,'Ice-Cream'),(318,2,'2020-11-18',14,400,'Books'),(319,2,'2020-11-19',5,800,'Lunch'),(320,2,'2020-11-20',1,600,'Mobile Bill'),(321,2,'2020-11-21',15,200,'Breakfast'),(322,2,'2020-11-22',36,300,'Games'),(323,2,'2020-11-24',40,700,'Gym'),(324,2,'2020-11-25',5,600,'Drinks'),(325,2,'2020-11-26',1,3000,'Tax Bill'),(326,2,'2020-11-27',44,100,'Ice-Cream'),(327,2,'2020-11-28',1,600,'Mobile Bill'),(328,2,'2020-11-29',15,500,'Breakfast'),(329,2,'2020-11-29',1,500,'Wifi bill'),(330,2,'2020-11-30',2,700,'Tution Fee'),(331,2,'2020-12-01',32,1000,'Electricity Bill'),(332,2,'2020-12-01',18,1100,'Cable Bills'),(333,2,'2020-12-02',47,500,'Medical'),(334,2,'2020-12-03',5,900,'Lunch'),(335,2,'2020-12-04',14,1200,'Car Diesel'),(336,2,'2020-12-05',36,400,'Games'),(337,2,'2020-12-06',15,300,'Breakfast'),(338,2,'2020-12-07',37,500,'Bike Petrol'),(339,2,'2020-12-08',4,1000,'Movie'),(340,2,'2020-12-09',46,400,'Society Maintenance'),(341,2,'2020-12-10',5,500,'Drinks'),(342,2,'2020-12-11',44,300,'Ice-Cream'),(343,2,'2020-12-13',14,400,'Books'),(344,2,'2020-12-14',5,1000,'Dinner'),(345,2,'2020-12-15',1,10000,'House Bill'),(346,2,'2020-12-17',1,600,'Mobile Bill'),(347,2,'2020-12-18',44,300,'Ice-Cream'),(348,2,'2020-12-19',22,300,'Clothes'),(349,2,'2020-12-20',15,300,'Breakfast'),(350,2,'2020-12-21',4,1000,'Movie'),(351,2,'2020-12-22',37,600,'Bike Petrol'),(352,2,'2020-12-23',5,900,'Lunch'),(353,2,'2020-12-23',1,3000,'Tax Bill'),(354,2,'2020-12-24',40,700,'Gym'),(355,2,'2020-12-25',44,200,'Ice-Cream'),(356,2,'2020-12-26',5,1100,'Dinner'),(357,2,'2020-12-27',4,500,'Night-out'),(358,2,'2020-12-28',15,500,'Breakfast'),(359,2,'2020-12-29',1,500,'Wifi bill'),(360,2,'2020-12-30',2,700,'Tution Fee'),(363,3,'2021-05-01',59,9800,'TATA Power'),(364,3,'2021-05-02',5,100,'Oreo'),(368,2,'2021-05-01',5,500,'Oreo'),(369,2,'2021-05-02',62,250,'Ola'),(370,2,'2021-05-03',58,50,'Pen and Paper'),(371,2,'2021-05-08',1,499,'airtel recharge'),(372,2,'2021-05-06',33,2120,'Keyboard'),(373,2,'2020-01-21',59,6700,'Coal India'),(374,2,'2020-01-15',37,300,'Petrol'),(375,2,'2020-01-11',1,570,'Tata Sky'),(376,2,'2020-01-04',3,4056,'iPhone 11'),(377,2,'2020-01-03',12,150,'Shampoo'),(378,2,'2020-01-08',40,2000,'Gym Memebership'),(379,2,'2020-01-12',5,450,'Dominos\'s'),(380,2,'2020-01-14',8,1500,'Health Insurance'),(381,2,'2020-01-18',1,1000,'Wifi'),(382,2,'2020-01-15',42,4500,'OYO in Goa'),(383,2,'2020-01-18',5,1450,'Sea Food'),(384,2,'2020-01-19',11,2500,'Back to Home'),(385,2,'2020-01-24',33,8500,'Monitor'),(386,2,'2021-02-11',33,10000,'Speakers'),(387,2,'2021-02-03',10,7500,'Laptop Loan'),(389,2,'2021-05-09',22,4850,'Jeans and Winterwear'),(390,2,'2021-05-10',13,3500,'Bike Servicing'),(393,2,'2021-05-24',37,300,'Petrol'),(394,2,'2021-05-24',54,1500,'Rent'),(402,2,'2021-05-18',29,2500,'KP'),(403,2,'2021-05-24',33,906,'Lamp'),(404,2,'2021-05-25',8,5000,'Health'),(405,2,'2021-04-15',49,5000,'SHINDE ENGG'),(407,2,'2021-06-22',1,500,'Bill');
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
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Neeraj Yadav','neeraj@gmail.com','$2b$12$9lZYj9sZ89fGt979LdBgWOSpb5CzwINa4QDW2s7GmD2wKldXkuBDO','8445436985','2021-01-30'),(2,'WADI','jiten@gmail.com','sha256$V3Mcf2YP$a1abe32640718cf3bfdfdcf9a9b64fc011eed313876e3be04a1cd1aff1e6598c','8446445885','2021-01-30'),(3,'Akash SHinde','akash@gmail.com','sha256$0ENnUhyB$1f872c2efc9385b27cb100aa679b630b20906846f3ce2c91ede70eaf27c12e46','8446453858','2021-05-02');
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

-- Dump completed on 2021-06-23 18:23:57
