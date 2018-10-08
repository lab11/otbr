#!/usr/bin/env bash

raspi-config --expand-rootfs
systemctl disable otbr-resize
reboot
