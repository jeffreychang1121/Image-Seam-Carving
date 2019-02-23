'''
  File name: rmVerSeam.py
  Author:Ningshan Zhang
  Date created:10/18/2018
'''

'''
  File clarification:
    Removes vertical seams. You should identify the pixel from My from which 
    you should begin backtracking in order to identify pixels for removal, and 
    remove those pixels from the input image. 
    
    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT Mx: n × m matrix representing the cumulative minimum energy map along vertical direction.
    - INPUT Tbx: n × m matrix representing the backtrack table along vertical direction.
    - OUTPUT Ix: n × (m - 1) × 3 matrix representing the image with the row removed.
    - OUTPUT E: the cost of seam removal.
'''
import numpy as np


def rmVerSeam(I, Mx, Tbx):
  # Your Code Here
  n=Mx.shape[0]
  m=Mx.shape[1]
  Ix=I[:,0:m-1,:].copy()
  E=np.min(Mx[-1,:])
  ind=Mx[-1, :].tolist().index(np.min(Mx[-1, :]))
  Ix[-1,:,:]=np.delete(I[-1,:,:],ind,0)

  for i in range(n-1,0,-1):
      ind=Tbx[i,ind]
      Ix[i-1,:,:]=np.delete(I[i-1,:,:],ind,0)
  return Ix, E
