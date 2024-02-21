import math

def calculer_rotate_point(un_tuple,un_angle,un_centre):  #angle en degrees
    angle=un_angle*(math.pi/180)                                                      #convertie les degrès en radian
    distance_x = un_tuple[0]-un_centre[0]                                             #calcul la distance en x   #calcul la distance en y
    distance_y = un_tuple[1]-un_centre[1]                                             #calcul la distance en y
    nv_x = distance_x * math.cos(angle) - distance_y * math.sin(angle) + un_centre[0] # calcul les nouvelles coordonné en x
    nv_y = distance_x * math.sin(angle) + distance_y * math.cos(angle) + un_centre[1] #calcul les nouvelles coordonné en y
    nv_x = round(nv_x,2)
    nv_y = round(nv_y,2)
    nv_pt=(nv_x,nv_y)                                                                 #initialisation d'un tuple
   
    return nv_pt

print(calculer_rotate_point((2,4),30,(0,0)))
