import numpy as np
import cv2

def main():
    img = np.zeros((512,512,3), np.uint8)

    cv2.imshow('lena' , img)
    cv2.waitKey(0)
    cv2.destroyWindow('lena')

if __name__ == '__main__':
    main()
