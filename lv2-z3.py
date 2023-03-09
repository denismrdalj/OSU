import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageEnhance

img=Image.open('road.jpg')
img_enhancer= ImageEnhance.Brightness(img)
original=img
brighter=img_enhancer.enhance(2)
plt.imshow(brighter)
plt.show()

width, height=img.size
left=160
top=height
right=320
bottom=0
cropped=img.crop((left,bottom,right,top))
plt.imshow(cropped)
plt.show()

rotated=img.rotate(90)
plt.imshow(rotated)
plt.show()