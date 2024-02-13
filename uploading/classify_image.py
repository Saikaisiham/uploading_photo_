import tensorflow as tf 
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense , Flatten , Conv2D , MaxPool2D , Dropout
from tensorflow.keras import layers 
from keras.utils import to_categorical
import numpy as np 
import matplotlib.pyplot as plt 
plt.style.use('fivethirtyeight')
from skimage.transform import resize
from PIL import Image
from keras.datasets import cifar10
from django.core.management import call_command

def classify_image(image):
    call_command('consumer')
    (x_train, y_train),(x_test, y_test) = cifar10.load_data()

    index = 0

    classification = ['airplane', 'autombile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    y_train_one_hot = to_categorical(y_train)
    y_test_one_hot = to_categorical(y_test)

    img_array = np.array(Image.open(image))


    x_train = x_train / 255
    x_test = x_test / 255


    model = Sequential()


    model.add(Conv2D(32, (5,5) , activation='relu' , input_shape = (32,32,3)))

    model.add(MaxPool2D(pool_size = (2,2)))

    model.add(Conv2D(32, (5,5) , activation='relu' , input_shape = (32,32,3)))

    model.add(MaxPool2D(pool_size = (2,2)))

    model.add(Flatten())


    model.add(Dense(1000, activation='relu'))

    model.add(Dropout(0.5))

    model.add(Dense(500, activation='relu'))


    model.add(Dropout(0.5))


    model.add(Dense(250, activation='relu'))

    model.add(Dense(10, activation='softmax'))

    model.compile(loss = 'categorical_crossentropy',
                optimizer = 'adam',
                metrics = ['accuracy'])
    
    hist = model.fit(x_train, y_train_one_hot,
                    batch_size = 256,
                    epochs = 10,
                    validation_split= 0.2)
    

    resized_image = resize(img_array, (32, 32, 3))
    img = plt.imshow(resized_image)


    predictions = model.predict(np.array([resized_image]))


    list_index = [0,1,2,3,4,5,6,7,8,9]
    x = predictions

    for i in range(10):
        for j in range(10):
            if np.any(x[0][list_index[i]] > x[0][list_index[j]]):
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp


    print(list_index)


    for i  in range(1):
        print(classification[list_index[i]])

  
    top_5_predictions = [classification[i] for i in list_index[:1]]
    return top_5_predictions 