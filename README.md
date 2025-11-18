#   N.O.V.A  
##  Navigation Operative Vehicle Autonomus

Este proyecto consiste en el diseño e implementación de un vehículo robótico autónomo de tracción trasera y dirección tipo Ackermann, optimizado para entornos de competencia. El sistema se basa en una arquitectura de procesamiento distribuido que integra visión por computadora, fusión sensorial y algoritmos de localización y mapeo simultáneo (SLAM) para ejecutar una estrategia de carrera de dos fases: reconocimiento de pista y optimización de trayectoria a alta velocidad.

## Indice
* [Sistema de Movimiento y Selección de Motores](#Sistema-de-Movimiento-y-Selección-de-Motores)
    * [Sistema de Movimiento](#Sistema-de-Movimiento)
    * [Selección de Motores](#Selección-de-Motores)

* [Electronica y Sensores](#Electronica-y-Sensores)
    * [Lista de componentes](#Lista-de-componentes)

## Sistema de Movimiento y Selección de Motores

Para nosotros, desarrollar un vehículo autónomo requiere integrar tres pilares con la misma importancia: la mecánica, la electrónica y la programación. Sabíamos que un buen código necesita un chasis excelente para funcionar, así que decidimos utilizar una plataforma comercial como punto de partida para ser más eficientes.

Sin embargo, no nos limitamos a ensamblar el kit. Dedicamos una parte del proyecto a diseñar estructuras para el vehículo adaptadas a nuestras necesidades específicas. Nuestro objetivo fue asegurar que la parte física tuviera el mismo nivel de calidad y detalle que nuestro software, garantizando que los componentes mecánicos y la programación trabajen juntos sin problemas durante la competición.


### Sistema de Movimiento

La movilidad de nuestro robot autónomo se diseñó priorizando la velocidad y la precisión en el posicionamiento, elementos críticos para la competición WRO.  
El sistema de movimiento se basa en una tracción trasera (RWD) con eje motriz rígido y dirección tipo Ackerman en el eje delantero. Esta configuración fue elegida por su simplicidad mecánica y robustez, ya que optimiza la eficiencia de la tracción y reduce la complejidad del sistema motriz.

El robot se construyó sobre un chasis de acrílico tipo 4WD, con dimensiones de 248 mm de largo por 146 mm de ancho. El peso total del conjunto, sin carga de misión, es de aproximadamente 680 g, y con todos los componentes alcanza 1.4 kg.

### Selección de Motores

Para la tracción, se seleccionó un único motor encargado de impulsar el eje trasero. La potencia se transfiere directamente al eje motriz rígido mediante un sistema de engranajes rectos con la siguiente configuración:  
- Piñón del motor: 30 dientes  
- Piñón del eje trasero: 54 dientes  

Relación de Transmisión: La relación de transmisión se calcula como:

i = Zsalida / Zentrada = 54 / 30 = 1.8

Distribución a Ruedas: El eje trasero es rígido (sin diferencial), lo que asegura que ambas ruedas motrices giren a la misma velocidad angular en todo momento.

Selección e Implementación de Motores: Se eligió un motor eléctrico cepillado tipo RC 540 de 35T, que ofrece mayor velocidad a costa de un menor torque, adecuado para el balance buscado entre rendimiento y fuerza.


## Electronica y Sensores

Para lograr que el vehículo navegue de forma autónoma y precisa, diseñamos una arquitectura electrónica que separa el 'pensamiento' de la acción. Utilizamos un sistema de procesamiento dual donde un cerebro se encarga de la estrategia y la visión, mientras que otro se dedica exclusivamente a leer los sensores en tiempo real. A continuación, detallamos los componentes específicos que elegimos.

### Lista de componentes

1. Unidades de Procesamiento

   Raspberry Pi 4 Model B: Es la unidad central de procesamiento (CPU). Ejecuta el sistema operativo, los algoritmos de visión artificial, la estrategia de navegación y coordina el movimiento del vehículo.

   ESP32: Actúa como coprocesador dedicado a la adquisición de datos. Se encarga de leer los sensores I2C de alta velocidad y enviar la informacion limpia a la Raspberry Pi 4 mediante comunicación serial (UART), liberando carga del procesador principal.

3. Sensores de Percepción (Los Sentidos)
   
   3x Sensores de Distancia Láser (VL53L0X):
   Ubicación: Frontal, Lateral Izquierdo, Lateral Derecho.
   Función: Utilizan tecnología de Tiempo de Vuelo (ToF) para medir con precisión milimétrica la distancia a las paredes y obstáculos, permitiendo el mapeo de la   pista.

   1x Encoder Óptico (HC-020K):
   Ubicación: Eje trasero o caja de cambios.
   Función: Cuenta las revoluciones de la rueda para calcular la odometría (distancia lineal recorrida y velocidad actual).

   1x Cámara (Raspberry Pi Camera Module V2):
   Función: Captura imágenes de la pista en tiempo real para la detección de líneas y corrección visual de la trayectoria.

4. Actuadores y Potencia
   
   Motor DC (Brushed): Proporciona la tracción trasera para el desplazamiento del vehículo.
   Controlador de Velocidad Electrónico (ESC): Regula la potencia que recibe el motor desde la batería, permitiendo controlar la velocidad de avance y frenado mediante señales PWM desde la Raspberry Pi.

   Servomotor: Controla el sistema de dirección Ackermann para girar las ruedas delanteras con precisión angular.

   Batería LiPo (Polímero de Litio): Fuente de energía principal de alta descarga para alimentar tanto los motores (a través del ESC) como la electrónica de control (mediante reguladores de voltaje).

## 🚀 Instalación

```bash
git clone https://github.com/usuario/proyecto.git
cd proyecto
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

## 🧪 Tests

```bash
pytest        # Pruebas funcionales
flake8 .      # Estilo de código
black --check .  # Formato
```

## 🔐 Acceso de Ejemplo

**Admin:**
📧 admin@mail.com — 🔑 Abc123#

**Invitado:**
📧 user@mail.com — 🔑 Abc123#

## 🛣️ Roadmap

- [ ] Login con redes sociales
- [ ] API pública
- [ ] Dashboard mejorado

## 🖇️ Contribuye

```bash
# Fork → Crea rama → Cambios → Commit → Pull Request
```

Lee [CONTRIBUTING.md](.github/CONTRIBUTING.md) para más detalles.

## 📄 Licencia

MIT — ver [LICENSE](LICENSE.md)

⌨️ con ❤️ por [Brayan Diaz C](https://github.com/brayandiazc)
