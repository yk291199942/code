import numpy as np
from matplotlib import pyplot as plt

def load_lut(path,LUT_size=17):
    lut=np.zeros((LUT_size**3,3))
    with open(path,'r') as f:
        for num,l in enumerate(f.readlines()[-LUT_size**3:]):
            l=np.array(l.strip().split(' ')).astype(np.float32)
            lut[num]=l
    return lut
def get_id_lut2(dim):
    bin_size = 1.0 / (dim - 1)
    lut = []
    for k in range(dim):
        for j in range(dim):
            for i in range(dim):
                lut.append([bin_size * i, bin_size * j, bin_size * k])
    lut = np.array(lut)
    print(lut.shape)
    r0 = lut[..., 0]
    g0 = lut[..., 1]
    b0 = lut[..., 2]
    for i in range(10):
        print(r0[i], g0[i], b0[i])
    r0=  r0.reshape([dim, dim, dim])
    g0 = g0.reshape([dim, dim, dim])
    b0 = b0.reshape([dim, dim, dim])
    for i in range(10):
        print(r0[0, 0, i], g0[0, 0, i], b0[0, 0, i])
    return lut





def show_lut(lut, lut_id, lut_dim, space=1):
    lut = lut.reshape(lut_dim, lut_dim, lut_dim, 3)
    lut_id = lut_id.reshape(lut_dim, lut_dim, lut_dim, 3)
    lut = lut[::space, ::space, ::space, :]
    lut_id = lut_id[::space, ::space, ::space, :]

    r0 = lut_id[..., 0]
    g0 = lut_id[..., 1]
    b0 = lut_id[..., 2]


    lut = (lut - lut.min()) / (lut.max() - lut.min())  # neccssary
    draw = lut.reshape(-1, 3)

    plt.figure()
    ax = plt.subplot(121, projection='3d')
    ax.scatter(r0, g0, b0, c=draw, alpha=1.0)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_zlim(0, 1)
    ax.set_xlabel('R', c='r')
    ax.set_ylabel('G', c='g')
    ax.set_zlabel('B', c='b')
    ax.set_title('clolored image distribution', color='w')

    draw0 = np.hstack((r0.reshape(-1, 1), g0.reshape(-1, 1), b0.reshape(-1, 1)))
    ax = plt.subplot(122, projection='3d')
    ax.scatter(r0, g0, b0, c=draw0, alpha=1.0)
    ax.set_zlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlim(0, 1)
    ax.set_xlabel('R', c='r')
    ax.set_ylabel('G', c='g')
    ax.set_zlabel('B', c='b')
    ax.set_title('clolored image distribution', color='w')
    plt.show()

def show_lut_slice(lut, lut_dim):
    r = lut[..., 0]
    g = lut[..., 1]
    b = lut[..., 2]

    X = np.linspace(0, lut_dim, lut_dim)
    Y = np.linspace(0, lut_dim, lut_dim)
    X, Y = np.meshgrid(X, Y)

    fig = plt.figure()
    ax1 = fig.add_subplot(131, projection='3d')
    ax2 = fig.add_subplot(132, projection='3d')
    ax3 = fig.add_subplot(133, projection='3d')
    for i in range(lut_dim)[0:lut_dim:lut_dim//3]:
        r_slice = r.reshape([lut_dim, lut_dim, lut_dim])[:, :, i] #r[i::lut_dim].reshape(lut_dim, lut_dim)
        g_slice = g.reshape([lut_dim, lut_dim, lut_dim])[:, i, :]
        b_slice = b.reshape([lut_dim, lut_dim, lut_dim])[i, :, :] #b[i*(lut_dim**2):(i+1)*(lut_dim**2)].reshape(lut_dim, lut_dim)

        surf1 = ax1.plot_surface(X, Y, r_slice)# hot, cool, summer, viridis, ocean, hsv,rainbow
        ax1.set_zlabel('R', c='b')
        surf2 = ax2.plot_surface(X, Y, g_slice)
        ax2.set_zlabel('G', c='g')
        surf3 = ax3.plot_surface(X, Y, b_slice)
        ax3.set_zlabel('B', c='b')
    plt.show()
def show_lut_2d(lut, lut_dim):

    len = np.floor(np.sqrt(lut_dim)).astype(np.int32) + 1
    lut = np.reshape(lut, [lut_dim, lut_dim, lut_dim, 3])

    width = len
    height = len
    while (height-1)*len > lut_dim:
        height = height - 1
    print(lut_dim, len)
    for i in range(height):
        for j in range(width):
            idx = i * len + j
            if idx >= lut_dim:
                hlut = np.hstack((hlut, np.zeros_like(lut[0])))
                continue
            if j == 0:
                hlut = lut[idx]
            else:
                hlut = np.hstack((hlut, lut[idx]))
            #print(idx, hlut.shape)
        if i == 0:
            lut_im = hlut
        else:
            lut_im = np.vstack((lut_im, hlut))
        #print(i, j, hlut.shape)
    #print(lut_im.shape)
    plt.imshow(lut_im)
    #plt.show()


    plt.show()

if __name__ == "__main__":
    path = 'D:\python-use-cube-lut-file-process-image-master\cube\cub.txt'
    lut_dim = 17
    lut = load_lut(path, 17)
    #lut1 = get_id_lut(lut_dim)
    lut_id = get_id_lut2(lut_dim)
    show_lut(lut, lut_id, lut_dim)
    #
    show_lut_slice(lut, lut_dim)

    show_lut_2d(lut, lut_dim)
    show_lut_slice(lut, lut_dim)

