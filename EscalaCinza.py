import cv2
import numpy as np

path = "teste.jpg"
img = cv2.imread(path)
h, w = img.shape[:2]

imgNova = np.zeros((h,w,3), np.uint8)

for i in range(h):
    for j in range(w):
        imgNova[i, j] = (img[i, j, 2] + img[i, j, 1] + img[i, j, 0]) / 3
        print(imgNova[i,j])



cv2.imshow("Imagem Original", img)
cv2.imshow("Escala de cinza", imgNova)
cv2.waitKey(0)
