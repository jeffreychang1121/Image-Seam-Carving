from carv import carv
import cv2
import matplotlib.pyplot as plt

im1 = cv2.imread('Test1.jpg')
b,g,r = cv2.split(im1)
im1_rgb = cv2.merge([r,g,b])

carv_img, _ = carv(im1_rgb, 20, 10)


print(im1.shape)
print(carv_img.shape)

plt.figure(1)
plt.imshow(im1_rgb)
plt.figure(2)
plt.imshow(carv_img)
# fig = plt.figure()
# ax1 = fig.add_subplot(211)
# ax2 = fig.add_subplot(222)
#
# ax1.title.set_text('Original image')
# ax2.title.set_text('Carving image')

plt.show()

