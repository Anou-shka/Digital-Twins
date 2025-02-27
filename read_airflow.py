from machine import ADC, Pin
import utime

# ✅ Define ADC pin for MPXV7002DP
MPXV_PIN = 27  # GP26 (Pin 31)
adc = ADC(Pin(MPXV_PIN))

# ✅ MPXV7002DP Sensor Constants
VCC = 5.0  # Operating voltage (5V)
ADC_MAX = 65535  # 16-bit ADC resolution
V_OFFSET = 2.5  # Zero pressure voltage (2.5V at 0 kPa)
SENSITIVITY = 0.0025  # ✅ Corrected sensitivity (2.5mV per Pa)

def read_pressure():
    """Read analog voltage and convert it to pressure (kPa)"""
    raw_adc = adc.read_u16()  # Read raw ADC value (0-65535)
    voltage = (raw_adc / ADC_MAX) * VCC  # Convert ADC value to voltage
    
    # ✅ Prevent negative pressure if sensor is not properly connected
    if voltage < 0.5 or voltage > 4.5:  # Noise check range
        return None, None, None

    pressure = (voltage - V_OFFSET) / SENSITIVITY  # Prevent negative values
    return raw_adc, voltage, pressure

# while True:
#     raw_adc, voltage, pressure = read_pressure()
# 
#     if raw_adc is None:
#         print("⚠️ No sensor detected or invalid reading! Check wiring.")
#     else:
#         print(f"ADC Value: {raw_adc}")
#         print(f"Voltage: {voltage:.3f}V")
#         print(f"Pressure: {pressure:.3f} kPa")
# 
#     utime.sleep(2)

