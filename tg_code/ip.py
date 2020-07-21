# @pythonamazing(Telegram)
import socket
# получить hostname 
hostname = socket.gethostname()
# получить IP address
ip_address = socket.gethostbyname(hostname)
# Принтить hostname и ip_address
print(f"Hostname: {hostname}")
print(f"IP Address: {ip_address}")