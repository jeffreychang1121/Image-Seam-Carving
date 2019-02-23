'''
  File name: rmVerSeam.py
  Author:
  Date created:
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

  r, c = Mx.shape
  # cost of seam removal
  E = np.min(Mx[-1, :])

  # initialize removed matrix
  Ix = np.zeros((r, c-1, 3)).astype(int)
  # Ix = I[:, :c - 1, :].copy()

  # ind = Mx[-1, :].tolist().index(np.min(Mx[-1, :]))
  # Ix[-1, :, :] = np.delete(I[-1, :, :], ind, 0)
  #
  # for i in range(r - 1, 0, -1):
  #   ind = Tbx[i, ind]
  #   Ix[i - 1, :, :] = np.delete(I[i - 1, :, :], ind, 0)

  # index of the min path
  idx = np.argmin(Mx[-1, :])

  for i in range(r - 1, -1, -1):
    Ix[i, :,:] = np.delete(I[i, :,:], [idx], axis=0)  # delete col
    idx = Tbx[i, idx]  # get the next index

  return Ix, E
