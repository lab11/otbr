#!/usr/bin/env python3

import os
import time
import subprocess

t_start = time.time()

while True:
    result = subprocess.run(['docker', 'exec', '-i', 'docker_otbr_1', 'ot-ctl', 'state'], capture_output=True)
    state = result.stdout.decode('utf-8').strip().split("\r\n")[0]
    print("Current otbr state: ", state)
    result = subprocess.run(['docker', 'exec', '-i', 'docker_otbr_1', 'ot-ctl', 'dataset'], capture_output=True)
    dataset = "\n\t".join(result.stdout.decode('utf-8').strip().split("\r\n"))
    print("Current otbr dataset: \n", dataset)

    if not any(x in state for x in ["leader", "router"]):
        subprocess.run(['systemctl', 'restart', 'border-router-docker-compose.service'])

    time.sleep(60)
