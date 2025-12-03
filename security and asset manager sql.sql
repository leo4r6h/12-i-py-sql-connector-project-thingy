CREATE DATABASE IF NOT EXISTS security_db;
USE security_db;

CREATE TABLE IF NOT EXISTS assets (
    asset_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_name VARCHAR(100) NOT NULL,
    asset_type VARCHAR(50),
    ip_address VARCHAR(20),
    owner VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS vulnerabilities (
    vuln_id INT AUTO_INCREMENT PRIMARY KEY,
    asset_id INT,
    cve_code VARCHAR(20) NOT NULL,
    description VARCHAR(255),
    severity ENUM('Low', 'Medium', 'High', 'Critical') NOT NULL,
    FOREIGN KEY (asset_id) REFERENCES assets(asset_id) ON DELETE CASCADE
);