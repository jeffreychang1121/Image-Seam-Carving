'''
  File name: carv.py
  Author:Ningshan Zhang
  Date created:10/18/2018
'''

'''
  File clarification:
    Aimed to handle finding seams of minimum energy, and seam removal, the algorithm
    shall tackle resizing images when it may be required to remove more than one seam, 
    sequentially and potentially along different directions.
    
    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT nr: the numbers of rows to be removed from the image.
    - INPUT nc: the numbers of columns to be removed from the image.
    - OUTPUT Ic: (n − nr) × (m − nc) × 3 matrix representing the carved image.
    - OUTPUT T: (nr + 1) × (nc + 1) matrix representing the transport map.
'''
import numpy as np
from genEngMap import genEngMap
from rmHorSeam1 import rmHorSeam
from rmVerSeam1 import rmVerSeam
from cumMinEngHor import cumMinEngHor
from cumMinEngVer import cumMinEngVer


def cutH(I):
    My, Tby = cumMinEngHor(genEngMap(I))
    Iy, Ey = rmHorSeam(I, My, Tby)
    return Iy, Ey


def cutV(I):
    Mx, Tbx = cumMinEngVer(genEngMap(I))
    Ix, Ex = rmVerSeam(I, Mx, Tbx)
    return Ix, Ex


def carv(I, nr, nc):
    # Your Code Here
    T = np.zeros([nr + 1, nc + 1])
    Tempv = [I]
    for i in range(1, nc+1):
        Img, T[0, i] = cutV(Tempv[-1])
        T[0,i]=T[0,i]+T[0,i-1]
        Tempv.append(Img)

    # I_1c=I
    for j in range(1, nr + 1):
        Temph, T[j, 0] = cutH(Tempv[0])
        Tempv[0] = Temph
        for i in range(1, nc + 1):
            comp = [cutH(Tempv[i])[1] + T[j - 1, i], cutV(Tempv[i - 1])[1] + T[j, i - 1]]
            if comp[0] < comp[1]:
                T[j, i] = comp[0]
                Tempv[i] = cutH(Tempv[i])[0]
            else:
                T[j, i] = comp[1]
                Tempv[i] = cutV(Tempv[i - 1])[0]
    Ic = Tempv[-1]
    return Ic, T
