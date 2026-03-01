!/bin/bash

if [ ! -f output/firmware.elf ]; then
    echo "Firmware not built. Run ./build.sh first."
    exit 1
fi

echo "Running firmware..."
./output/firmware.elf