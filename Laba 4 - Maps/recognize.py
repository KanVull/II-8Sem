from getcsv_RGB import getRGB_Average
import random
import pathlib
import numpy as np
from PIL import Image
from tensorflow import keras

def recognize(path, model):
    data = np.array(getRGB_Average(path)).reshape(1,3)
    prediction = model.predict(data)
    return np.argmax(prediction[0])

def uploadImage(path: pathlib.Path):
    image = Image.open(path)
    data = np.asarray(image)
    return data

classes = [ 'forest', 'field', 'lake', 'mountain' ]

model = keras.models.load_model( 'model.h5' )

Names = [ classes[i] for i in range(len(classes)) ]

paths = {
    'pathforest': './Pics/Test/forest.png',
    'pathfield': './Pics/Test/field.png',
    'pathlake': './Pics/Test/lake.png',
    'pathmountain': './Pics/Test/mountain.png',
}

# Getting predictions by model for every image + expected answer as Names element
# [ 
#   [ (recognized, expected), .. , (recognized, expected) ],
#   [ (recognized, expected), .. , (recognized, expected) ],
#   [ (recognized, expected), .. , (recognized, expected) ],
#   [ (recognized, expected), .. , (recognized, expected) ], 
# ]

# Formating grid of images
# image = np.concatenate(
#     [np.concatenate([RandomImages[3][i*j + i] for i in range(20)], axis=1) for j in range(20)],
#     axis=0
# )
# im = Image.fromarray(image)
# im.show()

predictions_list = [ (classes[recognize(path, model)], classes[i]) for i, path in enumerate(paths.values()) ]

for i in range(4):
    print(f'{predictions_list[i][1]} regognized as {predictions_list[i][0]}')      