#%%
import cv2
from PIL import Image
import os
from data_processor import *
from matplotlib import pyplot as plt
import numpy as np
a = np.load('/home/list_99/Python/Generate_Fake_ID_Card/feature_avatar.npy')
print(a.shape)
b = a[0][:,:,::-1]
b1 = a[1][:,:,::-1]
c = Image.fromarray(b).convert('RGB')
c1 = Image.fromarray(b1).convert('RGB')
c1.show()
c.show()
#%%