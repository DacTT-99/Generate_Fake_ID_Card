import os

import cv2
import numpy as np
from sklearn.model_selection import train_test_split

from sample_fake_image import get_image

rootpath = os.path.dirname(__file__) 
origin_path = os.path.join(rootpath,'./origin')
num_fake_sample = 170000
num_orig_img = len(os.listdir(origin_path))
samples_per_img = num_fake_sample//num_orig_img

train_path = os.path.join(rootpath,'./train')
valid_path = os.path.join(rootpath,'./valid')
train_au_path = os.path.join(train_path,'au')
train_tp_path = os.path.join(train_path,'tp')
valid_au_path = os.path.join(valid_path,'au')
valid_tp_path = os.path.join(valid_path,'tp')

def sample_random(save_path,img, num_samples, prefix,counter):
    '''
    randomly sample the given image n times

    Parameters
    -----------
    img : array
        image need to sample

    num_samples : number of time to sample

    '''
    samples = []
    col, row, chanel = img.shape
    if chanel > 3 :
        img = img[:,:,:3]
    for i in range(num_samples):
        x = np.random.randint(0, row-64)
        y = np.random.randint(0, col-64)
        cv2.imwrite(save_path+'/{}_au_{}.png'.format(prefix,counter*num_samples + i),img[y:y+64,x:x+64,:3])

def main():
    fns = get_image(origin_path)
    y = np.array([0]*len(fns))
    fns_train ,fns_valid,_,_=train_test_split(fns,y,test_size=0.2,stratify=y)
    for idx,fn in enumerate(fns_train):
        img = cv2.imread(fn + '.jpg')
        sample_random(train_au_path,img,samples_per_img,'train',idx)

    for idx,fn in enumerate(fns_valid):
        img = cv2.imread(fn + '.jpg')
        sample_random(valid_au_path,img,samples_per_img,'valid',idx)

if __name__=='__main__':
    main()
