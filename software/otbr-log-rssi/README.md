Openthread RSSI Logger
======================

### To run:

```
./otbr-log-rssi.py
```

This will generate `rssi_log.csv`, and log measurements every 10 seconds.

### To install and start as a service:

Copy service to systemd and enable:

```
sudo cp otbr-log-rssi.service /etc/systemd/system/.
sudo systemctl daemon-reload
sudo systemctl enable otbr-log-rssi.service
sudo systemctl start otbr-log-rssi.service
```
