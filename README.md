<div align="center">
  
```text
                    ██████╗  ██████╗ ███████╗███████╗ ██╗ ██╗ ██████╗  ██████╗ 
                    ██╔══██╗██╔═══██╗██╔════╝██╔════╝███║███║██╔═████╗██╔════╝ 
                    ██████╔╝██║   ██║███████╗███████╗╚██║╚██║██║██╔██║███████╗
                    ██╔═══╝ ██║   ██║╚════██║╚════██║ ██║ ██║████╔╝██║██╔═══██╗
                    ██║     ╚██████╔╝███████║███████║ ██║ ██║╚██████╔╝╚██████╔╝
                    ╚═╝      ╚═════╝ ╚══════╝╚══════╝ ╚═╝ ╚═╝ ╚═════╝  ╚═════╝ 
```

</div>

# Raspberry Pi System Monitor
  
![Status](https://img.shields.io/badge/Status-Work_in_Progress-yellow)
![License](https://img.shields.io/badge/License-MIT-blue.svg)
![Platform](https://img.shields.io/badge/Raspberry_Pi-5-C51A4A?logo=raspberry-pi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.13+-3776AB?logo=python&logoColor=white)


**POSS1106** is a lightweight system monitoring dashboard designed for **Raspberry Pi 5** using a **1.3-inch OLED display** (SH1106 controller).

Unlike standard scripts meant for 0.96" displays, this project is specifically optimized for the **SH1106** driver to prevent the common "static noise/shifting" visual bugs.

## 🚀 Features

* **Real-time Stats**: Displays Hostname, IP Address, CPU usage, CPU Temperature, and RAM usage.
* **Custom Icons**: Hand-drawn pixel-art hardware icons (ID Badge, Ethernet Port, Processor, and Memory Stick).
* **Smart Schedule**: Automatically hides the display during night hours (e.g., 23:00 - 07:00) to extend OLED lifespan and prevent burn-in.
* **Systemd Integration**: Runs as a background service, starting automatically on boot.

## 📸 Preview

![Image](https://github.com/user-attachments/assets/76830306-c345-4f59-9e8a-b5f4f7e64d7e)

## 🔌 Hardware Connection

Based on the Raspberry Pi 5 GPIO layout, connect your OLED as follows:

| OLED Pin | RPi Physical Pin | Function |
| --- | --- | --- |
| **VCC** | Pin 1 | 3.3V Power |
| **GND** | Pin 9 | Ground |
| **SCL** | Pin 5 | GPIO 3 (I2C Clock) |
| **SDA** | Pin 3 | GPIO 2 (I2C Data) |

Below is a character-based map of the Raspberry Pi 5 header. 
Only the pins used for the OLED (SH1106) are labeled for clarity.

```text
             Raspberry Pi 5 GPIO Header (Partial)
            +------------------------------------+
            |      [PINS]            [PINS]      |
   (VCC) ---| ( 1) [O]  [ ] ( 2)                 |
   (SDA) ---| ( 3) [O]  [ ] ( 4)                 |
   (SCL) ---| ( 5) [O]  [ ] ( 6)                 |
            | ( 7) [ ]  [ ] ( 8)                 |
   (GND) ---| ( 9) [O]  [ ] (10)                 |
            | (11) [ ]  [ ] (12)                 |
            |      [...]             [...]       |
            +------------------------------------+
              [O] = Connected   [ ] = Empty
```

## 📥 Installation

### 1. Enable I2C Interface

Open the Raspberry Pi configuration tool:

```bash
sudo raspi-config
```

Navigate to **Interface Options** > **I2C** and select **Yes**. Then, finish and exit.

### 2. Clone the Repository

```bash
git clone https://github.com/adamsiem4/pi-oled-stats-sh1106.git
```

```bash
cd pi-oled-stats-sh1106
```

### 3. Setup Virtual Environment & Dependencies

Since Raspberry Pi OS (Bookworm) requires virtual environments:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

### 4. Test the Script

```bash
python poss1106.py
```
### 5. Edit the Script
('YOUR_NAME' should be changed to match your system)
```bash
nano /home/YOUR_NAME/pi-oled-stats-sh1106/poss1106.py
```


## ⚙️ Automatic Start (Service)

To make the dashboard run in the background on every boot:

1. Create the service file:

```bash
sudo nano /etc/systemd/system/poss1106.service
```


2. Paste the following configuration and change 'YOUR_NAME' to match your system:

```ini
[Unit]
Description=POSS1106 OLED Stats Display
After=network.target

[Service]
ExecStart=/home/YOUR_NAME/pi-oled-stats-sh1106/venv/bin/python /home/YOUR_NAME/pi-oled-stats-sh1106/poss1106.py
WorkingDirectory=/home/YOUR_NAME/pi-oled-stats-sh1106
StandardOutput=inherit
StandardError=inherit
Restart=always
User=YOUR_NAME

[Install]
WantedBy=multi-user.target

```


3. Enable and start the service:

```bash
sudo systemctl daemon-reload
```

```bash
sudo systemctl enable poss1106.service
```

```bash
sudo systemctl start poss1106.service
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

### Created by adamsiem4
