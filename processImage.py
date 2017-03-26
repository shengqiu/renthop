from PIL import Image
from os import listdir
from os.path import isdir, join, isfile, getsize
mypath = "images_sample"


def getFileMetaData(picPath):
  directoryList = [f for f in listdir(picPath) if isdir(join(picPath, f))]
  dirDict = {}
  for directory in directoryList:
    fullPath = "images_sample/" + directory
    fileList = [f for f in listdir(fullPath) if isfile(join(fullPath, f))]
    dirDict[directory] = {}
    for picFile in fileList:
      picFileFull = fullPath + '/' + picFile
      pic = Image.open(picFileFull)
      dirDict[directory][picFile] = {
        'size': getsize(picFileFull),
        'width': pic.size[0],
        'ratio': pic.size[1]/float(pic.size[0])
      }
    #print '{} has {} pics'.format(directory, len(dirDict[directory]))
  return dirDict


if __name__ == '__main__':
  mypath = 'images_sample'
  fileMetaData = getFileMetaData(mypath)
  print fileMetaData
