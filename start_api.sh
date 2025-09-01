#!/bin/bash
eng=podman
container=demo_api
img=demo_api
rebuild=yes

if [[ "$rebuild" == "yes" ]]; then
    "$eng" build -t "$img" ./api/
fi

"$eng" container stop "$container" || true
"$eng" container rm "$container" || true

"$eng" run --name "$container" -d -p 8080:80 "$img"