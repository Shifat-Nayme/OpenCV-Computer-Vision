import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

img  = cv2.imread("C:\\Users\\shifa\\Desktop\\standard_test_images\\4.1.08.tiff")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
rows,col,channel = img.shape

probability = 0.05

output = np.zeros(img.shape, np.uint8)

for i in range(rows):
    for j in range(col):
        r = random.random()
        if r<probability/2:
            #pepper sprinkled
            output[i][j] = [0,0,0]
        elif r<probability:
            #salt sprinkled
            output[i][j] = [255,255,255]
        else:
            output[i][j] = img[i][j]

plt.imshow(output)
plt.title("salt & pepper")
plt.xticks([])
plt.yticks([])
plt.show()
