import cv2 as cv
import numpy as np

def half(img):
    height, width, channels = img.shape
    w = int(width/2)
    h = int(height/2)
    new_img = np.zeros((h, w, 3), dtype =  np.uint8)

    for i in range(h):
        for j in range(w):
            new_img[i, j] = img[i*2, j*2] 
    return new_img


def double(img):
    height, width, channels = img.shape
    w = int(width*2)
    h = int(height*2)
    new_img = np.zeros((h, w, 3), dtype =  np.uint8)
    
    for i in range(h-1):
        for j in range(w-1):
            new_img[i, j,0] = int((img[int(i/2), int(j/2), 0]+img[int((i + 1)/2), int((j + 1)/2), 0])/2)
            new_img[i, j,1] = int((img[int(i/2), int(j/2), 1]+img[int((i + 1)/2), int((j + 1)/2), 1])/2)
            new_img[i, j,2] = int((img[int(i/2), int(j/2), 2]+img[int((i + 1)/2), int((j + 1)/2), 2])/2)
    return new_img

img = cv.imread("b.png", -1)
cv.imshow('real_img', img)
# half_img = half(img)
# cv.imshow('HALF_img', half_img)
double_img = double(img)
cv.imshow('double_img', double_img)


cv.waitKey(0)
cv.destroyAllWindows()