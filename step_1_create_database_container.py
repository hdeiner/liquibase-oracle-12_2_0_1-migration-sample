#!/usr/bin/env python
import os
import subprocess
import time

os.system('figlet -w 160 -f standard "Create Oracle Container"')
os.system('docker-compose -f dockercompose-oracle-database.yml up -d')

print("waiting for Oracle to start")
ready = False
while not ready:
    process = subprocess.Popen(["docker","ps"], stdout=subprocess.PIPE)
    while True:
        line = process.stdout.readline()
        if not line:
            break
        ready = "(healthy)" in line.decode('utf-8') and "oracle" in line.decode('utf-8')
        time.sleep(1)