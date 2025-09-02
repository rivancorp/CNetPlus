Install-WindowsFeature  -name Web-Server  -includeManagementTools
New-Website -name "ngcpM.ph" -hostheader "www.ngcpM.ph" -physicalpath "d:\webs\datingbiz"