## Overview
- To better understand and utilize the concepts learned with the CySa+ certificate. I'm creating various scripts to learn about true Cybersecurity workflows such as automating threat intelligence, practice real-world Cybersecurity workflows, and system managment.

# STIX_PROD.py
- The MITRE STIX endpoint is queried for enterprise IOCs and threats. The data is collected, parsed, and written to a CSV.
- This data will later be uploaded to my Splunk home lab to enhance dashboards visibility.

# CSV_Compare.py
- CSV exports of Antivirus, Active Directory, and Remote Managment tools are compared. Outputs consist of CSV containing device similarity and differences between systems.
- AD_Query.ps1 -> A Powershell script used to query Active Directory for all ComputerNames and LastLogonDates. Devices are organized by LastLogonDate.
