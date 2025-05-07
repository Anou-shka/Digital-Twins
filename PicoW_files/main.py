# This file is part of the PicoW project.
# Main.py runs as soon as the Pico W is powered on.
from wlan import wifi_connect
from test import pico_main_run
from excel_update import excel_update
import time

# Keep trying to connect to WiFi before proceeding
 wifi_connect()

# Confirm that main.py ran by blinking LED
pico_main_run()

# Send data at synchronized intervals (every 20 seconds at x:00, x:20, x:40)
while True:
    time.sleep(20)  # Wait to sync
    excel_update()  # Send data

