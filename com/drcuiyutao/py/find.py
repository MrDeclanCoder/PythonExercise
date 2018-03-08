import os


def find_file_by_key(key, path=os.path.abspath('.')):
    for x in os.listdir(path):
        fpath = os.path.join(path, x)
        if os.path.isfile(fpath):
            if x.__contains__(key):
                print('file path : %s' % fpath)
        elif os.path.isdir(fpath):
            find_file_by_key(key, fpath)