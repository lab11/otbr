#!/usr/bin/env python3

import time 
import struct 
import subprocess
import asyncio
from aiocoap import *

COAP_SERVER = "coap://coap.permamote.com"
PARSE_ADDR = "lab11.github.io/thread-topology-monitor/gateway/"

GATEWAY_PACKET_VERSION = 2

device_id = ''
seq_no = 0 

with open('/etc/hostname', 'r') as f:
    device_id = bytes.fromhex(f.read().split('-')[-1].strip())

async def send_discovery(protocol):
    global seq_no
    t = time.time()
    t_sec = int(t)
    t_usec = int((t - t_sec) * 1E6)
    payload = bytes(PARSE_ADDR, 'utf-8')
    buf = struct.pack('<B%dsBIQLB%ds' % (len(device_id), len(payload)), len(device_id), device_id, GATEWAY_PACKET_VERSION, seq_no, t_sec, t_usec, len(payload), payload)
    seq_no += 1

    # Send discovery
    msg = Message(code=PUT, uri=COAP_SERVER + "/discovery", payload=buf)
    protocol.request(msg)
    #response = await protocol.request(msg).response
    #print(response)


async def main():
    global seq_no
    protocol = await Context.create_client_context()

    while(1):
        await send_discovery(protocol)

        # Get thread parameters
        #ext addr
        result = subprocess.run(['wpanctl', 'get', 'NCP:ExtendedAddress'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        ext_addr = bytes.fromhex(result.split('=')[-1].strip()[1:-1])
        print("ext_addr: ", ext_addr, ext_addr.hex())
        #rloc16
        result = subprocess.run(['wpanctl', 'get', 'Thread:Rloc16'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        rloc16 = int(result.split('=')[-1].strip(), 16)
        print("rloc16: ", rloc16, hex(rloc16))
        #router id
        result = subprocess.run(['wpanctl', 'get', 'Thread:RouterID'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        router_id = int(result.split('=')[-1].strip(), 16)
        print("router_id: ", router_id, hex(router_id))

        t = time.time()
        t_sec = int(t)
        t_usec = int((t - t_sec) * 1E6)
        payload = bytes(PARSE_ADDR, 'utf-8')
        buf = struct.pack('<B%dsBIQL%dsHBB' % (len(device_id), len(ext_addr)), len(device_id), device_id, GATEWAY_PACKET_VERSION, seq_no, t_sec, t_usec, ext_addr,rloc16,router_id, 1)
        seq_no += 1
        msg = Message(code=PUT, uri=COAP_SERVER + "/self_router_info", payload=buf)
        protocol.request(msg)

        await asyncio.sleep(60) 

run = asyncio.get_event_loop().run_until_complete
run(main())
