'''
  File name: cumMinEngVer.py
  Author:
  Date created:
'''

'''
  File clarification:
    Computes the cumulative minimum energy over the vertical seam directions.
    
    - INPUT e: n × m matrix representing the energy map.
    - OUTPUT min_energy_map: n × m matrix representing the cumulative minimum energy map along vertical direction.
    - OUTPUT backtrack_map: n × m matrix representing the backtrack table along vertical direction.
'''

import numpy as np

def cumMinEngVer(e):

  row, col = e.shape

  min_energy_map = np.zeros((row, col))
  backtrack_map, _ = np.meshgrid(np.arange(col), np.arange(row))

  # initialize energy map
  # backtrack_map[0, :] = min_energy_map[0,:]
  min_energy_map[0,:] = e[0,:]

  # create comparision matrix
  cmp = np.zeros((3, col))

  for i in range(1, row):
    cmp[0,:] = np.hstack(([np.inf],min_energy_map[i-1,:-1]))
    cmp[1,:] = min_energy_map[i-1,:]
    cmp[2,:] = np.hstack((min_energy_map[i-1,1:],[np.inf]))
    # get the min energy index
    idx = np.argmin(cmp, axis=0)
    idx -= 1
    # update backtrack and energy map
    backtrack_map[i,:] += idx
    min_energy_map[i,:] = min_energy_map[i-1,backtrack_map[i,:]] + e[i,:]

  return min_energy_map, backtrack_map

  # for i in range(1,row):
  #   for j in range(col):
  #     # compare method
  #     compare = np.full([1,3], np.inf)
  #     compare[1,2] = min_energy_map[i-1,j]
  #     # boundary cases
  #     if j != 0:
  #       compare[1,1] = min_energy_map[i-1,j-1]
  #     if j != col-1:
  #       compare[1,3] = min_energy_map[i-1,j+1]
  #     # return min value and index
  #     val = np.min(compare)
  #     idx = np.argmin(compare)
  #     # update both maps
  #     min_energy_map[i,j] = val+e[i,j]
  #     backtrack_map[i,j] = j+idx-1