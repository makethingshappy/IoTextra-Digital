"""
IoTextra Input - MicroPython example (GPIO mode)
Host: IoTsmart RP2040 (Waveshare RP2040-Tiny)

Reads 8 isolated digital inputs IN1-IN8 via AP0-AP7 on the HOST-P connector.

Signal polarity (IoTextra Input datasheet Rev.3-02):
  input 4...36 V -> opto-coupler on  -> AP line reads 0 (ACTIVE)
  input 0...2 V  -> opto-coupler off -> AP line reads 1 (INACTIVE)
"""
from machine import Pin
import time

# AP0..AP7 -> RP2040 GPIO (IoTsmart RP2040 pinout, rev 1-02)
GPIO_PINS = [12, 11, 10, 9, 26, 15, 14, 13]

inputs = [Pin(p, Pin.IN) for p in GPIO_PINS]


def is_active(pin):
    """True when voltage is present on the input (active-low line)."""
    return pin.value() == 0


print("IoTextra Input monitor. Press Ctrl+C to stop.")

while True:
    print("-" * 36)
    for ch, pin in enumerate(inputs, start=1):
        raw = pin.value()
        state = "ACTIVE   (voltage present)" if is_active(pin) else "inactive (no voltage)"
        print("IN{} (GP{}): raw={} -> {}".format(ch, GPIO_PINS[ch - 1], raw, state))
    time.sleep(1)
