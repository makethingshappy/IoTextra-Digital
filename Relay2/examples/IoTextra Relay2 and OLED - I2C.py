"""
IoTextra Relay2 over I2C (TCA9534) with SSD1306 OLED status - MicroPython

Hardware
  Base board : IoTbase PICO or IoTbase NANO
  MCU        : ESP32-S3 or RP2040 (detected automatically from sys.platform)
  Module     : IoTextra Relay2 (relays K1-K4 on expander pins P0-P3)
               Also works with IoTextra Combo (relays K1-K2 on P0-P1):
               set RELAY_BITS = (0, 1)
  Display    : SSD1306 128x32 OLED on the same I2C bus (optional)

What it does
  Switches the relays one by one through the TCA9534 I/O expander and shows
  the state of every relay on the OLED and in the console. If no OLED is
  found, the relay cycle still runs with console output only.

Relay polarity (IoTextra Relay2 datasheet)
  Expander pin = 1 -> relay OFF
  Expander pin = 0 -> relay ON
  The output register is written to all-ones BEFORE the pins are switched to
  outputs, so no relay clicks on during initialisation.

TCA9534 address
  Set by the module jumpers / DIP switch, NOT by the MCU type:
    TCA9534  : 0x20...0x27 (module default 0x27)
    TCA9534A : 0x38...0x3F (module default 0x3F)
  With TCA_ADDR = None the address is found by scanning the bus. 0x3C/0x3D are
  skipped during the scan because they are used by the SSD1306 OLED.

Required file on the board: ssd1306.py (standard MicroPython SSD1306 driver),
only if the OLED is used.
"""
from machine import I2C, Pin
import sys
import time

# ----------------------------------------------------------------- settings
BOARD = "pico"              # "pico" -> IoTbase PICO, "nano" -> IoTbase NANO
RELAY_BITS = (0, 1, 2, 3)   # IoTextra Relay2: (0, 1, 2, 3)   IoTextra Combo: (0, 1)
TCA_ADDR = None             # None = auto-detect, or e.g. 0x27 / 0x3F
OLED_ADDR = 0x3C
ON_TIME_S = 1.0             # how long each relay stays ON
OFF_TIME_S = 0.5            # pause after switching a relay OFF

# I2C pins of the HOST connector per base board and MCU
I2C_PINS = {
    ("pico", "rp2"):   {"sda": 20, "scl": 21},
    ("pico", "esp32"): {"sda": 4,  "scl": 5},
    ("nano", "rp2"):   {"sda": 12, "scl": 13},
    ("nano", "esp32"): {"sda": 11, "scl": 12},
}
I2C_FREQ = 400000


# ----------------------------------------------------------------- TCA9534
class TCA9534:
    """Minimal TCA9534 / TCA9534A driver for output use."""

    REG_INPUT = 0x00
    REG_OUTPUT = 0x01
    REG_CONFIG = 0x03       # bit = 1 -> input, bit = 0 -> output

    def __init__(self, i2c, address, output_bits):
        self.i2c = i2c
        self.address = address
        self.out_mask = 0
        for bit in output_bits:
            self.out_mask |= 1 << bit
        # Shadow copy of the output register: all ones = all relays OFF
        self.state = 0xFF
        # 1) set output latches HIGH first, 2) only then enable the outputs
        self._write(self.REG_OUTPUT, self.state)
        self._write(self.REG_CONFIG, 0xFF & ~self.out_mask)

    def _write(self, reg, value):
        self.i2c.writeto_mem(self.address, reg, bytes([value]))

    def write_bit(self, bit, level):
        """Set one expander pin to 0 or 1 (read-modify-write on the shadow)."""
        if level:
            self.state |= 1 << bit
        else:
            self.state &= ~(1 << bit)
        self._write(self.REG_OUTPUT, self.state)

    def set_all(self, level):
        """Set all configured output pins to the same level."""
        if level:
            self.state |= self.out_mask
        else:
            self.state &= ~self.out_mask
        self._write(self.REG_OUTPUT, self.state)


# ----------------------------------------------------------------- helpers
def find_tca9534(addresses):
    """Return the first expander address found on the bus (defaults first)."""
    candidates = [0x27, 0x3F]
    candidates += [a for a in range(0x20, 0x28) if a not in candidates]
    candidates += [a for a in range(0x38, 0x40)
                   if a not in candidates and a not in (0x3C, 0x3D)]
    for addr in candidates:
        if addr in addresses:
            return addr
    return None


def relay_on(tca, bit):
    tca.write_bit(bit, 0)       # active-low


def relay_off(tca, bit):
    tca.write_bit(bit, 1)


def relay_states(tca):
    """List of booleans: True = relay ON."""
    return [not (tca.state >> bit) & 1 for bit in RELAY_BITS]


def show_status(oled, tca, message):
    """Print the status line and update the OLED (if present)."""
    states = relay_states(tca)
    line = " ".join("K{}:{}".format(i, "1" if on else "0")
                    for i, on in enumerate(states, start=1))
    print("{:<14} {}".format(message, line))
    if oled is None:
        return
    # 128 px = 16 characters per line, so the OLED gets a compact form,
    # e.g. "K1-K4: 1000" (1 = ON)
    compact = "K1-K{}: {}".format(
        len(states), "".join("1" if on else "0" for on in states))
    oled.fill(0)
    oled.text("TCA9534 0x{:02X}".format(tca.address), 0, 0)
    oled.text(message, 0, 12)
    oled.text(compact, 0, 24)
    oled.show()


# ----------------------------------------------------------------- main
def main():
    chip = sys.platform                     # "rp2" or "esp32"
    pins = I2C_PINS.get((BOARD, chip))
    if pins is None:
        print("No I2C pin map for board '{}' with '{}'".format(BOARD, chip))
        return

    i2c = I2C(0, sda=Pin(pins["sda"]), scl=Pin(pins["scl"]), freq=I2C_FREQ)
    found = i2c.scan()
    print("I2C devices:", [hex(a) for a in found])

    addr = TCA_ADDR if TCA_ADDR is not None else find_tca9534(found)
    if addr is None or addr not in found:
        print("TCA9534 not found - check the module and its address jumpers")
        return
    tca = TCA9534(i2c, addr, RELAY_BITS)
    print("TCA9534 at 0x{:02X}, relays on P{}".format(
        addr, ", P".join(str(b) for b in RELAY_BITS)))

    oled = None
    if OLED_ADDR in found:
        try:
            from ssd1306 import SSD1306_I2C
            oled = SSD1306_I2C(128, 32, i2c, addr=OLED_ADDR)
        except Exception as e:              # driver missing or init error
            print("OLED disabled:", e)
    else:
        print("No OLED at 0x{:02X} - console output only".format(OLED_ADDR))

    show_status(oled, tca, "All OFF")
    print("Relay cycle running. Press Ctrl+C to stop.")
    try:
        while True:
            for k, bit in enumerate(RELAY_BITS, start=1):
                relay_on(tca, bit)
                show_status(oled, tca, "K{} ON".format(k))
                time.sleep(ON_TIME_S)
                relay_off(tca, bit)
                show_status(oled, tca, "K{} OFF".format(k))
                time.sleep(OFF_TIME_S)
    finally:
        tca.set_all(1)                      # every relay OFF on exit
        show_status(oled, tca, "Stopped")


main()
