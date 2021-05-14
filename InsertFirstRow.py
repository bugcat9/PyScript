import os


def insertFirst(content: str, file: str):
    '''
    在文章开头插入文本
    '''
    with open(file, 'r+') as f:
        old_content = f.read()
        f.seek(0, 0)
        f.write(content + old_content)


def insert_fliter_files(content: str, path: str, suffix: str):
    assert os.path.isdir(path)
    files = os.listdir(path)
    for file in files:
        p = os.path.join(path, file)
        if os.path.isfile(p) and file.endswith(suffix):
            insertFirst(content, p)
        elif os.path.isdir(p):
            insert_fliter_files(content, p, suffix)


def main():
    file = "test/test.md"
    content = "## ccccccccccccccccccccccccccc\n"
    path = 'test'
    insert_fliter_files(content, path, suffix='.md')
    print('finsh')

if __name__ == '__main__':
    main()
