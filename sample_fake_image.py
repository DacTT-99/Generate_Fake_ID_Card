import os
import random

import cv2
import numpy as np
from sklearn.model_selection import train_test_split
rootpath = os.path.dirname(__file__)
fake_path = os.path.join(rootpath,'fake')


def get_image(path):
    '''
    Get all filename in a direction
    
    Parameter
    ---------
    path:str, path to direction

    Return
    ------
    Return a list contains all filename no duplicate without extention in direction
    
    Example
    -------
    >>> cd image
    >>> tree
    .
    ├── a.png
    ├── b.png
    └── a.mask.png
    >>> get_image('./image')
    ['./image/a', './image/b']
    '''
    file = os.listdir(path)
    fn = set()
    for i in file:
        if i.split('.')[0] == '':
            continue
        fn.add(path + '/' + i.split('.')[0])
    return list(fn)


def count_fake_point(mask):
    '''
    return number of point with values equal to 255 (white point) in mask
    '''
    return mask[mask == 255].shape[0]


def sample_fake(img, mask):
    kernel_size = 64
    stride = 8
    threshold = 2000
    samples = []
    coordinates = []
    if len(mask.shape) > 2:
        mask = mask[:, :, 0]
    for y_start in range(kernel_size, img.shape[0] - 2 * kernel_size + 1, stride):
        for x_start in range(kernel_size, img.shape[1] - 2 * kernel_size + 1, stride):
            rand_x = random.randint(-7,7)
            rand_y = random.randint(-7,7)
            
            fake_point = count_fake_point(mask[y_start + rand_y:y_start + kernel_size + rand_y, x_start+rand_x:x_start + kernel_size + rand_x])
            if((img[y_start+rand_y:y_start + kernel_size + rand_y, x_start+rand_x:x_start + kernel_size + rand_x, :3].shape[0]+img[y_start+rand_y:y_start + kernel_size + rand_y, x_start+rand_x:x_start + kernel_size + rand_x, :3].shape[1])!=128):
                continue
            if (fake_point > 300) and (kernel_size * kernel_size - fake_point > threshold):
                samples.append(img[y_start+rand_y:y_start + kernel_size + rand_y, x_start+rand_x:x_start + kernel_size + rand_x, :3])
                coordinates.append((x_start,y_start))
    return samples,coordinates


def main():
    fns = get_image(fake_path)

    y = np.array([0]*len(fns))
    fns_train ,fns_valid,_,_=train_test_split(fns,y,test_size=0.2,stratify=y)
    #f = open('./patch_coord_neg.txt','w')
    #fns_train = fns_train[0:1]
    #fns_valid = fns_valid[0:1]
    counter = 0
    for idx,fn in enumerate(fns_train):
        img = cv2.imread(fn + '.jpg')
        mask = cv2.imread(fn + '.mask.png',0)
        for s in sample_fake(img,mask)[0]:
            cv2.imwrite(os.path.join(rootpath,'train/tp/train_tp_{}.png'.format(counter)),s)
            counter+=1
    print('number of fake samples for training : {}'.format(counter))
    counter = 0
    for idx,fn in enumerate(fns_valid):
        img = cv2.imread(fn + '.jpg')
        mask = cv2.imread(fn + '.mask.png',0)
        for s in sample_fake(img,mask)[0]:
            cv2.imwrite(os.path.join(rootpath,'valid/tp/valid_tp_{}.png'.format(counter)),s)
            counter+=1
    print('number of fake samples for validation :{}'.format(counter))
    print('done')

if __name__ == '__main__':
    main()
