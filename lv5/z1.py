import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn . linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn . metrics import accuracy_score, precision_score, recall_score


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
random_state=213, n_clusters_per_class=1, class_sep=1)
X_train, X_test, y_train, y_test = train_test_split(
X, y, test_size=0.2, random_state=5)

colors = ['red', 'blue']
plt.scatter(X_train[:,0], X_train[:,1], c=y_train, cmap=ListedColormap(colors))
plt.scatter(X_test[:,0], X_test[:,1], c=y_test, cmap=ListedColormap(colors), marker='x')
plt.legend(['Train', 'Test'])
plt.title('Podaci za učenje i testiranje')
plt.xlabel('x1')
plt.ylabel('x2')

LogRegression_model = LogisticRegression()
LogRegression_model.fit( X_train , y_train )

theta0 = LogRegression_model.intercept_
coefs = LogRegression_model.coef_.T
a = -coefs[0]/coefs[1]
c = -theta0/coefs[1]
xymin, xymax = -4, 4
xd = np.array([xymin, xymax])
yd = a*xd + c
plt.plot(xd, yd, linestyle='--')
plt.show()

y_test_p = LogRegression_model.predict(X_test)
cm = confusion_matrix(y_test, y_test_p)
print("Matrica zabune:", cm)
disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_test_p))
disp.plot()
plt.show()
print('Točnost:', round(accuracy_score(y_test, y_test_p), 2))
print('Preciznost:', round(precision_score(y_test, y_test_p), 2))
print('Odziv:', round(recall_score(y_test, y_test_p), 2))

y_color = (y_test == y_test_p)
plt.scatter(X_test[:, 0], X_test[:, 1], marker="o", c=y_color, s=25, cmap=mcolors.ListedColormap(["red", "green"]))
plt.show()




















