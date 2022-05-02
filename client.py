import socket
import time
#server_ip = "0.tcp.ap.ngrok.io"
#server_port = int(input("Enter Server Port:"))
SERVER_IP = "127.0.0.1"
SERVER_PORT = 10242
ADDR = (SERVER_IP, SERVER_PORT)
SIZE = 1024
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDR))
hostname = s.recv(SIZE).decode(FORMAT)
ip = str(hostname)
s.close()
while True:
    print(ip)
    time.sleep(1)