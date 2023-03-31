import socket
import ipaddress

def scan_ports(target_ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        address = (str(target_ip), port)
        result = sock.connect_ex(address)
        if result == 0:
            print(f"Port {port}: OPEN")
        sock.close()
ip_range = ipaddress.ip_network("192.168.1.0/24")
try:
    for ip in ip_range.hosts():
        print(f"Scanning {ip}")
        scan_ports(ip, 50, 85)
except KeyboardInterrupt:
    print("\nExiting...")






