#!/bin/bash
eng=podman
container=demo_db
img=demo_db
rebuild=yes
in_net=no

if [[ "$rebuild" == "yes" ]]; then
    "$eng" build -t "$img" ./db/
fi

"$eng" container stop "$container" || true
"$eng" container rm "$container" || true



if [[ "$in_net" == "yes" ]]; then
    "$eng" run -d --name "$container" --network app_net --ip 198.168.55.4 -v pgdata:/var/lib/postgresql/data "$img"
else
    "$eng" run -d --name "$container" -p 5432:5432 -v pgdata:/var/lib/postgresql/data "$img"
fi