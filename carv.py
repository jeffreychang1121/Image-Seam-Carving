'''
  File name: carv.py
  Author:
  Date created:
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

from cumMinEngHor import cumMinEngHor
from cumMinEngVer import cumMinEngVer
from rmHorSeam import rmHorSeam
from rmVerSeam import rmVerSeam
from genEngMap import genEngMap
import numpy as np

def delHor(I):
  e = genEngMap(I)
  Mh, Tbh = cumMinEngHor(e)
  Ih, Eh = rmHorSeam(I, Mh, Tbh)
  return Ih, Eh

def delVer(I):
  e = genEngMap(I)
  Mv, Tbv = cumMinEngVer(e)
  Iv, Ev = rmVerSeam(I, Mv, Tbv)
  return Iv, Ev

def carv(I, nr, nc):

  # energy path
  Te = np.zeros([nr+1,nc+1])
  # carve image
  Ti = [I]
  # create first row of the energy path and do DP
  for j in range(1, nc+1):
    Iv, Te[0,j] = delVer(Ti[-1])
    Te[0,j] += Te[0,j-1]
    Ti.append(Iv)

  # Te is 2d matrix: the min energy with shortest path
  # Ti is 1d array: the carved image represent either from horizontal or vertical
  for i in range(1, nr+1):
    Ih, Te[i,0] = delHor(Ti[0])
    Ti[0] = Ih

    for j in range(1, nc+1):
      # get previous image from Ti[j-1]
      Iv, Tv = delVer(Ti[j - 1])
      # get previous image from Ti[j]
      Ih, Th = delHor(Ti[j])
      # if horizontal has less energy cost next step would be vertical
      if Tv+Te[i, j-1] < Th+Te[i-1,j]:
        Te[i,j] = Tv+Te[i, j-1]
        Ti[j] = Iv
      else:
        Te[i,j] = Th+Te[i-1,j]
        Ti[j] = Ih

  Ic = Ti[-1]

  return Ic, Te