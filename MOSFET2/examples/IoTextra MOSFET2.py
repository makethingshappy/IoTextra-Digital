"""
IoTextra MOSFET2 - MicroPython example (GPIO mode)
Host: IoTsmart RP2040 (Waveshare RP2040-Tiny)

Switches 8 N-channel MOSFET outputs DO1-DO8 (control lines RL1-RL8)
via AP0-AP7 on the HOST-P connector
(two galvanically isolated groups: DO1-DO4 and DO5-DO8).

Control polarity (IoTextra MOSFET2 datasheet Rev.3-02):
  AP line = 1 -> MOSFET off
  AP line = 0 -> MOSFET on (channel LED lit)
Outputs are initialised to 1 (OFF) so no load switches on at start-up.
"""
from machine import Pin
import time

# DO1..DO8 (RL1..RL8) = AP0..AP7 -> RP2040 GPIO (IoTsmart RP2040 pinout, rev 1-02)
GPIO_PINS = [12, 11, 10, 9, 26, 15, 14, 13]

mosfets = [Pin(p, Pin.OUT, value=1) for p in GPIO_PINS]  # start OFF


def set_mosfet(pin, on):
    """Active-low: on=True drives the line low."""
    pin.value(0 if on else 1)


def all_off():
    for pin in mosfets:
        set_mosfet(pin, False)


print("IoTextra MOSFET2 switching cycle. Press Ctrl+C to stop.")

try:
    while True:
        for ch, pin in enumerate(mosfets, start=1):
            set_mosfet(pin, True)
            print("DO{} (GP{}): ON".format(ch, GPIO_PINS[ch - 1]))
            time.sleep(0.5)
        for ch, pin in enumerate(mosfets, start=1):
            set_mosfet(pin, False)
            print("DO{} (GP{}): OFF".format(ch, GPIO_PINS[ch - 1]))
            time.sleep(0.5)
        print("Cycle complete. Restarting in 3 s.\n")
        time.sleep(3)
finally:
    all_off()
    print("All MOSFET outputs OFF.")
