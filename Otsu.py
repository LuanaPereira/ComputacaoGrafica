import cv2
import numpy as np
from matplotlib import pyplot as plt

path = "arcoiris.jpg"
img = cv2.imread(path)
h, w = img.shape[:2]

cv2.imshow("IMG Original ", img)

#transformar img emn escala de cinza
imgcinza = np.zeros((h,w), np.uint8)
imgcinza = (img[...,0]*0.1 + img[..., 1]*0.65 + img[...,2]*0.25).astype('uint8')
cv2.imshow("Escala de Cinza ", imgcinza)


#histograma e printa
histograma = cv2.calcHist([imgcinza], [0], None, [256], [0,256])


#algoritmo de otsu para achar limiar
totalPixel = h*w
soma = 0

for i in range(256):
    soma += i * histograma[i]

somaB = 0

fundo = 0
frente = 0

varianciaMaior = 0
threshold = 0

for i in range(256):
    fundo += histograma[i]
    if (fundo == 0):
        continue

    frente = totalPixel - fundo
    if (frente == 0):
        break

    somaB += i*histograma[i]

    mediaFundo = somaB / fundo
    mediaFrente = (soma - somaB) / frente

    variancia = fundo * frente * (mediaFundo-mediaFrente) * (mediaFundo-mediaFrente)

    if (variancia > varianciaMaior):
        varianciaMaior = variancia
        threshold = i

binaria = np.zeros((h, w), np.uint8)

for i in range(h):
    for j in range(w):
        if imgcinza[i, j] >= threshold:
            binaria[i, j] = 255

cv2.imshow("Binaria ", binaria)
plt.plot(histograma)
plt.xlim([0,255])
plt.show()
cv2.waitKey(0)
