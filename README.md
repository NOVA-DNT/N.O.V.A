#   N.O.V.A  
## INDICE 
[1 Gestión de movilidad](#1-gestión-de-movilidad)
[2. Gestión de la potencia y los sentidos](#2-gestión-de-la-potencia-y-los-sentidos)
[3. Gestión de obstáculos](#3-gestión-de-obstáculos)
[4. Fotos- Equipo y vehículo](#4-fotos--equipo-y-vehículo)
[5. Performance videos](#5-performance-videos)
[6. Utilización de Github](#6-utilización-de-github)
[7. Factor de ingeniería](#7-factor-de-ingeniería)
## 1 Gestión de movilidad 

### 1.1 Sistema de Movimiento y Selección de Motores

La movilidad de nuestro robot autónomo se diseñó priorizando la velocidad y la precisión en el posicionamiento, elementos críticos para la competición WRO.  
El sistema de movimiento se basa en una tracción trasera (RWD) con eje motriz rígido y dirección tipo Ackerman en el eje delantero. Esta configuración fue elegida por su simplicidad mecánica y robustez, ya que optimiza la eficiencia de la tracción y reduce la complejidad del sistema motriz.

El robot se construyó sobre un chasis de acrílico tipo 4WD, con dimensiones de 248 mm de largo por 146 mm de ancho. El peso total del conjunto, sin carga de misión, es de aproximadamente 680 g, y con todos los componentes alcanza 1.4 kg.

Distribución a Ruedas: El eje trasero es rígido (sin diferencial), lo que asegura que ambas ruedas motrices giren a la misma velocidad angular en todo momento.

Selección e Implementación de Motores: Se eligió un motor eléctrico cepillado tipo RC 540 de 35T, que ofrece mayor velocidad a costa de un menor torque, adecuado para el balance buscado entre rendimiento y fuerza.

### 1.2  Diseño y Montaje del Chasis/Estructura

El diseño del chasis fue fundamental para garantizar la estabilidad y mantener un centro de gravedad bajo. La plataforma está construida sobre un chasis de acrílico tipo 4WD, con dimensiones de 248 mm × 146 mm y un peso aproximado de 680 g sin carga, alcanzando alrededor de 1.4 kg con todos los elementos montados.

La distribución interna de los módulos fue cuidadosamente organizada para equilibrar el peso y facilitar el acceso a las zonas de calibración y mantenimiento. Los componentes instalados son los siguientes:

Raspberry Pi 4 Model B
ESP32
3 × Sensores de distancia láser VL53L0X
1 × Encoder óptico HC-020K
1 × Cámara Raspberry Pi Camera Module V2
Actuadores y Sistema de Potencia
Motor DC tipo brushed
Controlador de Velocidad Electrónico (ESC)
Servomotor

## 1.3 Principios de Ingeniería Aplicados
El desempeño del robot se fundamenta en la aplicación de principios básicos de dinámica, cinemática y diseño mecánico, considerando una masa operacional de 1.4 kg y una masa de diseño de 1.5 kg para incorporar un margen de seguridad. A continuación, se presentan los criterios técnicos que guiaron la selección del motor, la relación de engranes, el chasis y la gestión del movimiento.

Para garantizar que el sistema motriz cumpliera con los requerimientos de aceleración, tracción y velocidad, se establecieron los siguientes parámetros:

Masa tomada para cálculo: 1.5 kg

Radio de la rueda: 0.035 m (diámetro 0.07 m)

Gravedad: 9.81 m/s²

Aceleración deseada en maniobra rápida: 1.0 m/s²

Coeficiente de resistencia a la rodadura: 0.05


Estos valores se usaron para estimar las fuerzas que el motor debía superar y definir el torque mínimo necesario en el eje de ruedas.

#### 1.3.1 Cálculo de Fuerzas Requeridas

Fuerzas primarias

Peso normal: N = m \cdot g = 1.5 \cdot 9.81 = 14.715\N

Fuerza de aceleración: Facc = m \cdot a = 1.5 \cdot 1 = 1.5\N

Fuerza por resistencia a la rodadura: Frr = Crr \cdot N = 0.05 \cdot 14.715 = 0.73575\N

Fuerza total en terreno plano: Ftotal = Facc + Frr = 2.23575\ \N. Caso conservador (incluyendo fricción adicional y pequeñas pendientes)

En los cálculos extendidos del proyecto se obtuvo una fuerza total máxima de:

Ftotal\max = 4.791\N

Este valor se utilizó para garantizar que el motor seleccionado funcionara incluso en situaciones adversas.

#### 1.3.2 Torque Requerido en el Eje

Torque en el eje de ruedas (caso conservador) : Taxle = Ftotal\_max \cdot r = 4.791 \cdot 0.035 = 0.1677\ N·m

Torque por rueda, el sistema de tracción trasera transmite el par equitativamente a dos ruedas motrices: Twheel = 0.0838\N·m

#### 1.3.3 Potencia Mecánica Requerida

Se estimó la potencia usando las dos formulaciones fundamentales:

Potencia por fuerza y velocidad lineal: P = F cdot v \approx 2.667\ W

Potencia por torque y velocidad angular: P = T \cdot \omega \approx 4.00\ W
Ambos resultados confirman que el robot requiere solo unos pocos watts de potencia mecánica continua, lo que es compatible con motores RC de escala pequeña.

#### 1.3.4 Selección del Motor y Relación de Engranes

Compromiso Velocidad–Par

Se realizó un análisis comparando la velocidad y el torque que ofrecen motores comerciales disponibles en tablas técnicas.
El motor que cumplió mejor con los requisitos fue un: → Motor RC 540 de 35T

Este motor destaca por su alta velocidad de giro, lo que permite obtener una buena velocidad máxima en misión.

Relación de engranajes seleccionada: 1.8 : 1 (54T / 30T)

Justificación técnica

Aumenta el torque disponible en las ruedas sin sacrificar excesivamente la velocidad, compensa la naturaleza de alta velocidad del motor RC 540, asegura que se supere la inercia inicial del robot y se alcance la aceleración deseada bajo carga, mantiene un desempeño competitivo para pruebas cronometradas.

Torque mínimo que debe entregar el motor (considerando la reducción)

T_motor_min = 0.1677 N·m / 1.8 = 0.093 N·m

Valor que está dentro de lo que puede entregar un motor RC 540 operando en condiciones normales.

La gestión de potencia, tracción y control: Fue diseñada para garantizar un desplazamiento eficiente, estable y preciso en todas las etapas de la misión. El movimiento del robot se controla mediante un Controlador de Velocidad Electrónico (ESC), el cual regula la velocidad del motor en función del ciclo de trabajo (PWM) enviado desde la unidad de procesamiento. Dado que la velocidad angular del motor es prácticamente proporcional al PWM —mientras el voltaje de la batería se mantenga constante—, este sistema permite ajustes finos en la aceleración y velocidad. Además, se recomienda el uso de rampas de aceleración para evitar picos de corriente y prevenir deslizamientos al inicio de la marcha.

Transmisión de potencia: Se emplea un sistema de tracción trasera (RWD) con eje rígido. Esta configuración entrega el 100% del par a las ruedas motrices sin las pérdidas típicas asociadas a un diferencial, lo que mejora la eficiencia mecánica y simplifica el montaje general del tren motriz. El chasis fue diseñado para ser rígido, estable y equilibrado, incorporando adecuadamente los componentes electrónicos y eléctricos, y asegurando una correcta distribución de masas para mejorar la adherencia y la maniobrabilidad.

Selección del motor y su interacción con el sistema de transmisión: Se realizó un análisis previo para encontrar el equilibrio adecuado entre velocidad y par. El motor RC 540 de 35T fue elegido porque ofrece una alta velocidad de giro, permitiendo alcanzar mayores velocidades en recorrido recto. Para compensar esta característica y asegurar que el robot pueda vencer la inercia inicial, acelerar con eficacia y mover una masa de 1.4 kg, se definió una relación de reducción de 1.8:1 (54 dientes / 30 dientes). Esta relación incrementa el par disponible sin sacrificar en exceso la velocidad, logrando un compromiso ideal para cumplir con los tiempos de misión y garantizar la fuerza de tracción necesaria.

Finalmente, la cinemática de giro se resuelve mediante la implementación de la geometría Ackerman en el eje delantero. Debido a que el eje trasero es rígido, las ruedas motrices no pueden girar a velocidades diferentes durante una curva, lo cual genera arrastre en la rueda interior. La dirección Ackerman minimiza este problema al permitir que las ruedas delanteras adopten ángulos de giro específicos para cada una, reduciendo el arrastre, mejorando la estabilidad en curva y acercando la trayectoria real a la trayectoria ideal. Esto se traduce en un giro más suave, preciso y eficiente, incluso con las limitaciones naturales de un eje rígido sin diferencial.

### 1. 4 Instrucciones de Construcción y Archivos CAD
El robot utiliza un chasis base comercial de acrílico (adquirido en Mercado Libre). Por lo tanto, no se requiere un modelo CAD completo del chasis.
Sin embargo, el equipo diseñó y fabricó u dos (2) piezas personalizadas esenciales para la integración de los actuadores y sensores:
Base de Montaje de la Cámara: Una estructura diseñada en SolidWorks para asegurar la cámara de visión de manera estable y a una altura optimizada para la detección de líneas.
Engranaje Motriz del Eje Trasero: Esta pieza fue rediseñada en SolidWorks y fabricada debido a una falla crítica en el engranaje original del kit.Justificación de Ingeniería: El engranaje original se estropeó por sobrecalentamiento/fricción (derretimiento). El nuevo diseño garantiza la tolerancia térmica y la resistencia mecánica necesarias para soportar el torque del motor RC 540 de 35T sin comprometer la relación de transmisión de 1.8:1

## 2. Gestión de la potencia y los sentidos 
El diseño de la arquitectura eléctrica y de percepción se basa en un enfoque de aislamiento de potencia y redundancia sensorial para garantizar la estabilidad operativa y la precisión en la navegación.
### 2.1 Gestión de la Energía (Aislamiento de Potencia)
La estrategia de energía utiliza un sistema de doble batería LiPo para aislar los sistemas de potencia (motores/actuadores) de los sistemas lógicos (procesamiento/sensores).
* Fuente de Energía: Dos (2) Baterías LiPo de 5200 mAh, 7.4 V (2 celdas).
Justificación del Aislamiento: Esta configuración de doble batería es fundamental para mitigar el "problema de la caída de voltaje (Brownout)".
* Batería 1 (Actuadores): Dedicada exclusivamente al Motor DC (Brushed) de tracción y al Servomotor de dirección (a través del ESC). Esta batería absorbe los picos de consumo y las caídas de voltaje de los motores sin afectar la electrónica sensible.
* Batería 2 (Lógica y Sensores): Dedicada a la Raspberry Pi 4 (CPU) y a todos los sensores. Esto garantiza un suministro de voltaje limpio y estable a los componentes de procesamiento, evitando reinicios inesperados que comprometerían la ejecución de la estrategia de navegación.
### 2.2 Selección e Implementación de Sensores (Los Sentidos)
La selección de sensores está orientada a proporcionar al robot la información precisa y de baja latencia necesaria para la localización y la corrección de trayectoria en tiempo real.
* 3x Sensores de Distancia Láser (VL53L0X): Utilizan tecnología Time-of-Flight (ToF). Son esenciales para el mapeo de la pista y la corrección lateral de la trayectoria (paredes). Su precisión milimétrica minimiza el error acumulado en el posicionamiento.
* 1x Cámara (ArduCam V3 12MP): Captura de imágenes de alta resolución. Utilizada para Visión Artificial, permitiendo la detección de líneas, el reconocimiento de patrones y la corrección visual de la trayectoria.

## 3. Gestión de obstáculos 
## 4. Fotos- Equipo y vehículo
<img width="751" height="489" alt="Captura de pantalla 2025-11-18 201911" src="https://github.com/user-attachments/assets/553cd6fb-8abc-4d31-b46e-da50b13f9ae0" />

## 5. Performance videos 
https://www.youtube.com/channel/UCp8W6HJ0NGMzdpxV4bdbbew

## 6. Utilización de Github
NOVA-DNT/N.O.V.A: N.O.V.A (Navigation Operative Vehicle Autonomus) WRO

## 7. Factor de ingeniería
El robot utiliza un chasis base comercial de acrílico (adquirido en Mercado Libre). Por lo tanto, no se requiere un modelo CAD completo del chasis.
Sin embargo, el equipo diseñó y fabricó u dos (2) piezas personalizadas esenciales para la integración de los actuadores y sensores:
Base de Montaje de la Cámara: Una estructura diseñada en SolidWorks para asegurar la cámara de visión de manera estable y a una altura optimizada para la detección de líneas.
Engranaje Motriz del Eje Trasero: Esta pieza fue rediseñada en SolidWorks y fabricada debido a una falla crítica en el engranaje original del kit. 
Justificación de Ingeniería: El engranaje original se estropeó por sobrecalentamiento/fricción (derretimiento). El nuevo diseño garantiza la tolerancia térmica y la resistencia mecánica necesarias para soportar el torque del motor RC 540 de 35T sin comprometer la relación de transmisión de 1.8:1


