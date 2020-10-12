import cv2
import numpy as np

img = cv2.imread("C:\\Users\\shifa\\Desktop\\standard_test_images\\book_page.jpg")
img = cv2.resize(img, (512,512))
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, threshold = cv2.threshold(img , 155, 255 ,cv2.THRESH_BINARY)
block_size = 15
const = 9
adaptive_mean = cv2.adaptiveThreshold(img_gray, 255,cv2.ADAPTIVE_THRESH_MEAN_C,
                                      cv2.THRESH_BINARY,block_size,const)
gaussian = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY,block_size,const)
cv2.imshow("original",img)
cv2.imshow("THRESHOLD",threshold)
cv2.imshow("adaptive_mean",adaptive_mean)
cv2.imshow("adaptive_gaussian",gaussian)
cv2.waitKey(0)
cv2.destroyAllWindows()

                 
