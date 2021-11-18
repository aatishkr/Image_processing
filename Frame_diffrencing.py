import cv2
import numpy as np
from numpy.core.fromnumeric import shape
numb_frame = 2
threshold  = 70
vid = cv2.VideoCapture(0)

ret, frame = vid.read()
height, width , chennel = frame.shape
frameMaster = np.zeros(shape=(height,width, numb_frame), dtype = np.uint8)
frameSum = np.zeros(shape=(height,width), dtype = np.float64)
frameShow = np.zeros(shape=(height,width), dtype = np.uint8)
for i in range(1, numb_frame):
    ret, frame = vid.read()
    framegrey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameSum[:,:] +=  framegrey[:,:]
    frameMaster[:,:,i] = framegrey[:,:]

frameAvg = frameSum/numb_frame

while(True):
    for i in range(1, numb_frame):
        ret, frame = vid.read()
        frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        for x in range(0, width):
            for y in range(0, height) :
                if abs(frameAvg[y][x] - frameGray[y][x]) > threshold:
                    frameShow[y][x] = 255
                else:
                    frameShow[y][x] = 0
                frameAvg[y][x] = frameAvg[y][x] + ((framegrey[y][x] - frameMaster[y][x][i])/numb_frame)
        frameMaster[:,:,i] = framegrey
        cv2.imshow('frame', frameShow)

            # the 'q' button is set as the
            # quitting button you may use any
            # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()