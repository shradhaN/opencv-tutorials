#source http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html#py-display-image

#import numpy
import numpy as np

#import opencv
import cv2 as cv

# load image in grayscale
img = cv.imread ("image2.jpg", 0)  
# to load color image us 1 , for image with alpha channel use -1

#display the image
cv.imshow("image", img)

#can display as many windows but must have different name

cv.imshow("image2", img)

#waits for any key for 0 millisecond to stop the processing, we can also specify it 
cv.waitKey(0)


#destroy all windows we created
cv.destroyAllWindows()
#use cv.destroyWindow("window_name") for a particular window

# can be used to create a window first so that the window can be resized
cv.namedWindow('image', cv2.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()

#saves an image
cv.writeimage("save1.png", img)

