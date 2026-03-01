# Workshop Docker for StudieVereniging Promptus Imperii

TODO; TEST everything :)

Here are some commands as used during the workshop.

For more information, check Docker Cli reference page: https://docs.docker.com/reference/cli/docker/

## Build a simple Debian container

In the '02-building' 

Build an image
```
docker build -f dockerfile -t debian13-slim .
```

Run a bash shell in the container:

```
docker run -it debian13-slim /bin/bash
```

Exit the container:
```
exit
```

## A simple webserver

In the '03-network' directory.

This command will start a NginX webserver, reachable via http://localhost:8380

```
docker run -d --name web -p 8380:80 -v ./:/usr/share/nginx/html:ro nginx:alpine
```

## Use volumes i.s.o. copying files into the image

In the '04-volumes' directory.

TODO:

## Rust development (build)

In the '05-compilation' folder.
```
docker build -t rust-dev .
```

Run a Rust build on a given project.
```
docker run --volume ./my-rust-app/hello-world:/workdir -t rust-dev
```

# Communication between containers

## Create docker "internal" network "my-net"

```
docker network create my-net
```

## Run a simple nginx webserver and a bash shell and check their communication

add the network to connect to via '--network' 
```
docker run -d --name web --network my-net nginx:alpine
```

```
docker build -f dockerfiles/dockerfile_debian13-networktools -t debian13-network .
```

```
docker run -it --network my-net debian13-network /bin/bash
```

Check the connection between "debian13-network" and the Nginx webserver (from within the "bash" shell):
```
ping web
```

## Running and automatically removing a container

Use '--rm' like:

```
docker run --rm -it --network my-net debian13-network /bin/bash
```

This will remove the container after it's finished running.


