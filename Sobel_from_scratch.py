# import matplotlib
from cv2 import COLOR_BGR2GRAY
import numpy as np
import cv2

path = "Goa.JPG"
img = cv2.imread(path,0)

left_sobel = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
top_sobel =  np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])
Gaussian = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]])

blur_image = np.zeros(img.shape, dtype=np.uint8)
for i in range(1,img.shape[0]-1):
    for j in range(1,img.shape[1]-1):
        mat_in = (np.multiply(img[i-1:i+2,j-1:j+2],Gaussian))
        blur_image[i][j] = np.sum(mat_in)/16

New_image_top =  np.zeros(blur_image.shape, dtype=np.int16)
New_image_left = np.zeros(blur_image.shape, dtype=np.int16)
sobel =          np.zeros(blur_image.shape, dtype=np.uint8)
for i in range(1,blur_image.shape[0]-1):
    for j in range(1,blur_image.shape[1]-1):
        New_image_left[i][j] = np.sum(np.multiply(blur_image[i-1:i+2,j-1:j+2],left_sobel))
        New_image_top[i][j] =  np.sum(np.multiply(blur_image[i-1:i+2,j-1:j+2],top_sobel))
        sobel[i][j] = np.sqrt(New_image_left[i][j]**2 + New_image_top[i][j]**2)
        temp = sobel[i][j]
        if sobel[i][j] < 40:
            sobel[i][j] = 0

cv2.imshow('graycsale image',img)
cv2.waitKey(0)
cv2.imshow('graycsale image',sobel)
cv2.waitKey(0)
