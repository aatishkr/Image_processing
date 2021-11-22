import cv2
import matplotlib.pyplot as plt
import numpy as np
import glob
min_threshold = 10
max_threshold = 10

img_array = []
for filename in glob.glob('/home/kali/Documents/16BitFrames/*.png'):
    img = cv2.imread(filename,-1)
    height, width = img.shape
    size = (width,height)
    img_array.append(img)

def histogram(img):
    (row, col) = img.shape[0:2]
    hist = np.zeros((65536), dtype=np.float64)
    for i in range(row):
        for j in range(col):
            hist[img[i,j]] += 1
    return hist

def AGC_contrast(img):
    hist = histogram(img)
    img_new = np.zeros((240,320), dtype=np.uint8)
    for i in range(1,65535):
        if hist[i] > min_threshold:
            h_min = i
            break
    for i in range(1,65535):
        if hist[65535 - i] > max_threshold:
            h_max = 65535 - i
            break
    print(h_min,h_max)
    height, width = img.shape
    if h_max == h_min:
        return img

    LUT  = np.zeros((65536), dtype=np.float64)
    for i in range(h_min, 65536):
        LUT[i] = ((np.float64(i) - h_min)/(h_max - h_min))*255
        if i >= h_max:
            LUT[i] = 255

    for i in range(height):
        for j in range(width):
            # if img[i, j] > h_max:
            #     img[i, j] = h_max
            # if img[i, j] < h_min:
            #     img[i, j] = h_min
            # img_new[i, j] = ((np.float64(img[i, j]) - h_min)/(h_max - h_min))*255
            img_new[i, j] = LUT[img[i, j]]
    return img_new

for i in range(len(img_array)):
    img = AGC_contrast(img_array[i])
    # cv2.imshow("grayscale image",img_array[i])
    cv2.imshow("grayscale image" ,img)
    print(i)
    # hist = histogram(img_array[i])
    # plt.plot(hist)
    # plt.show()
    cv2.waitKey(0)