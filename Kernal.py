import numpy as np
import cv2 as cv

left_sobel = np.array([[1, 0, -1], 
                       [2, 0, -2], 
                       [1, 0, -1]])
image = cv.imread("/Users/aatishkumar/Desktop/codes/DataSet/1a/img_00001.bmp")
result = cv.filter2D(image, -1, left_sobel)
cv.imshow('result', result)
cv.waitKey(0)  
bottom_sobel = np.array([[-1, -2, -1], 
                         [0, 0, 0], 
                         [1, 2, 1]])

kernel2 = np.ones((5, 5), np.float32) / 25

image = cv.imread("/Users/aatishkumar/Desktop/codes/DataSet/1a/img_00001.bmp")
result = cv.filter2D(image, -1, kernel2 )
cv.imshow('result', result)
cv.waitKey(0)