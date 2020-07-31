import cv2
import numpy as np

path = "arcoiris.jpg"

img = cv2.imread(path, 0)

h, w = img.shape[:2]

cv2.imshow("IMG Original ", img)

limiar = 150

binaria = np.zeros((h, w), np.uint8)

for i in range(h):
    for j in range(w):
        if img[i, j] >= limiar:
            binaria[i, j] = 255

cv2.imshow("Binaria ", binaria)
cv2.waitKey(0)