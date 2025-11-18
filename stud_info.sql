-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 18, 2025 at 08:02 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `stud_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `stud_info`
--

CREATE TABLE `stud_info` (
  `stud_nm` varchar(20) NOT NULL,
  `stud_rollnum` int(10) NOT NULL,
  `m1` int(10) NOT NULL,
  `m2` int(10) NOT NULL,
  `m3` int(10) NOT NULL,
  `tot` int(10) NOT NULL,
  `avg` int(10) NOT NULL,
  `remark` varchar(10) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stud_info`
--

INSERT INTO `stud_info` (`stud_nm`, `stud_rollnum`, `m1`, `m2`, `m3`, `tot`, `avg`, `remark`, `username`, `password`) VALUES
('radhika r', 1, 90, 80, 70, 240, 80, 'GRADE B', 'admin', 'admin'),
('shravani h', 2, 90, 99, 87, 276, 92, 'Grade A', 'admin', 'admin'),
('adah', 3, 87, 67, 45, 199, 66, 'GRADE B', '', ''),
('qwrf', 4, 28, 98, 70, 196, 65, 'GRADE B', '', ''),
('yrdtgde', 5, 99, 77, 66, 242, 81, 'Grade A', '', ''),
('ewsdws', 6, 55, 55, 55, 165, 55, 'GRADE C', '', ''),
('dfsad', 7, 66, 87, 50, 203, 68, 'GRADE B', '', ''),
('fghdcg', 8, 70, 55, 66, 191, 64, 'GRADE B', '', ''),
('gdfsf', 9, 80, 50, 86, 216, 72, 'GRADE B', '', ''),
('erfws', 10, 50, 66, 44, 160, 53, 'GRADE C', '', ''),
('zed', 54, 98, 89, 94, 281, 94, 'Grade A', '', '');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
