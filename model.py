import numpy as np
from keras.applications.vgg16 import VGG16
from keras.applications.resnet50 import ResNet50
from keras.applications.mobilenet_v2 import MobileNetV2
from keras.models import Model
from keras.layers import Dense,Dropout,BatchNormalization
from keras.activations import relu,sigmoid
from keras.optimizers import adam

from data_processor import *

print(get_image('/home/list_99/Python/Generate_Fake_ID_card'))