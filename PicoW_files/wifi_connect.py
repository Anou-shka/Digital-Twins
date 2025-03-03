import network
import time

SSID = "dlink"  # Your WiFi SSID
PASSWORD = "freewifi"  # Replace with your actual password

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSID, PASSWORD)

while not wlan.isconnected():
    print("Connecting...")
    time.sleep(1)

print("Connected!")
print("IP Address:", wlan.ifconfig()[0])
