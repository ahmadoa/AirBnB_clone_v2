-- Creates the hbnb_test_db database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create or update the user hbnb_test with the specified password
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges on the hbnb_test_db database to hbnb_test user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privilege on performance_schema to hbnb_test user
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
