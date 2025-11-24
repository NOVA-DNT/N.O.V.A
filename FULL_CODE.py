# --- IMPORTACIONES ---
# -*- coding: utf-8 -*-

import serial
import time
import cv2
import numpy as np
from picamera2 import Picamera2
from gpiozero import PWMOutputDevice, Servo

class sensorUART:
    def __init__(self): 
        self.ser = None 
        try: 
            self.ser = serial.Serial('/dev/serial0', 115200, timeout=0.01)
            self.ser.reset_input_buffer()
            print("Sensores conectados.")
        except:
            print("ADVERTENCIA: Sensores NO detectados.")
        
    def leer_frontal(self):
        """Devuelve la distancia S2 en mm. Si falla, devuelve 2000 (lejos)."""
        distancia = 2000.0
        if self.ser and self.ser.in_waiting:
            try:
                linea = self.ser.readline().decode('utf-8', errors='ignore').strip()
                partes = linea.split(',')
                for parte in partes:
                    if "S2" in parte:
                        valor = float(parte.split(':')[1])
                        if valor > 0: distancia = valor
            except: pass
        return distancia
    
    def cerrar(self):
        if self.ser: self.ser.close()


motor = PWMOutputDevice(18, frequency=50)
direccion = Servo(17)

NEUTRO = 0.076
VELOCIDAD_BASE = 0.085

KP = 0.00020  # Fuerza de giro
KD = 0.00015  # Estabilidad (Amortiguador)
error_anterior = 0

motor.value = NEUTRO
direccion.value = 0
print("Hardware listo. Esperando...")

picam2 = Picamera2()
config = picam2.create_video_configuration(main={"size": (320, 240), "format": "RGB888"})
picam2.configure(config)
picam2.start()
print("Camara iniciada.")

def arranque():
	motor.value = 0.087
	time.sleep (0.2)
	motor.value = VELOCIDAD_BASE 

def calcular_velocidad_con_freno(velocidad_objetivo, distancia_s2):
    DISTANCIA_INICIO = 400.0 
    DISTANCIA_PARADA = 100.0
    
    if distancia_s2 > DISTANCIA_INICIO:
        return velocidad_objetivo
    
    if distancia_s2 < DISTANCIA_PARADA:
        return NEUTRO
    
    rango = DISTANCIA_INICIO - DISTANCIA_PARADA
    progreso = distancia_s2 - DISTANCIA_PARADA
    factor = progreso / rango # 0.0 a 1.0
    
    delta = velocidad_objetivo - NEUTRO
    vel_final = NEUTRO + (delta * factor)
    
    return vel_final

def analizar_camara(frame):
    gris = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    gris = cv2.flip(gris, -1)
    
    alto, ancho = gris.shape
    roi = gris[int(alto/2):, :]
    
    _, binaria = cv2.threshold(roi, 105, 255, cv2.THRESH_BINARY)

    ancho_roi = binaria.shape[1]
    tercio = int(ancho_roi / 3)

    izq = cv2.countNonZero(binaria[:, 0:tercio])
    cen = cv2.countNonZero(binaria[:, tercio:2*tercio])
    der = cv2.countNonZero(binaria[:, 2*tercio:])
    
    return izq, cen, der, binaria

def calcular_pd(izq, cen, der):
    global error_anterior
    
    error = izq - der
    
    derivada = error - error_anterior
    
    giro = (error * KP) + (derivada * KD)
    
    giro = giro * -1
    
    if giro > 1.0:
        giro = 1.0
    elif giro < -1.0:
        giro = -1.0
        
    error_anterior = error
        
    return giro

print("3 SEGUNDOS PARA ARRANCAR...")
time.sleep(3)
print("CARRERA INICIADA")

try:
    while True:
        frame = picam2.capture_array()

        distancia = sensores.leer_frontal()
               
        p_izq, p_cen, p_der, imagen_proc = analizar_camara(frame)

        angulo_servo = calcular_pd(p_izq, p_cen, p_der)
        direccion.value = angulo_servo
        
        if abs(angulo_servo) > 0.4:
            motor.value = VELOCIDAD_BASE * 0.85
        else:
            motor.value = VELOCIDAD_BASE

        vel_real = calcular_velocidad_con_freno(vel_objetivo, distancia)
        motor.value = vel_real
        
        cv2.imshow("Vision", imagen_proc)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nDeteniendo...")

except Exception as e:
    print("\nError: " + str(e))

finally:
    print("Apagando motores...")
    motor.value = NEUTRO
    motor.close()
    direccion.close()
    picam2.stop()
    cv2.destroyAllWindows()
    print("Fin.")
