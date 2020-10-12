import cv2
import matplotlib.pyplot as plt
import numpy as np

img  = cv2.imread("C:\\Users\\shifa\\Desktop\\standard_test_images\\4.2.07.tiff",1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

kernel = np.ones(shape=(5,5),dtype=np.float32)/25
print(kernel)
result = cv2.filter2D(img, -1, kernel)

plt.subplot(1,2,1)
plt.imshow(img)
plt.title("original")


plt.subplot(1,2,2)
plt.imshow(result)
plt.title("convoluted")
plt.show()
