# POSS1106 - Pi OLED System Stats

**POSS1106** is a lightweight system monitor for **Raspberry Pi 5** using a **1.3-inch OLED** (SH1106 controller). It solves the common "static noise/QR code" visual bug found when using standard SSD1306 drivers on 1.3" screens.

## Features
- Optimized for **SH1106** controllers.
- Displays: Hostname, IP Address, CPU usage & temperature, RAM status.
- Custom **pixel-art icons** drawn directly in code.
- **Power Save Mode**: Automatically hides the display during scheduled hours to prevent OLED burn-in.



## Hardware Wiring (I2C)
| OLED Pin | RPi Physical Pin | Description |
| :--- | :--- | :--- |
| **VDD** | Pin 1 | 3.3V Power |
| **GND** | Pin 9 | Ground |
| **SDA** | Pin 3 | GPIO 2 (SDA) |
| **SCK/SCL** | Pin 5 | GPIO 3 (SCL) |

## Quick Installation
1. **Enable I2C** via `sudo raspi-config` (Interface Options > I2C).
2. **Clone repo**:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/poss1106.git](https://github.com/YOUR_USERNAME/poss1106.git)
   cd poss1106