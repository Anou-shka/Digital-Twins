print("I am a test file")
import os
print(os.uname())

import network

try:
    wlan = network.WLAN(network.STA_IF)  # Try to initialize WiFi
    wlan.active(True)
    print("✅ This is a Raspberry Pi Pico W with WiFi!")
except:
    print("❌ This is a regular Raspberry Pi Pico. No WiFi available.")