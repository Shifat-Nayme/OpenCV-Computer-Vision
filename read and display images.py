import cv2
import matplotlib.pyplot as plt

def main():
            imgpath = "C:\\Users\\Public\\Documents\\ScanDoc\\2019-04-10-00-51-47-01.jpg"

            #outpath ="C:\\Users\\shifa\\Desktop\\standard_test_images\\output\\o.jpg"
            
            img = cv2.imread(imgpath)
            grayed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            #grayed = cv2.resize(img,(512,512))
            #ret,gray = cv2.threshold(grayed,25,255,cv2.THRESH_BINARY)

            cv2.namedWindow('lena' ,cv2.WINDOW_AUTOSIZE)
            plt.imshow(grayed)
            plt.show()
            
            #cv2.imwrite(outpath, gray)
                 
                 
        
            cv2.waitKey(0)
            cv2.destroyWindow('lena')
                 
          
        
if __name__ == "__main__":
    main()
