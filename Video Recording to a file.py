import cv2

def main():
    windowname = 'webcam video capture'
    cv2.namedWindow(windowname)

    cap = cv2.VideoCapture(0)
    outfile = "C:\\Users\\shifa\\Desktop\\standard_test_images\\output\\output.avi"
    codec = cv2.VideoWriter_fourcc('X' ,'V' ,'I' ,'D')
    #codec = cv2.VideoWriter_fourcc(*'XVId')
    framerate = 30
    resolution =(640,480)
    videofileoutput = cv2.VideoWriter(outfile ,codec ,framerate,resolution,False)
    

    while(True):
        ret , frame = cap.read()
        gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        cv2.imshow('gray window', gray)
        videofileoutput.write(gray)
        cv2.imshow(windowname , frame)

        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()
    videofileoutput.release()
    cap.release()

if __name__ == '__main__':
    main()

    
                
