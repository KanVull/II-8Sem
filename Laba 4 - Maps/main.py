from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras import utils
from tensorflow.keras.preprocessing import image
import random
import numpy as np
import pathlib
import os
from PIL import Image       

with (open('dataset_clean.csv', 'r')) as dataset:
    data_train = []
    names_train = []
    for line in dataset:
        if line.find('contrast') != -1:
            continue
        data = line.replace('\n','').split(';')
        data_train.append(list(map(float, data[:-1])))
        names_train.append(data[-1])

names_train_dict = {'forest': 0, 'field': 1, 'lake': 2, 'mountain': 3}
# for i in range(len(names_train)):
#     names_train[i] = names_train_dict[names_train[i]]

data_train = np.array(data_train).reshape(len(data_train), 8)      

random_image_position = random.randint(0, len(data_train))
data_test = data_train[random_image_position].reshape(1, 8)
names_test = names_train[random_image_position]

# names_train = np.array(names_train).reshape(1, len(names_train))

names_train = utils.to_categorical(names_train, num_classes=4)
print(names_train[0])

model = Sequential()
model.add(Dense(10, input_dim=8, activation="elu"))
model.add(Dense(4, activation="softmax"))

model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])

print(model.summary())

history = model.fit(data_train, names_train, 
                    batch_size=5, 
                    epochs=4000, 
                    verbose=1)

model.save('model.h5')

print(names_train_dict)
predictions = model.predict(data_test)
n = 0
print(predictions[n])

print(np.argmax(predictions[n]))
print(names_test)