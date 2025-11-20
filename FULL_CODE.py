import time
import serial
import sys
import cv2
import numpy as np
from picamera2 import Picamera2
from gpiozero import PWMOutputDevice, Servo
from collections import deque

ESC_PIN = 18
esc = PWMOutputDevice(ESC_PIN, frequency=50)
NEUTRAL_SPEED = 0.074
BASE_SPEED = 0.085
MAX_SPEED = 0.089

SERVO_PIN = 17
steering = Servo(SERVO_PIN)

UART_PORT = '/dev/serial0'
UART_BAUD = 115200
TIMEOUT = 0.1

print("Inicinado Camara")
picam2 = Picamera2()
config = picam2.create_video_configuration(main={"size": (320, 240), "format": "RGB888"})
picam2.configure(config)
picam2.start() 

UMBRAL = 55

try: 
    while True: 
        frame = picam2.capture_array()
        gris = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        gris = cv2.flip(gris,0)
        height, width = gris.shape
        roi = gris[int(height/2):, :]
        _, imagen_binaria = cv2.threshold(roi, UMBRAL, 255, cv2.THRESH_BINARY)
        h_roi, w_roi = imagen_binaria.shape
        tercio = int(w_roi / 3)

        zona_izquierda = imagen_binaria[:, 0:tercio]
        zona_centro    = imagen_binaria[:, tercio:2*tercio]
        zona_derecha   = imagen_binaria[:, 2*tercio:]

        blancos_izq = cv2.countNonZero(zona_izquierda)
        blancos_cen = cv2.countNonZero(zona_centro)
        blancos_der = cv2.countNonZero(zona_derecha)

        visualizacion = cv2.cvtColor(imagen_binaria, cv2.COLOR_GRAY2BGR)
        cv2.line(visualizacion, (tercio, 0), (tercio, h_roi), (0, 255, 0), 2)
        cv2.line(visualizacion, (2*tercio, 0), (2*tercio, h_roi), (0, 255, 0), 2)

        texto = f"I:{blancos_izq}  C:{blancos_cen}  D:{blancos_der}"
        cv2.putText(visualizacion, texto, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        cv2.imshow("Vision 3 Zonas (Binaria)", visualizacion)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    pass
finally:
    picam2.stop()
    cv2.destroyAllWindows()
