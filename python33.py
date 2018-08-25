import getpass
import telnetlib

HOST = "172.16.1.30"
user = input("Enter your telnet username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    tn.read_until(b"Password: ")
    tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")

for vlan in range(2,10):
    tn.write(b"vlan " + str(vlan).encode('ascii') + b"\n")
    tn.write(b"name PYTHON_VLAN_" + str(vlan).encode('ascii') + b"\n")

tn.write(b"end\n")
tn.write(b"wr\n")
tn.write(b"exit\n")

print(tn.read_all().decode('ascii'))