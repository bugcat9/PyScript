import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import confusion_matrix


def plot_confusion_matrix(x, y):
    '''
    画混淆矩阵
    x: 混淆矩阵x轴
    y: 混淆矩阵y轴
    '''
    # 混淆矩阵
    confusion_mat = confusion_matrix(x, y)
    # interpolation 和 cmap都可以进行调节
    plt.imshow(confusion_mat, interpolation='nearest', cmap=plt.cm.Paired)
    plt.title('Confusion Matrix')
    plt.colorbar()
    tick_marks = np.arange(4)
    plt.xticks(tick_marks, tick_marks)
    plt.yticks(tick_marks, tick_marks)
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')
    plt.show()


if __name__ == '__main__':
    y_true = [1, 0, 0, 2, 1, 0, 3, 3, 3]
    y_pred = [1, 1, 0, 2, 1, 0, 1, 3, 3]
    plot_confusion_matrix(y_true, y_pred)
