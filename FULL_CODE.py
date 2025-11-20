# -*- coding: utf-8 -*-
import time
import cv2
import numpy as np
from picamera2 import Picamera2
from gpiozero import PWMOutputDevice, Servo

ESC = PWMOutputDevice(18, frequency=50)
direccion = Servo(17)

NEUTRO = 0.075
VELOCIDAD = 0.085 

# Inicializar en reposo
ESC.value = NEUTRO
direccion.value = 0
print("Hardware inicializado. Motor en Neutro.")


picam2 = Picamera2()
config = picam2.create_video_configuration(main={"size": (320, 240), "format": "RGB888"})
picam2.configure(config)
picam2.start()
print("Camara iniciada")


def analizar_camara(frame):
    gris = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gris = cv2.flip(gris, 0)
    
    alto, ancho = gris.shape
    roi = gris[int(alto/2):, :]
    
    _, binaria = cv2.threshold(roi, 60, 255, cv2.THRESH_BINARY)

    ancho_roi = binaria.shape[1]
    tercio = int(ancho_roi / 3)

    izq = cv2.countNonZero(binaria[:, 0:tercio])
    cen = cv2.countNonZero(binaria[:, tercio:2*tercio])
    der = cv2.countNonZero(binaria[:, 2*tercio:])
    
    return izq, cen, der, binaria

def decidir_direccion(izq, cen, der):
    MARGEN = 500 
    giro = 0
    
    if izq > (der + MARGEN):
        giro = -1 
    elif der > (izq + MARGEN):
        giro = 1 
    else:
        giro = 0 
        
    return giro


print("3 SEGUNDOS PARA ARRANCAR")
time.sleep(3)

ESC.value = VELOCIDAD

try:
    while True:
        frame = picam2.capture_array()
        imagen_color = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        p_izq, p_cen, p_der, imagen_procesada = analizar_camara(frame)
        
        angulo_servo = decidir_direccion(p_izq, p_cen, p_der)
        
        direccion.value = angulo_servo
        
        cv2.imshow("Vision Robot", imagen_procesada)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Deteniendo por usuario")

except Exception as e:
    print("Error")

finally:
    # F. APAGADO DE EMERGENCIA (Muy importante)
    print("Frenando motor")
    ESC.value = NEUTRO
    ESC.close()
    direccion.close()
    picam2.stop()
    cv2.destroyAllWindows()
    print("Sistema apagado")
