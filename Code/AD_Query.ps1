Import-Module ActiveDirectory

# Set the folder path here
$Output_Path = "C:\Your\Folder\Path\lastlogondate.csv"

Get-ADComputer -Filter "*" -Property Name, LastLogonDate |
Select-Object Name, LastLogonDate |
Sort-Object LastLogonDate -Descending | 
Export-Csv -Path $Output_Path -NoTypeInformation

