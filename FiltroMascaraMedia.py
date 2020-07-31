import cv2
import numpy as np
from matplotlib import pyplot as plt

path = "arcoiris.jpg"
img = cv2.imread(path)
h, w = img.shape[:2]

cv2.imshow("IMG Original ", img)
imgNova = np.zeros((h, w, 3), np.uint8)

mascara = np.array([[1, 1, 1],
                    [1, 7, 1],
                    [1, 1, 1]])
sumaEleMascara = np.sum(mascara)

for i in range(h):
    for j in range(w):
        if i == 0 and j == 0:
            imgNova[i, j, 0] = (img[i, j, 0]*mascara[1, 1] + img[i+1, j, 0]*mascara[1, 2] + img[i, j+1, 0]*mascara[2, 1] + img[i+1, j+1, 0]*mascara[2,2])/ sumaEleMascara
            imgNova[i, j, 1] = (img[i, j, 1]*mascara[1, 1] + img[i+1, j, 1]*mascara[1, 2] + img[i, j+1, 1]*mascara[2, 1] + img[i+1, j+1, 1]*mascara[2,2])/ sumaEleMascara
            imgNova[i, j, 2] = (img[i, j, 2]*mascara[1, 1] + img[i+1, j, 2]*mascara[1, 2] + img[i, j+1, 2]*mascara[2, 1] + img[i+1, j+1, 2]*mascara[2,2])/ sumaEleMascara

        elif i == h-1 and j == w-1:
            imgNova[i, j, 0] = (img[i, j, 0] * mascara[1, 1] + img[i-1, j, 0] * mascara[0, 1] + img[i, j-1, 0] * mascara[1, 0] + img[i-1, j-1, 0] * mascara[0, 0]) / sumaEleMascara
            imgNova[i, j, 1] = (img[i, j, 1] * mascara[1, 1] + img[i-1, j, 1] * mascara[0, 1] + img[i, j-1, 1] * mascara[1, 0] + img[i-1, j-1, 1] * mascara[0, 0]) / sumaEleMascara
            imgNova[i, j, 2] = (img[i, j, 2] * mascara[1, 1] + img[i-1, j, 2] * mascara[0, 1] + img[i, j-1, 2] * mascara[1, 0] + img[i-1, j-1, 2] * mascara[0, 0]) / sumaEleMascara

        elif j == 0 and i == h-1: #esquerdo baixo
            imgNova[i, j, 0] = (img[i, j, 0] * mascara[1, 1] + img[i, j+1, 0] * mascara[1, 2] + img[i-1, j, 0] * mascara[0, 1] + img[i-1, j+1, 0] *mascara[0, 2])/sumaEleMascara
            imgNova[i, j, 1] = (img[i, j, 1] * mascara[1, 1] + img[i, j+1, 1] * mascara[1, 2] + img[i-1, j, 1] * mascara[0, 1] + img[i-1, j+1, 1] *mascara[0, 2])/sumaEleMascara
            imgNova[i, j, 2] = (img[i, j, 2] * mascara[1, 1] + img[i, j+1, 2] * mascara[1, 2] + img[i-1, j, 2] * mascara[0, 1] + img[i-1, j+1, 2] *mascara[0, 2])/sumaEleMascara

        elif i == 0 and j == w-1: #direito cima
            imgNova[i, j, 0] = (img[i, j, 0] * mascara[1, 1] + img[i, j-1, 0] *mascara[1, 0] + img[i+1, j, 0] * mascara[2, 1] +img[i+1, j-1, 0] * mascara[2, 0])/sumaEleMascara
            imgNova[i, j, 1] = (img[i, j, 1] * mascara[1, 1] + img[i, j-1, 1] *mascara[1, 0] + img[i+1, j, 1] * mascara[2, 1] +img[i+1, j-1, 1] * mascara[2, 0])/sumaEleMascara
            imgNova[i, j, 2] = (img[i, j, 2] * mascara[1, 1] + img[i, j-1, 2] *mascara[1, 0] + img[i+1, j, 2] * mascara[2, 1] +img[i+1, j-1, 2] * mascara[2, 0])/sumaEleMascara

        elif j == 0: #esquerda
            imgNova[i, j, 0] = (img[i, j, 0] * mascara[1, 1] + img[i, j+1, 0] * mascara [1,2] + img[i-1, j, 0] * mascara[0, 1] + img[i-1, j+1, 0] * mascara[0,2] +img[i+1, j, 0] * mascara[2, 1] + img[i+1, j+1, 0] * mascara[2, 2])/sumaEleMascara
            imgNova[i, j, 1] = (img[i, j, 1] * mascara[1, 1] + img[i, j+1, 1] * mascara [1,2] + img[i-1, j, 1] * mascara[0, 1] + img[i-1, j+1, 1] * mascara[0,2] +img[i+1, j, 1] * mascara[2, 1] + img[i+1, j+1, 1] * mascara[2, 2])/sumaEleMascara
            imgNova[i, j, 2] = (img[i, j, 2] * mascara[1, 1] + img[i, j+1, 2] * mascara [1,2] + img[i-1, j, 2] * mascara[0, 1] + img[i-1, j+1, 2] * mascara[0,2] +img[i+1, j, 2] * mascara[2, 1] + img[i+1, j+1, 2] * mascara[2, 2])/sumaEleMascara

        elif j == w-1: #direita
            imgNova[i, j, 0] = (img[i, j, 0] * mascara[1,1] + img[i, j-1, 0] * mascara[1, 0] + img[i-1, j, 0] * mascara[0, 1] + img[i-1, j-1, 0] * mascara[0, 0] +img[i+1, j, 0] * mascara[2, 1] + img[i+1, j-1, 0] * mascara[2, 0])/sumaEleMascara
            imgNova[i, j, 1] = (img[i, j, 1] * mascara[1,1] + img[i, j-1, 1] * mascara[1, 0] + img[i-1, j, 1] * mascara[0, 1] + img[i-1, j-1, 1] * mascara[0, 0] +img[i+1, j, 1] * mascara[2, 1] + img[i+1, j-1, 1] * mascara[2, 0])/sumaEleMascara
            imgNova[i, j, 2] = (img[i, j, 2] * mascara[1,1] + img[i, j-1, 2] * mascara[1, 0] + img[i-1, j, 2] * mascara[0, 1] + img[i-1, j-1, 2] * mascara[0, 0] +img[i+1, j, 2] * mascara[2, 1] + img[i+1, j-1, 2] * mascara[2, 0])/sumaEleMascara

        elif i == 0: #cima
            imgNova[i, j, 0] = (img[i, j, 0] * mascara[1, 1] + img[i, j+1, 0] * mascara[1,2] + img[i, j-1, 0] *mascara[1, 0] + img[i+1, j, 0] * mascara[2, 1] + img[i+1, j+1, 0] * mascara[2, 2] + img[i+1, j-1, 0] * mascara[2, 0])/sumaEleMascara
            imgNova[i, j, 1] = (img[i, j, 1] * mascara[1, 1] + img[i, j+1, 1] * mascara[1,2] + img[i, j-1, 1] *mascara[1, 0] + img[i+1, j, 1] * mascara[2, 1] + img[i+1, j+1, 1] * mascara[2, 2] + img[i+1, j-1, 1] * mascara[2, 0])/sumaEleMascara
            imgNova[i, j, 2] = (img[i, j, 2] * mascara[1, 1] + img[i, j+1, 2] * mascara[1,2] + img[i, j-1, 2] *mascara[1, 0] + img[i+1, j, 2] * mascara[2, 1] + img[i+1, j+1, 2] * mascara[2, 2] + img[i+1, j-1, 2] * mascara[2, 0])/sumaEleMascara

        elif i == h-1: #baixo
            imgNova[i, j, 0] = (img[i, j, 0] * mascara[1, 1] + img[i, j+1, 0] * mascara[1, 2] + img[i, j-1, 0] * mascara[1, 0] + img[i-1, j, 0] * mascara[0, 1] + img[i-1, j+1, 0] * mascara[0, 2] + img[i-1, j-1, 0] * mascara[0, 0])/sumaEleMascara
            imgNova[i, j, 1] = (img[i, j, 1] * mascara[1, 1] + img[i, j+1, 1] * mascara[1, 2] + img[i, j-1, 1] * mascara[1, 0] + img[i-1, j, 1] * mascara[0, 1] + img[i-1, j+1, 1] * mascara[0, 2] + img[i-1, j-1, 1] * mascara[0, 0])/sumaEleMascara
            imgNova[i, j, 2] = (img[i, j, 2] * mascara[1, 1] + img[i, j+1, 2] * mascara[1, 2] + img[i, j-1, 2] * mascara[1, 0] + img[i-1, j, 2] * mascara[0, 1] + img[i-1, j+1, 2] * mascara[0, 2] + img[i-1, j-1, 2] * mascara[0, 0])/sumaEleMascara

        else : #meio
            imgNova[i, j, 0] = (img[i, j, 0] * mascara[1, 1] + img[i, j+1, 0] * mascara[1, 2] + img[i, j-1, 0] * mascara[1, 0] + img[i-1, j, 0] * mascara[0, 1] + img[i-1, j+1, 0] * mascara[0, 2] + img[i-1, j-1, 0] * mascara[0, 0] + img[i+1, j, 0] * mascara[2, 1] + img[i+1, j+1, 0] * mascara[2, 2] + img[i+1, j-1, 0] * mascara[2, 0])/sumaEleMascara
            imgNova[i, j, 1] = (img[i, j, 1] * mascara[1, 1] + img[i, j+1, 1] * mascara[1, 2] + img[i, j-1, 1] * mascara[1, 0] + img[i-1, j, 1] * mascara[0, 1] + img[i-1, j+1, 1] * mascara[0, 2] + img[i-1, j-1, 1] * mascara[0, 0] + img[i+1, j, 1] * mascara[2, 1] + img[i+1, j+1, 1] * mascara[2, 2] + img[i+1, j-1, 1] * mascara[2, 0])/sumaEleMascara
            imgNova[i, j, 2] = (img[i, j, 2] * mascara[1, 1] + img[i, j+1, 2] * mascara[1, 2] + img[i, j-1, 2] * mascara[1, 0] + img[i-1, j, 2] * mascara[0, 1] + img[i-1, j+1, 2] * mascara[0, 2] + img[i-1, j-1, 2] * mascara[0, 0] + img[i+1, j, 2] * mascara[2, 1] + img[i+1, j+1, 2] * mascara[2, 2] + img[i+1, j-1, 2] * mascara[2, 0])/sumaEleMascara


cv2.imshow("Filtro Mascara Media", imgNova)
cv2.waitKey(0)