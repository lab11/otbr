#!/usr/bin/env python3

import os
import time
import subprocess
import numpy as np
import pandas as pd

rssi_readings = []

t_start = time.time()

while True:
    result = subprocess.run(['docker', 'exec', '-i', 'docker_otbr_1', 'ot-ctl', 'scan', 'energy', '10'], capture_output=True)
    t = time.time()
    array = result.stdout.decode('utf-8').strip().split('\r\n')
    array = [x.replace('|', '') for x in array]
    array = [x.strip() for x in array][2:-1]
    array = [[int(y) for y in x.split()] for x in array]
    array = np.array(array)

    d = {"time": t}
    for i in range(array.shape[0]):
        d[array[i,0]] = array[i,1]

    rssi_readings.append(d)
    if (t - t_start >= 60):
        t_start = t
        df = pd.DataFrame(rssi_readings).set_index('time')
        df.to_csv("rssi_log.csv")

    time.sleep(10)
