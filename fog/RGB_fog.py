import numpy as np
import cv2 as cv
import os
import random
import cv2
file = r'E:\\mobilenet-yolov4-pytorch-main\\img\\' # 图片文件夹的输入路径

for file_img in os.listdir(file):  # 需要处理的文件夹
    img = cv.imread(file + file_img)  # 需要处理的文件夹
    mask_img = cv.imread(file + file_img)  # 需要处理的文件夹
    # mask_img[:, :] = (144, 128, 112)  # 112, 128, 144 RGB 三种颜色相同时为灰度色彩
    # mask_img[:, :] = (166, 178, 180)  # 雾的颜色可以调整，看看哪个效果符合自身的需要
    mask_img[:, :] = (220, 220, 220)
    image = cv.addWeighted(img, round(random.uniform(0.1, 0.1), 2), mask_img, 1, 0)  # 里面参数可调，主要调整雾的浓度（0.1， 0.1）这两个参数控制雾的浓度，多调整下就懂了
    cv2.imwrite(file_img, image) # 保存文件，图片名称和输入的相同，可以自己设置更改
