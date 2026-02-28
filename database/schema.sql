-- Create database
CREATE DATABASE IF NOT EXISTS app_db;
USE app_db;

-- Create items table
CREATE TABLE IF NOT EXISTS items (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert sample data
INSERT INTO items (name) VALUES 
    ('Sample Item 1'),
    ('Sample Item 2'),
    ('Sample Item 3');
