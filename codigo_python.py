# -*- coding: utf-8 -*-
# Dibuja la palabra SERGIO (2 veces) y luego una mariposa polar en RoboDK.

from robodk.robolink import *     # API RoboDK
from robodk.robomath import *     # utilidades de transformación
import math

# ------------------------------
# 1) Conexión e inicialización
# ------------------------------
#------------------------------------------------
RDK = Robolink()

# Elegir un robot (si hay varios, aparece un popup)
robot = RDK.ItemUserPick("Selecciona un robot", ITEM_TYPE_ROBOT)
home = RDK.Item("Target HOME2", ITEM_TYPE_TARGET)
if not robot.Valid():
    raise Exception("No se ha seleccionado un robot válido.")

# Conectar al robot físico
#if not robot.Connect():
#    raise Exception("No se pudo conectar al robot. Verifica que esté en modo remoto y que la configuración sea correcta.")

# Confirmar conexión
#if not robot.ConnectedState():
#    raise Exception("El robot no está conectado correctamente. Revisa la conexión.")

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
# 2) Puntos de SERGIO (orden RAPID)
#    Z=0 en todos (sin levantar durante el trazo)
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
