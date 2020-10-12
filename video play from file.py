import cv2

def main():
    name = 'play video'
    cv2.namedWindow(name)
    file = "C:\\Users\\shifa\\Desktop\\standard_test_images\\output\\output.avi"
    cap = cv2.VideoCapture(file)

    while(cap.isOpened()):
            ret ,frame = cap.read()
            print(ret)

            if ret:
                cv2.imshow(name, frame)
                if cv2.waitKey(33) ==27:
                    break
            else:
                break
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
