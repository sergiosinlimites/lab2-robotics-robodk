# Laboratorio No. 2 - Robótica Industrial - Análisis y Operación del Manipulador Motoman MH6

## Integrantes

* Sergio Andrés Bolaños Penagos
* Sergio Felipe Rodriguez Mayorga

## Introducción
En esta practica se buscaba trabajar con el manipulador Motoman MH6 de Yaskawa, permitiendo complementar la experiencia en robotica industrial adquirida con el ABB IRB 140 utilizado en el laboratoio 1, razon por la cual en este trabajo se realizo una comparacion detallada entre ambos modelos y el software utilizado para su interaccion. En este laboratorio en particular se implemento una trayectoria polar dibujada por el manipulador la cual consistia en dibujar nuestros nombres (para lo cual se reutilizo la trayectoria previamente diseñada para el ABB), y una mariposa definida en coordenadas polares para aprovechar la facilidad que RoboDK brinda al poder programar en Python.
## Planteamiento del problema
Programar el manipulador motoman MTH6 para que realice una trayectoria definida en coordenadas polares utilizando Python y el software RoboDK .
## Objetivos
* Comprender las diferencias entre las caracterısticas tecnicas del manipulador Motoman MH6 y el IRB140.
* Identificar y describir las configuraciones iniciales del manipulador Motoman MH6, incluyendo el home1 y
home2.
* Realizar movimientos manuales del manipulador Motoman en distintos modos de operacion (articulaciones,
cartesianos, traslaciones y rotaciones).
* Cambiar y controlar los niveles de velocidad para el movimiento manual del manipulador Motoman MH6.
* Comprender las principales aplicaciones del software RoboDK y su comunicacion con el manipulador.
* Comparar y analizar las diferencias entre RobotStudio y RoboDK.
* Diseñar y ejecutar una trayectoria polar en RoboDK y realizar su implementacion fısica en el manipulador Motoman.

## Comparación especificaciones técnicas Motoman MH6 y ABB IRB140
Cuadro comparativo detallado de las características técnicas del Motoman MH6 y el IRB140, incluyendo carga máxima, alcance, número de grados de libertad, velocidad, aplicaciones típicas, etc


| *Características* | *Motoman MH6* | *ABB IRB140* |
|---------------------|-----------------|----------------|
| *Carga máxima*    | 6 kg            | 6 kg           |
| *Alcance máximo (horizontal)* | 1422 mm | 700 mm  |
| *Alcance máximo (vertical)*   | 2486 mm | 1050 mm |
| *Número de grados de libertad*| 6       | 6       |
| *Repetibilidad*               | ± 0.08 mm | ± 0.05 mm |
| *Velocidad máxima (S)* | 220°/s | 150°/s  |
| *Velocidad máxima (L)*  | 200°/s   | 120°/s  |
| *Velocidad máxima (U)* | 220°/s | 120°/s  |
| *Velocidad máxima (R)* | 410°/s | 180°/s  |
| *Velocidad máxima (B)* | 410°/s | 180°/s  |
| *Velocidad máxima (T)* | 610°/s | 220°/s  |
| *Aplicaciones típicas* | Manipulación de materiales, procesamiento, etc. | Manipulación, ensamblaje, soldadura, etc.  |
| *Temperatura de operación*  | 0°C a +45°C| 0°C a +45°C|
| *Peso*| 130 kg  | 240 kg |
| *Tipo de montaje* | Piso, Techo, Pared | Piso, Techo |
### 🔗 Referencias

- [Yaskawa Motoman MH6 – Robots.com](https://www.robots.com/industrial-robots/motoman-mh6)  
- [Yaskawa MH6D/MH6F – Yaskawa Europe PDF](https://pdf.directindustry.com/pdf/yaskawa-europe-gmbh/mh6d-mh6f/14473-309337.html)  
- [ABB IRB 140 Product Specification – ABB Library (3HAC041346)](https://library.e.abb.com/public/a7121292272d40a9992a50745fdaa3b2/3HAC041346%20PS%20IRB%20140-en.pdf)  
- [ABB IRB 140 Datasheet – Manuallib.com](https://www.manuallib.com/download/pdf/2014/0624/abb-irb140-industrial-robot-datasheet.pdf)  
- [IRB 140 Product Manual Type C – Scribd](https://www.scribd.com/document/649705967/IRB-140-Type-C-Product-Manual-3HAC027400-001-RevC-En)

## Diferencias en el home en el Motoman MH6

 El Motoman MH6 cuenta con dos home, HOME1 y HOME2.

* El HOME1 está orientado a la configuración del robot para transporte o almacenamiento durante largas jornadas sin trabajo, es una posición en la que los ejes se encuentran retraidos en su totalidad para disminuir las fuerzas sobre los frenos y el espacio que ocupa el robot.
* El HOME2 está diseñado para cuando el robot se encuentra preparado para trabajar, con el fin de ejecutar sus tareas con facilidad y menores desplazamientos que los que tendría que hacer en HOME1 y facilitar el mantenimiento.

## Movimiento manual, tipos de procedimiento y procedimiento
Procedimiento detallado para realizar movimientos manuales, especificando c´omo cambiar entre modos de
operaci´on (articulaciones, cartesiano) y realizar traslaciones y rotaciones en los ejes X, Y, Z.
![Teach Pendant](img/Teach_Pendant.png) \
Teach pendant
![Interfaz del Teach Pendant](img/HMI.png) \
Interfaz del Teach Pendant

1. Dejar el Teach Pendant en modo Teach, y desactivar el botón de emergencia.
2. Definir la velocidad (Slow, Fast, High Speed)
3. Llevar el robot a HOME2 SERVO ON (Botón) > Robot > SECOND HOME POS > Botón hombre muerto + FWD (botón)
4. COORD (Botón) y elegir la opción Joint Coordinates (Robot) o Cartesian Coordinates (Marco de coordenadas), también se puede seleccionar algun otro tipo pero estas son las principales de movimiento articular y movimiento cartesiano.

![Movimientos Motoman](img/Movimientos_Motoman.png)

## Niveles de velocidad

Explicaci´on completa sobre los niveles de velocidad para movimientos manuales, el proceso para cambiar entre
niveles y c´omo identificar el nivel establecido en la interfaz del robot.
![Velocidades](img/Velocidades.png)
El robot tiene 4 modos de velocidad a utilizar, lento, medio y alto, tal como se ve en la imagen, y se cambia entre estos modos con los botones del Teach Pendant SLOW, FAST y HIGH SPEED.


## Aplicaciones  Principales
El Motoman MH6 es un robot industrial de seis ejes diseñado para aplicaciones de manipulación y ensamblaje de alta precisión. Su capacidad de carga de 6 kg y su amplio alcance de 1 422 mm lo hacen especialmente adecuado para tareas como alimentación de máquinas, empaque, paletizado ligero, carga y descarga de piezas, aplicación de adhesivos, dispensado y manipulación de materiales. Gracias a su estructura compacta y su posibilidad de montaje en piso, pared o techo, puede integrarse fácilmente en celdas de trabajo automatizadas. Además, su controlador DX100 ofrece funciones avanzadas de coordinación multirrobot y detección de colisiones, lo que permite una operación segura y eficiente en entornos de manufactura flexible.
## Comunicación con el manipulador

El software RoboDK es una plataforma de simulación y programación offline que permite desarrollar, validar y optimizar trayectorias de robots industriales sin necesidad de disponer del equipo físico. Entre sus principales funcionalidades se incluyen la simulación 3D de manipuladores, la planificación automática de trayectorias, la programación visual o por código, y la exportación directa de programas al controlador del robot.

En el caso del Motoman MH6, RoboDK se comunica con el robot mediante el controlador Yaskawa DX100 (o versiones posteriores como DX200 o YRC1000), utilizando interfaces como Ethernet/IP o MotoCom SDK. El software convierte las trayectorias diseñadas en su entorno virtual en código nativo INFORM (.JBI), que puede ejecutarse directamente en el controlador del robot.

RoboDK también permite la programación en Python, lo que brinda la posibilidad de generar, modificar y controlar trayectorias mediante scripts personalizados. Esto amplía sus capacidades de automatización y facilita la integración con sistemas externos o sensores.

Además, RoboDK funciona como un gemelo digital (digital twin) del manipulador, ya que reproduce en tiempo real el comportamiento cinemático y dinámico del robot dentro del entorno virtual. 

## Comparación RoboDK vs RobotStudio

 

| *Criterio* | *RoboDK* | *RobotStudio* |
|---------------|-------------|-----------------|
| *Fabricante / desarrollador* | RoboDK Inc. (Canadá) | ABB Robotics |
| *Compatibilidad* | Multimarca (Yaskawa, ABB, KUKA, Fanuc, UR, etc.) | Exclusivo para robots ABB( aunque con mas trabajo se pueden incluir otros) |
| *Lenguaje de programación* | Python (nativo) o programacion en bloques, además de generar código específico por postprocesador (INFORM, RAPID, KRL, etc.) | RAPID (lenguaje nativo ABB) |
| *Simulación* | 3D completa, cinemática directa e inversa, detección de colisiones, cálculo de trayectorias y tiempos de ciclo | Simulación 3D avanzada con Virtual Controller (emula el controlador real ABB) |
| *Comunicación con el robot real* | A través del controlador (por Ethernet/IP o transferencia de archivo .JBI, .mod, etc.) | Comunicación directa con el controlador IRC5/OmniCore mediante Virtual Controller |
| *Nivel de precisión* | Alta, dependiente del postprocesador y la calibración del modelo | Muy alta (usa el mismo firmware que el robot físico) |
| *Programación offline* | Sí, mediante interfaz gráfica y scripts en Python | Sí, mediante RAPID y Virtual Controller |
| *Capacidades de automatización* | Permite integración con visión, sensores externos y control por Python | Incluye librerías industriales (soldadura, pick & place, paletizado, mecanizado, etc.) |
| *Funcionalidad de gemelo digital* | Sí, actúa como un *Digital Twin* del robot en tiempo real | No en su modo mas basico, requiere activar otras opciones para sincronización total con el robot ABB físico |
| *Ventajas principales* | Multimarca, flexible, interfaz sencilla, programación por Python, rápida curva de aprendizaje | Precisión total, integración completa con hardware ABB, simulación realista de procesos |
| *Limitaciones* | Menor fidelidad dinámica, depende de postprocesadores, precisión limitada frente a simuladores nativos | Principalmente compatible con ABB, Rapid tiene una mayor curva de aprendizaje |
| *Aplicaciones típicas* | Investigación, docencia, integración multi-robot, prototipado rápido | Producción industrial ABB, validación de procesos, entrenamiento técnico |
| *Nivel de licencia / costo* | Versión gratuita con funciones limitadas, licencias comerciales asequibles | Licencia comercial (mayor costo, versiones académicas disponibles) |

---

### 🔗 Referencias

- [RoboDK Official Website](https://robodk.com)  
- [RobotStudio Official Page – ABB Robotics](https://new.abb.com/products/robotics/es/robotstudio)  
- [RoboDK Documentation](https://robodk.com/doc/en)  
- [RobotStudio Help and Learning Resources (ABB)](https://developercenter.robotstudio.com/)


## Programación de trayectoria polar

### Diagrama de flujo de acciones del robot
```mermaid
 flowchart TD
    A([Inicio]) --> B[Conectar con RoboDK]
    B --> C[Seleccionar robot]
    C --> D{Robot valido?}
    D -->|No| E[Error: robot no valido]
    D -->|Si| F[Ir al target HOME2]
    F --> G[Configurar velocidades y aceleraciones]
    G --> H[Definir offsets y escala]
    H --> I[Generar puntos de SERGIO/trayectoria de nombre]
    I --> J[Dibujar SERGIO dos veces]
    J --> K[Calcular puntos de mariposa]
    K --> L[Dibujar mariposa]
    L --> M[Volver a HOME2]
    M --> N([Fin])
```

### Plano de planta de la ubicacion de cada uno de los elementos
![Plano de planta](img/Plano_Planta.png)\
Plano de planta de la ubicación de cada uno de los elementos.

![Vista horizontal](img/Vista_horizontal.png)
Vista de distancia del WorkObject y la mesa

Como se puede ver, el software indica que la WorkObject del plano donde se dibuja se encuentra a una distancia X=993mm, Y=-34mm, Z=77mm y con una rotación de -180 en X y de -30 en Y, con respecto a la base del robot.

### Código desarrollado en RoboDK para ejecutar una trayectoria polar, adjuntado como anexo dentro del repositorio.
[Anexo codigo](./codigo_python.py)\
Código desarrollado en RoboDK para ejecutar una trayectoria polar
```python
from robodk.robolink import *     # API RoboDK
from robodk.robomath import *     # utilidades de transformación
import math

# ------------------------------
# 1) Conexión e inicialización
# ------------------------------
RDK = Robolink()

# Elegir un robot (si hay varios, aparece un popup)
robot = RDK.ItemUserPick("Selecciona un robot", ITEM_TYPE_ROBOT)
home = RDK.Item("Target HOME2", ITEM_TYPE_TARGET)
if not robot.Valid():
    raise Exception("No se ha seleccionado un robot válido.")

# Conectar al robot físico
if not robot.Connect():
    raise Exception("No se pudo conectar al robot. Verifica que esté en modo remoto y que la configuración sea correcta.")

# Confirmar conexión
if not robot.ConnectedState():
    raise Exception("El robot no está conectado correctamente. Revisa la conexión.")

print("Robot conectado correctamente.")
robot.MoveJ(home)
# ------------------------------
# Velocidad y blending (rápida, igual para todo)
# ------------------------------
# v_lin [mm/s], v_joint [deg/s], a_lin [mm/s^2], a_joint [deg/s^2]
V_LIN_FAST   = 400.0
V_JOINT_FAST = 180.0
A_LIN_FAST   = 3000.0
A_JOINT_FAST = 720.0
ZONE_MM      = 10.0   # equivalente a z10

robot.setSpeed(V_LIN_FAST, V_JOINT_FAST, A_LIN_FAST, A_JOINT_FAST)
robot.setRounding(ZONE_MM)

# Alturas/ajustes
z_surface = 0.0   # plano de dibujo
z_safe    = 30.0  # altura segura
offset_xy  = (-150.0, -120.0)  # 1ra pasada
offset_xy2 = (130.0, -120.0)   # 2da pasada (dejado igual a tu script)
scale     = 1.5                 # escala uniforme del texto

# ------------------------------
# 2) Puntos de SERGIO
# ------------------------------
pts_base = [
    (0,0,0),(0,18,0),(2,20,0),(21.75,20,0),(23.75,18,0),(23.75,9.5,0),
    (25.75,7.5,0),(30.5,7.5,0),(32.5,9.5,0),(32.5,25,0),
    (0,25,0),(0,45,0),(7.5,45,0),(7.5,34.5,0),(9.5,32.5,0),(14.25,32.5,0),
    (16.25,34.5,0),(16.25,45,0),(23.75,45,0),
    (23.75,34.5,0),(25.75,32.5,0),(30.5,32.5,0),(32.5,34.5,0),(32.5,50,0),
    (0,50,0),(0,57.5,0),(16.25,57.5,0),(0,62.5,0),(0,70,0),
    (16.25,65,0),(16.25,57.5,0),(23.75,57.5,0),(23.75,60.5,0),(25.75,62.5,0),
    (30.5,62.5,0),(32.5,60.5,0),(32.5,57.5,0),(16.25,57.5,0),(16.25,68,0),
    (18.25,70,0),(32.5,70,0),(32.5,75,0),(2,75,0),(0,77,0),
    (0,93,0),(2,95,0),(21.75,95,0),(23.75,93,0),(23.75,84.5,0),
    (16.25,84.5,0),(14.25,82.5,0),(9.5,82.5,0),(7.5,84.5,0),
    (9.5,87.5,0),(14.25,87.5,0),(16.25,85.5,0),(16.25,84.5,0),
    (23.75,84.5,0),(25.75,82.5,0),(30.5,82.5,0),(32.5,84.5,0),
    (32.5,106.25,0),(7.5,106.25,0),(7.5,100,0),(0,100,0),
    (0,120,0),(7.5,120,0),(7.5,113.75,0),(32.5,113.75,0),
    (32.5,125,0),(2,125,0),(0,127,0),(0,143,0),(2,145,0),
    (38,145,0),(40,143,0),(30.5,137.5,0),(9.5,137.5,0),
    (7.5,135.5,0),(7.5,134.5,0),(9.5,132.5,0),(30.5,132.5,0),
    (32.5,134.5,0),(32.5,135.5,0),(30.5,137.5,0),(40,143,0),
    (40,2,0),(38,0,0),(18.25,0,0),(16.25,2,0),(16.25,10.5,0),
    (14.25,12.5,0),(9.5,12.5,0),(7.5,10.5,0),(7.5,0,0),(0,0,0)
]

def adjust(p, offset_xy=(0,0), s=1.0, z=z_surface):
    x = offset_xy[0] + s*p[0]
    y = offset_xy[1] + s*p[1]
    return (x, y, z)

pts_sergio_1 = [adjust(p, offset_xy,  scale, z_surface) for p in pts_base]
pts_sergio_2 = [adjust(p, offset_xy2, scale, z_surface) for p in pts_base]

# ------------------------------
# Utilidades de trazado
# ------------------------------
R_id = eye(4)  # rotación identidad

def draw_polyline(points, z_up=z_safe, z_down=z_surface):
    """Aproxima por Z al primer punto, traza MoveL continuo y sale por Z."""
    if len(points) < 2:
        return
    # Garantiza que seguimos en modo rápido
    robot.setSpeed(V_LIN_FAST, V_JOINT_FAST, A_LIN_FAST, A_JOINT_FAST)
    

    x0, y0, _ = points[0]
    # Aproximación
    robot.MoveJ(transl(x0, y0, z_up) * R_id)
    robot.MoveL(transl(x0, y0, z_down) * R_id)
    # Trazo
    for (x, y, z) in points[1:]:
        robot.MoveL(transl(x, y, z) * R_id)
    # Salida segura
    xf, yf, _ = points[-1]
    robot.MoveL(transl(xf, yf, z_up) * R_id)

# ------------------------------
# 3) Dibujo de SERGIO (dos veces)
# ------------------------------
draw_polyline(pts_sergio_1, z_up=z_safe, z_down=z_surface)
draw_polyline(pts_sergio_2, z_up=z_safe, z_down=z_surface)

# ------------------------------
# 4) Mariposa polar desde (0,0) ROTADA +90° CCW
#     r = e^{sinθ} - 2 cos(4θ) + sin^5((2θ - π)/24)
# ------------------------------
origin_butterfly = (0.0, 0.0)   # parte desde (0,0)
scale_butterfly  = 30.0         # mm/ud polar (ajusta tamaño si deseas)
samples          = 500         # suavidad de la curva
theta_max        = 12*math.pi   # rango típico de la mariposa
angle_rot        = math.pi/2    # +90° CCW

pts_butterfly = []
cx, cy = origin_butterfly
for i in range(samples+1):
    t = i / samples
    theta = theta_max * t
    r = math.e**(math.sin(theta)) - 2.0*math.cos(4.0*theta) + math.sin((2.0*theta - math.pi)/24.0)**5
    
    # coordenadas sin rotación
    x = cx + scale_butterfly * (r * math.cos(theta))
    y = cy + scale_butterfly * (r * math.sin(theta))
    
    # rotación 2D alrededor de (cx, cy): +90° CCW
    xr = cx + (x - cx)*math.cos(-angle_rot) - (y - cy)*math.sin(-angle_rot)
    yr = cy + (x - cx)*math.sin(-angle_rot) + (y - cy)*math.cos(-angle_rot)
    
    pts_butterfly.append((xr, yr, z_surface))

# Traza mariposa con la misma velocidad rápida
draw_polyline(pts_butterfly, z_up=z_safe, z_down=z_surface)
robot.MoveJ(home)
print("Trayectorias completadas: SERGIO x2 y mariposa (todas a velocidad rápida).")
```




### Video de simulacion en RoboDK mostrando la trayectoria polar y evidencia de su implementacion en el manipulador Motoman de forma fısica, controlado desde el PC.

[Aquí se puede ver el video de la simulacion:](https://drive.google.com/file/d/1iuzeHvYXCrc1Aiu5uS5aBvG-MUil6M6l/view?usp=drive_link)

<video width="1080" height="720" controls>
  <source src="https://drive.google.com/file/d/1iuzeHvYXCrc1Aiu5uS5aBvG-MUil6M6l/view?usp=drive_link" type="video/mp4">
  Tu navegador no soporta video HTML5.
</video>


[Aquí se puede ver el video de la prueba con el Robot real:](https://drive.google.com/file/d/1L1ukfGe2Bonk_mbMSGQEHVqtfuFvAqZY/view?usp=drive_link)

<video width="1080" height="720" controls>
  <source src="https://drive.google.com/file/d/1L1ukfGe2Bonk_mbMSGQEHVqtfuFvAqZY/view?usp=drive_link" type="video/mp4">
  Tu navegador no soporta video HTML5.
</video>
 

 

 

 