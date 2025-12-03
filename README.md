# 4. INTRODUCTION
This software project is developed to automate the
functionalities of a Cybersecurity Asset Management
System. The purpose of this Management Information
System (MIS) is to automate the record-keeping of
hardware assets (like servers and laptops) and the
tracking of their security vulnerabilities.

A MIS mainly consists of a computerized database and
a collection of inter-related tables. An application
program (Front-end) is tied with the database (Back-
end) for easy access. Using this application,
security managers can store, retrieve, and manage
critical security data in a proper way.

This software is simple in design and does not
require much training. It uses Python as a powerful
front-end tool and MySQL as an open-source RDBMS for
the back-end.

# 5. OBJECTIVE & SCOPE OF THE PROJECT
The primary objective is to develop a computerized
system to automate the security tracking functions of
an organization. The proposed system is expected to
perform the following functionalities:

Centralized Storage:

To maintain records of all computer assets and their
associated security risks (Vulnerabilities) in a
central server.

User-Friendly Interface: To provide a console-based
menu system that allows users to interact with the
database easily.

Reporting: To generate instant reports showing which
devices are vulnerable and require patching.

Scope & Limitations:

In its current scope, the software enables users to
retrieve and update information from the centralized
MySQL database.

It allows adding assets and reporting
vulnerabilities.

It generates a combined risk report.

Limitation: It currently relies on manual entry
of data rather than automated network scanning
(Future Scope).

# 6. THEORETICAL BACKGROUND
# 6 .1 What is a Database?
A database is a structured collection of information.
It is like an electronic filing system. A table is a
collection of data about a specific topic, organized
into columns (fields) and rows (records). A Primary
Key is a field that uniquely identifies each record,
while a Foreign Key is used to link two tables
together.

# 6 .2 What is MySQL?
MySQL is the most popular Open-Source Relational
Database Management System (RDBMS). It uses SQL
(Structured Query Language) to access and manipulate
data. It is fast, reliable, and easy to use. In this
project, MySQL serves as the "Back-end" where all
data is permanently stored.

# 6 .3 What is Python?
Python is a high-level, object-oriented language
known for its readability and efficiency. By taking
away complex memory management and enforcing clean
indentation, it allows developers to focus on logic
rather than syntax.

Modular Design : Python promotes organization through
modules and classes, allowing code to be broken down
into reusable components. This modularity, combined
with a vast standard library, ensures that even large
applications remain easy to manage and maintain
without unnecessary repetition.

Exception Handling : To ensure stability, Python
employs a robust try...except framework. Instead of
crashing when a runtime error occurs, the program
catches the issue and handles it gracefully. This
allows the application to provide helpful feedback or
recover automatically, preserving the user
experience.

Platform Independence : Python adheres to a "Write
Once, Run Anywhere" philosophy. Because it relies on
an interpreter rather than direct compilation, a
script written on Windows can execute seamlessly on
Linux or macOS without any need for modification or
recompilation.

# 7. PYTHON - MYSQL CONNECTIVITY
Connecting Python to MySQL

To bridge the gap between a Python application
(Front-end) and a MySQL database (Back-end), we
utilize the MySQL Connector module. This specific
driver handles the communication protocol, allowing
Python to "talk" directly to the database server.

Import Library : Before using the functionality, we
must include the library in the script using import
mysql.connector. This makes all the necessary classes
and functions available for use.

Establish Connection : We initiate the link using the
connect() method. To authenticate successfully, we
must pass the correct credentials, including the Host
(server address), User (username), Password , and the
specific Database Name we wish to access.

Create Cursor : Once the connection is open, we
create a Cursor object. This object acts as a
temporary workspace or "pointer" that allows the
Python script to prepare and send instructions to the
database environment.

Execute Commands : We use the cursor.execute() method
to run standard SQL queries. This function allows us
to retrieve data using commands like SELECT or modify
the database structure and records using INSERT,
UPDATE, or DELETE.

# 8. SYSTEM IMPLEMENTATION
# 8 .1 Hardware Requirement
Processor: Intel Core i3 (6th Gen or newer) or AMD
Ryzen 3 equivalent (64-bit architecture).

RAM: 4 GB Minimum; 8 GB Recommended (to run the
Database Server and Python simultaneously).

Hard Disk: 5 GB free space (required for XAMPP/MySQL
installation and project files).

Input Device: Standard Keyboard and Mouse.

# 8 .2 Software Requirement
Operating System: Windows 10 / 11 (64-bit).

Language: Python 3.10 or higher

Database: MySQL Community Server 8.0 or MariaDB 10.
(via XAMPP).

Required Library: mysql-connector-python driver.

Interface: Command Line Interface (CLI) or IDE
Terminal (e.g., VS Code).

# 9. SYSTEM DESIGN & DEVELOPMENT
# 9 .1 Database Design
The system uses two main tables:

assets: Stores device details.

Columns: asset_id (Primary Key), asset_name,
asset_type, ip_address, owner.

vulnerabilities: Stores security risks.

Columns: vuln_id (Primary Key), asset_id (Foreign
Key), cve_code, severity, status.

# 9 .2 Coding for System Design
A. SQL Script (Database Setup)
Execute this in MySQL to create the database.

CREATE DATABASE IF NOT EXISTS security_db;
USE security_db;

CREATE TABLE IF NOT EXISTS assets (
asset_id INT AUTO_INCREMENT PRIMARY KEY,
asset_name VARCHAR( 100 ) NOT NULL,
asset_type VARCHAR( 50 ),
ip_address VARCHAR( 20 ),
owner VARCHAR( 50 )
);

CREATE TABLE IF NOT EXISTS vulnerabilities (
vuln_id INT AUTO_INCREMENT PRIMARY KEY,
asset_id INT,
cve_code VARCHAR( 20 ) NOT NULL,
description VARCHAR( 255 ),
severity ENUM('Low', 'Medium', 'High', 'Critical') NOT NULL,
FOREIGN KEY (asset_id) REFERENCES assets(asset_id) ON DELETE CASCADE
);

B. Python Source Code (Main Program)
Save this code as
security and asset manager.py

# 10. USER MANUAL & OUTPUT
Install Python 3.x and a MySQL server (such as XAMPP)
on the system.

A. Initial Setup

These steps must be completed before the application
can run for the first time.

Install Database Connector: The Python
application requires a driver to communicate with
MySQL. Open your Command Line Interface (CLI) or
terminal and install the official connector:
pip install mysql-connector-python
Configure Database Credentials: update the
db_config dictionary with the actual credentials
(Host, User, Password, and Port) that correspond
to the local MySQL server installation.
Setup Database Structure: The application
requires specific tables to store data. Run the
SQL script to create this structure.
o Go to Section 9. 2 and copy the script.
o Execute the script using a tool like MySQL
Workbench or the phpMyAdmin interface
provided by XAMPP.
B. Application Execution

Follow these steps every time to run the application.

Start Database Server:
Open the database control panel (e.g., the XAMPP
Control Panel or MySQL Workbench). Ensure the
MySQL module is running and operational before
proceeding (sometimes windows might use up the
default ports , so gotta make sure MySQL starts,
if not go to the config file and change the port.
Run Application:
Launch the Python application from the command
prompt:
o Open the Command Prompt or terminal.
o Navigate to the folder containing
the primary execution file
(security and asset manager.py).
o Execute the application using the Python
interpreter
o The application should now connect to the
MySQL server and begin execution.
#Operation/output
Select Option 1 to register a new Device.

Select Option 2 to log a security flaw.

Select Option 3 to see a combined report of risks.
