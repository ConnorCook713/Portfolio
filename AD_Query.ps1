Import-Module ActiveDirectory

Get-ADComputer -Filter "*" -Property Name, LastLogonDate |
Select-Object Name, LastLogonDate |
Sort-Object LastLogonDate -Descending