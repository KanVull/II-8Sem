import os
import numpy as np
from skimage.feature import greycomatrix, greycoprops
from skimage import io, color, img_as_ubyte

def GetImageCharacteristics(path):
    img = io.imread(path)
    img = img[:,:,:3]
    gray = color.rgb2gray(img)
    image = img_as_ubyte(gray)

    bins = np.array([0, 16, 32, 48, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240, 255]) #16-bit
    inds = np.digitize(image, bins)

    max_value = inds.max()+1
    matrix_coocurrence = greycomatrix(inds, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=max_value, normed=False, symmetric=False)
    contrast = greycoprops(matrix_coocurrence, 'contrast')
    correlation = greycoprops(matrix_coocurrence, 'correlation')
    return contrast.reshape(4), correlation.reshape(4)

if __name__ == '__main__':
    paths = {
        'forest': './Pics/forest/',
        'field': './Pics/field/',
        'lake': './Pics/lake/',
        'mountain': './Pics/mountain/',
    }

    with (open('dataset_clean.csv', 'w')) as dataset:
        dataset.write('contrast1;contrast2;contrast3;contrast4;correlation1;correlation2;correlation3;correlation4;class\n')
        names_train_dict = {'forest': 0, 'field': 1, 'lake': 2, 'mountain': 3}
        for path in paths.values():
            for imagename in os.listdir(path):
                s = ''
                for item in GetImageCharacteristics(path + "/" + imagename):
                    for i in range(4):
                        s += f'{item[i]}' + ';'
                name = path.split("/")[-2]        
                dataset.write(f'{s}{names_train_dict[name]}\n')

