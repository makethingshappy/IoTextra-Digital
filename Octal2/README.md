<!-- OVERVIEW_START -->
> **4x DI + 4x DO-NPN - IoTextra Octal2**
>
> 8-channel digital I/O module · 4 isolated inputs · 4 outputs · galvanic isolation · GPIO and/or I²C modes
>
> Bipolar and Extended signal modes · HOST and Qwiic connectors · 47×56 mm · 5 VDC supply
>
> Works with Raspberry Pi, Raspberry Pi Pico / Pico 2 (RP2040 / RP2350) and ESP32
>
> DIN-rail mounting: A 3D-printable DIN-rail mounting tray is available — <a href="https://www.printables.com/model/1802141-din-rail-mount-for-make-things-happy-iotextra">view on Printables</a>
>
> Part of the IoTextra series · compatible with IoTsmart and IoTbase · <a href="https://github.com/makethingshappy/iotextra-digital/tree/main/Octal2">Open Hardware</a>
>
> Hardware license: <a href="https://github.com/makethingshappy/iotextra-digital/blob/main/LICENSE_HARDWARE.md">CC BY-SA 4.0</a>
<!-- OVERVIEW_END -->

<!-- docs-sync:badges -->
[![Node-RED](https://img.shields.io/badge/Node--RED-8f0000)](#software) [![MQTT](https://img.shields.io/badge/MQTT-0c447c)](#software) [![Blynk](https://img.shields.io/badge/Blynk-007a4a)](#software) [![Tasmota](https://img.shields.io/badge/Tasmota-d4680a)](#software) [![Home Assistant](https://img.shields.io/badge/Home%20Assistant-0d7ab5)](#software)

<!-- PRODUCT_START -->
## Buy IoTextra Octal2

[IoTextra Octal2 at makethingshappy.io](https://makethingshappy.io/products/iotextra-octal2)
<!-- PRODUCT_END -->

<!-- SYNERGY_START -->
## Hardware Synergy

🔌 **Standalone:** Input states and output control are available through the HOST connector, or via the I²C bus using the onboard I/O expander.

🧠 **Smart:** An IoTsmart module is inserted into the HOST connector. I/O control and the 5V module supply are provided through HOST, powered from the IoTsmart module.

🏗 **Mezzanine:** The module is installed into an IoTbase carrier board. I/O control and the 5V module supply are provided through HOST.
<!-- SYNERGY_END -->

<!-- SOFTWARE_START -->
## Software

![Node-RED](https://img.shields.io/badge/Node--RED-8f0000)
- [IoTextra Octal2 Node-RED example flow](https://github.com/makethingshappy/IoTflow/blob/main/Node-RED%20Examples/octal_board_flow.json)

![MQTT](https://img.shields.io/badge/MQTT-0c447c)
- [IoTextra Octal2 MQTT example (Node-RED flow)](https://github.com/makethingshappy/IoTflow/blob/main/Node-RED%20Examples/octal_board_flow.json)

![Blynk](https://img.shields.io/badge/Blynk-007a4a)
- [IoTextra Octal2 Node-RED + Blynk example flow](https://github.com/makethingshappy/IoTflow/blob/main/Node-RED%20Examples/octal_board_flow_with_blynk.json)

![Tasmota](https://img.shields.io/badge/Tasmota-d4680a)
- [IoTextra Octal2 Tasmota template for IoTsmart ESP32-S3](https://github.com/makethingshappy/IoThome/blob/main/Tasmota_Templates/IoTsmart_ESP32-S3.md#iotextra-octal2)
- [IoTextra Octal2 Tasmota template for IoTsmart XIAO + XIAO ESP32-S3](https://github.com/makethingshappy/IoThome/blob/main/Tasmota_Templates/IoTsmart_XIAO_XIAO-ESP32-S3.md#iotextra-octal2)
- [IoTextra Octal2 Tasmota template for IoTbase NANO + Waveshare ESP32-S3-NANO](https://github.com/makethingshappy/IoThome/blob/main/Tasmota_Templates/IoTbase_Nano.md#iotextra-octal2)
- [IoTextra Octal2 Tasmota template for IoTbase Feather + Adafruit ESP32-C6 Feather](https://github.com/makethingshappy/IoThome/blob/main/Tasmota_Templates/IoTbase_Feather.md#iotextra-octal2)

![Home Assistant](https://img.shields.io/badge/Home%20Assistant-0d7ab5)
- [IoTextra Octal2 ESPHome config for IoTsmart ESP32-S3](https://github.com/makethingshappy/MTH-for-ESPHome/blob/main/Configs/IoTsmart_ESP32-S3/iotextra-octal2-v3-02-iotsmart-esp32s3-v2-01-gpio.yaml)
- [IoTextra Octal2 ESPHome config for IoTsmart XIAO + XIAO ESP32-S3](https://github.com/makethingshappy/MTH-for-ESPHome/blob/main/Configs/IoTsmart_XIAO_XIAO-ESP32-S3/iotextra-octal2-v3-02-iotsmart-xiao-v1-02-xiao-esp32s3-gpio.yaml)
- [IoTextra Octal2 ESPHome config for IoTbase PICO + Raspberry Pi Pico W](https://github.com/makethingshappy/MTH-for-ESPHome/blob/main/Configs/IoTbase_PICO_Raspberry-Pi-Pico-W/iotextra-octal2-v3-02-iotbase-pico-v3-05-pico-w-gpio.yaml)
- [IoTextra Octal2 ESPHome config for IoTbase NANO + Waveshare ESP32-S3-NANO](https://github.com/makethingshappy/MTH-for-ESPHome/blob/main/Configs/IoTbase_NANO_Waveshare-ESP32-S3-NANO/iotextra-octal2-v3-02-iotbase-nano-v3-06-ws-esp32s3-nano-gpio.yaml)
<!-- SOFTWARE_END -->

## SKU

See [SKU.md](SKU.md)

## Version history

| Version | Notes |
|---|---|
| 3.02 | Initial GitHub release |
