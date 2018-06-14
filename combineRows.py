import rasterio
import numpy as np
import scipy.ndimage.filters as fil
import urllib

# path1 = '/Users/djabernathy/Downloads/Hansen_GFC-2016-v1.4_treecover2000_10N_010E.tif'
# path2 = '/Users/djabernathy/Downloads/Hansen_GFC-2016-v1.4_treecover2000_10N_020E.tif'
# path3 = '/Users/djabernathy/Downloads/Hansen_GFC-2016-v1.4_treecover2000_00N_010E.tif'
# path4 = '/Users/djabernathy/Downloads/Hansen_GFC-2016-v1.4_treecover2000_00N_020E.tif'
outputPath = '/home/abernathyjdavid/forestNonforest.tif'

# read the txt file with the file names of each image
# the file names are in order
# 8 rows
# 8 per row

f = open('forestNonforestInRowOrder.txt', 'r')

fileNames = f.readlines()

for i in range(len(fileNames)):
	line = fileNames[i]
	fixed = line.replace('\n', '')
	fileNames[i] = fixed

basePath = '/home/abernathyjdavid/forestNonforest/'


fileIndex = 0;
for row in range(7):
    for col in range(6):
        print(fileIndex)
        with rasterio.open(basePath + fileNames[fileIndex]) as src:
            array = src.read()
            if col == 0:
                rowArray = array
                profile = src.profile
                print(profile)
            else:
                rowArray = np.append(rowArray, array, axis=2)
            fileIndex += 1



# top = np.concatenate((array1, array2), axis=2)
#
# bottom = np.concatenate((array3, array4), axis=2)
# #
# output = np.concatenate((top, bottom), axis=1)

profile['width'] *= 6
profile['height'] *= 6


# Write to tif, using the same profile as the source
with rasterio.open(outputPath, 'w', **profile) as dst:
    dst.write(fullImageArray)

print(type(fullImageArray))
