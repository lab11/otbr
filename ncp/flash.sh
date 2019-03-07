#!/usr/bin/env bash

cp -r ../openthread/build/nrf52840/examples/apps/ncp/* .
arm-none-eabi-objcopy -O ihex ot-ncp-ftd ot-ncp-ftd.hex
nrfutil pkg generate --hw-version 52 --sd-req 0x0 --application-version 1 --application ot-ncp-ftd.hex out.zip
#until nrfutil dfu usb-serial -pkg out.zip -p /dev/ttyACM0 -b 115200; do sleep 1; done;
nrfutil dfu usb-serial -pkg out.zip -p /dev/ttyACM0 -b 115200
