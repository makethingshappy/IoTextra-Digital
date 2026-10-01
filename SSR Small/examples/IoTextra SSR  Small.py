"""
IoTextra SSR Small - MicroPython example (GPIO mode)
Host: IoTsmart RP2040 (Waveshare RP2040-Tiny)

Switches 8 solid-state relays RL1-RL8 via AP0-AP7 on the HOST-P connector.

Control polarity (IoTextra SSR Small datasheet Rev.3-02):
  AP line = 1 -> SSR off
  AP line = 0 -> SSR on (channel LED lit)
Outputs are initialised to 1 (OFF) so no load switches on at start-up.
"""
from machine import Pin
import time

# RL1..RL8 = AP0..AP7 -> RP2040 GPIO (IoTsmart RP2040 pinout, rev 1-02)
GPIO_PINS = [12, 11, 10, 9, 26, 15, 14, 13]

ssrs = [Pin(p, Pin.OUT, value=1) for p in GPIO_PINS]  # start OFF


def set_ssr(pin, on):
    """Active-low: on=True drives the line low."""
    pin.value(0 if on else 1)


def all_off():
    for pin in ssrs:
        set_ssr(pin, False)


print("IoTextra SSR Small switching cycle. Press Ctrl+C to stop.")

try:
    while True:
        for ch, pin in enumerate(ssrs, start=1):
            set_ssr(pin, True)
            print("RL{} (GP{}): ON".format(ch, GPIO_PINS[ch - 1]))
            time.sleep(0.5)
        for ch, pin in enumerate(ssrs, start=1):
            set_ssr(pin, False)
            print("RL{} (GP{}): OFF".format(ch, GPIO_PINS[ch - 1]))
            time.sleep(0.5)
        print("Cycle complete. Restarting in 3 s.\n")
        time.sleep(3)
finally:
    all_off()
    print("All SSRs OFF.")
