from machine import Pin
import time

# --- Configuration ---
# Define the GPIO pins connected to the 4 Relay output channels.
# Configuration: IoTextra Relay2 (4 channels) driven by IoTsmart RP2040 (Waveshare RP2040-tiny).
# NOTE: Using actual GPIO numbers for RP2040: 12, 11, 10, 9
GPIO_PINS = [12, 11, 10, 9]

# List to hold the Pin objects representing the digital outputs (DO)
digital_relays = []

# --- Initialization ---
print(f"Initializing 4 Relay output pins: {GPIO_PINS}")
# We initialize Pin objects only ONCE, outside the main loop.
for pin_num in GPIO_PINS:
    # Set pin as OUTPUT
    digital_relays.append(Pin(pin_num, Pin.OUT))

# --- Main Loop ---
print("Starting 4-Channel Relay Switching Loop...")

while True:
    print("Turning channels ON sequentially...")
    # Iterate through all Pin objects
    for i, relay_pin in enumerate(digital_relays):
        relay_pin.value(1)  # Turn ON (High)
        # Using i+1 for Channel number for user-friendly 1-based indexing
        print(f"Channel {i+1} (Pin {GPIO_PINS[i]}): ON")
        time.sleep(1.5)   # Wait 1.5 seconds (for mechanical relays)

    print("Turning channels OFF sequentially...")
    for i, relay_pin in enumerate(digital_relays):
        relay_pin.value(0)  # Turn OFF (Low)
        print(f"Channel {i+1} (Pin {GPIO_PINS[i]}): OFF")
        time.sleep(1.5)   # Wait 1.5 seconds
        
    print("Cycle complete. Waiting 3 seconds before restart.\n")
    time.sleep(3)