import requests
out_file = "proxy.txt"
f = open(out_file,'wb')
socks4_api = [
	"https://api.proxyscrape.com/?request=displayproxies&proxytype=socks4&timeout=550&country=all",
]
for api in socks4_api:
	try:
		r = requests.get(api,timeout=5)
		f.write(r.content)
	except:
		pass
f.close()
