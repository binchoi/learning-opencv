import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

green = (0,255,0)
red = (0,0,255)

# blank[:] = red_tuple
# cv.imshow('Canvas', blank)

# blank[200:300, 200:300] = red_tuple
# cv.imshow('square', blank)

# Rectangle
cv.rectangle(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), green, thickness=-1)
# cv.imshow('Rectangle', blank)


# Circle
cv.circle(blank, (blank.shape[1]//2,blank.shape[0]//2), 40, red, thickness=3)
# cv.imshow('circle', blank)

# Line
cv.line(blank, (0,0), (blank.shape[1]//2,blank.shape[0]//2), (255,255,255), thickness=3)
# cv.imshow('line', blank)


# Text
cv.putText(blank, 'Hello', (225,225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,255), thickness=2)
cv.imshow('text', blank)

cv.waitKey(0)