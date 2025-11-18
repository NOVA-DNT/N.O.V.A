#   N.O.V.A  
##  Navigation Operative Vehicle Autonomus

Este proyecto consiste en el diseño e implementación de un vehículo robótico autónomo de tracción trasera y dirección tipo Ackermann, optimizado para entornos de competencia. El sistema se basa en una arquitectura de procesamiento distribuido que integra visión por computadora, fusión sensorial y algoritmos de localización y mapeo simultáneo (SLAM) para ejecutar una estrategia de carrera de dos fases: reconocimiento de pista y optimización de trayectoria a alta velocidad.

## Indice
* [Sistema de Movimiento y Selección de Motores](#Sistema-de-Movimiento-y-Selección-de-Motores)
    * [Sistema de Movimiento](#Sistema-de-Movimiento)
    * [Selección de Motores](#Selección-de-Motores)

* [Electronics and sensors](#electronics-and-sensors)
    * [List of components](#list-of-components)
    * [Sensor list](#sensor-list)
    * [Power Management](#power-management)
    * [PCB](#pcb)

* [Strategy and operation of the code](#strategy-and-operation-of-the-code)
    * [Slave code](#how-the-slave-code-works)
    * [Location of the robot](#location-of-the-robot-on-the-board)
    * [Open Challenge Strategy](#open-challenge-strategy)
    * [Obstacle Challenge Strategy](#obstacle-challenge-strategy)

* [Photos](#photos)
    * [Car images](#car-images)
    * [Team images](#team-images)

* [Demostration videos](#demonstration-videos)

## Sistema de Movimiento y Selección de Motores

Para nosotros, desarrollar un vehículo autónomo requiere integrar tres pilares con la misma importancia: la mecánica, la electrónica y la programación. Sabíamos que un buen código necesita un chasis excelente para funcionar, así que decidimos utilizar una plataforma comercial como punto de partida para ser más eficientes.

Sin embargo, no nos limitamos a ensamblar el kit. Dedicamos una gran parte del proyecto a modificar y rediseñar la estructura del vehículo para adaptarla a nuestras necesidades específicas. Nuestro objetivo fue asegurar que la parte física tuviera el mismo nivel de calidad y detalle que nuestro software, garantizando que los componentes mecánicos y la programación trabajen juntos sin problemas durante la competición.


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


## PHOTOS


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
