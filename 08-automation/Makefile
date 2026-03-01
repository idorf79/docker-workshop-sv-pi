CC = gcc
CFLAGS = -Wall -Wextra -Iinclude
SRC_DIR = src
OUT_DIR = output
TARGET = $(OUT_DIR)/firmware.elf

SOURCES = $(wildcard $(SRC_DIR)/*.c)
OBJECTS = $(SOURCES:$(SRC_DIR)/%.c=$(OUT_DIR)/%.o)

all: $(TARGET)

$(OUT_DIR):
	mkdir -p $(OUT_DIR)

$(OUT_DIR)/%.o: $(SRC_DIR)/%.c | $(OUT_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

$(TARGET): $(OBJECTS)
	$(CC) $(OBJECTS) -o $@
	@echo "Build complete: $(TARGET)"

clean:
	rm -rf $(OUT_DIR)

.PHONY: all clean
