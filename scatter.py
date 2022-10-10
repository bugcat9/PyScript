import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.manifold import TSNE
import numpy as np
from sklearn.datasets import load_iris


def plot_2D(data, label):
    '''
    画二维散点图
    data: [n*2]
    label: [n]
    '''
    x_min, x_max = np.min(data, 0), np.max(data, 0)
    data = (data - x_min) / (x_max - x_min)
    # plt.figure(dpi=600)
    plt.scatter(data[:, 0], data[:, 1], c=label)
    plt.show()


def plot_3D(data, label):
    '''
    画三维散点图
    data:
    label:
    '''
    x_min, x_max = np.min(data, 0), np.max(data, 0)
    data = (data - x_min) / (x_max - x_min)
    fig = plt.figure()
    ax = Axes3D(fig)
    ax.scatter3D(data[:, 0], data[:, 1], data[:, 2], c=label)
    plt.show()

    # plt.savefig(filename)


if __name__ == '__main__':
    iris = load_iris()
    x = iris.data
    label = iris.target
    # 查看维度
    print(x.shape)
    print(label.shape)
    # 画二维图, 其中init可以进行更改
    tsne = TSNE(n_components=2, init='pca', random_state=0)
    data = tsne.fit_transform(x)
    plot_2D(data, label)
    # 画三维图
    tsne = TSNE(n_components=3, init='pca', random_state=0)
    data = tsne.fit_transform(x)
    plot_3D(data, label)