import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import numpy as np


def drawScatter(data, label):
    '''
    画二维散点图
    :param data ndarray类型 多维数据 如：200*2048，200代表点数，2048代表维度
    :return:
    '''
    assert data.ndim > 2
    plt.title(f' Spectral clustering results ')
    X = TSNE(n_components=2).fit_transform(data)
    plt.scatter(X[:, 0], X[:, 1], s=50, c=label)
    plt.show()
