from PIL import Image, ImageEnhance
import os

paths = {
    'forest': './Pics/forest/',
    'field': './Pics/field/',
    'lake': './Pics/lake/',
    'mountain': './Pics/mountain/',
    'Test': './Pics/Test/'
}

for path in paths.values():
    for imagename in os.listdir(path):
        image = Image.open(path + "/" + imagename)
        image = image.resize( size=(200, 200) )
        image.save(path + "/" + imagename)
        
