from machine import Pin
import time

# --- Configuration ---
# Define the GPIO pins connected to the input channels.
# Configuration: IoTextra Octal2 (INPUT channels) driven by IoTsmart RP2040 (Waveshare RP2040-tiny).
# NOTE: Using actual GPIO numbers for RP2040: 12, 11, 10, 9
GPIO_PINS = [12, 11, 10, 9]

# List to hold the Pin objects representing the digital inputs (DI)
digital_inputs = []

# --- Initialization ---
print(f"Initializing input pins: {GPIO_PINS}")
# We initialize Pin objects only ONCE, outside the main loop.
for pin_num in GPIO_PINS:
    # Set pin as INPUT. 
    # IoTextra Octal2 (INPUT) modules have internal circuitry for 24V,
    # so standard Pin.IN is sufficient.
    digital_inputs.append(Pin(pin_num, Pin.IN))

# --- Main Loop ---
print("Starting Input Monitor. Press Ctrl+C to stop.")

while True:
    print("-" * 30)
    # Iterate through all configured channels
    for i, input_pin in enumerate(digital_inputs):
        # Read the current value (0 or 1)
        state = input_pin.value()
        
        # Determine status for clear output
        status_text = "HIGH / Active" if state else "LOW / Inactive"
        
        # Print status clearly
        print(f"Channel {i} (Pin {GPIO_PINS[i]}): {state} ({status_text})")
    
    # Wait for 1 second before the next scan
    time.sleep(1)