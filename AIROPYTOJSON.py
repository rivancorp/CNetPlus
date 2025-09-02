import json
import telnetlib

# read the JSON configuration file
with open('importv1.json', 'r') as f:
    config = json.load(f)

# extract the configuration parameters
host_ip = aironet['host_ip']
username = entry['username']
password = entry['password']
hostname = entry['hostname']
ssid = entry['ssid']
authen = entry['authentication']
keyman = entry['key-man']
wifipass = entry['wifi-pass']
channel = entry['channel']
encmod = entry['enc-mod']       

# connect to the router using telnetlib
tn = telnetlib.Telnet(host)
tn.read_until(b"Username: ")
tn.write(username.encode('ascii') + b"\n")
tn.read_until(b"Password: ")
tn.write(password.encode('ascii') + b"\n")
tn.write(b"enable\n")
tn.read_until(b"Password: ")
tn.write(enable_password.encode('ascii') + b"\n")

# enter configuration mode and configure the interface
tn.write(b"conf t\n")
tn.write(b"hostname " + hostname.encode('ascii') + b"\n")
tn.write(b"Dot11 ssid " + ssid.encode('ascii') + b"\n")
tn.write(b"authentication " + authen.encode('ascii') + b"\n")
tn.write(b"authentication key-management " + keyman.encode('ascii') + b"\n")
tn.write(b"wpa-psk ascii " + wifipass.encode('ascii') + b"\n")
tn.write(b"guest-mode " + b"\n")

tn.write(b"Default Int Dot11Radio 0" + b"\n")
tn.write(b"Int Dot11Radio 0" + b"\n")
tn.write(b"Channel " + channel.encode('ascii') + b"\n")
tn.write(b"no shut\n")
tn.write(b"encryption mode ciphers " + encmod.encode('ascii') + b"\n")
tn.write(b"ssid " + ssid.encode('ascii') + b"\n")
tn.write(b"exit\n")

# exit configuration mode and exit telnet session
tn.write(b"end\n")
tn.write(b"exit\n")
#print(tn.read_all().decode('ascii'))
print(tn.read_all().decode('ascii'))
tn.close()
