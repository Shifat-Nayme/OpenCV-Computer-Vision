import cv2
import time

def main():
    name ='live video feed'
    cv2.namedWindow(name)
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret , frame = cap.read()
    else:
        ret = False

    
    rows,columns ,channel = frame.shape
    angle = 0
    scale = 1

    while(True):
        ret ,frame =cap.read()
        if angle == 360:
            angle =0
            
        r = cv2.getRotationMatrix2D((columns/2 ,rows/2),angle,scale)
        output = cv2.warpAffine(frame, r, (columns,rows))

        cv2.imshow(name , output)
        angle = angle+1
        time.sleep(0.05)

        if cv2.waitKey(1) == 27:
            break
    cv2.destroyWindow(name)
    cap.release()

if __name__ == "__main__":
    main()
