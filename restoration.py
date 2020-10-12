import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("C:\\Users\\shifa\\Desktop\\standard_test_images\\Inked.jpg")
mask = cv2.imread("C:\\Users\\shifa\\Desktop\\standard_test_images\\mask.jpg")
img_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
mask = cv2.cvtColor(mask,cv2.COLOR_BGR2GRAY)
##ret, th = cv2.threshold(img_gray,6,255,cv2.THRESH_BINARY_INV)
##cv2.imwrite("C:\\Users\\shifa\\Desktop\\standard_test_images\\mask.jpg",th)
telea = cv2.inpaint(img1,mask,20,cv2.INPAINT_TELEA)
ns= cv2.inpaint(img1,mask,10,cv2.INPAINT_NS)




cv2.imshow("damage image",img1)
cv2.imshow("gray",img_gray)
#cv2.imshow("binary",th)
cv2.imshow("inpaint telea",telea)
cv2.imshow("inpainr ns",ns)

cv2.waitKey(0)
cv2.destroyAllWindows()
