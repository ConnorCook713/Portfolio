## Initial Setup

# VMware and VMs
- VMware installed with bridged networking.
- Host: Windows Server 2021 (Splunk Enterprise)
- Clients: Windows 10 VM and 11 Windows 11 workstations

# Splunk Enterprise (Server)
- Ports allowed in Windows Firewall:
  - 8000 → Splunk Web Interface
  - 9997 → Receive logs from forwarders

# Splunk Universal Forwarders (Clients)
- Forwarders installed on Windows 10 VM and 11 Windows 11 workstations
- Outbound rules allowed to 8000 and 9997
- Security and System logs sent to `wineventlog` index
