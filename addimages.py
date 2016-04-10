import cv2
import numpy as np
img1= cv2.imread('a1.jpg')
img2= cv2.imread('a2.jpg')
#add = img1 + img2
add = cv2.add(img1,img2)

cv2.imshow('add',add)
cv2.waitKey(0)
cv2.destroyAllWindows()

