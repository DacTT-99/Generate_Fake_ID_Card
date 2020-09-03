import numpy as np
import os
import cv2
import glob

data_path = './'
crop_avatar = [0.29,0.95,0,0.33]
crop_info = [0.24,0.99,0.31,0.99]
size_avatar =(128,192)
size_info = (384,384)

def get_image(data_path):
    files = []
    label = []
    idx = 0
    for ext in ['jpg','png','jpeg','JPG']:
        for x in os.listdir(data_path):
            if x == 'fake':
                files.extend(glob.glob(os.path.join(data_path + '/' +x, '*.{}'.format(ext))))
                label.extend([0 for i in range(len(glob.glob(os.path.join(data_path + '/' + x, '*.{}'.format(ext)))))])
            elif x =='origin':
                files.extend(glob.glob(os.path.join(data_path + '/' + x, '*.{}'.format(ext))))
                label.extend([1 for i in range(len(glob.glob(os.path.join(data_path + '/' + x, '*.{}'.format(ext)))))])
    return files, label

def data_processor(crop,size):
    image_list ,label  = get_image(data_path)
    print('{} training images in {}'.format(len(image_list),data_path))
    image_list = np.array(image_list)
    images = []
    
    for i in range(0,image_list.shape[0]):
        im_fn = image_list[i]
        im = cv2.imread(im_fn)
        h,w,_= im.shape
        ava = im[int(h*crop[0]+1):int(h*crop[1]+1),int(w*crop[2]+1):int(w*crop[3]+1),:]
        ava = cv2.resize(ava,size)
        images.append(ava)
        
    return np.array(images),np.array(label)

if __name__=='__main__':
    avatar,label_avatar = data_processor(crop_avatar,size_avatar)
    info, label_info = data_processor(crop_info,size_info)

    np.save('./feature_avatar.npy',avatar)
    np.save('./feature_info.npy',info)
    np.save('./label_ava.npy',label_avatar)
    np.save('./label_info.npy',label_info)