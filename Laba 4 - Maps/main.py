from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras import utils
from tensorflow.keras.preprocessing import image
import random
import numpy as np
import pathlib
import os
from PIL import Image       

with (open('dataset.csv', 'r')) as dataset:
    data_train = []
    names_train = []
    for line in dataset:
        data = line.replace('\n','').split(';')
        data_train.append(list(map(int, data[1:])))
        names_train.append(data[0])

names_train_set = set(names_train)
names_train_dict = {key, item for item in names_train}

data_train = np.array(data_train).reshape(len(data_train), 3)
data_train = data_train / 255       

random_image_position = random.randint(0, len(data_train))
data_test = data_train[random_image_position].reshape(1, 3)
names_test = names_train[random_image_position]

print(names_train[0])

model = Sequential()
model.add(Dense(3, input_dim=3, activation="relu"))
model.add(Dense(2, activation="softmax"))

model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])

print(model.summary())

history = model.fit(data_train, names_train, 
                    batch_size=200, 
                    epochs=50, 
                    verbose=1)

# os.chdir(os.path.dirname(os.path.realpath(__file__)))
# model.save('BarPy_model.h5')

predictions = model.predict(data_test)
n = 0
print(predictions[n])

print(np.argmax(predictions[n]))
print(names_test)