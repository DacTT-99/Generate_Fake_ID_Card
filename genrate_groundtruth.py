import os

import cv2
import numpy as np

import data_processor

file_path=''

idnumber_region=[]
name_region=[]
birthday_region=[]
gender_region=[]
nation_region=[]
address_region=[]
avatar_region=[]
expirationdate_region =[]

def determiner_region(h,w):
    idnumber = [x*h if index <= 1 else x*w for index,x in enumerate(idnumber_region)]
    name = [x*h if index <= 1 else x*w for index,x in enumerate(name_region)]
    birthday = [x*h if index <= 1 else x*w for index,x in enumerate(birthday_region)]
    gender = [x*h if index <= 1 else x*w for index,x in enumerate(gender_region)]
    nation = [x*h if index <= 1 else x*w for index,x in enumerate(nation_region)]
    address  = [x*h if index <= 1 else x*w for index,x in enumerate(address_region)]
    avatar = [x*h if index <= 1 else x*w for index,x in enumerate(avatar_region)]
    expirationdate= [x*h if index <= 1 else x*w for index,x in enumerate(expirationdate_region)]

    return idnumber,name,birthday,gender,nation,address,avatar,expirationdate

def generate_groundtruth_mask(h,w,idnumber,name,birthday,gender,nation,address,avatar,expirationdate):
    mask = np.zeros([h,w])
    mask[idnumber[0]:idnumber[1],idnumber[2]:idnumber[3]] = 255
    mask[name[0]:name[1],name[2]:name[3]] = 255
    mask[birthday[0]:birthday[1],birthday[2]:birthday[3]] = 255
    mask[gender[0]:gender[1],gender[2]:gender[3]] = 255
    mask[nation[0]:nation[1],nation[2]:nation[3]] = 255
    mask[address[0]:address[1],address[2]:address[3]] = 255
    mask[avatar[0]:avatar[1],avatar[2]:avatar[3]] = 255
    mask[expirationdate[0]:expirationdate[1],expirationdate[2]:expirationdate[3]] = 255
    return mask

def main():
    files,labels = data_processor.get_image(file_path)
    for file,label in zip(files,labels):
        if label == 0:
            img = cv2.imread(file)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
            generate_groundtruth_mask(img.shape[0],img.shape[1],determiner_region(img.shape[0],img.shape[1]))