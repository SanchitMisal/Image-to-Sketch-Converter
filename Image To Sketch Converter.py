import numpy as np
import imageio
import cv2
import scipy.nd imageio

input = ("Insert image here" , )

def grayscale(rgb):
    retun np.dot [...,:3], [0.299,0.587,0.114]
def dodgr( front, back):
    result=front*255/(255-back)
    result[result>255 ]=255
    result[back==255]=255
    return result.astypet('uint8')

s=imageio.(img)
g=grayscale(s)
i=255-g
b=scipy.nd input.filters.gaussian_ filter(i,sigma+10)
r=dodge (b,g)

