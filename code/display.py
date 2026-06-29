import machine
import time

# --- Change your import to use the MIP folder structure ---
from lcd_i2c import LCD

# --- I2C Configuration ---
I2C_NUM = 0
SDA_PIN = 0
SCL_PIN = 1

# Initialize Hardware I2C
i2c = machine.I2C(I2C_NUM, sda=machine.Pin(SDA_PIN), scl=machine.Pin(SCL_PIN), freq=400000)

print("Scanning I2C bus...")
devices = i2c.scan()

if not devices:
    print("No I2C devices found! Check wiring.")
else:
    lcd_address = devices[0]
    print(f"Found LCD at Address: {hex(lcd_address)}")
    
    # Initialize the MIP library's LCD class
    # Arguments for this version: (i2c_instance, address, rows, columns)
    lcd = LCD(addr=lcd_address, cols=16, rows=2, i2c=i2c)
    
    # Test Display
    lcd.begin() # Some versions need an explicit begin/init call
    lcd.clear()
    lcd.print("I2C Mode Online!")
    
    while True:
        lcd.set_cursor(col=0, row=1)
        lcd.print("Status: Active *")
        time.sleep(0.5)
        lcd.set_cursor(col=0, row=1)
        lcd.print("Status: Active  ")
        time.sleep(0.5)