import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
from PIL import Image


dir='img'
full_name=[]
files=os.listdir(dir)
for file in files:
    name= os.path.join(dir, file)
    full_name.append(name)


'''
    用于图像预处理，模拟ps的色阶调整
    img：传入的图片
    Highlight：白场(Shadow-255)
    Shadow：黑场(0-Highlight)
    0 <= Shadow < Highlight <= 255
    返回一张图片
'''
def Whiite_Black_Level_Pretreatment(img, Shadow,Highlight):
        if Highlight > 255:
            Highlight = 255
        if Shadow < 0:
            Shadow = 0
        if Shadow >= Highlight:
            Shadow = Highlight - 2
        # 转类型
        img = np.array(img, dtype=int)
        # 计算白场黑场离差
        Diff = Highlight - Shadow
        # 计算系数
        coe = 255.0 / Diff
        rgbDiff = img - Shadow
        rgbDiff = np.maximum(rgbDiff, 0)
        img = rgbDiff * coe
        # 四舍五入到整数
        img = np.around(img, 0)
        # 变为int型
        img = img.astype(int)
        return img

if __name__ == '__main__':
    for name in full_name:
        img = Image.open(name)
        img = np.array(img)
        Whiite_Black_Level_Pretreatment(img, 0, 115)
        plt.xticks([])  # remove ticks
        plt.yticks([])

        fig, ax = plt.subplots()
        im = img[:, :, (2, 1, 0)]
        ax.imshow(im, aspect='equal')
        plt.axis('off')
        # 去除图像周围的白边
        height, width, channels = im.shape
        # 如果dpi=300，那么图像大小=height*width
        fig.set_size_inches(width / 100.0, height / 100.0)
        plt.gca().xaxis.set_major_locator(plt.NullLocator())
        plt.gca().yaxis.set_major_locator(plt.NullLocator())
        plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
        plt.margins(0, 0)


        plt.imshow(img)

        plt.savefig(name,bbox_inches='tight',pad_inches=0.0)
