<!-- OVERVIEW_START -->
> **4x DI + 4x Latching-DPDT - IoTextra Octal3**
>
> 4 isolated digital inputs · 4 latching DPDT relays · galvanic isolation · 3750 VRMS
>
> Inputs up to 36 VDC via GPIO · relay contacts 250 VAC / 220 VDC / 2 A · relay control via I²C → TCA9534A → DRV8837C
>
> Works with Raspberry Pi, Raspberry Pi Pico / Pico 2 (RP2040 / RP2350) and ESP32
>
> DIN-rail mounting: A 3D-printable DIN-rail mounting tray is available — <a href="https://www.printables.com/model/1802141-din-rail-mount-for-make-things-happy-iotextra">view on Printables</a>
>
> Part of the IoTextra series · compatible with IoTsmart and IoTbase · <a href="https://github.com/makethingshappy/iotextra-digital/tree/main/Octal3">Open Hardware</a>
>
> Hardware license: <a href="https://github.com/makethingshappy/iotextra-digital/blob/main/LICENSE_HARDWARE.md">CC BY-SA 4.0</a>
<!-- OVERVIEW_END -->

<!-- docs-sync:badges -->
[![Node-RED](https://img.shields.io/badge/Node--RED-8f0000)](#software) [![MQTT](https://img.shields.io/badge/MQTT-0c447c)](#software) [![Blynk](https://img.shields.io/badge/Blynk-007a4a)](#software) [![Tasmota](https://img.shields.io/badge/Tasmota-d4680a)](#software)

<!-- PRODUCT_START -->
## Buy IoTextra Octal3

[IoTextra Octal3 at makethingshappy.io](https://makethingshappy.io/products/iotextra-octal3)
<!-- PRODUCT_END -->

<!-- SYNERGY_START -->
## Hardware Synergy

🔌 **Standalone:** Input states are read through the HOST connector; relay control is via the I²C bus using the onboard I/O expander.

🧠 **Smart:** An IoTsmart module is inserted into the HOST connector. Input reading, relay control, and the 5V module supply are provided through HOST, powered from the IoTsmart module.

🏗 **Mezzanine:** The module is installed into an IoTbase carrier board. Input reading, relay control, and the 5V module supply are provided through HOST.<br>
*Exception: SKU 040304302311, 040304302309 can be installed only with a spacer (Height Extender) or via a cable connection.*
<!-- SYNERGY_END -->

<!-- SOFTWARE_START -->
## Software

![Node-RED](https://img.shields.io/badge/Node--RED-8f0000)
- [IoTextra Octal3 Node-RED example flow](https://github.com/makethingshappy/IoTflow/blob/main/Node-RED%20Examples/octal3_board_flow.json)

![MQTT](https://img.shields.io/badge/MQTT-0c447c)
- [IoTextra Octal3 MQTT example (Node-RED flow)](https://github.com/makethingshappy/IoTflow/blob/main/Node-RED%20Examples/octal3_board_flow.json)

![Blynk](https://img.shields.io/badge/Blynk-007a4a)
- [IoTextra Octal3 Node-RED + Blynk example flow](https://github.com/makethingshappy/IoTflow/blob/main/Node-RED%20Examples/octal3_board_flow_with_blynk.json)

![Tasmota](https://img.shields.io/badge/Tasmota-d4680a)
- [IoTextra Octal3 Tasmota template for IoTsmart ESP32-S3](https://github.com/makethingshappy/IoThome/blob/main/Tasmota_Templates/IoTsmart_ESP32-S3.md#iotextra-octal3)
- [IoTextra Octal3 Tasmota template for IoTbase NANO + Waveshare ESP32-S3-NANO](https://github.com/makethingshappy/IoThome/blob/main/Tasmota_Templates/IoTbase_Nano.md#iotextra-octal3)
<!-- SOFTWARE_END -->

![latching](latching.svg)

## SKU

See [SKU.md](SKU.md)

## Version history

| Version | Notes |
|---|---|
| 3.02 | Initial GitHub release |
