import os
import random
from os import listdir
from os.path import isfile
from os.path import join as joinpath

def files_listdir(Path):
    for image_file in listdir(Path):
        if isfile(joinpath(Path, image_file)):
            filesindir = os.listdir(Path)
            for files in filesindir:
                random.shuffle(filesindir)
                files = os.path.join(files)
                return files
                