import cv2
import numpy as np
from numpy.core.fromnumeric import shape

threshold = 150
vid = cv2.VideoCapture(0)
ret, frame_previous = vid.read()
height, width , chennel = frame_previous.shape
print(height, width , chennel)
frameShow = np.zeros(shape=(height,width), dtype = np.uint8)
frameGray_previous = cv2.cvtColor(frame_previous, cv2.COLOR_BGR2GRAY)

while(True):
    ret, frame = vid.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    for x in range(0, width):
        for y in range(0, height) :
            if abs(frameGray_previous[y][x] - frameGray[y][x]) > threshold:
                frameShow[y][x] = 255
            else:
                frameShow[y][x] = 0
    frameGray_previous = frameGray

    cv2.imshow('frame', frameShow)
                # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()