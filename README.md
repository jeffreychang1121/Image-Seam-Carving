# Image-Seam-Carving
### 1. Computing Cumulative Minimum Energy
       [My, Tby] = cumMinEngHor(e)
- (INPUT) e: *n* x *m* matrix representing the energy map
- (OUTPUT) My: n* x *m* matrix representing the cumulative minimum energy map along horizontal direction
- (OUTPUT) Tby: n* x *m* matrix representing the backtrack table along horizontal direction
### 2. Removing a Seam
       [Iy, E] = rmHorSeam(I, My, Tby)
- (INPUT) I: n* x *m* x 3 matrix representing the input image
- (INPUT) My: n* x *m* matrix representing the cumulative minimum energy map along the horizontal direction
- (INPUT) Tby: n* x *m* matrix representing the backtrack table along horizontal direction
- (OUTPUT) Iy: (n-1) x *m* x 3 matrix representing the image with the row removed
- (OUTPUT) E: the cost of seam removal
### 3. Discrete Image Resizing
        [Ic, T] = carv(I, nr, nc)
- (INPUT) I: n* x *m* x 3 matrix representing the input image.
- (INPUT) nr: the numbers of rows to be removed from the image.
- (INPUT) nc: the numbers of columns to be removed from the image.
- (OUTPUT) Ic: (*n* - *nr*) x (*m* - *nc*) x 3 matrix representing the carved image.
- (OUTPUT) T: (*nr* + 1) x (*nc* + 1) matrix representing the transport map.
