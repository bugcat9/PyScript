# PyScripy
记录一些有用的python脚本(自己写的或者网上找的)



| 文件名              | 说明                                          | 用法                                                         |
| ------------------- | --------------------------------------------- | ------------------------------------------------------------ |
| tensorboardToCSV.py | 用来将tensorboard生成的event文件转化为csv文件 | python python文件位置.py --in-path event文件夹路径 --ex-path csv文件夹保存位置 |
|                     |                                               |                                                              |
|                     |                                               |                                                              |

### tensorboardToCSV

将tensorboard生成的event文件转化为csv文件。

使用时输入：

```
python python文件位置.py --in-path event文件夹路径 --ex-path csv文件夹保存位置
```

其中`in-path`是整个event文件夹的路径，如果想输入单个文件的路径其实也可以。

eg：

在当前文件夹里面存在着event文件，将其生成out.csv文件

```
python exportTensorboard.py --in-path . --ex-path out.csv
```

**目前存在的问题：**存在数据没有办法转化，原因是event当中所有数据不是一样长的在使用`pandas`进行转化时会导致数据丢失

**参考：**https://blog.csdn.net/weixin_40539826/article/details/111083471