import random
import os
import cv2, math
import numpy as np


def demo(img_path, img_save_path):
    img = cv2.imread(img_path)
    print(img.dtype)
    img_f = img / 255.0
    (row, col, chs) = img.shape
    A = 0.5  # 亮度
    beta = random.uniform(0.04,0.08)  # 雾的浓度
    size = math.sqrt(max(row, col))  # 雾化尺寸
    center = (random.uniform(1,row), random.uniform(1,col))  # 雾化中心
    for j in range(row):
        for l in range(col):
            d = -0.04 * math.sqrt((j - center[0]) ** 2 + (l - center[1]) ** 2) + size
            td = math.exp(-beta * d)
            img_f[j][l][:] = img_f[j][l][:] * td + A * (1 - td)
    #转换格式，防止在保存时出现图片全黑的情况
    img_f = cv2.normalize(img_f, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
    cv2.imwrite(img_save_path, img_f)


if __name__ == '__main__':
        demo(r'E:\mobilenet-yolov4-pytorch-main\fog\aa.jpg', r'E:\mobilenet-yolov4-pytorch-main\fog\aa.jpg')
