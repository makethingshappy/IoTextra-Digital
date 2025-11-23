Python

from machine import Pin
import time

# --- Configuration ---
# Define the GPIO pins connected to the output channels.
# Configuration: IoTextra Octal2 driven by IoTsmart RP2040 (Waveshare RP2040-tiny).
# NOTE: Using actual GPIO numbers for RP2040: 26, 15, 14, 13
GPIO_PINS = [26, 15, 14, 13]

# List to hold the Pin objects representing the digital outputs (DO)
digital_outputs = []

# --- Initialization ---
print(f"Initializing output pins: {GPIO_PINS}")
# We initialize Pin objects only ONCE, outside the main loop.
for pin_num in GPIO_PINS:
    # Set pin as OUTPUT
    digital_outputs.append(Pin(pin_num, Pin.OUT))

# --- Main Loop ---
print("Starting Output Cycle Loop...")

while True:
    print("Turning channels ON sequentially...")
    # Iterate through the list of Pin objects
    for i, output_pin in enumerate(digital_outputs):
        output_pin.value(1)  # Turn ON (High)
        # Use GPIO_PINS[i] to print the actual pin number from the list
        print(f"Channel {i} (Pin {GPIO_PINS[i]}): ON")
        time.sleep(1)  # Wait 1 second

    print("Turning channels OFF sequentially...")
    for i, output_pin in enumerate(digital_outputs):
        output_pin.value(0)  # Turn OFF (Low)
        print(f"Channel {i} (Pin {GPIO_PINS[i]}): OFF")
        time.sleep(1)  # Wait 1 second
        
    print("Cycle complete. Waiting 3 seconds before restart.\n")
    time.sleep(3)