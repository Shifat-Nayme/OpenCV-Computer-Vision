import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('C:\\Users\\shifa\\Desktop\\123.png')
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
resize_img = cv2.resize(img1, (256 , 256))

x = np.copy(resize_img)

red = resize_img[:,:,2]
green = resize_img[:,:,1]
blue = resize_img[:,:,0]

#print(red,green,blue)

print(np.mean(x))

height, width,canal = x.shape

zeros = np.zeros(x.shape, np.uint8)
z = np.zeros(x.shape, np.uint8)

for i in range (height):
    for j in range (width):
        if i<= 128:
            #zeros = x[i][j] - z[i][j]
            z[i][j]= 0
            #z[i][j] = x[i][j] + zeros
        else:
            z[i][j] = x[i][j]

plt.imshow(z)
plt.show()
