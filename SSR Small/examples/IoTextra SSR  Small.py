from machine import Pin
import time

# --- Configuration ---
# Define the GPIO pins connected to the 8 SSR output channels.
# Configuration: IoTextra SSR Small (8 channels) driven by IoTsmart RP2040 (Waveshare RP2040-tiny).
# NOTE: Using actual GPIO numbers for RP2040.
GPIO_PINS = [12, 11, 10, 9, 26, 15, 14, 13]

# List to hold the Pin objects representing the digital outputs (DO)
digital_outputs = []

# --- Initialization ---
print(f"Initializing 8 SSR output pins: {GPIO_PINS}")
# We initialize Pin objects only ONCE, outside the main loop.
for pin_num in GPIO_PINS:
    # Set pin as OUTPUT
    digital_outputs.append(Pin(pin_num, Pin.OUT))

# --- Main Loop ---
print("Starting 8-Channel SSR Switching Loop...")

while True:
    print("Turning channels ON sequentially...")
    # Iterate through all Pin objects
    for i, output_pin in enumerate(digital_outputs):
        output_pin.value(1)  # Turn ON (High)
        # Using i+1 for Channel number for user-friendly 1-based indexing
        print(f"Channel {i+1} (Pin {GPIO_PINS[i]}): ON")
        time.sleep(0.5)   # Wait 0.5 second

    print("Turning channels OFF sequentially...")
    for i, output_pin in enumerate(digital_outputs):
        output_pin.value(0)  # Turn OFF (Low)
        print(f"Channel {i+1} (Pin {GPIO_PINS[i]}): OFF")
        time.sleep(0.5)   # Wait 0.5 second
        
    print("Cycle complete. Waiting 3 seconds before restart.\n")
    time.sleep(3)