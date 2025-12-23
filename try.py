import math
import numpy as np

def distance(taillel,poidsl):
    maison = ['A','B','C','D','E']
    l = []
    surfaces = [50,60,70,80,90]
    prix = [100,120,140,160,180]
    for i in range(len(maison)):
        x = math.pow(((maison[i]) - taillel),2)
        y = math.pow(((surfaces[i]) - poidsl), 2)
        d = math.sqrt((x + y))
        l.append([d,maison[i],surfaces[i],prix[i]])
    min = l[0][0]
    minn = []
    for element in l:
        if (element[0] < min):
            min = element[0]
            minn = element
    return l

print(distance(taillel=168,poidsl=62))
