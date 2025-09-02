import telnetlib
import json

with open('autowifi.json') as f:
    data = json.load(f)

for entry in data['aironet']:
    host_ip = entry['host_ip']
    username = entry['username']
    password = entry['password']
    hostname = entry['hostname']
    ssid = entry['ssid']
    authen = entry['authentication']
    keyman = entry['key-man']
    wifipass = entry['wifi-pass']
    channel = entry['channel']
    encmod = entry['enc-mod']             

    tn = telnetlib.Telnet(host_ip)
    
    #b is a bytes literal as string.encode("ascii") calls are converting#
    # str to bytes so that they can be added to bytes literal because telnet
    # ascii byes to be send and received
    # username admin privilege 15 secret password
    tn.read_until(b"Username: ")
    tn.write(username.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    # tn.write(b"enable\n")
    # tn.write(b"pass\n")
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

    tn.write(b"end\n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))
    tn.close()

f.close()
