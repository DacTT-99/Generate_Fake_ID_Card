import os
import numpy as np
import cv2
from PIL import Image
import random

# Project path
rootpath = os.path.dirname(__file__)

# file path to dir of origin image used to generate fake image
dirpath = os.path.join(rootpath,'origin')

# all image filenames to generated fake image
filenames = os.listdir(dirpath)

N=10
n=4
def generate(img,mask=None):
    '''
    Create a new image by randomly pasting a blank space to origin image

    Paramater
    --------
    img: PIL.image.image object 

    mask : PIL.image.image object

    Return
    ------
    img : new image

    mask : marked where is pasted 
    '''
    W,H = img.size

    angle = random.randint(0,180)

    size=(random.randint(int(H*0.1), int(H*0.2)),random.randint(int(W*0.1), int(W*0.2)))
    i = random.randint(0,int(H*0.85))
    j = random.randint(0,int(W*0.85))

    if mask is None:
        mask = Image.new('L',img.size,0)
    maskOfRoi = Image.new('L',size,255)
    maskOfRoi = maskOfRoi.rotate(angle,expand=True)
    
    img.paste(maskOfRoi,(i,j),maskOfRoi)
    mask.paste(maskOfRoi,(i,j),maskOfRoi)
    print('a')
    return img,mask

def main():
    counter = 0
    for fn in filenames:
        orig = Image.open(os.path.join(dirpath,fn))
        for i in range(N):
            img = orig.copy()
            img,mask = generate(img)
            for j in range(n-1):
                img,mask = generate(img,mask)
            
            img.save(os.path.join(rootpath,'./fake/style3_fake{}.png'.format(counter)))
            mask.save(os.path.join(rootpath,'./fake/style3_fake{}.mask.png'.format(counter)))
            counter += 1
    print('{} images was generated'.format(counter))
if __name__=='__main__':
    main()