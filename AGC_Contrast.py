import cv2
import matplotlib.pyplot as plt
import numpy as np
import glob
threshold = 10

img_array = []
for filename in glob.glob('/home/kali/Documents/16BitFrames/*.png'):
    img = cv2.imread(filename,0)
    height, width = img.shape
    size = (width,height)
    img_array.append(img)

def histogram(img):
    (row, col) = img.shape[0:2]
    hist = np.zeros((65536), dtype=np.int32)
# Take the average of pixel values of the BGR Channels
# to convert the colored image to grayscale image
    for i in range(row):
        for j in range(col):
            hist[img[i,j]] += 1
    return hist

def AGC_contrast(img):
    hist = histogram(img)
    for i in range(65535):
        if hist[i] > threshold:
            h_min = hist[i]
            break
    for i in range(65535):
        if hist[65535 - i] > threshold:
            h_max = hist[i]
            break
    height, width = img.shape
    for i in range(height):
        for j in range(width):
            img[i, j] = ((img[i, j] - float(h_min))/float(h_max - h_min))*255
            
    return img

for i in range(len(img_array)):
    img = AGC_contrast(img_array[i])
    # cv2.imshow("grayscale image",img_array[i])
    cv2.imshow("grayscale image",img)
    #hist = histogram(img_array[i])
    #plt.plot(hist)
    #plt.show()
    cv2.waitKey(0)