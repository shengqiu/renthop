from PIL import Image
from os import listdir, chdir
from os.path import isdir, join, isfile, getsize


def getNumberOfPics(postingId):
  fileList = [f for f in listdir(postingId) if isfile(f)]
  numOfPics = len(fileList)
  return numOfPics


def getAverageSize(postingId):
  sizeList = [getsize(f) for f in listdir(postingId) if isfile(f)]
  if len(sizeList) == 0:
    averageSize = 0
  else:
    averageSize = sum(sizeList) / len(sizeList)
  return averageSize


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
  chdir('/Users/f/scripts/renthop/images_sample')
  postingIdList = [f for f in listdir('.') if isdir(f)]
  for postingId in postingIdList:
    print postingIdList
    print getAverageSize(postingId)
    print getNumberOfPics(postingId)
