-- Show existing databases
SHOW DATABASES;

-- Create a proper database
CREATE DATABASE park;
USE park;

-- Drop old tables if they exist (for clean re-run)
DROP TABLE IF EXISTS Slots;
DROP TABLE IF EXISTS Areas;
DROP TABLE IF EXISTS Users;

-- Create Users table
CREATE TABLE Users (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    User_Name VARCHAR(50) NOT NULL UNIQUE,
    Password VARCHAR(50) NOT NULL
);

-- Create Areas table
CREATE TABLE Areas (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Area_Name VARCHAR(100) NOT NULL UNIQUE
);

-- Create Slots table
CREATE TABLE Slots (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    Area_ID INT NOT NULL,
    Slot_Number INT NOT NULL,
    Vehicle_Type ENUM('Car','Bike','EV','Auto','Cycle') DEFAULT 'Car',
    Booking_Time DATETIME,
    Token VARCHAR(20),
    Status ENUM('Available', 'Occupied') NOT NULL DEFAULT 'Available',
    FOREIGN KEY (Area_ID) REFERENCES Areas(ID) ON DELETE CASCADE
);

-- Show tables
SHOW TABLES;

-- Insert sample Users
INSERT INTO Users (User_Name, Password) VALUES
('User1', 'pass1'),
('User2', 'pass2'),
('User3', 'pass3'),
('User4', 'pass4'),
('User5', 'pass5'),
('User6', 'pass6'),
('User7', 'pass7'),
('User8', 'pass8'),
('User9', 'pass9'),
('User10', 'pass10'),
('User11', 'pass11'),
('User12', 'pass12'),
('User13', 'pass13'),
('User14', 'pass14'),
('User15', 'pass15'),
('User16', 'pass16'),
('User17', 'pass17'),
('User18', 'pass18'),
('User19', 'pass19'),
('User20', 'pass20');

-- Check Users
SELECT * FROM Users;

-- Insert Parking Areas
INSERT INTO Areas (Area_Name) VALUES
('SCOE Parking'),
('SKN Parking'),
('Krishna Hostel Parking');

-- Check Areas
SELECT * FROM Areas;

-- Insert Slots for each Area
INSERT INTO Slots (Area_ID, Slot_Number, Vehicle_Type, Booking_Time, Token, Status) VALUES
(1, 101, 'Car', NULL, NULL, 'Available'),
(1, 102, 'Bike', '2025-09-29 09:00:00', 'TKN101', 'Occupied'),
(1, 103, 'EV', NULL, NULL, 'Available'),
(1, 104, 'Auto', NULL, NULL, 'Available'),
(1, 105, 'Cycle', NULL, NULL, 'Available'),
(1, 106, 'Bike', NULL, NULL, 'Available'),
(1, 107, 'Cycle', NULL, NULL, 'Available'),
(1, 108, 'Car', NULL, NULL, 'Available'),
(1, 109, 'EV', NULL, NULL, 'Available'),
(1, 110, 'Auto', NULL, NULL, 'Available'),

(2, 201, 'Car', '2025-09-29 10:30:00', 'TKN201', 'Occupied'),
(2, 202, 'Bike', NULL, NULL, 'Available'),
(2, 203, 'EV', NULL, NULL, 'Available'),
(2, 204, 'Auto', NULL, NULL, 'Available'),
(2, 205, 'Car', '2025-10-15  4:30:40',"TK2N5","Occupied"),
(2, 206, 'Cycle', NULL, NULL, 'Available'),
(2, 207, 'Bike', NULL, NULL, 'Available'),
(2, 208, 'EV', '2025-10-20 5:00:00',"TK2N5T","Occupied"),
(2, 209, 'EV', NULL, NULL, 'Available'),
(2, 210, 'Car', NULL, NULL, 'Available'),

(3, 301, 'Car', '2025-09-29 11:00:00', 'TKN301', 'Occupied'),
(3, 302, 'Car', NULL, NULL, 'Available'),
(3, 303, 'Bike', NULL, NULL, 'Available'),
(3, 304, 'EV', NULL, NULL, 'Available'),
(3, 305, 'EV',  '2025-10-12 3:20:45',"TKN37T","Occupied"),
(3, 306, 'Car', NULL, NULL, 'Available'),
(3, 307, 'Cycle',  '2025-10-10 12:00:30', "TKN30R","Occupied"),
(3, 308, 'Bike', NULL, NULL, 'Available'),
(3, 309, 'Bike', NULL, NULL, 'Available'),
(3, 3010, 'Auto', NULL, NULL, 'Available');

-- Check Slots
SELECT * FROM Slots;
SELECT *from Users;
SELECT *from Areas;
-- Confirm current DB server can be reached and list DBs
SHOW DATABASES;

-- Confirm you are using the DB the app should use
USE park;
SELECT DATABASE() AS current_db;

-- List tables in that database
SHOW TABLES;

-- See exactly what tables MySQL knows about in that schema
SELECT TABLE_NAME FROM information_schema.TABLES
 WHERE TABLE_SCHEMA = 'park';
