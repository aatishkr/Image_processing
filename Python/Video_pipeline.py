import cv2
import numpy as np
  
  
# define a video capture object
vid = cv2.VideoCapture(0)
  
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame

    height, width = frameGray.shape
    print(height, width)
    for x in range(0, width) :
        for y in range(0, height) :
            print(frameGray[y,x])



    cv2.imshow('frame', frameGray)
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()