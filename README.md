# Workshop Docker for StudieVereniging Promptus Imperii

Here are some commands as used during the workshop.

For more information, check

- Docker Cli reference page: https://docs.docker.com/reference/cli/docker/
- Docker Compose: https://docs.docker.com/compose/


## Check your Docker Desktop installation

```
docker run hello-world
```

Note: `docker run` is an alias for `docker container run`.

Check Docker Desktop, page: Images.

```
docker run -it debian:12-slim /bin/bash
```

Check Docker Desktop, page: Images, Containers

Quit the 'bash' terminal.


## Build a simple Debian container

In the '02-building' 

```
docker build -f dockerfile .
```

Check Docker Desktop, page: Images. (And/Or `docker image ls`)

Build an image with a name.
```
docker build -f dockerfile -t my-first-image .
```
Check Docker Desktop, page: Images. (And/Or `docker image ls`)

Build an image with a name and tag.
```
docker build -f dockerfile -t my-first-image:1.0 .
```
Check Docker Desktop, page: Images. (And/Or `docker image ls`)

Run a bash shell in the container:

```
docker run -it my-first-image /bin/bash
```

Exit the container:
```
exit
```

### Data in a container

```
docker run -it --name my-first-container my-first-image /bin/bash
```

Make some changes to files in the container and exit.

Restart the container
```
docker start -i my-first-container
```

## A simple webserver

In the '03-webserver' directory.

Build the image.

```
docker build -f dockerfile -t 03-webserver-demo .
```

Run the image.

```
docker run -t 03-webserver-demo
```

Check if you can reach the webserver. (Start a webbrowser and connect to http://localhost:8000)


## Use volumes i.s.o. copying files into the image

In the '04-volumes' directory.

Build and run the image.

```
docker build -f dockerfile -t 04-webserver-demo .
```

To re-use this image at a later stage, tag the image:
```
docker tag 04-webserver-demo 04-webserver-demo:1.0
```

## Rust development (build)

In the '05-compilation' folder.
```
docker build -t rust-dev .
```

Run a Rust build on a given project.
```
docker run --volume ./hello-world:/workdir -t rust-dev
```

Run the rust program

```
```

## Multi stage

In the '06-multistage' directory.

Build the large image:
```
docker build -t calculator-large -f dockerfile-large .
```

Check the size of the image:
```
docker images | grep calculator
```

Build the multi-stage image(s):
```
docker build -t calculator-multi -f dockerfile-multi .
```

## Docker Compose

In directory '07-compse':

```
docker-compose up
```

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
docker build -f dockerfiles/dockerfile_debian-networktools -t debian-network .
```

```
docker run -it --network my-net debian-network /bin/bash
```

Check the connection between "debian-network" and the Nginx webserver (from within the "bash" shell):
```
ping web
```

## Running and automatically removing a container

Use '--rm' like:

```
docker run --rm -it --network my-net debian-network /bin/bash
```

This will remove the container after it's finished running.


## Clean-up

```
docker system df
```

```
docker image prune
```

```
docker system prune
```
