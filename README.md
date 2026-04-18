# Workshop Docker for StudieVereniging Promptus Imperii

Here are some commands as used during the workshop.

For more information, check

- Docker Cli reference page: <https://docs.docker.com/reference/cli/docker/>
- Docker Compose: <https://docs.docker.com/compose/>

## Check your Docker Desktop installation

```bash
docker run hello-world
```

Note: `docker run` is an alias for `docker container run`.

Check Docker Desktop, page: Images.

```bash
docker run -it debian:12-slim /bin/bash
```

Check Docker Desktop, page: Images, Containers

Quit the 'bash' terminal.

## Build a simple Debian container

In the '02-building' directory:

```bash
docker build -f dockerfile .
```

Check Docker Desktop, page: Images. (And/Or `docker image ls`)

Build an image with a name.

```bash
docker build -f dockerfile -t my-first-image .
```

Check Docker Desktop, page: Images. (And/Or `docker image ls`)

Build an image with a name and tag.

```bash
docker build -f dockerfile -t my-first-image:1.0 .
```

Check Docker Desktop, page: Images. (And/Or `docker image ls`)

Run a bash shell in the container:

```bash
docker run -it my-first-image /bin/bash
```

Exit the container:

```bash
exit
```

### Data in a container

```bash
docker run -it --name my-first-container my-first-image /bin/bash
```

Make some changes to files in the container and exit.

Restart the container

```bash
docker start -i my-first-container
```

## A simple webserver

In the '03-webserver' directory:

Build the image.

```bash
docker build -f dockerfile -t 03-webserver-demo .
```

Run the image.

```bash
docker run -t 03-webserver-demo
```

Check if you can reach the webserver. (Start a webbrowser and connect to <http://localhost:8000>)

## Use volumes i.s.o. copying files into the image

In the '04-volumes' directory:

Build and run the image.

```bash
docker build -f dockerfile -t 04-webserver-demo .
```

To re-use this image at a later stage, tag the image:

```bash
docker tag 04-webserver-demo 04-webserver-demo:1.0
```

## Rust development (build)

In the '05-compilation' directory:

```bash
docker build -t rust-dev .
```

Run a Rust build on a given project.

```bash
docker run --volume ./hello-world:/workdir -t rust-dev
```

Run the rust program

```bash
```

## Multi stage

In the '06-multistage' directory:

Build the large image:

```bash
docker build -t calculator-large -f dockerfile-large .
```

Check the size of the image:

```bash
docker images | grep calculator
```

Build the multi-stage image(s):

```bash
docker build -t calculator-multi -f dockerfile-multi .
```

Recheck the size

## Docker Compose

In the '07-compose' directory:

```bash
docker-compose up
```

## Networking

In the '08-networking' directory:

```bash
docker-compose up
```

"De-attach"

### Build a small network-inspector

```bash
docker build -f dockerfile_debian-networktools -t debian-network .
```

### Connect to 'between_containers' network

```bash
docker run -it --network 08-networking_between_containers debian-network /bin/bash
```

Check the connection between "debian-network" and the webserver (from within the "bash" shell):

```bash
ping web
```

### Connect to 'to_host' network

```bash
docker run -it --network 08-networking_to_host debian-network /bin/bash
```

Check the connection between "debian-network" and the webserver (from within the "bash" shell):

```bash
ping web
```

```bash
ping <ip-address>
```

```bash
ping proxy
```

## Tips

### Keep the container as little as possible

### Think before doing

Write down expectations (in words and/or drawings)

### Running and automatically removing a container

Use '--rm' like:

```bash
docker run --rm -it --network my-net debian-network /bin/bash
```

This will remove the container after it's finished running.

### Write used commands down

### Try to reuse images

### Keep dynamic data out of the containers - use volumes

### In production use tags, not 'latest'/'stable'

### Name your containers

```bash
docker run -it --name my-web-server -p 8000:8000 04-webserver-demo:1.0
```

Restart/continue:

```bash
docker start my-web-server
```

```bash
docker rm my-web-server
```

### Don't be scared to make mistakes

## Clean-up

Use the following commands to check and clean-up:

```bash
docker container ls -a
```

```bash
docker image ls -a
```

```bash
docker system df
```

```bash
docker image prune
```

```bash
docker volume ls
```

```bash
docker system prune
```

```bash
docker network ls
```

```bash
docker network prune
```

```bash
docker system prune
```

```bash
docker buildx history ls | tail -n +2 | awk '{print $1}' | xargs -r docker buildx history rm
```
