-- phpMyAdmin SQL Dump
-- version 4.1.14
-- http://www.phpmyadmin.net
--
-- Client :  127.0.0.1
-- Généré le :  Sam 23 Juin 2018 à 01:42
-- Version du serveur :  5.6.17
-- Version de PHP :  5.5.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données :  `pfa`
--

-- --------------------------------------------------------

--
-- Structure de la table `admin`
--

CREATE TABLE IF NOT EXISTS `admin` (
  `name` varchar(30) NOT NULL,
  `password` varchar(10) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

--
-- Contenu de la table `admin`
--

INSERT INTO `admin` (`name`, `password`) VALUES
('admin', 'pass123');

-- --------------------------------------------------------

--
-- Structure de la table `cv_hindi`
--

CREATE TABLE IF NOT EXISTS `cv_hindi` (
  `cv_name` varchar(100) NOT NULL,
  `user_fullname` varchar(100) NOT NULL,
  `user_email` varchar(100) NOT NULL,
  `user_contact` varchar(100) NOT NULL,
  `user_address` varchar(250) NOT NULL,
  `user_residance` varchar(250) NOT NULL,
  `user_birthdate` varchar(250) NOT NULL,
  `user_languages` varchar(250) NOT NULL,
  `user_gcollege` varchar(250) NOT NULL,
  `user_gsubjects` varchar(250) NOT NULL,
  `user_gyear` varchar(100) NOT NULL,
  `user_gmark` varchar(100) NOT NULL,
  `user_tnboard` varchar(100) NOT NULL,
  `user_tnsubject` varchar(150) NOT NULL,
  `user_tnpassyear` varchar(100) NOT NULL,
  `user_tnmark` varchar(100) NOT NULL,
  `user_twboard` varchar(100) NOT NULL,
  `user_twstream` varchar(250) NOT NULL,
  `user_twpassyear` varchar(100) NOT NULL,
  `user_twmark` varchar(100) NOT NULL,
  `user_projects` text NOT NULL,
  `user_skills` text NOT NULL,
  `user_achievements` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `cv_hindi`
--

INSERT INTO `cv_hindi` (`cv_name`, `user_fullname`, `user_email`, `user_contact`, `user_address`, `user_residance`, `user_birthdate`, `user_languages`, `user_gcollege`, `user_gsubjects`, `user_gyear`, `user_gmark`, `user_tnboard`, `user_tnsubject`, `user_tnpassyear`, `user_tnmark`, `user_twboard`, `user_twstream`, `user_twpassyear`, `user_twmark`, `user_projects`, `user_skills`, `user_achievements`) VALUES
('aaaa', 'htyhzzz', 'titieeee', 'fazrrrr', 'iohoifffff', 'ioffff', 'hossss', 'hoihiqqq', 'hvvvv', 'hoccccc', 'hiohio', 'hiohbbb', 'iohnnnn', 'ihoiiiiiii', 'iohyyy', 'hioooo', 'hoppppp', 'hoiyyyyy', 'hoittttt', 'ihionnnn', 'hoiyuyuy', 'hgaga', 'iiohiosafdada'),
('aaaaaa', 'zzzzzz', 'eeeeeee', 'rrrrrrr', 'yyyyyyyyyy', 'uuuuuuuuuu', 'iiiiiiiiii', 'oooooooooo', 'pppppppp', 'qqqqqqqqq', 'ssssssssss', 'dddddddd', 'ffffffff', 'jjjjjjjjjjjjj', 'hhhhhhhhhhhh', 'gggggggggg', 'kkkkkkkkk', 'wwwwwwwwwww', 'mlmmmmmmmmmmmm', 'llllllllllll', 'xxxxxxxxxxxxxx', 'ccccccccccccyu', 'jbiuvczhbeivuzioebciuze');

-- --------------------------------------------------------

--
-- Structure de la table `user`
--

CREATE TABLE IF NOT EXISTS `user` (
  `id` int(25) NOT NULL AUTO_INCREMENT,
  `nom` varchar(25) NOT NULL,
  `prenom` varchar(25) NOT NULL,
  `email` varchar(100) NOT NULL,
  `username` varchar(30) NOT NULL,
  `password` varchar(100) NOT NULL,
  `register_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `image` varchar(255) NOT NULL,
  `cv_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=31 ;

--
-- Contenu de la table `user`
--

INSERT INTO `user` (`id`, `nom`, `prenom`, `email`, `username`, `password`, `register_date`, `image`, `cv_name`) VALUES
(1, 'mehdi', '', '', '', '', '0000-00-00 00:00:00', '', ''),
(2, 'toto', '', '', '', '', '0000-00-00 00:00:00', '', ''),
(3, 'titi', '', '', '', '', '0000-00-00 00:00:00', '', ''),
(4, 'ismail', '', '', '', '', '0000-00-00 00:00:00', '', ''),
(5, 'ismail', '', '', '', '', '0000-00-00 00:00:00', '', ''),
(6, 'ismayil', '', '', '', '', '0000-00-00 00:00:00', '', ''),
(7, 'cici', 'coco', 'caca@hotmail.fr', 'cico45', '$5$rounds=535000$3gIGYA256oQKjz./$.bhYDkBstadNLMekfYfpQetyiS2uh2q4rVP0c00pYw3', '0000-00-00 00:00:00', '', ''),
(8, 'medi', 'coco', 'caca@hotmail.fr', 'cico45', '$5$rounds=535000$U8nMjqwrLZKJ5U9W$8QlTKRJm8VI6NtiJvipMaQbrwYvBYdW54vL/cXasNxA', '0000-00-00 00:00:00', '', ''),
(9, 'coco', 'cicic', 'coca@hotmail.fr', 'coco45', '$5$rounds=535000$7ITJZgz991wA1ddG$6to.x9Nu0DrBBaCzZy13WBuhwkbkORpEvrF54W7KA05', '0000-00-00 00:00:00', '', ''),
(10, 'coco', 'cicic', 'coca@hotmail.fr', 'coco45', '$5$rounds=535000$GBAokb.3q.kW2dzP$EfFSfHRTenh7vcZm1YAAIovbXz0jdliBvltJOmsSuqC', '2018-06-14 01:44:34', '', ''),
(11, 'coco', 'cicic', 'coca@hotmail.fr', 'coco45', '$5$rounds=535000$BhRoC4Bt3.1zPMyr$vKNU4zSI80qDNPiH1hSsw/z2FixrYbHzwxksqivMQNC', '2018-06-14 01:45:21', '', ''),
(12, 'titi', '', '', '', '', '2018-06-22 23:20:22', '', ''),
(17, 'aaaaa', 'zzzzzzzzzz', 'eeeeeeeeeeeee', 'rrrrrrrr', '$5$rounds=535000$Yx37LH5hFkJ702Wl$pc8Vwpf9IjQ04V5UImwAfPUJQuXO4Byy439yBstPNL/', '2018-06-18 03:55:30', '', ''),
(18, 'aaaaaaaaaaaaaaaaaaaaaaaa', 'zzzzzzzzzzzzzzzz', 'eeeeeeeeeeeeeeeeeeee', 'rrrrrrrrrrrrrrrrr', '$5$rounds=535000$J39L4KvQ8L/meWGm$HOPZTGFUTFvGkV3x1TWUKD6uBwkWmORiTUsqlvWSL6.', '2018-06-18 03:56:33', '', ''),
(19, '', '', '', '', '', '2018-06-19 11:14:45', '', 'aaaaaa'),
(30, 'haha', '', '', '', '', '2018-06-22 23:34:36', '', '');

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
