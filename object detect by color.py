import cv2
import numpy as np

def main():
    cap = cv2.VideoCapture(0)

    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while(True):
        ret ,frame = cap.read()
        
        hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

        #green color
        #low =np.array([40,50,50])
        #high =np.array([80,255,255])

        #red color
        low =np.array([0,100,100])
        high =np.array([10,255,255]) 

        #Blue color
        #low = np.array([100,50,50])
        #high = np.array([140,255,255])

        image_mask = cv2.inRange(hsv, low, high)
        output = cv2.bitwise_and(frame, frame, mask =image_mask)
        cv2.imshow('image mask' ,image_mask)
        cv2.imshow('color tracking', output)








        
        cv2.imshow('original webcam', frame)
        #cv2.imshow('HSV' , hsv)

        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
    cap.release()

if __name__ == "__main__":
    main()
    
