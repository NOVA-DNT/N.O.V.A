#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import serial
import sys
from typing import Optional, Dict

# Configuración
UART_PORT = '/dev/serial0'
UART_BAUD = 115200
TIMEOUT = 0.1  # Timeout reducido
DISTANCIA_MINIMA = 100.0

class SensorUART:
    def __init__(self):
        self.ser = None
        
    def conectar(self) -> bool:
        """Conecta al puerto serial"""
        try:
            self.ser = serial.Serial(
                port=UART_PORT,
                baudrate=UART_BAUD,
                timeout=TIMEOUT,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE
            )
            print(f"OK: Puerto {UART_PORT} abierto a {UART_BAUD} baudios\n")
            return True
            
        except serial.SerialException as e:
            print(f"ERROR: {e}")
            return False
    
    def leer_linea(self) -> Optional[str]:
        if self.ser and self.ser.in_waiting:
            try:
                return self.ser.readline().decode('utf-8', errors='ignore').strip()
            except:
                return None
        return None
    
    def cerrar(self):
        """Cierra el puerto serial"""
        if self.ser and self.ser.is_open:
            self.ser.close()
            print("\n[OK] Puerto cerrado")

def parse_datos(linea: str) -> Optional[Dict[str, float]]:
    try:
        partes = linea.split(',')
        if len(partes) != 3:
            return None
        
        datos = {}
        for parte in partes:
            sensor, valor = parte.split(':')
            datos[sensor] = float(valor)
        
        return datos if all(k in datos for k in ['S1', 'S2', 'S3']) else None
    except:
        return None

def mostrar_datos(datos: Dict[str, float]):
    def fmt(val):
        return "ERROR  " if val < 0 else f"{val:6.1f} mm"
    
    print(f"S1: {fmt(datos['S1'])} | S2: {fmt(datos['S2'])} | S3: {fmt(datos['S3'])}", end='')
    
    # Alertas en la misma línea
    alertas = []
    for sensor in ['S1', 'S2', 'S3']:
        if 0 < datos[sensor] < DISTANCIA_MINIMA:
            alertas.append(sensor)
    
    if alertas:
        print(f" [ALERTA: {','.join(alertas)}]")
    else:
        print()

def main():
    print("=" * 50)
    print("=" * 50)
    print()
    
    uart = SensorUART()
    
    if not uart.conectar():
        sys.exit(1)
    
    try:
        print("Recibiendo datos...\n")
        while True:
            linea = uart.leer_linea()
            
            if linea:
                datos = parse_datos(linea)
                if datos:
                    mostrar_datos(datos)
                    # Aquí puedes agregar lógica adicional
                    # guardar_datos(datos)s
                    # enviar_a_servidor(datos)
    
    except KeyboardInterrupt:
        print("\n\n[OK] Detenido por usuario")
    
    finally:
        uart.cerrar()

if __name__ == "__main__":
    main()
