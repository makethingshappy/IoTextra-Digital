<!-- OVERVIEW_START -->
> **4x SPST + 4x Latching-DPDT - IoTextra Relay**
>
> 4 SPST relays · 4 latching DPDT relays · state retained without coil power · LED state indication on all 8 channels
>
> SPST contacts 250 VAC / 30 VDC / 5 A, direct GPIO control · latching contacts 250 VAC / 220 VDC / 2 A, control via I²C → TCA9534 → DRV8837C
>
> Works with Raspberry Pi, Raspberry Pi Pico / Pico 2 (RP2040 / RP2350) and ESP32
>
> DIN-rail mounting: A 3D-printable DIN-rail mounting tray is available — <a href="https://www.printables.com/model/1802141-din-rail-mount-for-make-things-happy-iotextra">view on Printables</a>
>
> Part of the IoTextra series · compatible with IoTsmart and IoTbase · <a href="https://github.com/makethingshappy/iotextra-digital/tree/main/Relay">Open Hardware</a>
>
> Hardware license: <a href="https://github.com/makethingshappy/iotextra-digital/blob/main/LICENSE_HARDWARE.md">CC BY-SA 4.0</a>
<!-- OVERVIEW_END -->

![software](5-logo.svg)

<!-- PRODUCT_START -->
## Buy IoTextra Relay

[IoTextra Relay at makethingshappy.io](https://makethingshappy.io/products/iotextra-relay)
<!-- PRODUCT_END -->

<!-- SYNERGY_START -->
## Hardware Synergy

🔌 **Standalone:** Connect via the HOST connector cable from any host microcontroller: SPST relay control (AP0–AP3), the latching-driver enable signal (AP5) and the 5V supply are provided through HOST. Latching relays are controlled via the I²C bus (Qwiic connectors or SDA / SCL pins) using the onboard I/O expander.

🧠 **Smart:** An IoTsmart module is inserted into the HOST connector. Relay control, the latching-driver enable signal and the 5V module supply are provided through HOST, powered from the IoTsmart module.

🏗 **Mezzanine:** The module is installed into an IoTbase carrier board. Relay control, the latching-driver enable signal and the 5V module supply are provided through HOST.<br>
*Exception: SKU 040201302201, 040201302101 can be installed only with a spacer (Height Extender) or via a cable connection.*
<!-- SYNERGY_END -->

![latching](latching.svg)

## SKU

See [SKU.md](SKU.md)

## Version history

| Version | Notes |
|---|---|
| 3.02 | Initial GitHub release |
