import os
import time


def insertFirst(content: str, file: str):
    '''
    在文章开头插入文本
    '''
    with open(file, 'r+', encoding='utf-8', errors='ignore') as f:
        old_content = f.read()
        f.seek(0, 0)
        f.write(content + old_content)


def insert_fliter_files(content: str, path: str, suffix: str):
    assert os.path.isdir(path)
    files = os.listdir(path)
    for file in files:
        p = os.path.join(path, file)
        if os.path.isfile(p) and file.endswith(suffix):
            c = content.format(file[:-3], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
            insertFirst(c, p)
        elif os.path.isdir(p):
            insert_fliter_files(content, p, suffix)


def main():
    # file = "test/android studio安装.md"
    content = "---\n title: {0} \n date: {1} \n tags: \n categories: \n---\n"
    path = 'E:\\work_space\\zhouning\\source\\_posts'
    insert_fliter_files(content, path, suffix='.md')
    # insertFirst(content, file)
    print('finsh')
    # 格式化成2016-03-20 11:45:39形式
    # print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


if __name__ == '__main__':
    main()
