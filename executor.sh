#!/bin/bash

echo "Starting webserver"
python3 webserver.py &
echo "Starting websocketserver"
python3 websocketserver.py &
