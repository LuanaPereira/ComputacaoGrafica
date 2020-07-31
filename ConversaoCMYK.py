import cv2
import numpy as np

path = "arcoiris.jpg"

img = cv2.imread(path)

h, w = img.shape[:2]

imgCopy = img.copy()
imgCopy = imgCopy/255.
cv2.imshow("Original ", imgCopy)
imgCMYK = np.zeros((h, w, 4), np.float)

for i in range(h):
    for j in range(w):
        black = np.min([imgCopy[i, j, 0], imgCopy[i, j, 1], imgCopy[i, j, 2]])
        blue = imgCopy[i, j, 0]
        green = imgCopy[i, j, 1]
        red = imgCopy[i, j, 2]

        imgCMYK[i, j, 3] = black
        imgCMYK[i, j, 0] = (1-red-black)/(1-black)
        imgCMYK[i, j, 1] = (1-green-black)/(1-black)
        imgCMYK[i, j, 2] = (1-blue-black)/(1-black)

imgCMYR = (imgCMYK*255).astype('uint8')
cv2.imshow("Preto ", imgCMYR[:, :, 3])
cv2.imshow("Ciano ", imgCMYR[:, :, 0])
cv2.imshow("Magenta ", imgCMYR[:, :, 1])
cv2.imshow("Amarelo ", imgCMYR[:, :, 2])
cv2.waitKey(0)