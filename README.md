# IoTextra-Digital: Industrial Digital I/O Modules for MQTT & Node-RED Automation

## Overview

**IoTextra-Digital** is a family of isolated digital I/O modules designed for reliable operation in IoT, IIoT, and smart home environments.  
The modules support **36 VDC–tolerant** digital inputs and robust relay or solid-state relay outputs suitable for PLC-style panels and field wiring.

IoTextra modules integrate cleanly with IoTsmart MCU boards and can be used with MQTT and Node-RED workflows (e.g., via the IoTflow automation framework).

---

## Features & Capabilities

- Industrial-style digital I/O with **36 VDC** tolerant inputs  
- Opto-isolated inputs and relay/SSR outputs for improved noise immunity  
- Clean terminal block layout for fast, error-free wiring  
- Compatible with IoTsmart modules, Raspberry Pi PICO, and other MCUs  
- Suitable for long-term installations in smart buildings, labs, and light industrial systems  

---

## Hardware Specifications

Each IoTextra-Digital module has its own electrical and mechanical specifications, documented inside its versioned folder.

Typical specifications include:

- Maximum input voltage: **36 VDC**  
- Relay or SSR output ratings  
- Electrical thresholds and isolation design  
- Load and protection characteristics  
- Mechanical layout and terminal labeling  

Module folders:

- `Input/v3.02/`  
- `Relay2/v3.02/`  
- `SSR Small/v3.02/`  
- `Octal2/v3.02/`  

Refer to each module’s documentation for exact technical data.

---

## Digital I/O Channel Configuration

Channel mapping and wiring details are provided per module.

Documentation includes:

- Input and output channel numbering  
- Terminal block identification  
- Wiring patterns for switches, sensors, and loads  
- Recommended safety and polarity guidelines  

> **Important:**  
> NPN transistor outputs apply **only to the IoTextra Octal2 module**.  
> All other IoTextra modules use relays or solid-state relays.

---

## Wiring & Pinout Diagrams

Module-level wiring diagrams include:

- Terminal block layout  
- Polarity and signal direction  
- Relay/SSR load wiring examples  
- Safety considerations for higher-voltage operation  

See the diagrams located in:

- `Input/v3.02/`  
- `Relay2/v3.02/`  
- `SSR Small/v3.02/`  
- `Octal2/v3.02/`

---

## Software Support

IoTextra-Digital is a **hardware-only** series, but integrates cleanly into automation stacks:

Typical usage includes:

- Connecting module inputs/outputs to IoTsmart or Raspberry Pi PICO boards  
- Reading/writing digital I/O via GPIO or MCU firmware  
- Triggering MQTT events or Node-RED flows  
- Following IoTflow’s MQTT topic conventions for automation

### Examples

An `/examples/` folder is included, providing usage examples for common digital input/output workflows.

---

## Ordering Information

For SKUs, part numbers, and module-specific ordering details,  
please refer to the individual module folders:

- `Input/`  
- `Relay2/`  
- `SSR Small/`  
- `Octal2/`  

Each folder contains its own ordering notes and datasheets.

---

## Licensing

This repository uses separate licenses for each category of assets:

- **Code:** [`LICENSE_CODE.md`](./LICENSE_CODE.md) — MIT License  
- **Schematics & Documentation:** [`LICENSE_HARDWARE.md`](./LICENSE_HARDWARE.md) — CC BY-SA 4.0  
- **Documentation:** [`LICENSE_DOCS.md`](./LICENSE_DOCS.md)  
- **Media:** [`LICENSE_MEDIA.md`](./LICENSE_MEDIA.md)

