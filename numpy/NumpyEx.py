import cv2
import numpy

image_grey = cv2.imread("smallgray.png", 0)

ims = numpy.vstack((image_grey, image_grey))
lst = numpy.hsplit(image_grey, 5)
print(lst)