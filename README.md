# POSS1106 - Raspberry Pi System Monitor

**POSS1106** is a lightweight system monitoring dashboard designed for **Raspberry Pi 5** using a **1.3-inch OLED display** (SH1106 controller).

Unlike standard scripts meant for 0.96" displays, this project is specifically optimized for the **SH1106** driver to prevent the common "static noise/shifting" visual bugs.

## 🚀 Features

* **Real-time Stats**: Displays Hostname, IP Address, CPU usage, CPU Temperature, and RAM usage.
* **Custom Icons**: Hand-drawn pixel-art hardware icons (ID Badge, Ethernet Port, Processor, and Memory Stick).
* **Smart Schedule**: Automatically hides the display during night hours (e.g., 23:00 - 07:00) to extend OLED lifespan and prevent burn-in.
* **Systemd Integration**: Runs as a background service, starting automatically on boot.

## 🛠 Hardware Connection

Based on the Raspberry Pi 5 GPIO layout, connect your OLED as follows:

| OLED Pin | RPi Physical Pin | Function |
| --- | --- | --- |
| **VCC** | Pin 1 | 3.3V Power |
| **GND** | Pin 9 | Ground |
| **SCL** | Pin 5 | GPIO 3 (I2C Clock) |
| **SDA** | Pin 3 | GPIO 2 (I2C Data) |

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

## ⚙️ Automatic Start (Service)

To make the dashboard run in the background on every boot:

1. Create the service file:

```bash
sudo nano /etc/systemd/system/poss1106.service
```


2. Paste the following configuration:

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
