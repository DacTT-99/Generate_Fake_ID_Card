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

N = 10 # number of fake image generated form 1 real image
num = 3 # number of operation 
def generate(img,mask=None):
    '''
    Create a new image by randomly cropping, rotating, pasting on the origin image

    Parameter
    --------- 
    img : an PIL format image

    Return
    ------
    a new PIL format image 
    '''

    H, W = img.size

    # position to crop
    x = random.randint(0, int(H*0.85))
    y = random.randint(0, int(W*0.85))
    h = random.randint(int(H*0.1), int(H*0.15))
    w = random.randint(int(W*0.1), int(W*0.15))

    # rotation angle for cropped part
    angle = random.randint(0, 360)

    # position to paste
    i = random.randint(0,int(H*0.8))
    j = random.randint(0,int(W*0.8))

    roi = img.crop((x, y, x+h, y+w))

    if mask is None:
        mask = Image.new('L', img.size, 0)
    maskOfRoi = Image.new('L', roi.size, 255)

    roi = roi.rotate(angle, expand=True)
    maskOfRoi = maskOfRoi.rotate(angle, expand=True)

    img.paste(roi,(i,j),maskOfRoi)
    mask.paste(maskOfRoi,(i,j),maskOfRoi)

    return img,mask

def main():
    counter = 0
    for fn in filenames:
        orig = Image.open(os.path.join(dirpath,fn))
        for i in range(N):

            img = orig.copy()
            img , mask = generate(img)
            for j in range(num - 1):
                img , mask = generate(img,mask)

            img.save(os.path.join(rootpath,'fake/style2_fake{}.jpg'.format(counter)))
            mask.save(os.path.join(rootpath,'fake/style2_fake{}.mask.png'.format(counter)))
            counter += 1
    print('{} images was generated'.format(counter))

if __name__=='__main__':
    main()