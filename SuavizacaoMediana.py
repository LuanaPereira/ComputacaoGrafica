import cv2
import numpy as np
from matplotlib import pyplot as plt

path = "arcoiris.jpg"
img = cv2.imread(path)
h, w = img.shape[:2]

cv2.imshow("IMG Original ", img)
imgNova = np.zeros((h, w, 3), np.uint8)
#dimensao = 7 --> matriz 7x7
dimensao = 11
raio = int(dimensao - (dimensao/2)+1)

for i in range(h):
    for j in range(w):
        b = []
        g = []
        r = []

        for s in range(i-raio, i+raio):
            for t in range(j-raio, j+raio):

                if s>=0 and t>=0 and s<h and t < w:
                    b.append(img[s, t, 0])
                    g.append(img[s, t, 1])
                    r.append(img[s, t, 2])


        medianaB = np.median(b)
        medianaG = np.median(g)
        medianaR = np.median(r)

        imgNova[i, j, 0] = medianaB
        imgNova[i, j, 1] = medianaG
        imgNova[i, j, 2] = medianaR


cv2.imshow("Suavizacao Medidana ", imgNova)
cv2.waitKey(0)

