import cv2
import numpy as np
from matplotlib import pyplot as plt

path = "arcoiris.jpg"
img = cv2.imread(path, 0)
h, w = img.shape[:2]
imgNova = np.ones([h, w])

mascara = np.array([[-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]])
m, n = mascara.shape[:2]
sum = np.sum(mascara)
a = int((m-1)/2)
b = int((n-1)/2)

mascara = mascara/sum
max = 0
min = 999

for x in range(h-1):
    for y in range(w-1):
        for s in range(-a, a):
            for t in range(-b, b):
                if ((x+s)<(h-1) and (x+s)>0 and (y+t)<(w-1) and (y+t)>0):
                    imgNova[x, y] = imgNova[x, y] + mascara[s+a, t+b] * img[x+s, y+t]

        if imgNova[x, y] > max:
            max = imgNova[x, y]
        if imgNova[x, y] < min:
            min = imgNova[x, y]

imgNova = (imgNova - min) / (max - min)
imgNova = imgNova * 255


imgNova = imgNova.astype('uint8')


cv2.imshow("IMG Original ", img)
cv2.imshow("Concolucao", imgNova)
cv2.waitKey(0)