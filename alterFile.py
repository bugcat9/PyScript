import os


def alter(file, old_str, new_str):
    """
    替换文件中的字符串
    :param file:文件名
    :param old_str:就字符串
    :param new_str:新字符串
    :return:
    """
    file_data = ""
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            if old_str in line:
                line = line.replace(old_str, new_str)
            file_data += line
    with open(file, "w", encoding="utf-8") as f:
        f.write(file_data)


def alter_fliter_files(old_str: str, new_str: str, path: str, suffix: str):
    assert os.path.isdir(path)
    files = os.listdir(path)
    for file in files:
        p = os.path.join(path, file)
        if os.path.isfile(p) and file.endswith(suffix):
            alter(p, old_str, new_str)
        elif os.path.isdir(p):
            alter_fliter_files(old_str, new_str, p, suffix)


if __name__ == '__main__':
    old_str = "123"
    new_str = "test"
    path = "test"
    suffix = ".txt"
    alter_fliter_files(old_str, new_str, path, suffix)
    print('finsh')
