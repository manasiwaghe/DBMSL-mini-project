-- Create the database
CREATE DATABASE PetManagement;

USE PetManagement;

-- Create table for shelters
CREATE TABLE shelters (
    shelter_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    location VARCHAR(100),
    capacity INT
);

-- Create table for pets
CREATE TABLE pets (
    pet_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    species VARCHAR(50),
    breed VARCHAR(50),
    age INT,
    health_status VARCHAR(100),
    shelter_id INT,
    FOREIGN KEY (shelter_id) REFERENCES shelters(shelter_id)
);

-- Create table for adopter
CREATE TABLE adopter (
    adopter_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    contact_info VARCHAR(100),
    address VARCHAR(150)
);

-- Create table for adoption
CREATE TABLE adoption (
    adoption_id INT AUTO_INCREMENT PRIMARY KEY,
    pet_id INT,
    adopter_id INT,
    adoption_date DATE,
    FOREIGN KEY (pet_id) REFERENCES pets(pet_id),
    FOREIGN KEY (adopter_id) REFERENCES adopter(adopter_id)
);

-- Create table for daycare facility
CREATE TABLE daycare (
    daycare_id INT AUTO_INCREMENT PRIMARY KEY,
    shelter_id INT,
    facility_name VARCHAR(255),
    capacity INT,
    pet_name VARCHAR(255),
    owner_name VARCHAR(255),
    contact_number VARCHAR(15),
    availability BOOLEAN,
    check_in_date DATE,
    check_out_date DATE,
    FOREIGN KEY (shelter_id) REFERENCES shelters(shelter_id)
);




