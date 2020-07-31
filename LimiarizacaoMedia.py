import cv2
import numpy as np
from matplotlib import pyplot as plt

path = "arcoiris.jpg"
img = cv2.imread(path, 0)

h, w = img.shape[:2]

cv2.imshow("IMG Original ", img)

histograma = cv2.calcHist([img], [0], None, [256], [0,256])

totalPixel = h * w

imgNova = np.zeros((h, w), np.uint8)

maiorProbabilidade = 0
limiar = 0
for i in range(256):
    probabilidade = histograma[i]/totalPixel

    if probabilidade > maiorProbabilidade:
        maiorProbabilidade = probabilidade
        limiar = i

print(limiar)
for i in range(h):
    for j in range(w):
        if img[i, j] >= limiar:
            imgNova[i, j] = 255

cv2.imshow("Media Limiar ", imgNova)

plt.plot(histograma)
plt.xlim([0,255])
plt.show()
cv2.waitKey(0)