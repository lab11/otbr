#!/usr/bin/env bash
ot-ctl reset&
sleep 1
killall ot-ctl
ot-ctl channel 25&
sleep 1 
killall ot-ctl
ot-ctl masterkey 00112233445566778899aabbccddeeff&
sleep 1 
killall ot-ctl
ot-ctl panid 0xface&
sleep 1 
killall ot-ctl
ot-ctl extpanid 1111111122222222&
sleep 1 
killall ot-ctl
ot-ctl ifconfig up&
sleep 1
killall ot-ctl
ot-ctl thread start&
sleep 1
killall ot-ctl
ot-ctl prefix add fd11:22::/64 pasor&
sleep 1
killall ot-ctl&
ot-ctl netdataregister
