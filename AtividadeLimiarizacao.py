#Exercício: Ler uma imagem, converter em escala de cinza,
# utilizando a seguinte fórmula:
#	Gr = R*0,25 + G*0,65 + B*0,1
#ler o seu histograma e verificar qual o nível de cor
# possui maior intensidade na imagem. Imprima o histograma.
# A partir da imagem do histograma, identifique um limiar
# para fazer a limiarização desta imagem. Imprima a imagem
# resultante.

import cv2
import numpy as np
from matplotlib import pyplot as plt
path = "arcoiris.jpg"

img = cv2.imread(path)
h, w = img.shape[:2]
cv2.imshow("IMG Original ", img)
limiar = 150
imgcinza = np.zeros((h,w), np.uint8)
imgcinza = (img[...,0]*0.1 + img[..., 1]*0.65 + img[...,2]*0.25).astype('uint8')
cv2.imshow("Escala de Cinza ", imgcinza)
histograma = cv2.calcHist([imgcinza], [0], None, [256], [0,256])
max = np.argmax(histograma)
print(max)
th, res = cv2.threshold(img[...,1],220,255,cv2.THRESH_BINARY)
cv2.imshow("Limiarizado", res)
plt.plot(histograma,color = 'b')
plt.xlim([0,255])
plt.show()
cv2.waitKey(0)