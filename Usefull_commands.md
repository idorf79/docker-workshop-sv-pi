# Usefull commands

## Connect a serial device to a container

This will only work when running Docker natively. (So not using Docker Desktop).

Remove docker-desktop.

Install `docker.io`:

```bash
sudo apt install docker.io
```

```bash
docker run -it --rm --device /dev/ttyUSB0:/dev/ttyUSB0 esp32_test
```
