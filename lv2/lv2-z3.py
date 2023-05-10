import numpy as np
import matplotlib . pyplot as plt

img = plt.imread ("road.jpg")
img = img [ :,:,0]. copy ()

#a
plt.figure()
plt.imshow(img, 'gray', alpha=0.5)
plt.show()

#b
quarters=np.hsplit(img,4)
plt.imshow(quarters[1], cmap="gray")
plt.show()

#c
rotated=img.rotate(90)
plt.imshow(rotated, cmap="gray")
plt.show()

#d
mirror=np.flip(img,axis=1)
plt.imshow(mirror, cmap="gray")
plt.show()