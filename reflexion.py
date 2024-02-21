def calculer_reflexion_point(iterable,axe):   #reflexion selon l'axe x
    if axe == 'x' :
        x=int ( iterable[0] )
        y= -1 * int(iterable[1])               #retourne les x
        un_tuple=(x,y)
        return un_tuple

    elif axe == 'y' :                       #reflexion selon l'axe y
        x = -1 * int(iterable[0])
        y = int(iterable[1])
        un_tuple=(x,y)                      #retourne les y
        return un_tuple



print(calculer_reflexion_point((2,4),'x'))