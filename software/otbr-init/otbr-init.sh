#!/usr/bin/env bash 

wpanctl reset
wpanctl leave
wpanctl form OpenThread -T r
wpanctl dataset get-active
wpanctl set dataset:channel 25
wpanctl set dataset:panid 0xFACE
wpanctl set dataset:extendedpanid "DEAD00BEEF00CAFE"
wpanctl set dataset:masterkey "00112233445566778899aabbccddeeff"
wpanctl dataset set-active
wpanctl config-gateway -d fd11:22::

