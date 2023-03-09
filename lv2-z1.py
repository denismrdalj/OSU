import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
points = np.array([[1,1],[2,2],[3,2],[3,1]])
p = Polygon(points, edgecolor='blue', facecolor='white', linewidth=3)
fig,ax=plt.subplots()
ax.add_patch(p)
ax.set_xlim([0,4])
ax.set_ylim([0,4])
plt.show()