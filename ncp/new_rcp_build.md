Building newer versions of the RCP
==================================

To use the latest otbr docker image you must use a version of the RCP that is more up
to date than the version built in this repository. To build the newer version:

1) Clone the new repo

```
git clone https://github.com/openthread/ot-nrf528xx
```

2) Build the RCP firmware

```
cd ot-nrf528xx
./script/bootstrap
./script/build nrf52840 USB_trans -DOT_BOOTLOADER=USB
```

3) Copy and package the output

```
cd ..
cp -r ot-nrf528xx/build/bin/ot-rcp build/
arm-none-eabi-objcopy -O ihex build/ot-rcp build/ot-rcp.hex
nrfutil pkg generate --hw-version 52 --sd-req 0x0 --application-version 1 --application build/ot-rcp.hex build/out.zip
```

4) Flash like normal

```
./flash.sh
```
