<!-- OVERVIEW_START -->
> **4x SPDT - IoTextra Relay2**
>
> 4-channel SPDT relay module · 250 VAC / 30 VDC · 10 A · GPIO and/or I²C modes
>
> Relay options: Panasonic ALQ105 · Omron G5Q-14 · HF33F/005-ZS3 · TE PE014005 · HOST and Qwiic connectors
>
> Works with Raspberry Pi, Raspberry Pi Pico / Pico 2 (RP2040 / RP2350) and ESP32
>
> DIN-rail mounting: A 3D-printable DIN-rail mounting tray is available — <a href="https://www.printables.com/model/1802141-din-rail-mount-for-make-things-happy-iotextra">view on Printables</a>
>
> Part of the IoTextra series · compatible with IoTsmart and IoTbase · <a href="https://github.com/makethingshappy/iotextra-digital/tree/main/Relay2">Open Hardware</a>
>
> Hardware license: <a href="https://github.com/makethingshappy/iotextra-digital/blob/main/LICENSE_HARDWARE.md">CC BY-SA 4.0</a>
<!-- OVERVIEW_END -->

<!-- docs-sync:badges -->
[![Node-RED](https://img.shields.io/badge/Node--RED-8f0000)](#software) [![MQTT](https://img.shields.io/badge/MQTT-0c447c)](#software) [![Blynk](https://img.shields.io/badge/Blynk-007a4a)](#software) [![Tasmota](https://img.shields.io/badge/Tasmota-d4680a)](#software) [![Home Assistant](https://img.shields.io/badge/Home%20Assistant-0d7ab5)](#software)

<!-- SYNERGY_START -->
## Hardware Synergy

- 🔌 **Standalone** — Relay control is available through the HOST connector, or via the I²C bus using the onboard I/O expander.
- 🧠 **Smart** — An IoTsmart module is inserted into the HOST connector. Relay control and the 5V module supply are provided through HOST, powered from the IoTsmart module.
  *Exception: SKU 040202302310, 040202302311 — only with a spacer (Height Extender) or via a cable connection.*
- 🏗 **Mezzanine** — The module is installed into an IoTbase carrier board. Relay control and the 5V module supply are provided through HOST.
  *Exception: SKU 040202302310, 040202302311, 040202302411 — only with a spacer (Height Extender) or via a cable connection.*
<!-- SYNERGY_END -->

<!-- SOFTWARE_START -->
## Software

![Node-RED](https://img.shields.io/badge/Node--RED-8f0000)
- [IoTextra Relay2 Node-RED example flow](https://github.com/makethingshappy/IoTflow/blob/main/Node-RED%20Examples/relay2_board_flow.json)

![MQTT](https://img.shields.io/badge/MQTT-0c447c)
- [IoTextra Relay2 MQTT — Node-RED example flow](https://github.com/makethingshappy/IoTflow/blob/main/Node-RED%20Examples/relay2_board_flow.json)

![Blynk](https://img.shields.io/badge/Blynk-007a4a)
- [IoTextra Relay2 Node-RED + Blynk example flow](https://github.com/makethingshappy/IoTflow/blob/main/Node-RED%20Examples/relay2_board_flow_with_blynk.json)

![Tasmota](https://img.shields.io/badge/Tasmota-d4680a)
- [IoTextra Relay2 Tasmota template — IoTsmart ESP32-S3](https://github.com/makethingshappy/IoThome/blob/main/Tasmota_Templates/IoTsmart_ESP32-S3.md#iotextra-relay2)
- [IoTextra Relay2 Tasmota template — IoTsmart XIAO + XIAO ESP32-S3](https://github.com/makethingshappy/IoThome/blob/main/Tasmota_Templates/IoTsmart_XIAO_XIAO-ESP32-S3.md#iotextra-relay2)
- [IoTextra Relay2 Tasmota template — IoTbase NANO + Waveshare ESP32-S3-NANO](https://github.com/makethingshappy/IoThome/blob/main/Tasmota_Templates/IoTbase_Nano.md#iotextra-relay2)
- [IoTextra Relay2 Tasmota template — IoTbase Feather + Adafruit ESP32-C6 Feather](https://github.com/makethingshappy/IoThome/blob/main/Tasmota_Templates/IoTbase_Feather.md#iotextra-relay2)

![Home Assistant](https://img.shields.io/badge/Home%20Assistant-0d7ab5)
- [IoTextra Relay2 ESPHome config — IoTsmart ESP32-S3](https://github.com/makethingshappy/MTH-for-ESPHome/blob/main/Configs/IoTsmart_ESP32-S3/iotextra-relay2-v3-02-iotsmart-esp32s3-v2-01-gpio.yaml)
- [IoTextra Relay2 ESPHome config — IoTsmart XIAO + XIAO ESP32-S3](https://github.com/makethingshappy/MTH-for-ESPHome/blob/main/Configs/IoTsmart_XIAO_XIAO-ESP32-S3/iotextra-relay2-v3-02-iotsmart-xiao-v1-02-xiao-esp32s3-gpio.yaml)
- [IoTextra Relay2 ESPHome config — IoTbase PICO + Raspberry Pi Pico W](https://github.com/makethingshappy/MTH-for-ESPHome/blob/main/Configs/IoTbase_PICO_Raspberry-Pi-Pico-W/iotextra-relay2-v3-02-iotbase-pico-v3-05-pico-w-gpio.yaml)
- [IoTextra Relay2 ESPHome config — IoTbase NANO + Waveshare ESP32-S3-NANO](https://github.com/makethingshappy/MTH-for-ESPHome/blob/main/Configs/IoTbase_NANO_Waveshare-ESP32-S3-NANO/iotextra-relay2-v3-02-iotbase-nano-v3-06-ws-esp32s3-nano-gpio.yaml)
<!-- SOFTWARE_END -->

<!-- DOCS_START -->
## Documentation

- [IoTextra Relay2 Datasheet, Rev. 3-02 (PDF)](https://makethingshappy.io/d040202302)
- [IoTextra Relay2 Schematic, Rev. 3-02 (PDF)](https://makethingshappy.io/s040202302)
- [IoTextra Relay2 Rev. 3-02 — GitHub](https://makethingshappy.io/g040202302)

Product page: [IoTextra Relay2 — buy at makethingshappy.io](https://makethingshappy.io/products/iotextra-relay2)
<!-- DOCS_END -->

## SKU

See [SKU.md](SKU.md)

## Version history

| Version | Notes |
|---|---|
| 3.02 | Initial GitHub release |
