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


