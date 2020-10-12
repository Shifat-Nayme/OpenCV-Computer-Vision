import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread("C:\\Users\\shifa\\Desktop\\standard_test_images\\road.jpg")
img2 = cv2.imread("C:\\Users\\shifa\\Desktop\\standard_test_images\\car.jpg")
img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, threshold = cv2.threshold(img2_gray,240,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(threshold)
road = cv2.bitwise_and(img1,img1,mask = threshold)
car = cv2.bitwise_and(img2,img2, mask = mask_inv)
sum = cv2.add(road,car)


cv2.imshow("result",sum)
cv2.imshow("road",road)
cv2.imshow("img2",img2)
cv2.imshow("car",car)
cv2.imshow("mask_inv",mask_inv)
cv2.waitKey(0)
cv2.destroyAllWindows()
