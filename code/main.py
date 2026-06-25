from machine import Pin
from utime import sleep
import network
import secrets

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(secrets.ssid, secrets.password)


