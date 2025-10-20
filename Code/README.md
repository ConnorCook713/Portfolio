## Overview
- To better understand and utilize the concepts learned with the CySa+ certificate. I'm creating various scripts to learn about true Cybersecurity workflows such as automating threat intelligence, practice real-world Cybersecurity workflows, and system managment.

# STIX_PROD.py
- The MITRE STIX endpoint is queried for enterprise IOCs and threats. The data is collected, parsed, and written to a CSV.
- This data will later be uploaded to my Splunk home lab to enhance dashboards visibility.

# CSV_Compare.py
- CSV exports of Antivirus, Active Directory, and Remote Managment tools are compared. Outputs consist of CSV containing device similarity and differences between systems.
- AD_Query.ps1 -> A Powershell script used to query Active Directory for all ComputerNames and LastLogonDates. Devices are organized by LastLogonDate.

# Scapy Branch
- App.py creates a virtual environment to run a simple Flask web application that connects to an MySQL database using SQLAlchemy.
- The login pages checks if a user's inserted username and password are present in the database and forwards the user to the Scapy webpage interface.
- Once authenticated the user can use the Scapy library to sniff packets between two endpoints. The results are written to the database as well.
- This code will be hosted on my lab server and the database log will be integrated into Splunk.
