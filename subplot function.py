import cv2
import matplotlib.pyplot as plt

def main():
    path ="C:\\Users\\shifa\\Desktop\\standard_test_images\\"
    imgpath1 = path + '4.2.01.tiff'
    imgpath2 = path + 'lena_color_256.tif'

    img1 = cv2.imread(imgpath1,1)
    img2 = cv2.imread(imgpath2,1)

    img1 =cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 =cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

    title = ['liquid drop' , 'lena']
    image = [img1, img2]

    for i in range(2):
        plt.subplot(1,2,i+1)
        plt.imshow(image[i])
        plt.title(title[i])
        plt.xticks([])
        plt.yticks([])
        
    plt.show()
        

if __name__ == '__main__':
    main()
