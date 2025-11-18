#   N.O.V.A  
##  Navigation Operative Vehicle Autonomus

Este proyecto consiste en el diseño e implementación de un vehículo robótico autónomo de tracción trasera y dirección tipo Ackermann, optimizado para entornos de competencia. El sistema se basa en una arquitectura de procesamiento distribuido que integra visión por computadora, fusión sensorial y algoritmos de localización y mapeo simultáneo (SLAM) para ejecutar una estrategia de carrera de dos fases: reconocimiento de pista y optimización de trayectoria a alta velocidad.

## Indice
* [Hardware](#hardware)
    * [Car movement](#car-movement)
    * [Structural design](#structural-design)

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

## ⚙️ Requisitos

- Python 3.10+
- Django 4.2
- PostgreSQL 13+

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
