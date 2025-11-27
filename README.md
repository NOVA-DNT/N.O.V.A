#   N.O.V.A  
## INDEX 
* [1 Mobility Management](#1-movility-management)
* [2. Power  and  sensory  management](#2-power-and-sensory-management)
* [3.  Obstacle  Management](#3-obstacle-management)
* [4. Photos  -  Equipment  and  vehicle](#4-photos--equipment-and-vehicle)
* [5. Performance videos](#5-performance-videos)
* [6. Using Github](#6-using-github)
* [7. Engineering  Factor](#7-engineering-factor)
## 1. Mobility Management
### 1.1 Motor  Movement  and  Selection  System
The  mobility  of  our  autonomous  robot  was  designed  prioritizing  speed  and  positioning  accuracy,  critical  elements  for  the  WRO  competition.
The  drive  system  is  based  on  rear-wheel  drive  (RWD)  with  a  rigid  drive  axle  and  Ackerman-type  steering  on  the  front  axle.  This  configuration  was  chosen for  its  mechanical  simplicity  and robustness,  as  it  optimizes  traction  efficiency  and  reduces  the  complexity  of  the  drive  system.
The  robot  was  built  on  a  4WD-type  acrylic  chassis,  measuring  248  mm long  by  146  mm  wide.  The  total  weight  of  the  assembly,  without  mission  payload,  is approximately  680  g,  and  with  all  components  it  reaches  1.4  kg.

* Wheel  distribution:  The  rear  axle  is  rigid  (without  differential),  which  ensures  that  both  drive  wheels  rotate  at  the  same  angular  speed  at  all  times.
* Motor  Selection  and  Implementation:  A  brushed  electric  motor  was  chosen,  which  offers  higher  speed  at  the  cost  of  lower  torque,  suitable  for  the  desired balance  between  performance  and  strength.

### 1.2 Chassis/Structure  Design  and  Assembly
The  chassis  design  was  fundamental  to  ensuring  stability  and  maintaining  a  low  center  of  gravity.  
The  platform  is  built  on  a  4WD-type  acrylic  chassis,  measuring  248  mm  ×  146  mm  and  weighing  approximately  680  g  unloaded,  reaching  around  1.4  kg  with  all  components  assembled.
The  internal  layout  of  the  modules  was  carefully  organized  to  balance  the  weight  and  facilitate access  to  the  calibration  and  maintenance  areas.  The  installed  components  are  as  follows:  
* Raspberry  Pi  4  Model  B
* Esp32
* 3  ×  VL53L0X  Laser  Distance  Sensors
* 1  ×  Raspberry  Pi  Camera  Module  V2
* DC  motor  type  RC  540  of  35  T  brushed
* Electronic  Speed  Controller  (ESC)
* Servomoto

    <img width="143" height="332" alt="image" src="https://github.com/user-attachments/assets/4f686cc4-54b7-4f8f-80f8-2c028fa1c636" />
Image 1. Components
    <img width="196" height="340" alt="image" src="https://github.com/user-attachments/assets/c81cacbe-b05c-49eb-97fa-15c7ce557b92" />
Image 2. Components

### 1.3  Applied  Engineering  Principles
The  robot's  performance  is  based  on  the  application  of  fundamental  principles  of  dynamics,  kinematics,  and  mechanical design,  considering  an  operational  mass  of  1.4  kg  and  a  design  mass  of  1.5  kg  to  incorporate  a  safety  margin.  The technical  criteria  that  guided  the  selection  of  the  motor,  gear  ratio, chassis,  and  motion  management  are  presented  below.
To  ensure  that  the  drive  system  met  the  acceleration,  traction,  and  speed  requirements,  the  following  parameters  
were  established:
* Mass  used  for  calculation:  1.5  kg  
* Wheel  radius:  0.035  m  (diameter  0.07  m)
* Gravity:  9.81  m/s² 
* Desired  acceleration  in  fast  maneuver:  1.0  m/s² 
* Rolling  resistance  coefficient:  0.05
These  values  were  used  to  estimate  the  forces  that  the  engine  had  to  overcome  and  to  define  the  minimum  torque  
required  at  the  wheel  axle.

####  1.3.1  Calculation  of  Required  Forces 
* Primary  forces
* Normal  weight:  N  =  m  \cdot  g  =  1.5  \cdot  9.81  =  14.715\N
* Acceleration  force:  Facc  =  m  \cdot  a  =  1.5  \cdot  1  =  1.5\N
* Rolling  resistance  force:  Frr  =  Crr  \cdot  N  =  0.05 \cdot  14.715  = 0.73575\N
* Total  force  on  flat  terrain:  F  total  =  Facc  +  Frr  =  2.23575  N.  Conservative  case  (including  additional  friction  and small  slopes)
The  extended  project  calculations  yielded  a  maximum
* Total force  of:-  Ftotal\max  =  4.791\N
This  value  was  used  to  ensure  that  the  selected  engine  would function  even  in  adverse  situations.
#### 1.3.2  Required  Torque  on  the  Shaft
* Torque  at  the  wheel  axle  (conservative  case):  Taxle  =  Ftotal\_max  \cdot  r  =  4.791  \cdot  0.035  =  0.1677\  N·m
* Torque  per  wheel,  the  rear-wheel  drive  system  transmits  torque  equally  to  two  drive  wheels:  Twheel  =  0.0838  N·m
#### 1.3.3  Required  Mechanical  Power
The  power  was  estimated  using  the  two  fundamental  formulations:
* Power  times  force  and  linear  speed:  P  =  F  cdot  v  \approx  2.667\  W
* Power  by  torque  and  angular  velocity:  P  =  T  \cdot  \omega  \approx  4.00\W

Both  results  confirm that  the  robot  requires  only  a  few  watts  of  continuous  mechanical  power,  which  is  compatible  with  small-scale  RC  
motors.
#### 1.3.4  Engine  Selection  and  Gear  Ratio
Speed-Torque  Compromise
An  analysis  was  performed  comparing  the  speed  and  torque  offered  by  commercially  available  motors  in  technical tables.
The  motor  that  best  met  the  requirements  was  a:  ÿ  35T  RC  540  motor.
This  motor  stands  out  for  its  high  rotational  speed,  which  allows for  a  good  maximum  speed  on  mission.
* Selected  gear  ratio:  1.8 :  1  (54T /  30T).

Technical  justification
It  increases  the  torque  available  at  the  wheels  without  excessively  sacrificing  speed,  compensates  for  the  high-speed nature  of  the  RC  540  motor,  ensures  that  the  robot's  initial  inertia  is  overcome  and  the  desired  acceleration  is  achieved under  load,  and  maintains  competitive  performance  for  timed  tests.
Minimum  torque  that  the  engine  must  deliver  (considering  the  reduction)
* T_motor_min  =  0.1677  N·m /  1.8  =  0.093  N·m

This  value  is  within  what  an  RC  540  motor  can  deliver  under  normal conditions.

* Power,  traction,  and  control  management:  This  system  was  designed  to  ensure  efficient,  stable,  and  precise movement  throughout  all  mission  stages.  The  robot's  movement  is  controlled  by  an  Electronic  Speed  Controller (ESC),  which  regulates  the  motor  speed  based  on  the  pulse-width  modulation  (PWM)  signal  sent  from  the  processing unit.  Since  the  motor's  angular  velocity  is  practically  proportional  to  the  PWM  signal—as  long  as  the  battery  voltage remains  constant—this  system  allows  for  fine  adjustments  to  acceleration  and  speed.  Furthermore,  the  use  of acceleration  ramps  is  recommended  to  avoid  current  spikes  and  prevent  slippage  at  the  start  of  movement.
* Power  transmission:  A  rear-wheel  drive  (RWD)  system  with  a  rigid  axle  is  used. This  configuration  delivers  100%  of  the  torque  to  the  drive  wheels  without  the  typical  losses  associated  with  a  differential,  improving  mechanical  efficiency  and  simplifying  the  overall  powertrain  assembly.  The  chassis  was  
designed  to  be  rigid,  stable,  and  balanced,  properly  integrating  the  electronic  and  electrical  components  and  ensuring  correct  weight  distribution  to improve  grip  and  handling.
* Motor  selection  and  its  interaction  with  the  transmission  system:  A  preliminary  analysis  was  conducted  to  find  the  appropriate  balance  between  speed  and torque.  The  35T  RC  540  motor  was  chosen  because  it  offers  a  high  rotational  speed,  allowing  for  higher  speeds  in  a  straight  line.  To  compensate  for this  characteristic  and  ensure  the  robot  can  overcome  initial  inertia,  accelerate  effectively,  and  move  a  mass  of  1.4  kg,  a  reduction  ratio  of  1.8:1  (54  teeth /  30  teeth)  was  defined.  This  ratio  increases  available  torque  without  excessively  sacrificing  speed,  achieving  an  ideal  compromise  to  meet  mission  timelines  and  guarantee  the  necessary  traction  force.

Finally,  the  turning  kinematics  are  resolved  by  implementing  Ackerman  geometry  on  the  front  axle.  Because  the  rear  axle  is  rigid,  the  drive  wheels  cannot  rotate  at  different  speeds  during  cornering,  which  generates  drag  on  the  inside  wheel.  Ackerman  steering  minimizes  this  problem  by  allowing  the  front  wheels  to  adopt  specific  turning  angles,  reducing  drag,  improving  cornering  stability,  and  bringing  the  actual  trajectory  closer  to  the  ideal  trajectory.  This  results  in  smoother,  more  precise,  and  more  efficient  cornering,  even  with  the  inherent  limitations  of  a  rigid  axle  without  a  differential.

###  1.4  Construction  Instructions  and  CAD  Files
The  robot  uses  a  commercially  available  acrylic  chassis  (purchased  from  Mercado  Libre).  Therefore,  a  complete  CAD  model  of  the  chassis  was  not  required. However,  the  team  designed  and  fabricated  essential  custom  parts  for  integrating  the  actuators  and  sensors  into  the  SolidWorks  CAD  software.
* Camera  Mounting  Base:  A  structure  designed  to  secure  the  camera
The  camera  provides  a  stable  field  of  view  and  an  optimized  height  for  line  detection.  A  75-degree  viewing  angle  was  set  to  facilitate  programming logic.
* Battery  and  Raspberry  Pi  4  Mounting  Base:  A  stand  was  designed  in  which  the  battery  is  placed  in  the  center  of  the  cart  at  the  bottom.
* Rear  Axle  Drive  Gear:  This  part  was  redesigned  and  manufactured  due  to a  critical  failure  in  the  original  kit  gearing

<img width="904" height="479" alt="image" src="https://github.com/user-attachments/assets/61775168-1b69-484b-90d6-8f3b8da9ce92" />

Image  3.  Design  of  support  for  Raspberry  Pi  Camera  Module  V2

<img width="904" height="490" alt="image" src="https://github.com/user-attachments/assets/0ca16f22-686a-4800-86eb-c840409cbc20" />

Image  4.  Battery  and  Raspberry  Pi  support  design

<img width="909" height="486" alt="image" src="https://github.com/user-attachments/assets/44c25d4d-010b-47cd-b7ee-08a8da5e67ad" />

Image  5.  Gear  design

### 2. Power  and  sensory  management
#### 2.1  Energy  Management  (Power  Isolation)
The  energy  strategy  uses  a  dual  LiPo  battery  system  to  isolate  the  power  systems  (motors/actuators)  from  the  logic  systems  (processing/sensors).

* Power  Source:  Two  (2)  5200  mAh,  7.4  V  LiPo  Batteries  (2  cells).

Justification  for  Isolation:  This  dual  battery  configuration  is  essential  to  mitigate  the  "Brownout  problem".
* Battery  1  (Actuators):  Dedicated  exclusively  to  the  brushed  DC  traction  motor  and  the  steering  servo  motor  (via  the  ESC).  This  battery  absorbs  the  motors'  power  consumption  spikes  and  voltage  drops  without  affecting  the  sensitive  electronics.
* Battery  2  (Logic  and  Sensors):  Dedicated  to  the  Raspberry  Pi  4  (CPU)  and  all  the sensors.  This  ensures  a  clean  and  stable  voltage  supply  to  the  processing  components,  preventing  unexpected  restarts  that  could  compromise  the  execution  of  the  navigation  strategy.

#### 2.2  Selection  and  Implementation  of  Sensors  (The  Senses)
The  selection  of  sensors  is  geared  towards  providing  the  robot  with  the  precise,  low-latency  information  needed  for  real-time  localization  and  trajectory  correction.

* 3x  Laser  Distance  Sensors  (VL53L0X):  Use  Time-of-Flight  (ToF)  technology. They  are  essential  for  track  mapping  and  lateral  trajectory  correction  (walls).  Their  millimeter  precision  minimizes  accumulated  positioning  error.
* 1x  Camera  (ArduCam  V3  12MP):  Captures  high-resolution  images.  Used  for  machine  vision,  enabling  line  detection,  pattern  recognition,  and  visual  path  correction.

### 3. Obstacle  Management
This  section  describes  the  logic  behind  the  autonomous  vehicle's  operation  and  its  adaptation  to  the  real-world  track  conditions,  where  there  are  no  moving  physical  obstacles.  In  this  context,  the  system  must  react  to  the  walls  that  define  the  track  and  follow  the  colored  guide  on  the  ground.  To  achieve  this,  obstacle  management  relies  on  a  combination  of  distance  sensors  and  machine  vision.  This  system  allows  the  robot  to  detect  its  proximity  to  walls,  correct  its  trajectory,  and  follow  the  colored  guide  line,  maintaining  stability  within  the  track.
#### 3.1  Vision  System
NOVA  uses  an  Arducam  for  Raspberry  Pi.  This  camera  plays  an  essential  role  within  the  perception  system,  as  it  is  responsible  for  capturing  visual  information  from  the  environment  in  real  time.  Its  main  components  are:
* Sony  IMX708  sensor  (12  MP):  Converts  light  into  electrical  signals,  generating  the digital  image.
* 75°  lens  with  autofocus:  Directs  light  to  the  sensor  and  automatically  adjusts  sharpness  to  maintain  clear  details  in  motion.
* FFC  cable  (15–22  pins):  Provides  power  and  connects  the  camera  to  the  Raspberry  Pi  via  a  high-speed  link.
Thanks  to  this  camera,  the  robot  can  distinguish  between  different  colors  (mainly  orange  and  blue),  interpret  the  track,  
and  determine  which  way  to  turn  when  the  path  is  free  of  walls.

#### 3.2  Image  processing  for  boundary  detection
After  each  image  is  taken,  the  system  applies  processing  operations  that  include:
* Flipping  the  image  to  orient  it  correctly.  •  Extracting  a  region  of  interest  (ROI)  where  the  guide  line  is  located.
* Converting  the  color  space  to  HSV  to  identify  orange  or  blue  tones.Under  normal  conditions  (when  there  are  no  nearby  walls),  the  camera  is  used  for  color  detection.

The  robot  compares  the  detected  areas  of  each  color:
* If  you  dominate  the  orange  area,  turn  to  the  right.
* If  the  blue  area  dominates,  turn  left.
* If  neither  area  dominates,  keep  the  servo  in  the  neutral  position.
  
Contour  analysis  only  occurs  if  at  least  two  seconds  have  passed  since  the  last  correction,  avoiding  excessive  or  unstable  rotations.

#### 3.3  Distance  estimation
Although  a  direct  estimation  of  distance  is  not  made  using  images,  the  robot  uses  the  camera  to  supplement  orientation  and  detect  the  presence  or absence  of  guide  lines.
When  the  color  is  not  detected,  the  robot  remains  in  safe  mode  and  avoids  aggressive  turning,  using  only  information  from  the  distance  sensors.
If  both  systems  (vision  and  sensors)  are  in  agreement,  navigation  is  more  stable  and  accurate.

### 3.4  Distance  sensors
To  complement  the  vision  system,  the  vehicle  uses  three  VL53L0X  laser  sensors,  located  on  the  sides  and  front.  
These  sensors  allow  for  precise  measurement  of  the  distance  to  walls,  helping  to  avoid  collisions.

The  system  constantly  analyzes:
* Left  distance
* Front  distance
* Right  distance

Comparing  left  and  right  allows  you  to  decide  the  best  direction  when  you  need  to  avoid  a  nearby  wall.

#### 3.5  Obstacle  management  logic
Even  if  there  are  no  moving  obstacles,  the  robot  must  behave  as  if  the  walls  were  static  obstacles  that  it  must  avoid  at  all  costs.
The  current  logic  is  divided  into  three  main  levels:
 1. Emergency  brake: If  any  sensor  detects  less  than  100  mm,  the  motor  stops  completely.
 2. Proximity  avoidance:  If  a  side  wall  is  less  than  200  mm  away
    * The  robot  reduces  speed.
    * It  compares  which  side  has  more  space.
    * It  turns  toward  the  safer  side.
      * More  space  to  the  right, turns  right.
      * More  space  to  the  left, turns  left.

 3. Color  vision  (clear  path): When  walls  pose  no  risk,  the  robot  follows  the  line  using  the  camera:
    * Orange  predominates, turns  right.  
    * Blue  predominates  ÿ  turns  left.
    * No  dominant  color  ÿ  servo  centered.
      
 In  this  way,  the  robot  combines  distance  and  vision  to  move  safely  without  colliding  with  walls

<img width="531" height="472" alt="image" src="https://github.com/user-attachments/assets/13cbfc75-eecb-498b-a89c-30f052c156e1" />

Image  6.  Flowchart  of  the  general  process,  detailing  Phase  1  (Start  and  Configuration)  and  Phase  2  (Main  Loop  and  Reading)

<img width="531" height="472" alt="image" src="https://github.com/user-attachments/assets/3bccf904-7806-40dd-a629-b35de68f1b09" />

Image  7.  Flowchart  of  the  general  process,  detailing  Phase  3  Control  Decision  (Main  Logic)  and  Phase  4  Convergence  and  Termination.

### 5. Performance  videos
https://www.youtube.com/channel/UCp8W6HJ0NGMzdpxV4bdbbew

### 6. Using  Github
NOVA-DNT/NOVA:  NOVA  (Navigation  Operative  Vehicle  Autonomus)  WRO



