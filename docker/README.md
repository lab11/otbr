OTBR Docker image with Docker Compose
====================================

This setups up a border router using the otbr docker image and docker compose.

## Dependencies

To use this you need to install docker and docker compose

```shell
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker pi
sudo apt-get install -y libffi-dev libssl-dev
sudo apt-get install -y python3 python3-pip
sudo apt-get remove python-configparser
sudo pip3 -v install docker-compose
```

## Configure

You should set the values after the ot-ctl commands at the end of docker_entrypoint.sh
to configure your border router.

## Setup the PI

*Make sure that there are no other border router services running*

```shell
sudo systemctl disable wpantund
sudo systemctl stop wpantund
sudo systemctl disable otbr-web
sudo systemctl stop otbr-web
sudo systemctl disable tayga
sudo systemctl stop tayga
sudo systemctl disable ncp_state_notifier
sudo systemctl stop ncp_state_notifier
```

## Run with command

```shell
docker-compose up
```

## Run with systemd

```shell
sudo cp border-router-docker-compose.service /etc/systemd/system/.
sudo systemctl enable border-router-docker-compose
sudo systemctl start border-router-docker-compose
```
