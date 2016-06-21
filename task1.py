""" Loads an image in grayscale, displays it, 
saves if presses's' and exit if press ESC"""
#source http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_image_display/py_image_display.html#py-display-image

import numpy as numpy

import cv2 as cv

img = cv.imread("image3.jpg",0)
cv.imshow("image", img)

k = cv.waitKey(0)

if k == 27:
	cv.destroyAllWindows()
elif k == ord('s'): #waits until we press s
	cv.imwrite('saved_image.png', img)
	cv.destroyAllWindows()
