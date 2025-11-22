# IoTextra-Digital: Industrial Digital I/O Modules for MQTT & Node-RED Automation

## Overview

**IoTextra-Digital** is a family of isolated digital I/O modules designed for reliable use in IoT, IIoT, and smart home environments.  
The modules provide robust 24 V digital inputs and relay / solid-state relay outputs suitable for PLC-style panels, field wiring, and edge devices such as Raspberry Pi, Arduino-compatible boards, and IoTsmart.

These boards are intended to be used together with MQTT and Node-RED automation flows (for example via the [IoTflow](https://github.com/makethingshappy/IoTflow) project), but remain simple, standalone hardware modules that can be wired into any digital I/O control system.

## Features & Capabilities

- Isolated industrial digital I/O suitable for 24 V field wiring  
- Compatible with common single-board computers and microcontroller platforms  
- Opto-isolated inputs and relay / SSR outputs for improved safety and noise immunity  
- DIN-rail friendly form factor (on supported modules)  
- Clearly labeled terminal blocks for fast wiring and maintenance  
- Designed for long-term reliability in hobby, lab and light industrial environments  

> **Note:** Please refer to the module-specific documentation in each `/v3.02/` folder for exact ratings, pinouts and dimensions.

## Hardware Specifications

The exact specifications (number of channels, maximum current, voltage limits, isolation ratings, etc.) depend on the selected IoTextra-Digital module.

Typical parameters documented per module include:

- Supply voltage range  
- Input voltage thresholds  
- Output type (mechanical relay / solid-state relay / digital input)  
- Maximum load current and voltage  
- Isolation and protection features  

See the hardware documentation in:

- `Input/v3.02/`  
- `Octal2/v3.02/`  
- `Relay2/v3.02/`  
- `SSR Small/v3.02/`

for detailed per-board specifications.

## Digital I/O Channel Configuration

Each IoTextra-Digital module provides a fixed set of digital input and/or output channels.  
The channel mapping, default states and wiring examples are described in the module-level documentation.

Typical information includes:

- Channel numbering and terminal labeling  
- Which terminals correspond to inputs vs. outputs  
- Shared commons / reference lines  
- Example wiring for switches, sensors and loads  

Refer to the relevant `README.md` or datasheet inside each `/v3.02/` folder for full channel details.

## Wiring & Pinout Diagrams

Wiring and pinout information is provided per module, including:

- Terminal block layout  
- Signal names and polarity  
- Recommended wire types and gauges  
- Safety notes for higher-voltage loads on relay / SSR outputs  

Please consult the diagrams and images in:

- `Input/v3.02/`  
- `Octal2/v3.02/`  
- `Relay2/v3.02/`  
- `SSR Small/v3.02/`

before connecting the module to field wiring or loads.

## Software Support

While IoTextra-Digital is purely a hardware family, it is designed to integrate cleanly with MQTT-based and Node-RED-based automation stacks.

Typical usage patterns include:

- Connecting the module to a Raspberry Pi, IoTsmart board or similar device  
- Exposing the digital I/O through GPIO, I²C, SPI or other supported interfaces on the host  
- Publishing and subscribing to MQTT topics from Node-RED or other workflow tools

To accelerate development:

- See the code and flow **examples** in the `/examples/` folder of the relevant software repositories (for example, [IoTflow](https://github.com/makethingshappy/IoTflow)).  
- Use IoTflow’s Node-RED flows and MQTT topic conventions as a reference when integrating IoTextra-Digital modules into your own projects.

> This repository does **not** contain firmware or full software stacks – it documents the hardware used by those tools.

## SKU Table / Ordering Options

The IoTextra-Digital series currently includes the following modules:

| Module Name        | Type                        | Typical Use Case                                      |
|--------------------|-----------------------------|-------------------------------------------------------|
| **IoTextra Input** | Digital input module        | Reading industrial switches, sensors and 24 V signals |
| **IoTextra Relay2** | Relay output module        | Switching AC/DC loads via mechanical relays           |
| **IoTextra SSR Small** | Solid-state relay module | Quiet, fast switching of low-to-medium power loads    |
| **IoTextra Octal2** | Multi-channel I/O module   | Compact, multi-channel digital control                |

For detailed mechanical drawings, ratings and part numbers, please refer to the datasheets inside each module’s `/v3.02/` folder.

## Licensing

This repository uses separate licenses for different asset types:

- **Code:** [`LICENSE_CODE.md`](./LICENSE_CODE.md) – MIT License  
- **Hardware design files & schematics:** [`LICENSE_HARDWARE.md`](./LICENSE_HARDWARE.md) – CC BY-SA 4.0  
- **Documentation:** [`LICENSE_DOCS.md`](./LICENSE_DOCS.md)  
- **Media assets:** [`LICENSE_MEDIA.md`](./LICENSE_MEDIA.md)
