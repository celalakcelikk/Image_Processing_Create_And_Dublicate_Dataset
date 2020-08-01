import cv2
import random
import numpy as np
from skimage.transform import rotate,AffineTransform,warp
from skimage.util import random_noise
from scipy import ndimage

# https://stackoverflow.com/questions/9041681/opencv-python-rotate-image-by-x-degrees-around-specific-point
# https://github.com/govinda007/Images/blob/master/augmentation.ipynb

def rgb_to_gray(img,control=0):
    if control==1:
        img = cv2.imread(img)
    return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

def gray_to_rgb(img):
    if control==1:
        img = cv2.imread(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    return cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

def rgb_to_bgr(img,control=0):
    if control==1:
        img = cv2.imread(img)
    return cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

def bgr_to_gray(img,control=0):
    if control==1:
        img = cv2.imread(img)
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def horizantally_flipped(img,control=0):
    if control==1:
        img = cv2.imread(img)
    return np.fliplr(img)

def vertically_flipped(img,control=0):
    if control==1:
        img = cv2.imread(img)
    return np.flipud(img)

def rotate_image(img, angle:float,control=0):
    if control==1:
        img = cv2.imread(img)
    rotated = ndimage.rotate(img, angle)
    return rotated

def image_adding_noise(img,control=0):
    if control==1:
        img = cv2.imread(img)
    return random_noise(image=img)

def blur_image(img,ksize:int,control=0):
    if control==1:
        img = cv2.imread(img)
    return cv2.GaussianBlur(img,(int(ksize),int(ksize)),0)

def central_crop(img,zoom:float,control=0):
    if control==1:
        img = cv2.imread(img)
    x=img.shape[1]
    x_zoom=int(x*(zoom/100))//2
    y=img.shape[0]
    y_zoom=int(y*(zoom/100))//2
    img_result = img[y_zoom:(y-y_zoom), x_zoom:(x-x_zoom)]
    return img_result

def image_resize(img,y:int,x:int,control=0):
    # (y,x,r)
    if control==1:
        img = cv2.imread(img)
    if y==0:
        y = img.shape[0]
    if x==0:
        x = img.shape[1]
    return cv2.resize(img,(y,x))
    
def adjust_brightness(img,alpha:float,beta=1.0,gamma=1.0):
    if control==1:
        img = cv2.imread(img)
    return cv2.addWeighted(src1=img,alpha=alpha,src2=np.zeros(img.shape,img.dtype),beta=beta,gamma=gamma)


# path = "./images/cat.jpg"

# cv2.imshow("Selam",rotate_image(img=path,angle=90))

# cv2.waitKey(0)  
  
# cv2.destroyAllWindows() 
# cv2.imwrite("0.jpg",central_crop("./images/cat.jpg",10))