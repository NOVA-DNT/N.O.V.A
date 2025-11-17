#!/usr/bin/env python3
import serial
import time
import sys

UART_PORT = '/dev/serial0' 
UART_BAUD = 115200
TIMEOUT = 1

def main():
    print("="*50)
    print("  Receptor UART - 3 Sensores VL53L0X")
    print("  Raspberry Pi 4")
    print("="*50)
    print()
    
    try:
        ser = serial.Serial(
            port=UART_PORT,
            baudrate=UART_BAUD,
            timeout=TIMEOUT,
            bytesize=serial.EIGHTBITS,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE
        )
        print(f"OK: Puerto {UART_PORT} abierto a {UART_BAUD} baudios")
        print(f"OK: Esperando datos del ESP32...\n")
        time.sleep(2)
        
    except serial.SerialException as e:
        print(f"ERROR: Error al abrir puerto serial: {e}")
        print("\nVerifica:")
        print("1. UART habilitado en raspi-config")
        print("2. Conexiones fisicas correctas")
        print("3. ESP32 conectado y funcionando")
        sys.exit(1)
    
    try:
        while True:
               if ser.in_waiting > 0:
                line = ser.readline().decode('utf-8').strip()
                
                if line:
                    try:
                        data = parse_sensor_data(line)
                        
                        if data:
                            print(f"S1: {format_distance(data['S1'])} | "
                                  f"S2: {format_distance(data['S2'])} | "
                                  f"S3: {format_distance(data['S3'])}")
                            
                            process_data(data)
                    
                    except Exception as e:
                        print(f"ADVERTENCIA: Error procesando: {line} - {e}")
            
            time.sleep(0.01)
    
    except KeyboardInterrupt:
        print("\n\nOK: Programa detenido por usuario")
    
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close()
            print("OK: Puerto serial cerrado")


def parse_sensor_data(line):

    try:
        parts = line.split(',')
        data = {}
        
        if len(parts) != 3:
            return None
            
        for part in parts:
            sensor, value = part.split(':')
            data[sensor.strip()] = float(value)
        
        if 'S1' in data and 'S2' in data and 'S3' in data:
            return data
        else:
            return None
    
    except (ValueError, IndexError):
        return None


def format_distance(distance):

    if distance < 0:
        return "ERROR  "
    else:
        return f"{distance:6.1f} mm"


def process_data(data):

    DISTANCIA_MINIMA = 100 
    
    if 0 < data['S1'] < DISTANCIA_MINIMA:
        print("  * ADVERTENCIA: Objeto detectado cerca del Sensor 1!")
    
    if 0 < data['S2'] < DISTANCIA_MINIMA:
        print("  * ADVERTENCIA: Objeto detectado cerca del Sensor 2!")
    
    if 0 < data['S3'] < DISTANCIA_MINIMA:
        print("  * ADVERTENCIA: Objeto detectado cerca del Sensor 3!")


if __name__ == "__main__":
    main()
