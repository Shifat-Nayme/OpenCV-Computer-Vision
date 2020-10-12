import cv2
import matplotlib.pyplot as plt

def main():
    path = "C:\\Users\\shifa\\Desktop\\standard_test_images\\"
    imgpath = path + "gray21.512.tiff"
    #imgpath = path + "7.2.01.tiff"
    img = cv2.imread(imgpath, 1)
    img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

    th = 127
    max_val =255

    ret , img1 = cv2.threshold(img , th, max_val, cv2.THRESH_BINARY)
    ret , img2 = cv2.threshold(img , th, max_val, cv2.THRESH_BINARY_INV)
    ret , img3 = cv2.threshold(img , th, max_val, cv2.THRESH_TOZERO)
    ret , img4 = cv2.threshold(img , th, max_val, cv2.THRESH_TOZERO_INV)
    ret , img5 = cv2.threshold(img , th, max_val, cv2.THRESH_TRUNC)

    
    output = [img,img1,img2,img3,img4,img5]
    titles = ['original' , 'thres_binary','binary_inv','tozero',
              'tozero_inv','trunc']
    for i in range(6):
        plt.subplot(2,3,i+1)
        plt.imshow(output[i])
        plt.title(titles[i])
        plt.xticks([])
        plt.yticks([])

    plt.show()

if __name__ == "__main__":
    main()
    
    

    

    
