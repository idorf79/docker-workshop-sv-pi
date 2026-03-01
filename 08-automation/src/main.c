#include "hal.h"

int main()
{
    printf("Firmware starting...\n");
    hal_init();

    for (int i = 0; i < 5; i++)
    {
        hal_gpio_write(13, 1);
        hal_gpio_write(13, 0);
    }

    printf("Firmware complete\n");
    return 0;
}