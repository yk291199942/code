from skimage import util
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import os

dir='img'
img_name=[]
files=os.listdir(dir)
for file in files:
    name=os.path.join(dir,file)
    img_name.append(name)
print(img_name)

for name in img_name:
    img = Image.open(name)
    img = np.array(img)

    noisy3 = util.random_noise(img, mode='gaussian', mean=0, var=0.1)



    plt.xticks([])   # remove ticks
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

    plt.savefig(name,bbox_inches='tight',pad_inches=0.0)
    plt.imshow(noisy3)
    plt.show()

