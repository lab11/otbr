#!/usr/bin/env bash

cd ../openthread
make -f examples/Makefile-nrf52840 COMMISSIONER=1 JOINER=1 COAP=1 DNS_CLIENT=1 MTD_NETDIAG=1 BORDER_ROUTER=1 MAC_FILTER=1 TMF_PROXY=1 DHCP6_SERVER=1 DHCP6_CLIENT=1 DISABLE_SPI=1 SNTP_CLIENT=1 DISABLE_BUILTIN_MBEDTLS=1 USB=1 BOOTLOADER=USB
cd -
cp -r ../openthread/build/nrf52840/examples/apps/ncp/ot-rcp build/
arm-none-eabi-objcopy -O ihex build/ot-rcp build/ot-rcp.hex
nrfutil pkg generate --hw-version 52 --sd-req 0x0 --application-version 1 --application build/ot-rcp.hex build/out.zip

