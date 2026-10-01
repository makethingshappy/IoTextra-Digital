"""
IoTextra Octal2 - digital outputs, MicroPython example (GPIO mode)
Host: IoTsmart RP2040 (Waveshare RP2040-Tiny)

Switches 4 isolated digital outputs DO1-DO4 via AP4-AP7 on the HOST-P connector.
(Inputs IN1-IN4 are on AP0-AP3, see "IoTextra Octal2 - input.py".)

Control polarity (IoTextra Octal2 datasheet Rev.3-02):
  AP line = 1 -> output transistor OFF
  AP line = 0 -> output transistor ON
Outputs are initialised to 1 (OFF) so no load switches on at start-up.
"""
from machine import Pin
import time

# DO1..DO4 = AP4..AP7 -> RP2040 GPIO (IoTsmart RP2040 pinout, rev 1-02)
GPIO_PINS = [26, 15, 14, 13]

outputs = [Pin(p, Pin.OUT, value=1) for p in GPIO_PINS]  # start OFF


def set_output(pin, on):
    """Active-low: on=True drives the line low."""
    pin.value(0 if on else 1)


def all_off():
    for pin in outputs:
        set_output(pin, False)


print("IoTextra Octal2 output cycle. Press Ctrl+C to stop.")

try:
    while True:
        for ch, pin in enumerate(outputs, start=1):
            set_output(pin, True)
            print("DO{} (GP{}): ON".format(ch, GPIO_PINS[ch - 1]))
            time.sleep(1)
        for ch, pin in enumerate(outputs, start=1):
            set_output(pin, False)
            print("DO{} (GP{}): OFF".format(ch, GPIO_PINS[ch - 1]))
            time.sleep(1)
        print("Cycle complete. Restarting in 3 s.\n")
        time.sleep(3)
finally:
    all_off()
    print("All outputs OFF.")
