/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - eye_hospital
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`eye_hospital` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `eye_hospital`;

/*Table structure for table `tbl_appointment` */

DROP TABLE IF EXISTS `tbl_appointment`;

CREATE TABLE `tbl_appointment` (
  `ap_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` int(11) DEFAULT NULL,
  `doc_id` int(11) DEFAULT NULL,
  `t_box` varchar(11) DEFAULT NULL,
  `adate` varchar(20) DEFAULT NULL,
  `fees` int(11) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `booking_date` varchar(30) DEFAULT NULL,
  `report` varchar(20) DEFAULT NULL,
  `history` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`ap_id`)
) ENGINE=MyISAM AUTO_INCREMENT=34 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_appointment` */

insert  into `tbl_appointment`(`ap_id`,`patient_id`,`doc_id`,`t_box`,`adate`,`fees`,`status`,`booking_date`,`report`,`history`) values 
(1,1,1,'09:06','2023-03-16',600,'cancelled','2023-03-15','Reported',NULL),
(2,2,2,'17:05','2023-03-24',600,'booked','2023-03-16','pending','not prescribed'),
(3,1,11,'13:05','2023-03-23',400,'cancelled','2023-03-17','pending',NULL),
(4,1,11,'13:05','2023-03-19',400,'booked','2023-03-17','Reported','contact lens'),
(5,1,1,'09:06','2023-03-19',600,'booked','2023-03-17','Reported','not prescribed'),
(6,2,11,'13:05','2023-03-24',400,'booked','2023-03-17','pending','eye drops'),
(8,2,11,'13:50','2023-03-29',400,'booked','2023-03-17','pending','not prescribed'),
(22,4,11,'13:35','2023-03-29',400,'booked','2023-03-17','pending','not prescribed'),
(24,1,12,'17:04','2023-03-24',700,'booked','2023-03-18','pending','not prescribed'),
(29,1,11,'13:05','2023-03-21',400,'booked','2023-03-18','Not Reported','not prescribed'),
(31,6,4,'16:05','2023-03-22',500,'booked','2023-03-21','pending','not prescribed'),
(32,6,12,'17:40','2023-03-25',700,'booked','2023-03-22','pending','not prescribed'),
(33,7,3,'09:06','2023-03-23',600,'booked','2023-03-22','Reported','Antazoline and xylometazoline ');

/*Table structure for table `tbl_cancel` */

DROP TABLE IF EXISTS `tbl_cancel`;

CREATE TABLE `tbl_cancel` (
  `can_id` int(11) NOT NULL AUTO_INCREMENT,
  `ap_id` int(11) NOT NULL,
  `p_id` int(11) NOT NULL,
  `refund` decimal(10,2) NOT NULL,
  `acc_no` varchar(100) DEFAULT NULL,
  `bank_name` varchar(35) NOT NULL,
  `bank_branch` varchar(35) NOT NULL,
  PRIMARY KEY (`can_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_cancel` */

insert  into `tbl_cancel`(`can_id`,`ap_id`,`p_id`,`refund`,`acc_no`,`bank_name`,`bank_branch`) values 
(1,1,1,300.00,'77736738388282773','ICICI BANK','KADAVANTHARA'),
(2,3,3,200.00,'66666272727272772','ICICI BANK','KADAVANTHARA');

/*Table structure for table `tbl_card` */

DROP TABLE IF EXISTS `tbl_card`;

CREATE TABLE `tbl_card` (
  `d_card_id` int(11) NOT NULL AUTO_INCREMENT,
  `patient_id` varchar(5) NOT NULL,
  `card_no` varchar(20) NOT NULL,
  `card_name` varchar(25) NOT NULL,
  `exp_date` varchar(100) NOT NULL,
  PRIMARY KEY (`d_card_id`)
) ENGINE=MyISAM AUTO_INCREMENT=35 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_card` */

insert  into `tbl_card`(`d_card_id`,`patient_id`,`card_no`,`card_name`,`exp_date`) values 
(1,'1','1111 1111 1111 1111','Devana Rose','09/24'),
(22,'1','8888 8888 8888 8888','Devana Rose','09/24'),
(23,'2','2222 2222 2222 2222','ADITHYA K L','09/24'),
(21,'2','8888 8888 8888 8888','ADITHYA K L','09/23'),
(20,'1','1111 1111 1111 1111','Devana Rose','09/24'),
(19,'4','2222 3333 2222 2222','Pranav Prasanth','09/24'),
(18,'1','1111 1111 1111 1111','Devana Rose','09/24'),
(17,'2','8872 9998 8728 8299','ADITHYA K L','09/24'),
(2,'2','3526 5632 8776 8723','sankar','02/33'),
(24,'1','2222 2222 2222 2222','Devana Rose','09/24'),
(25,'1','2233 2223 3222 2222','Devana Rose','09/24'),
(26,'1','1111 1111 1111 1111','Devana Rose','09/24'),
(27,'2','2222 2222 2222 2222','ADITHYA K L','09/24'),
(28,'2','6666 6666 6666 6666','ADITHYA K L','09/25'),
(29,'4','7777 7777 7777 7777','Pranav Prasanth','09/23'),
(30,'1','2222 2222 2222 2222','Devana Rose','09/24'),
(31,'1','5556 6655 6676 5566','Devana Rose','09/24'),
(32,'6','6652 6635 6266 2652','Nazir omer','09/24'),
(33,'6','7773 6367 3737 3737','Nazir omer','09/24'),
(34,'7','6665 6737 6265 2562','Vimala Mary','09/24');

/*Table structure for table `tbl_doctor` */

DROP TABLE IF EXISTS `tbl_doctor`;

CREATE TABLE `tbl_doctor` (
  `doc_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `doc_name` varchar(30) NOT NULL,
  `doc_dob` varchar(100) NOT NULL,
  `doc_specialization` varchar(40) NOT NULL,
  `description` varchar(2000) NOT NULL,
  `st_slot` varchar(6) NOT NULL,
  `et_slot` varchar(6) NOT NULL,
  `fees` int(3) NOT NULL,
  `doc_hname` varchar(20) NOT NULL,
  `doc_district` varchar(20) NOT NULL,
  `doc_pin` varchar(6) NOT NULL,
  `doc_gender` varchar(6) NOT NULL,
  `doc_phno` varchar(10) NOT NULL,
  `max_p` int(10) NOT NULL,
  `image` varchar(1000) NOT NULL,
  `doc_status` varchar(10) NOT NULL,
  PRIMARY KEY (`doc_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_doctor` */

insert  into `tbl_doctor`(`doc_id`,`username`,`doc_name`,`doc_dob`,`doc_specialization`,`description`,`st_slot`,`et_slot`,`fees`,`doc_hname`,`doc_district`,`doc_pin`,`doc_gender`,`doc_phno`,`max_p`,`image`,`doc_status`) values 
(1,'TJenny@gmail.com','DR TREESA JENNY','2002-05-07','GENERAL OPHTHALMOLOGY','Dr Treesa Jenny completed her medical education at Christian Medical College, Vellore with a Third Rank Merit Award in the final MBBS and received the second Certificate of Honour in General Medicine and General Surgery from CMC, Vellore. DNB from National Board of Examinations, New Delhi.   Very much involved with the community ophthalmology program of the hospital. She received the Professional Excellence Award  in 2004 for community work.','09:00','10:00',600,'maramhouse','Thrissur','567676','Female','6543219987',10,'static/image655a2f88-8f92-4ac6-9dd1-600c92446dc6doctor1.jpeg','1'),
(2,'arjunsudhi@gmail.com','DR ARJUN SUDHISH','2002-03-15','LASER VISION CORRECTION','He has worked in Chaithanya Eye Hospital, Sankara Nethralaya, Chennai and LV Prasad Eye Institute, Hyderabad.  Special interest in Ocular Surface Disorders & Corneal Stem Cells, Keratoprosthesis, Ectatic Corneal Disorders, High Risk Corneal Transplants & Pediatric Corneal Disorders. ','17:00','18:00',600,'sudhi house','Malappuram','682025','Male','8712345678',12,'static/image77910b26-1218-4ae0-a329-f367a6d8cc55doctor2.jpg','1'),
(3,'sivanand@gmail.com','DR SIVANAND M','2002-06-12','LASER VISION CORRECTION','Sivanand completed his medical education at Christian Medical College, Vellore with a Third Rank Merit Award in the final MBBS and received the second Certificate of Honour in General Medicine and General Surgery from CMC, Vellore. DNB from National Board of Examinations, New Delhi.   Very much involved with the community ophthalmology program of the hospital. He received the Professional Excellence Award  in 2004 for community work.','09:00','10:00',600,'CVAhouse','Kozhikode','898766','Male','2874636662',9,'static/image80daba1d-be89-44d3-9a81-000c25f55301team1.jpg','1'),
(4,'rose@gmail.com','DR ROSE','1993-06-22','VITREO RETINA','Dr Rose passed MBBs from Govt. Medical College, Kozhikode in 1993, DNB from Sankara Nethralaya, in June 1997, and FRCS (Glasgow, UK) in May 2006.  Dr rose has over 20 years’ experience.','16:00','17:00',500,'ghghg','Malappuram','999999','Female','4444443333',12,'static/image23142e21-888c-4016-9efe-39c905b234f7team2.jpg','1'),
(5,'mahima@gmail.com','DR MAHIMA','1996-07-18','CATARACT & GLAUCOMA','MBBS from Mysore Medical College, DO & MS from Calicut Medical College and DNB from National Board.Long Term Anterior Segment Fellowship in Giridhar Eye Institute.Over 10 years experience in cataract surgery including phaco-emulsification.She has published many articles in national and international journals and has made several presentations at National level conferences.','17:00','18:00',700,'mahihousese','Palakkad','223343','Female','2232223333',8,'static/image1bdadc2f-0c11-42f8-9256-7a3d32eb5abcteam4.jpg','1'),
(6,'shivay@gmail.com','DR SHIVAY SINGH','1986-12-17','PAEDIATRIC OPHTHALMOLOGY','MBBS, DO, MS (Ophthalmology) from Regional Institute of Ophthalmology, Trivandrum.  DNB from National Board of Examinations. Sir Ratan Tata Fellowship in Advanced cataract surgery and community Ophthalmology from Sankara Nethralaya, Chennai  Fellowship training in Paediatric Ophthalmology and Strabismus in Sankara Nethralaya, Chennai  Over 10 years teaching and clinical experience. Worked in Sankara Nethralaya.  Participated in several continuing medical education programs and presented papers. ','10:00','11:00',600,'HAGUSIJ','Malappuram','334443','Male','2277766555',12,'static/imagee8245ec6-1390-48da-9c95-47248983fe50doctor4.jpg','1'),
(7,'doctor1@gmail.com','DR MARIAN PAULY','1985-05-28','ORBIT & OCULOPLASTY','Dr Marian Pauly, DO MS from Kerala University and DNB from National Board of Examinations.  Two year Clinical fellowship programme (FMRF) in Orbit, Oculoplasty, Trauma and Reconstructive Aesthetic surgery from Sankara Nethralaya (Medical Research Foundation), Chennai. Dr Gangadhara Sundar Award for young Oculoplastic Surgeon from Sankara Nethralaya, Chennai (2012).  Life member of Oculoplastic Association of India (OPAI).  Performed more than 1000 Cataract Surgeries (SICS & Phaco). ','15:00','17:00',700,'weloksj','Kannur','879987','Female','6667637677',20,'static/image14583d8e-4aed-4170-846b-10d428d62037doctor3.jpg','0'),
(12,'aben@gmail.com','DR ABEN REJI MATHEW','2000-01-02','LASER VISION CORRECTION','Associate ConsultantCornea Corneal infections pose the major threat to the health of cornea in our environment It is the leading cause of damage to cornea resulting in corneal blindness Many microorganisms can cause corneal ulcer of which main agents are the bacteria and fungi Virus is also well known to cause corneal infections In corneal infection there will be pain reduction in vision and watering or discharge from the eye Treatment is mainly with medication in the form of eye drops Some cases that do not heal with medicines may require surgery  corneal transplantation for proper healing','17:00','18:00',700,'Reji House','Thrissur','892982','Male','7272763728',15,'static/image3eb89d4a-dd0e-4ce5-b279-b95ecc4a2a03doctor7.jpg','1'),
(11,'doctor2@gmail.com','DR NAYANTHARA','2000-12-07','LASER VISION CORRECTION','Se has worked in Chaithanya Eye Hospital Sankara Nethralaya Chennai and LV Prasad Eye Institute Hyderabad  Special interest in Ocular Surface Disorders  Corneal Stem Cells Keratoprosthesis Ectatic Corneal Disorders High Risk Corneal Transplants  Pediatric Corneal Disorders ','13:00','14:00',400,'house2 gandhi road','Malappuram','682067','Male','7726677266',12,'static/image4f62314a-7270-4c12-afbf-abaeb5e40870doctor5.jpeg','1');

/*Table structure for table `tbl_login` */

DROP TABLE IF EXISTS `tbl_login`;

CREATE TABLE `tbl_login` (
  `username` varchar(25) NOT NULL,
  `password` varchar(10) NOT NULL,
  `usertype` varchar(10) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `tbl_login` */

insert  into `tbl_login`(`username`,`password`,`usertype`) values 
('sivanand@gmail.com','cva','doctor'),
('emmanuel332@gmail.com','23asdsad','Patient'),
('staff4@gmail.com','staff4','staff'),
('staff3@gmail.com','staff3','staff'),
('arjunsudhi@gmail.com','sudhi','doctor'),
('TJenny@gmail.com','maram','doctor'),
('staff2@gmail.com','staff2','staff'),
('staff1@gmail.com','staff1','staff'),
('devanaemmanuel@gmail.com','ponnu','Patient'),
('admin@gmail.com','admin','admin'),
('rose@gmail.com','rose','doctor'),
('mahima@gmail.com','mahima','doctor'),
('shivay@gmail.com','shivay','doctor'),
('doctor1@gmail.com','doctor1','doctor'),
('carolin@gmail.com','carioline','Patient'),
('pranav@gmail.com','pranav','Patient'),
('adithya@gmail.com','adhi','Patient'),
('aben@gmail.com','reji','doctor'),
('doctor2@gmail.com','doctor2','doctor'),
('sankar22@gmail.com','dasdsa','Patient'),
('nazir@gmail.com','nazir','Patient'),
('vimala@gmail.com','mommy','Patient');

/*Table structure for table `tbl_patient` */

DROP TABLE IF EXISTS `tbl_patient`;

CREATE TABLE `tbl_patient` (
  `patient_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `patient_fname` varchar(15) NOT NULL,
  `patient_lname` varchar(15) NOT NULL,
  `p_dob` date NOT NULL,
  `p_gender` varchar(6) NOT NULL,
  `patient_hname` varchar(50) NOT NULL,
  `patient_district` varchar(20) NOT NULL,
  `patient_pin` varchar(6) NOT NULL,
  `patient_phno` varchar(10) NOT NULL,
  `status` varchar(1) NOT NULL,
  `rid` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`patient_id`)
) ENGINE=MyISAM AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_patient` */

insert  into `tbl_patient`(`patient_id`,`username`,`patient_fname`,`patient_lname`,`p_dob`,`p_gender`,`patient_hname`,`patient_district`,`patient_pin`,`patient_phno`,`status`,`rid`) values 
(1,'devanaemmanuel@gmail.com','Devana','Rose','2002-08-05','Female','93 North Girinagar','Ernakulam','682020','8847738388','1','PAT0001'),
(2,'adithya@gmail.com','Adithya','K L','2002-03-13','Female','marshall house','Ernakulam','682020','8877799888','1','PAT0002'),
(3,'carolin@gmail.com','Carolin','Periera','2001-02-08','Female','Pereira house','Ernakulam','682021','7278288778','1','PAT0003'),
(4,'pranav@gmail.com','pranav','prasanth','2002-09-09','Male','house','Thrissur','680012','9633617655','1','PAT0004'),
(5,'sankar22@gmail.com','san','kar','2023-03-19','Male','93 North Girinagar','Alappuzha','688523','8775673214','0','PAT5479'),
(6,'nazir@gmail.com','nazir','omr','2002-08-01','Male','zns house vtt','Malappuram','676102','9847127666','1','PAT8088'),
(7,'vimala@gmail.com','Vimala','Mary','1978-03-16','Female','93 North Girinagar','Ernakulam','682020','8383999483','1','PAT5006');

/*Table structure for table `tbl_payment` */

DROP TABLE IF EXISTS `tbl_payment`;

CREATE TABLE `tbl_payment` (
  `p_id` int(11) NOT NULL AUTO_INCREMENT,
  `ap_id` int(11) NOT NULL,
  `date_pay` date NOT NULL,
  `p_status` varchar(10) NOT NULL,
  PRIMARY KEY (`p_id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_payment` */

insert  into `tbl_payment`(`p_id`,`ap_id`,`date_pay`,`p_status`) values 
(1,1,'2023-03-15','Refund'),
(2,2,'2023-03-16','paid'),
(3,3,'2023-03-17','Refund'),
(4,4,'2023-03-17','paid'),
(5,5,'2023-03-17','paid'),
(6,6,'2023-03-17','paid'),
(7,8,'2023-03-17','paid'),
(8,22,'2023-03-17','paid'),
(9,24,'2023-03-18','paid'),
(10,29,'2023-03-18','paid'),
(11,31,'2023-03-21','paid'),
(12,32,'2023-03-22','paid'),
(13,33,'2023-03-22','paid');

/*Table structure for table `tbl_staff` */

DROP TABLE IF EXISTS `tbl_staff`;

CREATE TABLE `tbl_staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `staff_fname` varchar(15) NOT NULL,
  `staff_lname` varchar(15) NOT NULL,
  `staff_dob` date NOT NULL,
  `staff_hno` int(3) NOT NULL,
  `staff_hname` varchar(20) NOT NULL,
  `staff_district` varchar(20) NOT NULL,
  `staff_pin` varchar(6) NOT NULL,
  `staff_gender` varchar(6) NOT NULL,
  `staff_phno` decimal(10,0) NOT NULL,
  `staff_status` varchar(10) NOT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `tbl_staff` */

insert  into `tbl_staff`(`staff_id`,`username`,`staff_fname`,`staff_lname`,`staff_dob`,`staff_hno`,`staff_hname`,`staff_district`,`staff_pin`,`staff_gender`,`staff_phno`,`staff_status`) values 
(1,'staff1@gmail.com','Morticia','Addams','1993-06-16',122,'idek','Malappuram','682020','Female',8775673214,'1'),
(2,'staff2@gmail.com','Merin','Varghese','2002-05-07',14,'93 North Girinagar','Ernakulam','682020','Female',8712345678,'1'),
(3,'staff3@gmail.com','Karthik','A','1993-11-26',1,'khouse','Kollam','345554','Male',2434165261,'0'),
(4,'staff4@gmail.com','Aswin','Sadhan','2002-05-10',4,'sadhan house','Ernakulam','456353','Male',3333333333,'1');

/* Procedure structure for procedure `dateCk` */

/*!50003 DROP PROCEDURE IF EXISTS  `dateCk` */;

DELIMITER $$

/*!50003 CREATE DEFINER=`root`@`localhost` PROCEDURE `dateCk`()
    NO SQL
BEGIN 
	SELECT *,
      tbl_appointment.status as status, 
      (select if(adate BETWEEN 
                 DATE_SUB(adate,INTERVAL 1 DAY)
                 AND  DATE_ADD(adate,INTERVAL 1 DAY),0,1)
      ) as dt
      FROM tbl_appointment 
     INNER JOIN tbl_doctor USING(doc_id) 
     INNER JOIN tbl_patient USING(patient_id) 
     INNER JOIN tbl_payment USING(ap_id) 
     WHERE p_status='paid' and doc_id=11 order by adate;
END */$$
DELIMITER ;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
