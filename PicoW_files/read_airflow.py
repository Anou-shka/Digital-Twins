from machine import ADC
from time import sleep

# Constants
ADC_PIN = 26  # GP26 = ADC0 on Pico W
VREF = 3.3  # ADC reference voltage (Pico)
SUPPLY_VOLTAGE = 5.0  # MPXV7002DP powered by 5V
DIVIDER_SCALING = 2.5  # 15kΩ / 10kΩ voltage divider
ADC_MAX = 65535  # 16-bit ADC

# Initialize ADC
adc = ADC(ADC_PIN)

def read_voltage():
    raw = adc.read_u16()
    voltage_at_adc = (raw / ADC_MAX) * VREF
    actual_sensor_voltage = voltage_at_adc * DIVIDER_SCALING
    return actual_sensor_voltage

def voltage_to_pressure_kpa(voltage):
    # From MPXV7002DP datasheet:
    # Vout = Vs * (0.2 * P + 0.5)
    # Rearranged: P = ((Vout / Vs) - 0.5) / 0.2
    pressure_kpa = ((voltage / SUPPLY_VOLTAGE) - 0.5) / 0.2
    return pressure_kpa

def pressure_kpa_to_pa(pressure_kpa):
    return pressure_kpa * 1000

def pressure_to_airspeed(pressure_pa, temperature_c=28.1):
    R = 287.05  # Specific gas constant for dry air [J/(kg·K)]
    temp_k = temperature_c + 273.15
    rho = 101325 / (R * temp_k)  # Ideal gas law

    pressure_diff = max(abs(pressure_pa), 0)  # Only use positive pressure
    airspeed = (2 * pressure_diff / rho) ** 0.5 if pressure_diff > 0 else 0
    return airspeed


while True:
    voltage = read_voltage()
    pressure_kpa = voltage_to_pressure_kpa(voltage)
    pressure_pa = pressure_kpa_to_pa(pressure_kpa)
    airspeed = pressure_to_airspeed(pressure_pa, temperature_c=28.1)
    print(f"Voltage (corrected): {voltage:.3f} V")
    print(f"Pressure: {pressure_kpa:.3f} kPa")
    print(f"Pressure: {pressure_pa:.1f} Pa")
    print(f"Airspeed: {airspeed:.2f} m/s")
    print("-" * 30)

    sleep(10)

