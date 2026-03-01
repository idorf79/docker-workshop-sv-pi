#include "hal.h"

void hal_init(void)
{
    printf("HAL: Initializing hardware...\n");
}

void hal_gpio_write(int pin, int value)
{
    printf("HAL: GPIO pin %d set to %d\n", pin, value);
}