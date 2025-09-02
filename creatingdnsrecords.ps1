#creating all important zones:
add-DnsServerResourceRecord -zonename ngcp12.com -A -name ns -ipv4address 10.12.1.10
add-DnsServerResourceRecord -zonename ngcp12.com -A -name "." -ipv4address 10.12.1.10
#
add-DnsServerResourceRecord -zonename ngcp12.com -Cname -name www -hostname ns.ngcp12.com
add-DnsServerResourceRecord -zonename ngcp12.com -Cname -name pop -hostname ns.ngcp12.com
add-DnsServerResourceRecord -zonename ngcp12.com -Cname -name imap -hostname ns.ngcp12.com
add-DnsServerResourceRecord -zonename ngcp12.com -Cname -name smtp -hostname ns.ngcp12.com
#
Add-DnsServerResourceRecordMX -Preference 10  -Name "." -MailExchange "ns.ngcp12.com" -ZoneName "ngcp12.com"