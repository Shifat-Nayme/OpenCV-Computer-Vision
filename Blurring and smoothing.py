import cv2
import matplotlib.pyplot as plt
import numpy as np

img  = cv2.imread("C:\\Users\\shifa\\Desktop\\standard_test_images\\4.2.07.tiff",1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

##LOW pass filters

box_blur = cv2.boxFilter(img,-1,(20,20))
blur = cv2.blur(img,(13,13))
gaussian_blur = cv2.GaussianBlur(img,(15,15),5) #parameter =img,kernel size,sigma value
median = cv2.medianBlur(img,5) #remove noise salt and paper
bilateral = cv2.bilateralFilter(img,15,75,75) #this filter removes noise and keep the edges sharp

titles =["Original","box_blur","Blur","Gaussian_blur","meadian blur","Bilateral"]
image = [img,box_blur,blur,gaussian_blur,median,bilateral]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(image[i])
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

    
