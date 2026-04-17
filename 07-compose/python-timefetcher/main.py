# Source - https://stackoverflow.com/a/74599678
# Posted by import random, modified by community. See post 'Timeline' for change history
# Retrieved 2026-04-17, License - CC BY-SA 4.0

import datetime
import time
from pathlib import Path

filePath = Path('.')

while True:
    with open('./time_file/time.html', 'a') as f:
        currentTime = datetime.datetime.now()
        msg = "is the current date and time"
        file_msg = f"""{currentTime.strftime("%d-%b-%Y %H:%M:%S.%f")} {msg}\n"""
        print(file_msg)
        f.write(file_msg)

    time.sleep(5)
