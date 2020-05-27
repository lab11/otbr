#!/usr/bin/env bash
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  nrfutil dfu usb-serial -pkg build/out.zip -p /dev/ttyACM0 -b 115200
elif [[ "$OSTYPE" == "darwin"* ]]; then
  nrfutil dfu usb-serial -pkg build/out.zip -p /dev/tty.usb* -b 115200
else
  echo "Unsupported OS"
fi
