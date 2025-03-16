from wlan import wifi_connect
from test import pico_main_run
from excel_update import excel_update
import time

# ✅ Keep trying to connect to WiFi before proceeding
 wifi_connect()

# ✅ Confirm that main.py ran by blinking LED
pico_main_run()

# ✅ Send data at synchronized intervals (every 20 seconds at x:00, x:20, x:40)
while True:
#     wifi_connect()
    pico_main_run()
#     current_time = time.time()  # Get current time
#     wait_time = 20 - (current_time % 20)  # Calculate time to wait for sync
#     print(f"Waiting {wait_time:.2f} seconds to sync with 20-second intervals...")
    time.sleep(20)  # Wait to sync
# 
#     # ✅ Send data
    excel_update()

