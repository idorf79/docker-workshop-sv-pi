# Workshop Docker for StudieVereniging Promptus Imperii

Here are some commmands as used during the workshop.

For more information, check Docker Cli reference page: https://docs.docker.com/reference/cli/docker/

## Run a simple Debian container

Build an image
```
docker build -f dockerfiles/dockerfile_debian13-slim -t debian13-slim .
```

Run a bash shell in the container:

```
docker run -it debian13-slim /bin/bash
```

## A simple webserver

This command will start a NginX webserver, reachable via http://localhost:8380

```
docker run -d --name web -p 8380:80 -v ./:/usr/share/nginx/html:ro nginx:alpine
```

## Rust development (build)
In the 'rust' folder.
```
docker build -t rust-dev .
```

Run a Rust build on a given project.
```
docker run --volume ./my-rust-app/hello-world:/workdir -t rust-dev
```



# Create docker "internal" network "my-net"
docker network create my-net
# Run a simple nginx webserver
docker run -d --name web --network my-net nginx:alpine
docker run --rm -it --network my-net busybox