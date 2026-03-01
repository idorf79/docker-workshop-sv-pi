#!/bin/bash

set -e

echo "=== Docker Automated Build System ==="
echo ""

# Build the Docker image
echo "Building Docker image..."
docker build -t firmware-builder .

# Run the build
echo "Compiling firmware..."
docker run --rm \
    -v $(pwd):/workspace \
    -u $(id -u):$(id -g) \
    firmware-builder

# Check if build succeeded
if [ -f output/firmware.elf ]; then
    echo ""
    echo "Build successful!"
    echo "Output: output/firmware.elf"
    ls -lh output/firmware.elf
else
    echo "Build failed!"
    exit 1
fi