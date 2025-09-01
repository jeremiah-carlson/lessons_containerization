#!/bin/bash
eng=podman
container=demo_db
img=demo_db
rebuild=yes

if [[ "$rebuild" == "yes" ]]; then
    "$eng" build -t "$img" ./db/
fi

"$eng" container stop "$container" || true
"$eng" container rm "$container" || true

"$eng" run -d --name "$container" -p 5432:5432 -v pgdata:/var/lib/postgresql/data "$img"