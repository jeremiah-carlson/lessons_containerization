#!/bin/bash
eng=podman
container=demo_web
img=demo_web
rebuild=yes

if [[ "$rebuild" == "yes" ]]; then
    "$eng" build -t "$img" ./web/
fi

"$eng" container stop "$container" || true
"$eng" container rm "$container" || true

"$eng" run -d --name "$container" -p 80:80 "$img"