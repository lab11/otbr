#!/bin/bash

docker exec -i docker_otbr_1 ot-ctl thread stop
docker exec -i docker_otbr_1 ot-ctl ifconfig down
docker-compose down
