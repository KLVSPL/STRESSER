import requests
import threading
import socks
import time
import os
import sys
nums = 0
out_file = "proxy.txt"
f = open(out_file,'wb')
socks4_api = [
	"https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=2000&country=all",
    "https://multiproxy.org/txt_all/proxy.txt",
    "https://api.openproxylist.xyz/http.txt",
    "https://www.proxyscan.io/download?type=http",
]
for api in socks4_api:
	try:
		r = requests.get(api,timeout=5)
		f.write(r.content)
	except:
		pass
f.close()
proxies = open(out_file).readlines()
def checking(lines,proxy_type,ms,rlock,):#Proxy checker coded by Leeon123
	global nums
	global proxies
	proxy = lines.strip().split(":")
	if len(proxy) != 2:
		rlock.acquire()
		proxies.remove(lines)
		rlock.release()
		return
	err = 0
	while True:
		if err >= 3:
			rlock.acquire()
			proxies.remove(lines)
			rlock.release()
			break
		try:
			s = socks.socksocket()
			s.set_proxy(socks.HTTP, str(proxy[0]), int(proxy[1]))
			s.settimeout(ms)
			s.connect(("1.1.1.1", 80))
			'''
			if protocol == "https":
				ctx = ssl.SSLContext()
				s = ctx.wrap_socket(s,server_hostname=target)'''
			sent = s.send(str.encode("GET / HTTP/1.1\r\n\r\n"))
			if not sent:
				err += 1
			s.close()
			break
		except:
			err +=1
	nums += 1

def check_socks(ms):#Coded by Leeon123
	global nums
	thread_list=[]
	rlock = threading.RLock()
	for lines in list(proxies):
		th = threading.Thread(target=checking,args=(lines,0,ms,rlock,))
		th.start()
		thread_list.append(th)
		time.sleep(0.01)
		sys.stdout.write("> Checked "+str(nums)+" proxies\r")
		sys.stdout.flush()
	for th in list(thread_list):
		th.join()
		sys.stdout.write("> Checked "+str(nums)+" proxies\r")
		sys.stdout.flush()
	print("\r\n> Checked all proxies, Total Worked:"+str(len(proxies)))
	#ans = input("> Do u want to save them in a file? (y/n, default=y)")
	#if ans == "y" or ans == "":
	with open(out_file, 'wb') as fp:
		for lines in list(proxies):
			fp.write(bytes(lines,encoding='utf8'))
		fp.close()
	print("> They are saved in "+out_file)

check_socks(3)
