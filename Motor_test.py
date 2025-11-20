# -*- coding: utf-8 -*-
import time
from gpiozero import PWMOutputDevice

ESC_PIN = 18
esc = PWMOutputDevice(ESC_PIN, frequency=50)

print("--- PRUEBA DE MOTOR ---")

# Neutral
esc.value = 0.075
print("Motor en neutral...")
time.sleep(2)

print("Motor avanzando MEDIO...")
esc.value = 0.089  # VELOCIDAD MEDIA
time.sleep(100)

# DETENER
print("Motor detenido")
esc.value = 0.075
time.sleep(1)

esc.close()
print("Prueba finalizada")
