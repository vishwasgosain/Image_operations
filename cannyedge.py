import cv2
def nothing (x):
	pass
cap = cv2.VideoCapture(0)
cv2.namedWindow('frame')
cv2.createTrackbar('H','frame',0,255,nothing)
cv2.createTrackbar('L','frame',0,255,nothing)
while (True):
	ret,frame = cap.read()
	h = cv2.getTrackbarPos('H','frame')
	l = cv2.getTrackbarPos('L','frame')
	edges = cv2.Canny(frame,h,l)
	cv2.imshow('frame',edges)
	k = cv2.waitKey(5) & 0xFF
	if k==27:
		break
cap.release()
cv2.destroyAllWindows()
