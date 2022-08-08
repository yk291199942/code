import os

import numpy as np
from PIL import Image
import math

from matplotlib import pyplot as plt


def cubeIndex(r, g, b):
    return int(r + g * 17 + b * 17 * 17)

def mix(a, b, c):
    return a + (b - a) * (c - math.floor(c))

dir='D:\python-use-cube-lut-file-process-image-master\img'
full_name=[]
files=os.listdir(dir)
for file in files:
    name=os.path.join(dir,file)
    full_name.append(name)

fd = open('NightFromDay.CUBE')
lines = fd.readlines()
rgbFloatCube = []
cubeDataStart = False
for l in lines:
    if cubeDataStart:
        rgbStr = l.split(" ")
        if len(rgbStr) == 3:
            rgbFloat = (float(rgbStr[0]), float(rgbStr[1]), float(rgbStr[2]))
            rgbFloatCube.append(rgbFloat)
    if l.startswith("#LUT data points"):
        cubeDataStart = True

for names in full_name:
    img = Image.open(names)
    bitmap = img.load()
    print(len(rgbFloatCube))
    print(img.size)

    for x in range(img.size[0]):
        for y in range(img.size[1]):
            pixelColor = bitmap[x, y]
            red = pixelColor[0] / 255.0 * 16
            green = pixelColor[1] / 255.0 * 16
            blue = pixelColor[2] / 255.0 * 16

            redH = math.ceil(red)
            redL = math.floor(red)

            greenH = math.ceil(green)
            greenL = math.floor(green)

            blueH = math.ceil(blue)
            blueL = math.floor(blue)

            indexH = cubeIndex(redH, greenH, blueH)
            indexL = cubeIndex(redL, greenL, blueL)

            toColorH = rgbFloatCube[indexH]
            toColorL = rgbFloatCube[indexL]

            toR = mix(toColorL[0], toColorH[0], red)
            toG = mix(toColorL[1], toColorH[1], green)
            toB = mix(toColorL[2], toColorH[2], blue)

            toColor2 = (int(toR * 255), int(toG * 255), int(toB * 255))
            bitmap[x, y] = toColor2
    img = np.array(img)
    plt.xticks([])  # remove ticks
    plt.yticks([])

    fig, ax = plt.subplots()
    im = img[:, :, (2, 1, 0)]
    ax.imshow(im, aspect='equal')
    plt.axis('off')
    # 去除图像周围的白边
    height, width, channels = im.shape
    # 如果dpi=300，那么图像大小=height*width
    fig.set_size_inches(width / 100.0 , height / 100.0 )
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.subplots_adjust(top=1, bottom=0, left=0, right=1, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.imshow(img)
    plt.savefig(names,bbox_inches='tight',pad_inches=0.0)



