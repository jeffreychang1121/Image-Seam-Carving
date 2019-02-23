'''
  File name: cumMinEngVer.py
  Author:Ningshan Zhang
  Date created: 10/18/2018
'''

'''
  File clarification:
    Computes the cumulative minimum energy over the vertical seam directions.
    
    - INPUT e: n × m matrix representing the energy map.
    - OUTPUT Mx: n × m matrix representing the cumulative minimum energy map along vertical direction.
    - OUTPUT Tbx: n × m matrix representing the backtrack table along vertical direction.
'''
import numpy as np


def cumMinEngVer(e):
  # Your Code Here

  Tbx=np.zeros(e.shape).astype('int')
  h=np.size(e,axis=0)
  w=np.size(e,axis=1)
  for i in range(1,h):
      Mx=e.copy()
      upleft=np.hstack([np.array([10000]),e[i-1,0:-1]])
      up=e[i-1,:]
      upright=np.hstack([e[i-1,1:],np.array([100000])])

      Mx[i,:]=np.min((upleft,up,upright),axis=0)+e[i,:]
      Tbx[i,:]=np.argmin((upleft,up,upright),axis=0)+np.arange(-1,w-1)
  return Mx, Tbx