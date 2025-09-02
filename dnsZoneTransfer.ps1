Start-DnsServerZoneTransfer -name "ngcp12.ph" -FullTransfer
#Add-DnsServerSecondaryZone -name "ngcpK.ph" -ZoneFile "ngcpK.ph.dns" -MasterServers 10.k.1.10