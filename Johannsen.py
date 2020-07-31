import cv2
import numpy as np
from matplotlib import pyplot as plt

path = "arcoiris.jpg"
img = cv2.imread[path, 0]
hm,  = img.shape[:2]

cv2.imshow("IMG Original ", img)


#histograma e printa
histograma = cv2.calcHist([imgcinza], [0], None, [256], [0,256])

somaPit = 0
somaPi_1 = 0
somaPt = 0
somaPi_t255_1 = 0

for t in range(1, 256):
    for a in range(1, t):
        somaPit += histograma[a]
    for b in range(t-1):
        somaPi_1 += histograma[b]
   
    entropia = -histograma[t] * np.log(histograma[t])
    entropiaSoma = -somaPi_1 * np.log(somaPi_1)



    sbt = np.log(somaPit) + (1 / somaPit+1) * (entropia + entropiaSoma)

    print(sbt)
    c = t
    d = t+1
    for c in range(255):
        somaPt += histograma[c]
    for d in range(255):
        somaPi_t255_1 += histograma[d-1]

    entropiaSWT = -somaPi_t255_1*np.log(somaPi_t255_1)
    swt = np.log(somaPt) + (1/somaPt) * (entropia + entropiaSWT)

    val = sbt + swt

binaria = np.zeros((h, w), np.uint8)

for i in range(h):
    for j in range(w):
        if imgcinza[i, j] >= val:
            binaria[i, j] = 255

cv2.imshow("Binaria ", binaria)
plt.plot(histograma,color = 'b')
plt.xlim([0,255])
plt.show()
cv2.waitKey(0)