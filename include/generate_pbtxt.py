# file to generate a pbtxt file that tensorflow uses to label models
import os
from include.common import common

def create_file():
    dirpath = os.getcwd()
    dirpath = dirpath + '/data/'
    filepath = os.path.join(dirpath, 'custom_detect_label_map.pbtxt')
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)

    return filepath

def generate(filepath):
    custom_label_map = open(filepath, "w+")
    label_map_string = "item {\n  id: %d\n  name: '%s'\n}\n" % (1, common.model_name)
    custom_label_map.write(label_map_string)
    custom_label_map.close()

def main():
    filepath = create_file()
    generate(filepath)
