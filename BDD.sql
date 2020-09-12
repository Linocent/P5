import sqlalchemy


-- Creation BDD

CREATE DATABASE IF NOT EXISTS OpenFoodFact CHARACTER SET 'utf8';

-- Creation table

-- Creation table Categorie

CREATE TABLE IF NOT EXISTS Categorie (
	id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
	Noms_Categorie VARCHAR(50),
	PRIMARY KEY (id)
	)
	ENGINE = INNODB;

-- Creation table Produits

CREATE TABLE IF NOT EXISTS Produits (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	Noms_Produits VARCHAR(50),
	Nutriscore CHAR(1),
	URL_Produit TINYTEXT,
	Clé_catégorie Char(2)
	PRIMARY KEY (id)
	)
	ENGINE = INNODB;

-- Creation table Store

CREATE TABLE IF NOT EXISTS Store (
	id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT,
	Nom_Magasin VARCHAR(20),
	PRIMARY KEY (id),
	)
	ENGINE = INNODB;

-- Creation table Substitue

CREATE TABLE IF NOT EXISTS Substitue (
	id SMALLINT UNSIGNED NOT NULL AUTO_INCREMENT,
	Nom_Produit VARCHAR(50),
	Substitue VARCHAR(50),
	PRIMARY KEY (id),
	)
	ENGINE = INNODB;

-- On remplit les tables.

INSERT INTO Categorie(noms_categorie)
VALUES ('Citronades'),
    ('Boissons gazeuses'),
    ('Purée de PDT'),
    ('chips de PDT'),
    ('Fromages'),
    ('Yaourts aux fruits'),
    ('Pate a tartiné'),
    ('Biscuits sables'),
    ('Oeufs'),
    ('Pizzas'),
    ('Hamburger');