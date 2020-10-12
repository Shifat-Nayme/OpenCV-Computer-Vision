import cv2
import numpy as np

img  = cv2.imread("C:\\Users\\shifa\\Desktop\\standard_test_images\\house.tif")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
L1 = cv2.Canny(img,100,200, L2gradient=False)
L2 = cv2.Canny(img,100,200,apertureSize=5, L2gradient=True)

canny_edge = cv2.Canny(img,100,200)
cv2.imshow("L1",L1)
cv2.imshow("L2",L2)
cv2.imshow("original",img)
cv2.imshow("canny edge detection",canny_edge)
cv2.waitKey(0)
cv2.destroyAllWindows()
