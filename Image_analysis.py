from scipy import ndimage
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from PIL import ImageEnhance
import cv2
import skimage 




def Image_open(filename):
    '''Opens image and assigns it a variable name'''
    bubble=Image.open(filename)
    width, height =bubble.size
    print 'The width of the original image is ' +str(width) +' and height of the image is ' + str(height)
    return bubble
    
def Image_crop(image,left,top,right,lower,cropped_name):
    '''Takes an imported image and crops according to the co-ordinates entered(left,upper,right,lower).Image then resaved under inputted name'''
    cropped_bubble=image.crop((left,top,right,lower))
    cropped_bubble.save(cropped_name)
    width,height = cropped_bubble.size
    print 'The width of the cropped image is ' +str(width) +' and height of the image is ' + str(height)
    return cropped_bubble

def Image_array(filename):
    '''Converts the image to a numpy array and plots the image'''
    np_image=ndimage.imread(filename,flatten=True,mode=None)
    plt.imshow(np_image,cmap=plt.cm.gray)
#    print np_image
    return np_image


def Image_contrast(filename, contrast):
    '''Changes the contrast of an image, 0.0 gives solid grey 1.0 gives the original image'''
    enhancer = ImageEnhance.Contrast(filename)
    image = enhancer(contrast)
    image.save('image.png')
    return None
    
def getRGB(image,save_name):
    '''Converts the mode of an image to RGB'''
    rgbimage=image.convert('RGB')
    rgbimage.save(save_name)
    return
    
def Pixel_BW(pixels):
    '''Creats a new list of pixel values depending on the value of pixels in the input list. 
    White pixels are kept white but any other pixel are made the same colour(dark)'''
    pixel_bw=[]
    Max=max(pixels)
    Min=min(pixels)
    for r in range(len(pixels)-1):
        if pixels[r] != Max:
            pixel_bw.append(0)
        else:
            pixel_bw.append(Max)
    return pixel_bw

def count(pixel_list,value):
    '''Finds the number of pixels in an image with a certain value'''
    count = 0
    for i in range(len(pixel_list)-1):
        if pix_val[i]==value :
            count = count +1
        else:
            count = count
    return count


def edge_det(filename,threshold1,threshold2):
    img=cv2.imread(filename,0)
    edges = cv2.Canny(img,threshold1,threshold2)
    plt.imshow(edges,cmap='gray')
    return 
    


bubble = Image_open('nuc_background.png')
nucleation = Image_crop(bubble,310,230,360,270,'nuc_crop.png')
np_image = Image_array('nuc_crop.png')
nuc=Image.open('nuc_crop.png')

edge_det('nuc_crop.png',10,100)


#
#pix_val=list(nuc.getdata())
#count=count(pix_val,65535)  
#RGBbub = getRGB(bubble,'RBGbubble.png')
#
#pixel_bw=Pixel_BW(pix_val)
#
#
#
#im=Image.frombytes("I",(70,70),str(pix_val))
#im.save('test.png')
#
#edges = edge_det('nucleation.png',450,500)

    

    




