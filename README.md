otbr: OpenThread Border Router
==============================

<img src="media/border_router_iso.jpg" alt="BorderRouter"  align="right" width="50%">

Lab11's specific Border Router build and related software and services. The
most recent Raspberry Pi border router images are hosted
[here](https://drive.google.com/drive/folders/1PPWXb8jNRH-0Om33MEdCzh-wI4fYrNA-?usp=sharing),
based on OpenThread's [reference
implementation](https://github.com/openthread/openthread).

## Assembling a Border Router

What you need: A Rasbperry Pi 3 B+ and a Nordic NRF52840 Dongle. The Raspberry
Pi acts as an IPv6 forwarder, while the NCP acts as a bridge between the Thread
network and the Pi forwarder.

You will also need to install nrfutil:
```
pip3 install nrfutil
```

### Prepare the Border Router
Grab the most recent image hosted
[here](https://drive.google.com/drive/folders/1PPWXb8jNRH-0Om33MEdCzh-wI4fYrNA-?usp=sharing).
Flash this image to a micro-sd card according to the normal [RPi
directions](https://www.raspberrypi.org/documentation/installation/installing-images/).

Each Border Router has a unique ID that defines its MAC address and hostname.
This ID resembles `C0:98:E5:C1:XX:XX`, and the derived hostname is
`tb-c098e5c1xxxx`.  Modify the `/etc/hosts`, `/etc/hostname`, and
`/boot/cmdline.txt` files to reflect the hostname and MAC address of your
chosen ID.

For example, modify the following lines to reflect your ID:
#### `/etc/hostname`:
```
tb-c098e5c10001
```
#### `/etc/hosts`:
```
127.0.1.1	tb-c098e5c10001
```
#### `/boot/cmdline.txt`:
```
smsc95xx.macaddr=c0:98:e5:c1:00:01
```
Make sure that you add no extra newlines in `/boot/cmdline.txt`, and it just consists of one line.

### Prepare the Network Co-Processor (NCP)
Navigate to the openthread submodule. Bootstrap your system, the repo, and build the NCP firmware:
```
cd openthread/
./scripts/bootstrap
./bootstrap
make -f examples/Makefile-nrf52840 COMMISSIONER=1 JOINER=1 COAP=1 DNS_CLIENT=1 MTD_NETDIAG=1 BORDER_ROUTER=1 MAC_FILTER=1 UDP_PROXY=1 USB=1 BOOTLOADER=1 DHCP6_SERVER=1 DHCP6_CLIENT=1 DNS_SERVER=1
```

Plug in the dongle, and press the reset button. This puts the dongle into the
bootloader.
Run the `ncp/flash.sh` script to program the dongle with NCP firmware:
```
cd ncp/
./flash.sh
```

Plug the programmed NCP into any USB port on the Border Router. Plug the Border
Router into power, connect it to a network, and wait a few minutes. If your
computer is on the same local network as the Border Router, you should now be
able to SSH into the Border Router using the MDNS `.local` hostname:
```
ssh pi@tb-c098e5c1XXXX.local
```
Where `XXXX` is the ID specific to your Border Router.
The default password for the `pi` user on our image is `lab11otbr!`.

After successfully logging into your new Border Router, while optional, it is
good practice to **change the password**. Better yet, [disable SSH password
access](https://stackoverflow.com/questions/20898384/ssh-disable-password-authentication)
and [generate and install your public key](https://serverfault.com/questions/2429/how-do-you-setup-ssh-to-authenticate-using-keys-instead-of-a-username-password)
on the Border Router.
