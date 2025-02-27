# import network
# import time
# import socket
# 
# 
# def web_page():
#   html = """<html><head><meta name="viewport" content="width=device-width, initial-scale=1"></head>
#             <body><h1>Hello World</h1></body></html>
#          """
#   return html
# 
# # if you do not see the network you may have to power cycle
# # unplug your pico w for 10 seconds and plug it in again
# def ap_mode(ssid, password):
#     """
#         Description: This is a function to activate AP mode
#         
#         Parameters:
#         
#         ssid[str]: The name of your internet connection
#         password[str]: Password for your internet connection
#         
#         Returns: Nada
#     """
#     # Just making our internet connection
#     ap = network.WLAN(network.AP_IF)
#     ap.config(essid=ssid, password=password)
#     ap.active(True)
#     
#     while ap.active() == False:
#         pass
#     print('AP Mode Is Active, You can Now Connect')
#     print('IP Address To Connect to:: ' + ap.ifconfig()[0])
#     
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #creating socket object
#     s.bind(('', 80))
#     s.listen(5)
# 
#     while True:
#       conn, addr = s.accept()
#       print('Got a connection from %s' % str(addr))
#       request = conn.recv(1024)
#       print('Content = %s' % str(request))
#       response = web_page()
#       conn.send(response)
#       conn.close()
#       
# ap_mode('PICO2F53',
#         'freepicow')



# import network
# import socket
# import time
# 
# def start_ap(ssid, password):
#     ap = network.WLAN(network.AP_IF)  # Create access point
#     ap.config(essid=ssid, password=password)
#     ap.active(True)
#     
#     while not ap.active():
#         pass
# 
#     print("AP Mode is Active")
#     print("IP Address:", ap.ifconfig()[0])
# 
#     return ap.ifconfig()[0]  # Returns Pico's IP address
# 
# # Start Access Point
# ip_address = start_ap("PICO_W", "mypassword")
# 
# # Wait for laptop to connect
# time.sleep(5)
# print("Now connect your laptop to 'PICO_W' Wi-Fi network.")
# print("Then access Pico W at:", ip_address)

import network
import wifi_config as wifi
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




