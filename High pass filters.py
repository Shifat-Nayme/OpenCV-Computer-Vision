import cv2
import numpy as np

img  = cv2.imread("C:\\Users\\shifa\\Desktop\\standard_test_images\\lena_color_256.tif")
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


kernel_size = 3
depth = -1

laplacian_edge = cv2.Laplacian(img,depth,kernel_size,scale=1, delta =0,
                               borderType = cv2.BORDER_DEFAULT)


grad_x = cv2.Sobel(img, depth, dx =1, dy=0,ksize=3,scale=1,delta=0,
                   borderType = cv2.BORDER_DEFAULT)



                   
grad_y = cv2.Sobel(img, depth, dx =0, dy=1, ksize=3,scale=1,delta=0,
                   borderType = cv2.BORDER_DEFAULT)


scharr_x =cv2.Scharr(img ,depth ,dx=1 ,dy=0,scale =1,delta=0,
                     borderType = cv2.BORDER_DEFAULT)
scharr_y =cv2.Scharr(img ,depth ,dx=0 ,dy=1,scale =1,delta=0,
                     borderType = cv2.BORDER_DEFAULT)

scharr_edges = scharr_x+scharr_y
addweight_scharr = cv2.addWeighted(scharr_x, 0.5, scharr_y, 0.5, 0)

cv2.imshow("Scharr edges", scharr_edges)
cv2.imshow("addweight_scharr", addweight_scharr)



#abs_grad_x = cv2.convertScaleAbs(grad_x)
#abs_grad_y = cv2.convertScaleAbs(grad_y)

addweight_sobel = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)
edges_sobel = grad_x + grad_y

cv2.imshow("addweight sobel",addweight_sobel)
cv2.imshow("Sobel edge",edges_sobel)
cv2.imshow("laplacian_edge",laplacian_edge)
cv2.imshow("original grayscale",img)
cv2.waitKey(0)
cv2.destroyAllWindows()



