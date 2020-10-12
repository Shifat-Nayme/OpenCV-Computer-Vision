import cv2

windowname = "live video"
cv2.namedWindow(windowname)
cap = cv2.VideoCapture(0)

print('width: ' +str(cap.get(3)))    
print('height: ' +str(cap.get(4)))

cap.set(3 ,1080)
cap.set(4, 720)

print('width: ' +str(cap.get(3)))    
print('height: ' +str(cap.get(4)))

if cap.isOpened():
    ret , frame = cap.read()

else:
    ret = False

while(True):
    ret ,frame = cap.read()
    cv2.imshow(windowname, frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyWindow(windowname)
cap.release()
