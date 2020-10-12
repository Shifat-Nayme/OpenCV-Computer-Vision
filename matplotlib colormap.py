import cv2
import matplotlib.pyplot as plt

impath = "C:\\Users\\shifa\\Desktop\\routine.jpg"
img = cv2.imread(impath,0)
plt.imshow(img, cmap ='gray')
plt.title('Spring 2019')
plt.xticks([])
plt.yticks([])
plt.show()
    


