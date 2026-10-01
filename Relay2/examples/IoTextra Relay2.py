"""
IoTextra Relay2 - MicroPython example (GPIO mode)
Host: IoTsmart RP2040 (Waveshare RP2040-Tiny)

Switches 4 relays K1-K4 (RL1-RL4) via AP0-AP3 on the HOST-P connector.

Control polarity (IoTextra Relay2 datasheet Rev.3-02):
  AP line = 1 -> relay off (NC contact closed)
  AP line = 0 -> relay on  (NO contact closed)
Outputs are initialised to 1 (OFF) so no relay clicks on at start-up.
"""
from machine import Pin
import time

# RL1..RL4 = AP0..AP3 -> RP2040 GPIO (IoTsmart RP2040 pinout, rev 1-02)
GPIO_PINS = [12, 11, 10, 9]

relays = [Pin(p, Pin.OUT, value=1) for p in GPIO_PINS]  # start OFF


def set_relay(pin, on):
    """Active-low: on=True drives the line low."""
    pin.value(0 if on else 1)


def all_off():
    for pin in relays:
        set_relay(pin, False)


print("IoTextra Relay2 switching cycle. Press Ctrl+C to stop.")

try:
    while True:
        for ch, pin in enumerate(relays, start=1):
            set_relay(pin, True)
            print("K{} (GP{}): ON".format(ch, GPIO_PINS[ch - 1]))
            time.sleep(1.5)  # slow cycle for mechanical relays
        for ch, pin in enumerate(relays, start=1):
            set_relay(pin, False)
            print("K{} (GP{}): OFF".format(ch, GPIO_PINS[ch - 1]))
            time.sleep(1.5)
        print("Cycle complete. Restarting in 3 s.\n")
        time.sleep(3)
finally:
    all_off()
    print("All relays OFF.")
