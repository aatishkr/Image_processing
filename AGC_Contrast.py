import cv2
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import glob
path = '/home/kali/Documents/16BitFrames/frameIndex_0_2019-11-16_23.08.04.png'
img = cv2.imread(path, 0)

img_array = []
for filename in glob.glob('home/kali/Documents/16BitFrames/*.png'):
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)
    img_array.append(img)

def histogram(img):
    (row, col) = img.shape[0:2]
    hist = np.zeros((255,), dtype=int)
# Take the average of pixel values of the BGR Channels
# to convert the colored image to grayscale image
    for i in range(row):
        for j in range(col):
            hist[img[i,j]] += 1 
    return hist

hist = histogram(img)
# plt.plot(hist)
# plt.show()

cv2.imshow('img',img_array[:,:,:,1])

for i in range(len(img_array)):
    cv2.imshow('img',img_array[i], 0)
    cv2.waitKey(100)