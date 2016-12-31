#!/bin/bash
dir=$(cd -P -- "$(dirname -- "$0")" && pwd -P)

kill $(ps aux | grep  pump_control.py| grep python | awk '{ print $1 }')
nohup python pump_control.py > /dev/null 2>&1 &


