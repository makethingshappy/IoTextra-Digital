# IoTextra-Digital  
Industrial Digital I/O Modules for MQTT, IoTsmart & Node-RED Automation

**IoTextra-Digital** is a family of isolated industrial digital I/O modules designed for reliable operation in IoT, IIoT, automation, and smart building environments.  
The modules support **36 VDC–tolerant digital inputs**, relay or SSR outputs, and clean integration with **IoTsmart MCU boards**, **MQTT**, and **Node-RED** through the IoTflow ecosystem.

IoTextra-Digital is part of the wider **IoTextra Ecosystem**, including:

- **IoTextra-Digital** – Digital I/O  
- **IoTextra-Analog** – Analog modules  
- **IoTextra-Combo** – Mixed-signal modules  
- **IoTsmart** – RP2040 / ESP32-S3 / RP2350A MCU boards  
- **IoTflow** – MQTT + Node-RED automation framework  

---

## 📦 Module Index

Each module includes versioned documentation (datasheet, schematic), media, and examples.

| Module | Channels | Output Type | Folder |
|--------|----------|-------------|--------|
| **Input** | 1–8 Inputs | Isolated Digital Inputs | [Input/v3.02](./Input/v3.02/) |
| **Relay2** | 2 Outputs | Relay Outputs | [Relay2/v3.02](./Relay2/v3.02/) |
| **SSR Small** | 1 Output | Solid-State Relay | [SSR Small/v3.02](./SSR%20Small/v3.02/) |
| **Octal2** | 8 Outputs | NPN Transistor Outputs | [Octal2/v3.02](./Octal2/v3.02/) |

---

## 🔧 Key Features

- **36 VDC tolerant** digital inputs  
- Opto-isolation for clean, noise-resistant signal integrity  
- Relay, SSR, or NPN transistor outputs depending on module  
- Screw-terminal field wiring for fast and reliable installation  
- Designed for industrial, lab, and automation environments  
- Fully compatible with **IoTsmart RP2040 / RP2350A / ESP32-S3** MCU boards  
- Works with **MQTT** and **Node-RED** (via IoTflow)

---

## 🛠 Hardware Documentation

Each module folder includes:

- **/docs** – Datasheet (PDF)  
- **/hardware** – Schematic (PDF)  
- **/media** – 3D views, PCB images, host-board diagrams  
- **/examples** – Python / MicroPython GPIO examples  

Quick navigation:

- **Input** → [Input/v3.02](./Input/v3.02/)  
- **Relay2** → [Relay2/v3.02](./Relay2/v3.02/)  
- **SSR Small** → [SSR Small/v3.02](./SSR%20Small/v3.02/)  
- **Octal2** → [Octal2/v3.02](./Octal2/v3.02/)  

---

## 🔌 Digital I/O Behavior

### **Input Module**
- Opto-isolated digital inputs  
- 36 VDC tolerant  
- Suitable for switches, sensors, PLC outputs  

### **Relay-Based Modules (Relay2 / SSR Small)**
- Fully isolated load side  
- Clean relay or SSR actuation  
- Ideal for building automation and low-current switching  

### **Octal2 Module**
⚠ **NPN transistor outputs apply ONLY to the Octal2 module.**  
All other modules use relays or solid-state relays.

---

## 🧰 Wiring & Pinout Resources

Module folders include:

- Terminal layouts  
- Channel numbering  
- Mechanical diagrams  
- MCU pairing images  
- Load wiring examples  

Located in:

- `Input/v3.02/media/`  
- `Relay2/v3.02/media/`  
- `SSR Small/v3.02/media/`  
- `Octal2/v3.02/media/`

---

## 🧑‍💻 Software Support

IoTextra-Digital is a **hardware-focused** series but integrates seamlessly with MCU firmware and automation platforms.

### ✔ With IoTsmart MCU Boards  
Use standard GPIO libraries on:

- RP2040  
- RP2350A  
- ESP32-S3  

Host pairing images are included in each module’s `/media` folder.

### ✔ With IoTflow (MQTT + Node-RED)  
IoTextra modules are compatible with:

- **IoTflow Kernel**  
- **IoTflow Forge** (configuration → JSON tools)  
- **node-red-contrib-iotextra**

IoTflow repository:  
https://github.com/makethingshappy/IoTflow

### ✔ Example Code  
Each module’s `/examples/` folder includes:

- Digital input reading  
- Relay / SSR output control  
- Automation workflows for Node-RED and MQTT

---

## 🛒 Ordering Information

Each module folder contains:

- SKU / part numbers  
- Ordering details  
- Supported MCU hosts  
- Mechanical specifications  

Navigate to:

- `/Input/`  
- `/Relay2/`  
- `/SSR Small/`  
- `/Octal2/`

---

## 📜 Licensing

Separate licenses apply depending on asset type:

- **Code** → [LICENSE_CODE.md](./LICENSE_CODE.md)  
- **Schematics & Hardware Docs** → [LICENSE_HARDWARE.md](./LICENSE_HARDWARE.md) (CC BY-SA 4.0)  
- **Documentation** → [LICENSE_DOCS.md](./LICENSE_DOCS.md)  
- **Media** → [LICENSE_MEDIA.md](./LICENSE_MEDIA.md)  

