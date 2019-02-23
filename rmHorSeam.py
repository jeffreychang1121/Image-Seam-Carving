'''
  File name: rmHorSeam.py
  Author:
  Date created:
'''

'''
  File clarification:
    Removes horizontal seams. You should identify the pixel from My from which 
    you should begin backtracking in order to identify pixels for removal, and 
    remove those pixels from the input image. 
    
    - INPUT I: n × m × 3 matrix representing the input image.
    - INPUT My: n × m matrix representing the cumulative minimum energy map along horizontal direction.
    - INPUT Tby: n × m matrix representing the backtrack table along horizontal direction.
    - OUTPUT Iy: (n − 1) × m × 3 matrix representing the image with the row removed.
    - OUTPUT E: the cost of seam removal.
'''

import numpy as np

def rmHorSeam(I, My, Tby):

  r, c = My.shape
  # cost of seam removal
  E = np.min(My[:,-1])

  # initialize removed matrix
  Iy = np.zeros((r-1,c,3)).astype(int)
  # Iy = I[:r - 1, :, :].copy()

  # index of the min path
  idx = np.argmin(My[:,-1])

  for j in range(c-1, -1,-1):
    Iy[:, j, :] = np.delete(I[:, j, :], [idx], axis=0)  # delete row
    idx = Tby[idx, j] # get the next index

  return Iy, E
