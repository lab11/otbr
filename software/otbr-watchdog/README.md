Openthread Watchdog
======================

### To install and start as a service:

Copy service to systemd and enable:

```
sudo cp otbr-watchdog.service /etc/systemd/system/.
sudo systemctl daemon-reload
sudo systemctl enable otbr-watchdog.service
sudo systemctl start  otbr-watchdog.service
```
