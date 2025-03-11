from machine import UART, Pin
import time

# Initialize UART1 with correct TX and RX pins
uart = UART(1, baudrate=9600, tx=Pin(4), rx=Pin(5))

# MH-Z19C command to request CO₂ concentration
request_data = bytearray([0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79])

def read_co2():
    uart.read()  # Clear any buffered data before sending a request
    uart.write(request_data)  # Send request command
    time.sleep(0.2)  # Wait longer for sensor response

    attempts = 5  # Retry up to 5 times
    response = None

    for _ in range(attempts):
        if uart.any():  # Check if data is available
            response = uart.read(9)  # Read 9 bytes
            if response and len(response) == 9:  # Ensure correct length
                break
        time.sleep(0.1)  # Wait and retry if needed

    if response and len(response) == 9:
        if response[0] == 0xFF and response[1] == 0x86:  # Validate packet structure
            high = response[2]
            low = response[3]
            co2_concentration = (high << 8) + low  # Convert to ppm
            return co2_concentration
        else:
            print("Invalid data format received. Raw:", response)
    else:
        print("No valid response or data length mismatch. Raw:", response)

    return None  # Return None if invalid or no response

# Run the CO₂ reading function in a loop
while True:
    co2_concentration = read_co2()
    if co2_concentration is not None:
        print(f"CO₂ Concentration: {co2_concentration} ppm")
    else:
        print("Failed to read CO₂ concentration.")
    time.sleep(2)  # Read every 2 seconds


# from machine import UART, Pin
# import time

# # Initialize UART1 with correct TX and RX pins
# uart = UART(1, baudrate=9600, tx=Pin(8), rx=Pin(9))

# # MH-Z19C command to request CO₂ concentration
# request_data = bytearray([0xFF, 0x01, 0x86, 0x00, 0x00, 0x00, 0x00, 0x00, 0x79])

# def read_co2():
#     uart.write(request_data)  # Send request command
# #     time.sleep(0.1)  # Wait for response

#     if uart.any():  # Check if data is available
#         response = uart.read(9)  # Read 9 bytes of response

#         if response and len(response) == 9:
#             high = response[2]
#             low = response[3]
#             co2_concentration = (high << 8) + low  # Convert to ppm
            
#             # Return the CO₂ value
#             return co2_concentration  
#         else:
#             print("Invalid data received.")
#             return None  # Return None if invalid data
#     else:
#         print("No response from sensor.")
#         return None  # Return None if no response


# # Run the CO₂ reading function in a loop
# # while True:
# #     co2_concentration = read_co2()
# #     print(f"Co2 concentration: {co2_concentration} ppm")
# #     time.sleep(2)  # Read every 2 seconds

