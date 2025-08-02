import sys
import os
from PIL import Image

def getList(dirTosearch):
    return os.listdir(dirTosearch)

def getNewName(oldExtention):
    newName = os.path.splitext(oldExtention)[0]
    return newName + '.png'

def converter(dirTosearch, newDir):
    os.mkdir(newDir) 
    imageList = getList(dirTosearch)
    print('geteing the list')
    for x in imageList:
        print(x)
        if x.endswith('.jpg'):
            im = Image.open(os.path.join(dirTosearch, x))
            print('opening the img')
            im.save(os.path.join(newDir, getNewName(x)))
            print('saving the img')

        else:
            print(f'this is not jpg format {x}')

if (__name__ == '__main__'):
    if (len(sys.argv) == 3):
        converter(sys.argv[1], sys.argv[2])
    else:
        print('wrong number of argument')
