import cv2
import numpy as np
from matplotlib import pyplot as plt

img= cv2.imread('to.png')

kernel = np.ones((5,5),np.float32)/25
dst = cv2.filter2D(img,-1,kernel) 
#blur = cv2.GaussianBlur(img,(5,5),0)
#median = cv2.medianBlur(img,5)
#blur = cv2.bilateralFilter(img,9,75,75)
plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Smooth Image')
plt.xticks([]), plt.yticks([])
plt.show()
