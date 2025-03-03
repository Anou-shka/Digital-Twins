import network
import socket
import time
import os

# ✅ Set WiFi SSID & Password
SSID = "PicoW_AP"
PASSWORD = "12345678"  # Minimum 8 characters

# ✅ Create Access Point
ap = network.WLAN(network.AP_IF)
ap.active(True)
ap.config(essid=SSID, password=PASSWORD)

print("Starting WiFi AP...")
while not ap.active():
    pass
print(f"✅ Access Point Active! IP Address: {ap.ifconfig()[0]}")

# ✅ Function to Run the Sensor Script
def run_script():
    try:
        if "excel_update_online.py" in os.listdir():  # ✅ Check if file exists
            exec(open("excel_update_online.py").read(), globals())  # ✅ Runs script safely
            return "✅ Sensor script started successfully!"
        else:
            return "❌ Error: Script file not found!"
    except Exception as e:
        return f"❌ Error running script: {str(e)}"

# ✅ HTML Web Interface
html = """<!DOCTYPE html>
<html>
<head>
    <title>Pico W Control</title>
</head>
<body>
    <h2>Run Sensor Script</h2>
    <button onclick="fetch('/run').then(res => res.text()).then(alert)">Run Script</button>
</body>
</html>"""

# ✅ Start Web Server
def web_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # ✅ Prevent socket errors on restart
    s.bind(("0.0.0.0", 80))
    s.listen(5)
    
    print("✅ Web Server Running... Visit http://192.168.4.1")

    while True:
        conn, addr = s.accept()
        request = conn.recv(1024).decode()

        if "GET /run" in request:
            response = run_script()  # ✅ Runs script when button is clicked
        else:
            response = html  # ✅ Serves the webpage
        
        http_response = f"HTTP/1.1 200 OK\nContent-Type: text/html\n\n{response}"
        conn.send(http_response.encode())
        conn.close()

# ✅ Run the Web Server
web_server()

