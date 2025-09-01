#!/bin/bash

docker network create -d bridge --subnet 198.168.55.0/24 --dns 1.1.1.1 --dns 8.8.8.8 app_net