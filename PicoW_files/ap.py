# WiFi Access Point
import network
import wifi_pico_config as wifi
import time


def wifi_access_point():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid = wifi.essid, password=wifi.ap_password)  # Change SSID & password
    while ap.active == False:
        print('Waiting...')
        time.sleep(1)
    ap = ap.ifconfig()[0]
    print(f'Connect to Pico W as {ap}')



