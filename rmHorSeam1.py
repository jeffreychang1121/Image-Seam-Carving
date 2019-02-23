'''
  File name: rmHorSeam.py
  Author:Ningshan Zhang
  Date created:10/18/2018
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
  # Your Code Here
  n = My.shape[0]
  m = My.shape[1]
  Iy = I[0:n-1, :, :].copy()
  E = np.min(My[:, -1])
  ind = My[:, -1].tolist().index(np.min(My[:, -1]))
  Iy[:, -1, :] = np.delete(I[:, -1, :], ind, 0)

  for i in range(m-1, 0, -1):
      ind = Tby[ind,i]
      Iy[:, i-1, :] = np.delete(I[:, i-1, :], ind, 0)
  return Iy, E
