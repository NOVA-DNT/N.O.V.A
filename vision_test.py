# -*- coding: utf-8 -*-
import cv2 
import numpy as np
from picamera2 import Picamera2

picam2 = Picamera2()
config = picam2.create_video_configuration(main={"size": (720, 480)})
picam2.configure(config)

# Autofoco continuo mejorado
picam2.set_controls({
    "AfMode": 2,  # Continuous autofocus
    "AfSpeed": 1,  # Velocidad rapida (0=lento, 1=rapido)
    "AfRange": 1   # 0=normal, 1=macro (objetos muy cerca)
})

picam2.start()
print("Camara con autofoco continuo. Presiona 'q' para salir")

try: 
    while True: 
        frame = picam2.capture_array()
        img_opencv = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        img_opencv = cv2.flip(img_opencv, -1)
        
        cv2.imshow("Robot Vision (Presiona Q)", img_opencv)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    picam2.stop()
    cv2.destroyAllWindows()
    print("Captura finalizada")

#hola
