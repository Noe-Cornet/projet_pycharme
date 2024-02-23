import math
def calculer_inclinaison_point(point_1,angle_1,direction):
    angle_1=angle_1*(math.pi/180)
    m = float(math.tan(angle_1))
    if direction == 'x':
        n_x = round(point_1[0]+m*point_1[1],2)
        n_y = float(point_1[1])

    elif direction == 'y':
        n_x =  point_1[0]
        n_y =  round(point_1[0]*m+point_1[2],2)
    return n_x,n_y

print(calculer_inclinaison_point((2,4),5,'x'))

gg