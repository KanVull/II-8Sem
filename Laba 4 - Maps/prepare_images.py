from PIL import Image
import os

paths = {
    'forest': './Pics/forest/',
    'field': './Pics/field/',
    'lake': './Pics/lake/',
    'mountain': './Pics/mountain/',
}

for path in paths.values():
    for imagename in os.listdir(path):
        image = Image.open(path + "/" + imagename)
        image = image.resize( size=(200, 200) )
        image.save(path + "/" + imagename)
        
