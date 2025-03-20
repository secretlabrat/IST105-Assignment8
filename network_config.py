import ipaddress
import random
import re
import sys


_, mac, ip_version = sys.argv

mac_regex = re.compile(r"^([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}$")

html = "<html>\n<head>\n<title>\nAssignment 8\n</title>\n</head>\n<body>\n"
if not mac_regex.match(mac):
    html += (
        "<p style='color:red'>Mac Adress is invalid</p>\n<a href='/form.php'>Back</a>\n"
    )
else:
    if ip_version == "4":
        network = "192.168.1.0/24"
        ipv4_network = ipaddress.IPv4Network(network)
        usable_ip = list(ipv4_network.hosts())[1:]
        ip = random.choice(usable_ip)
    elif ip_version == "6":
        prefix = "2001:db8:100::/64"
        eui64 = re.sub(r"[.:-]", "", mac).lower()
        eui64 = eui64[0:6] + "FFFE" + eui64[6:]
        eui64 = hex(int(eui64[0:2], 16) ^ 2)[2:].zfill(2) + eui64[2:]
        eui64 = int("0x{0}".format(eui64), 16)
        ipv6_network = ipaddress.IPv6Network(prefix, strict=False)
        ip = ipaddress.IPv6Address(ipv6_network.network_address + eui64)
    html += "<p>mac_address: {}</p>\n<p>assigned_ipv{}: {}</p>\n<p>lease_time: 3600 seconds</p>\n".format(
        mac, ip_version, ip
    )
html += "</body>\n</html>"

print(html)
