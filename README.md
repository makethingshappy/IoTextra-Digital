# IoTextra-Digital: Industrial Digital I/O Modules for MQTT & Node-RED Automation

## Overview

[**IoTextra-Digital**](https://makethingshappy.io/collections/digital-iotextra) is a family of isolated digital I/O modules designed for reliable operation in IoT, IIoT, and smart home environments.  
Each module combines digital inputs with relay, solid-state relay, transistor, or MOSFET outputs — the exact configuration, voltage range, and isolation technology vary by module and are documented in its own datasheet.

IoTextra modules integrate cleanly with IoTsmart MCU boards and can be used with MQTT and Node-RED workflows (e.g., via the IoTflow automation framework).

---

## Features & Capabilities

- Industrial-grade digital I/O, galvanically isolated per channel
- Relay, solid-state relay, transistor, or MOSFET outputs depending on the module
- Clean terminal block layout for fast, error-free wiring
- Compatible with IoTsmart modules, Raspberry Pi PICO, and other MCUs
- Suitable for long-term installations in smart buildings, labs, and light industrial systems

---

## Hardware Specifications

Each IoTextra-Digital module has its own electrical and mechanical specifications, documented inside its versioned folder.

Module folders:

- **[Input](./Input/)**
- **[MOSFET2](./MOSFET2/)**
- **[Octal](./Octal/)**
- **[Octal2](./Octal2/)**
- **[Octal3](./Octal3/)**
- **[Octal4](./Octal4/)**
- **[Relay](./Relay/)**
- **[Relay2](./Relay2/)**
- **[SSR Small](./SSR%20Small/)**

Typical documentation includes:

- Maximum input voltage and isolation rating (varies by module — see individual datasheet)
- Output type and ratings (relay, SSR, transistor, or MOSFET)
- Electrical thresholds and isolation design
- Load and protection characteristics
- Mechanical layout and terminal labeling

Refer to each module's documentation for exact technical data.

---

## Digital I/O Channel Configuration

Documentation includes:

- Input and output channel numbering
- Terminal block identification
- Wiring patterns for switches, sensors, and loads
- Recommended safety and polarity guidelines

> **Important:**  
> Output type differs by module — NPN transistor outputs (Octal2), MOSFET outputs (MOSFET2), and relay or solid-state relay outputs (all other modules). Check the specific module's datasheet before wiring.

---

## Wiring & Pinout Diagrams

Module-level wiring diagrams include:

- Terminal block layout  
- Polarity and signal direction  
- Relay/SSR/transistor/MOSFET load wiring examples  
- Safety considerations for higher-voltage operation  

See the diagrams located in each module's folder listed above.

---

## Software Support

IoTextra-Digital is a **hardware-only** series, but integrates cleanly into automation stacks.

Typical usage includes:

- Connecting module inputs/outputs to IoTsmart or Raspberry Pi PICO boards  
- Reading/writing digital I/O via GPIO or MCU firmware  
- Triggering MQTT events or Node-RED flows  
- Following IoTflow's MQTT topic conventions for automation

---

## Examples

IoTextra-Digital modules are used together with [**IoTsmart**](https://makethingshappy.io/collections/iotsmart) or [**IoTbase**](https://makethingshappy.io/collections/iotbase) boards and [**IoTflow-based**](https://makethingshappy.io/pages/iotflow) automation.

Module-specific diagrams and connection examples are included inside each module's folder listed above.

### MCU Firmware Examples (IoTsmart)

IoTsmart does **not** yet contain its own `/examples` folder.  
Firmware reference examples will be added in a future update.

### Node-RED Automation Examples (IoTflow)

👉 **IoTflow Node-RED Examples**  
https://github.com/makethingshappy/IoTflow/tree/main/Node-RED%20Examples

---

## Ordering Information

### 📦 SKU Information  
The complete list of SKUs is provided in the following PDF located in the repository root:

- **SKU Digital IoTextra.pdf**

---

### 🛒 Purchase Links  
Order directly from the official store:

* [**IoTextra Input Module**](https://makethingshappy.io/collections/digital-iotextra/products/iotextra-input)
* [**IoTextra MOSFET2 Module**](https://makethingshappy.io/collections/digital-iotextra/products/iotextra-mosfet2)
* [**IoTextra Octal Module**](https://makethingshappy.io/collections/digital-iotextra/products/iotextra-octal)
* [**IoTextra Octal2 Module**](https://makethingshappy.io/collections/digital-iotextra/products/iotextra-octal2)
* [**IoTextra Octal3 Module**](https://makethingshappy.io/collections/digital-iotextra/products/iotextra-octal3)
* [**IoTextra Octal4 Module**](https://makethingshappy.io/collections/digital-iotextra/products/iotextra-octal4)
* [**IoTextra Relay2 Module**](https://makethingshappy.io/collections/digital-iotextra/products/iotextra-relay2)
* [**IoTextra SSR Small Module**](https://makethingshappy.io/collections/digital-iotextra/products/iotextra-ssr-small)

---

## Licensing

This repository uses separate licenses for each category of assets:

- **Code:** [`LICENSE_CODE.md`](./LICENSE_CODE.md) — MIT License  
- **Schematics & Documentation:** [`LICENSE_HARDWARE.md`](./LICENSE_HARDWARE.md) — CC BY-SA 4.0  
- **Documentation:** [`LICENSE_DOCS.md`](./LICENSE_DOCS.md)  
- **Media:** [`LICENSE_MEDIA.md`](./LICENSE_MEDIA.md)
