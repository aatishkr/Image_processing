# import the opencv library
import cv2 as cv
import numpy as np
# define a video capture object
vid = cv.VideoCapture(0)

while(True):
	ret, frame = vid.read()
	left_sobel = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
	result = cv.filter2D(frame, -1, left_sobel)
	cv.imshow('result', result)


	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()

