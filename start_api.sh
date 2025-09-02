#!/bin/bash
eng=podman
container=demo_api
img=demo_api
rebuild=yes
in_net=no

if [[ "$rebuild" == "yes" ]]; then
    "$eng" build -t "$img" ./api/
fi



"$eng" container stop "$container" || true
"$eng" container rm "$container" || true

if [[ "$in_net" == "yes" ]]; then
    "$eng" run --name "$container" -d --network app_net --ip 198.168.55.3 "$img"
else
    "$eng" run --name "$container" -d -p 8080:80 "$img"
fi