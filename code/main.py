from machine import Pin
from utime import sleep
import network
import secrets
import socket
import ujson

wlan = network.WLAN(network.STA_IF)
wlan.active(True)

wlan.connect(secrets.ssid, secrets.password)

PORT = 25565

connection_timeout = 10
while connection_timeout > 0:
    if wlan.status() >= 3:
        break
    connection_timeout -= 1
    print("Waiting for WiFi")
    sleep(1)

if wlan.status() != 3:
    raise RuntimeError('Failed to establish wifi connection')
else:
    print("Connection successful!")
    network_info = wlan.ifconfig()
    print("IP ADDR:", network_info[0])


