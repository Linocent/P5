# Creation BDD

CREATE DATABASE Categorie CHARACTER SET 'utf8';

# Creation table

# Creation table Categorie

CREATE TABLE Categorie (
	id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
	Noms_Categorie VARCHAR(50),
	PRIMARY KEY (id)
	)
	ENGINE = INNODB;

# Creation table Produits

CREATE TABLE Produits (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	Noms_Produits VARCHAR(50),
	Nutriscore CHAR(1),
	URL_Produit TINYTEXT,
	PRIMARY KEY (id)
	)
	ENGINE = INNODB;

# Creation table Store

CREATE TABLE Store (
	id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
	Nom_Magasin VARCHAR(20),
	PRIMARY KEY (id),
	)
	ENGINE = INNODB;

# Creation table Substitue

CREATE TABLE Substitue (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	Nom_Produit VARCHAR(50),
	Substitue VARCHAR(50),
	PRIMARY KEY (id),
	)
	ENGINE = INNODB;