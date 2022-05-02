rm -r ngrok-stable-linux-amd64.tgz
wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz
tar xf ngrok-stable-linux-amd64.tgz
./ngrok authtoken 1lyHSXmWALEpfefY2rJp5w2dkAg_4sJueHyGbpetK1vN3GD3h
./ngrok tcp -region=ap 10242
