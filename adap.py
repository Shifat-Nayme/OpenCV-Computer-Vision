import cv2 
import numpy as np
import matplotlib.pyplot as plt
import math
import glob
final_img =[]

def function(image):
    global final_img
    #th3 = cv2.adaptiveThreshold(image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C)
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    th = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                             cv2.THRESH_BINARY,11,2)
    final_img.append(th)



images = [cv2.imread(file) for file in glob.glob("C://Users//shifa//Desktop//New folder (3)//*.jpg")]
print(len(images))

for i in range(len(images)): 
    function(images[i])


outpath ="C://Users//shifa//Desktop//New folder (2)//"
idx =1

for j in range(len(final_img)):
    img = final_img[j]
    cv2.imwrite(outpath + str(idx) + '.jpg', img)
    idx = idx + 1