import os

# This folder is custom
rootdir = 'E:\\work_space\\DL\\BaSNet-pytorch-master\\dataset\\THUMOS14\\features'
video_count = 0
for parent, dirnames, filenames in os.walk(rootdir):
    # Case1: traversal the directories
    for dirname in dirnames:
        print("Parent folder:", parent)
        print("Dirname:", dirname)
    # Case2: traversal the files
    for filename in filenames:
        print("Parent folder:", parent)
        print("Filename:", filename)
        video_count += 1

print("video_count:  ", video_count)
