#!/bin/bash
eng=podman
container=demo_web
img=demo_web
rebuild=yes
in_net=no

if [[ "$rebuild" == "yes" ]]; then
    "$eng" build -t "$img" ./web/
fi

"$eng" container stop "$container" || true
"$eng" container rm "$container" || true



if [[ "$in_net" == "yes" ]]; then
    "$eng" run -d --name "$container" --network app_net --ip 198.168.55.2 -p 80:80 "$img"
else
    "$eng" run -d --name "$container" -p 80:80 "$img"
fi
