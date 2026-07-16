# Configure local Windows Server 2022 as an NTP server

# Set server as NTP type
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\W32Time\Parameters" -Name "Type" -Value "NTP"

# Set announce flags to make server reliable
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\W32Time\Config" -Name "AnnounceFlags" -Value 5

# Enable NTP Server
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\NtpServer" -Name "Enabled" -Value 1

# Enable NTP Client (optional but common for upstream sync)
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\NtpClient" -Name "Enabled" -Value 1

# Optional: Specify upstream NTP servers
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\W32Time\Parameters" -Name "NtpServer" -Value "0.pool.ntp.org,0x8 1.pool.ntp.org,0x8"

# Restart Windows Time service
Restart-Service w32time

# Update config and force resync
w32tm /config /update
w32tm /resync

Write-Output "Windows Server 2022 is now configured as an NTP server."
