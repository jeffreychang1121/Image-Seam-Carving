'''
  File name: cumMinEngHor.py
  Author:Ningshan Zhang
  Date created:10/18/2018
'''

'''
  File clarification:
    Computes the cumulative minimum energy over the horizontal seam directions.
    
    - INPUT e: n × m matrix representing the energy map.
    - OUTPUT My: n × m matrix representing the cumulative minimum energy map along horizontal direction.
    - OUTPUT Tby: n × m matrix representing the backtrack table along horizontal direction.
'''
import numpy as np


def cumMinEngHor(e):

  Tby = np.zeros(e.shape).astype('int')
  h = np.size(e, axis=0)
  w = np.size(e, axis=1)
  for i in range(1, w):
    My = e.copy()
    upleft = np.hstack([np.array([10000]), e[0:-1,i-1]])
    left = e[:, i-1]
    downleft = np.hstack([e[1:, i-1], np.array([10000])])
    left_three=np.stack([upleft,left,downleft],axis=-1)

    My[:, i] = np.min(left_three, axis=-1) + e[:, i]
    Tby[:, i] = np.argmin(left_three, axis=-1) + np.arange(-1, h - 1)
  return My, Tby