import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread("imgs\\test_2.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w, h, d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()

# broj boja u slici
print("Broj boja u slici: " + str(len(img_array)))

distortions = []
K = range(1, 10)
for k in range(1, 10):
    kmeanModel = KMeans(n_clusters=k)
    kmeanModel.fit(img_array)
    distortions.append(kmeanModel.inertia_)

plt.figure(figsize=(16, 8))
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Distortion')
plt.title('The Elbow Method showing the optimal k')
plt.show()

km = KMeans(n_clusters=3, init='random',
            n_init=5, random_state=0)
# pokretanje grupiranja primjera
km.fit(img_array)
# dodijeljivanje grupe svakom primjeru
labels = km.predict(img_array)

colour = km.cluster_centers_

print(colour)
plt.figure()
plt.scatter(img_array[:, 0], img_array[:, 1], c=labels)
plt.xlabel('$x_1$')
plt.ylabel('$x_2$')
plt.title('podatkovni primjeri')
plt.show()

plt.figure(2)
plt.clf()
plt.axis("off")
#plt.ittle(f"Quantized image ({n_colors} colors, K-Means)")
plt.imshow(recreate_image(km.cluster_centers_, labels, w, h))
plt.show()
