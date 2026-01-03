import os
import socket
import psutil
import time
from luma.core.interface.serial import i2c
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import ImageFont

# --- CONFIGURATION ---
START_HOUR = 7    # Hour to turn the screen ON
END_HOUR = 23     # Hour to turn the screen OFF
I2C_ADDR = 0x3C   # Standard I2C address for OLED

# Initialize the I2C interface and SH1106 device
serial = i2c(port=1, address=I2C_ADDR)
device = sh1106(serial)

def draw_custom_icons(draw):
    # --- 1. HOSTNAME: ID Badge Icon ---
    draw.rectangle((2, 2, 13, 11), outline="white") 
    draw.line((4, 5, 11, 5), fill="white")          
    
    # --- 2. IP: Ethernet Port Icon ---
    draw.rectangle((2, 18, 13, 27), outline="white") 
    draw.rectangle((5, 26, 10, 28), fill="white")    
    draw.line((4, 20, 11, 20), fill="white")

    # --- 3. CPU: Processor Icon ---
    draw.rectangle((3, 35, 12, 44), outline="white") 
    for i in range(35, 46, 3):
        draw.point((1, i), fill="white")  # Left pins
        draw.point((14, i), fill="white") # Right pins
        
    # --- 4. RAM: Memory Stick Icon ---
    draw.rectangle((1, 52, 14, 59), outline="white") 
    draw.rectangle((3, 54, 5, 57), fill="white")
    draw.rectangle((10, 54, 12, 57), fill="white")

def get_stats():
    # Retrieve system hostname
    hostname = socket.gethostname()
    
    # Retrieve local IP address
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except:
        ip = "Disconnected"
        
    # CPU usage and temperature
    cpu_usage = psutil.cpu_percent()
    temp = os.popen("vcgencmd measure_temp").readline().replace("temp=","").replace("'C\n","C")
    
    # RAM usage (percentage and used MB)
    ram = psutil.virtual_memory()
    ram_text = f"{ram.percent}% ({ram.used // 1048576}MB)"
    
    return hostname, ip, f"{cpu_usage}%  {temp}", ram_text

def is_active_time():
    # Check if the current time is within the active schedule
    current_hour = time.localtime().tm_hour
    if START_HOUR < END_HOUR:
        return START_HOUR <= current_hour < END_HOUR
    else:
        # Handles overnight schedules (e.g., 22:00 to 06:00)
        return current_hour >= START_HOUR or current_hour < END_HOUR

def main():
    font = ImageFont.load_default()
    screen_on = True
    print(f"POSS1106: OLED script started. Active hours: {START_HOUR}-{END_HOUR}")

    while True:
        if is_active_time():
            if not screen_on:
                device.show() # Wake up display
                screen_on = True
            
            hostname, ip, cpu, ram = get_stats()
            with canvas(device) as draw:
                draw_custom_icons(draw)
                # Text offset by 20px to make room for icons
                draw.text((20, 1),  hostname, font=font, fill="white")
                draw.text((20, 17), ip, font=font, fill="white")
                draw.text((20, 33), cpu, font=font, fill="white")
                draw.text((20, 49), ram, font=font, fill="white")
            time.sleep(2)
        else:
            if screen_on:
                device.clear()
                device.hide() # Power off the OLED panel
                screen_on = False
            time.sleep(60) # Check time every minute when inactive

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        device.clear()
        print("\nPOSS1106: Script stopped by user.")
        