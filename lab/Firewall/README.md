
### **Overview**

This lab demonstrates FortiGate firewall configuration for secure VPN access, traffic filtering, and centralized log forwarding to Splunk Enterprise.
It simulates a small network where VPN users connect remotely, and all activity is logged for monitoring and analysis.

---

### **Lab Setup**

* **Firewall:** FortiGate connected to a FortiSwitch, which connects to the internal server and clients.
* **VPN:** Full-tunnel SSL VPN configured; only users in the designated VPN group can connect. LDAP authentication integrated with the Domain Controller; 2FA enforced via FortiToken or SMS.
* **Security Profiles:**

  * Intrusion Prevention (IPS)
  * Antivirus (AV)
  * Web Filtering
  * DNS Filtering
  * Data Loss Prevention (DLP)
  * SSL inspection enabled
* **Access Control:** Only VPN traffic is allowed to the internal server subnet. Traffic from GEO_BLOCK countries is denied.

---

### **Logging**

* Logs are forwarded to Splunk Enterprise via Syslog.
* Splunk indexes the logs under `fortigate` and visualizes VPN login activity, blocked connections, and security events.
* Provides visibility into VPN usage and potential security threats.

---

### **Purpose**

* Centralize firewall logging for monitoring VPN and network activity.
* Visualize blocked connections and authentication events in Splunk dashboards.
* Document firewall configuration and analyze traffic/security events in a lab environment.
