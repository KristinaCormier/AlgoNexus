# AlgoNexus
Algorithmic Trade Project Using Digital Research Alliance of Canada Resources (Fir + PostgreSQL)

### Overview

This project focuses on the database administration and data management components of an Algorithmic Trading system. The primary objective is to design, deploy, and manage a PostgreSQL database hosted on the Digital Research Alliance of Canada (DRAC) infrastructure, specifically on the Fir server. The database supports secure storage, retrieval, and processing of financial market data required for algorithmic trading workflows.

### Objectives

Provision and configure DRAC resources for database hosting.
Set up secure authentication (SSH keys and MFA).
Deploy a PostgreSQL database on the Fir compute environment.
Administer the database using pgAdmin.
Support data ingestion and retrieval processes for algorithmic trading algorithms.

### DRAC Setup and Configuration Steps

1. Create and Activate DRAC Account
Register for a DRAC account.
Accept the project sponsorship invitation to gain access to computing resources.

2. Configure Security Requirements
Generate an SSH key pair for connecting to Fir.
Enable and set up Multi-Factor Authentication (MFA) to secure the DRAC account.

3. Request Resource Access
Submit a request to enable necessary project resources on DRAC.
Email DRAC support to request the provisioning of a PostgreSQL database on the Fir server.

4. Database Provisioning
Wait for confirmation from DRAC regarding the creation of your database (e.g., your_db) on the Fir environment.
pgAdmin Configuration

### Once the database is provisioned:

Open pgAdmin.
Create a Server Group for organizational purposes.
Add a new Server and enter:
Host, port, and maintenance DB information provided by DRAC
Username and password
SSH tunnel configuration 

This allows secure access to your PostgreSQL instance on Fir.

### Technologies Used

PostgreSQL – core database engine
pgAdmin – database management tool
DRAC Fir Compute Server – hosting environment
Linux Shell / SSH – secure remote access
GitHub – version control and collaboration

### Use Cases

Storing historical market data
Managing datasets for model training and backtesting
Supporting data retrieval APIs for trading algorithms
Logging, auditing, and maintaining data integrity

### Future Enhancements

Automate data ingestion pipelines
Deploy real-time streaming via Kafka or similar tools
Implement database scaling and load balancing strategies
Add monitoring dashboards for Fir resource usage
