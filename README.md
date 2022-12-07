# Brief - Projet "restaurant_BI", par Elias et ZoLTaR
## Technologies utilisées : Python, Django, SQLite, SQLAlchemy
### Installation des prérequis pour lancer l'application Web

```sh
conda create -n restaurant_BI
conda activate restaurant_BI
conda install sqlalchemy
conda install django
conda install python-dotenv
```

## Ressources complémentaires

- Diagramme UML EER (schéma logique Entités-Relations étendu)

![alt text](restaurant_BI_EER.png "EER Model")

- Script de génération du schéma de données (compatible MySQL Server)

```sql
-- Création du schéma FastFood et des tables associées
-- Script pour MySQL Server
-- DEVIA P3 : Brief FastFood
-- Groupe : Elias et ZoLTaR
-- Date de création : 08/12/2022

CREATE SCHEMA IF NOT EXISTS `FastFood` ;

CREATE TABLE IF NOT EXISTS `FastFood`.`Poste` (
  `id_Poste` INT NOT NULL,
  `nom` VARCHAR(10) NOT NULL,
  PRIMARY KEY (`id_Poste`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `FastFood`.`Carte` (
  `id_Carte` INT NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `id_Restaurant` VARCHAR(45) NULL,
  PRIMARY KEY (`id_Carte`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `FastFood`.`Pays` (
  `id_Pays` INT NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id_Pays`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `FastFood`.`CodePostal` (
  `id_CodePostal` INT NOT NULL,
  `code` VARCHAR(10) NOT NULL,
  `id_Pays` INT NOT NULL,
  PRIMARY KEY (`id_CodePostal`),
  INDEX `fk_Pays_idx` (`id_Pays` ASC) VISIBLE,
  CONSTRAINT `fk_Pays`
    FOREIGN KEY (`id_Pays`)
    REFERENCES `FastFood`.`Pays` (`id_Pays`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `FastFood`.`Ville` (
  `id_Ville` INT NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `id_CodePostal` INT NOT NULL,
  PRIMARY KEY (`id_Ville`),
  INDEX `fk_CodePostal_idx` (`id_CodePostal` ASC) VISIBLE,
  CONSTRAINT `fk_CodePostal`
    FOREIGN KEY (`id_CodePostal`)
    REFERENCES `FastFood`.`CodePostal` (`id_CodePostal`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `FastFood`.`Adresse` (
  `id_Adresse` INT NOT NULL,
  `numero_adresse` VARCHAR(45) NULL,
  `voie_adresse` VARCHAR(45) NULL,
  `id_Ville` INT NOT NULL,
  PRIMARY KEY (`id_Adresse`),
  INDEX `fk_Ville_idx` (`id_Ville` ASC) VISIBLE,
  CONSTRAINT `fk_Ville`
    FOREIGN KEY (`id_Ville`)
    REFERENCES `FastFood`.`Ville` (`id_Ville`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `FastFood`.`Ingredient` (
  `id_Ingredient` INT NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `prix_achat` FLOAT NOT NULL,
  PRIMARY KEY (`id_Ingredient`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `FastFood`.`Item` (
  `id_Item` INT NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `type` VARCHAR(10) NOT NULL,
  `taille_boisson` VARCHAR(10) NULL,
  `prix_vente` FLOAT NOT NULL,
  PRIMARY KEY (`id_Item`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `FastFood`.`Recette` (
  `id_Recette` INT NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `quantité` INT NOT NULL,
  `id_Ingredient` INT NOT NULL,
  `id_Item` INT NOT NULL,
  PRIMARY KEY (`id_Recette`),
  INDEX `fk_Ingredient_idx` (`id_Ingredient` ASC) VISIBLE,
  INDEX `fk_Item_idx` (`id_Item` ASC) VISIBLE,
  CONSTRAINT `fk_Ingredient`
    FOREIGN KEY (`id_Ingredient`)
    REFERENCES `FastFood`.`Ingredient` (`id_Ingredient`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Item`
    FOREIGN KEY (`id_Item`)
    REFERENCES `FastFood`.`Item` (`id_Item`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `FastFood`.`Menu` (
  `id_Menu` INT NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `id_Item_plat` INT NOT NULL,
  `id_Item_boisson` INT NOT NULL,
  `id_Item_dessert` INT NOT NULL,
  PRIMARY KEY (`id_Menu`),
  INDEX `fk_item_plat_idx` (`id_Item_plat` ASC) VISIBLE,
  INDEX `fk_item_boisson_idx` (`id_Item_boisson` ASC) VISIBLE,
  INDEX `fk_item_dessert_idx` (`id_Item_dessert` ASC) VISIBLE,
  CONSTRAINT `fk_item_plat`
    FOREIGN KEY (`id_Item_plat`)
    REFERENCES `FastFood`.`Item` (`id_Item`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_item_boisson`
    FOREIGN KEY (`id_Item_boisson`)
    REFERENCES `FastFood`.`Item` (`id_Item`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_item_dessert`
    FOREIGN KEY (`id_Item_dessert`)
    REFERENCES `FastFood`.`Item` (`id_Item`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `FastFood`.`Restaurant` (
  `id_Restaurant` INT NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `espace_enfants` TINYINT NOT NULL,
  `borne_service` TINYINT NOT NULL,
  `accessible_pmr` TINYINT NOT NULL,
  `parking` TINYINT NOT NULL,
  `id_Carte` INT NOT NULL,
  `id_Employe_directeur` INT NULL,
  `id_Adresse` INT NOT NULL,
  PRIMARY KEY (`id_Restaurant`),
  INDEX `fk_Carte_idx` (`id_Carte` ASC) VISIBLE,
  INDEX `fk_Employe_directeur_idx` (`id_Employe_directeur` ASC) VISIBLE,
  INDEX `fk_Adresse_idx` (`id_Adresse` ASC) VISIBLE,
  CONSTRAINT `fk_Carte`
    FOREIGN KEY (`id_Carte`)
    REFERENCES `FastFood`.`Carte` (`id_Carte`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Adresse`
    FOREIGN KEY (`id_Adresse`)
    REFERENCES `FastFood`.`Adresse` (`id_Adresse`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `FastFood`.`Employe` (
  `id_Employe` INT NOT NULL,
  `prenom` VARCHAR(45) NOT NULL,
  `nom` VARCHAR(45) NOT NULL,
  `date_embauche` DATE NOT NULL,
  `num_compte` VARCHAR(10) NOT NULL,
  `experience` TINYINT NOT NULL,
  `id_Poste` INT NOT NULL,
  `id_Employe_responsable` INT NULL,
  `id_Restaurant` INT NULL,
  `id_Adresse_restaurant` INT NOT NULL,
  PRIMARY KEY (`id_Employe`),
  INDEX `fk_Employe_responsable_idx` (`id_Employe_responsable` ASC) VISIBLE,
  INDEX `fk_Poste_idx` (`id_Poste` ASC) VISIBLE,
  INDEX `fk_Restaurant_idx` (`id_Restaurant` ASC) VISIBLE,
  INDEX `fk_Adresse_restaurant_idx` (`id_Adresse_restaurant` ASC) VISIBLE,
  CONSTRAINT `fk_Poste`
    FOREIGN KEY (`id_Poste`)
    REFERENCES `FastFood`.`Poste` (`id_Poste`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Adresse_restaurant`
    FOREIGN KEY (`id_Adresse_restaurant`)
    REFERENCES `FastFood`.`Adresse` (`id_Adresse`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

ALTER TABLE `fastfood`.`Restaurant`
	ADD CONSTRAINT `fk_Employe_directeur`
		FOREIGN KEY (`id_Employe_directeur`)
		REFERENCES `FastFood`.`Employe` (`id_Employe`)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION;

ALTER TABLE `fastfood`.`Employe` 
	ADD CONSTRAINT `fk_Employe_responsable`
		FOREIGN KEY (`id_Employe_responsable`)
		REFERENCES `FastFood`.`Employe` (`id_Employe`)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION,
	ADD CONSTRAINT `fk_Restaurant`
		FOREIGN KEY (`id_Restaurant`)
		REFERENCES `FastFood`.`Restaurant` (`id_Restaurant`)
		ON DELETE NO ACTION
		ON UPDATE NO ACTION;

CREATE TABLE IF NOT EXISTS `FastFood`.`Salaire` (
  `id_Salaire` INT NOT NULL,
  `note` INT NOT NULL,
  `montant` DOUBLE NOT NULL,
  `date_debut` DATETIME NOT NULL,
  `date_fin` DATETIME NULL,
  `id_Employe` INT NOT NULL,
  PRIMARY KEY (`id_Salaire`),
  INDEX `fk_id_Employe_idx` (`id_Employe` ASC) VISIBLE,
  CONSTRAINT `fk_id_Employe`
    FOREIGN KEY (`id_Employe`)
    REFERENCES `FastFood`.`Employe` (`id_Employe`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `FastFood`.`TicketCaisse` (
  `id_TicketCaisse` INT NOT NULL,
  `date_heure` DATETIME NOT NULL,
  `moyen_paiement` VARCHAR(45) NOT NULL,
  `id_vendeur` INT NOT NULL,
  PRIMARY KEY (`id_TicketCaisse`),
  INDEX `fk_id_vendeur_idx` (`id_vendeur` ASC) VISIBLE,
  CONSTRAINT `fk_id_vendeur`
    FOREIGN KEY (`id_vendeur`)
    REFERENCES `FastFood`.`Employe` (`id_Employe`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;
```