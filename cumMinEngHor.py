'''
  File name: cumMinEngHor.py
  Author:
  Date created:
'''

'''
  File clarification:
    Computes the cumulative minimum energy over the horizontal seam directions.
    
    - INPUT e: n × m matrix representing the energy map.
    - OUTPUT min_energy_map: n × m matrix representing the cumulative minimum energy map along horizontal direction.
    - OUTPUT backtrack_map: n × m matrix representing the backtrack table along horizontal direction.
'''

import numpy as np

def cumMinEngHor(e):

  row, col = e.shape

  min_energy_map = np.zeros((row, col))
  _, backtrack_map = np.meshgrid(np.arange(col), np.arange(row))

  # initialize energy map
  # backtrack_map[:,0] = min_energy_map[:,0]
  min_energy_map[:,0] = e[:,0]

  # create comparision matrix
  cmp = np.zeros((row, 3))

  for j in range(1, col):
    cmp[:,0] = np.hstack(([np.inf],min_energy_map[:-1,j-1]))
    cmp[:,1] = min_energy_map[:,j-1]
    cmp[:,2] = np.hstack((min_energy_map[1:, j-1], [np.inf]))
    # get the min energy index
    idx = np.argmin(cmp, axis=1)
    idx -= 1
    # update backtrack and energy map
    backtrack_map[:,j] += idx
    min_energy_map[:,j] = min_energy_map[backtrack_map[:,j], j-1] + e[:,j]

  return min_energy_map, backtrack_map


  # for i in range(1,col):
  #   for j in range(row):
  #     # compare method
  #     compare = np.full([1,3], np.inf)
  #     compare[1,2] = min_energy_map[j,i-1]
  #     # boundary cases
  #     if j != 0:
  #       compare[1,1] = min_energy_map[j-1,i-1]
  #     if j != row-1:
  #       compare[1,3] = min_energy_map[j+1,i-1]
  #     # return min value and index
  #     val = np.min(compare)
  #     idx = np.argmin(compare)
  #     # update both maps
  #     min_energy_map[j,i] = val+e[j,i]
  #     backtrack_map[j,i] = j+idx-1