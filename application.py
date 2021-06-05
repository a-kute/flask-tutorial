from flask import Flask, render_template, request
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D
from keras.layers import MaxPooling2D



application = Flask(__name__)


@application.route('/')
def hello_world():

    return render_template('before.html')


emotion_model = Sequential()

emotion_model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48, 48, 1)))
emotion_model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
emotion_model.add(MaxPooling2D(pool_size=(2, 2)))
emotion_model.add(Dropout(0.25))

emotion_model.add(Flatten())
emotion_model.add(Dense(1024, activation='relu'))
emotion_model.add(Dropout(0.5))
emotion_model.add(Dense(7, activation='softmax'))
emotion_model.load_weights('static/emotion_model.h5')
emotion_model.summary()
if __name__ == '__main__':
    application.run()


@application.route('/uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

        files = request.files.getlist("file")
        for file in files:
            file.filename="static/s1.jpg"
            file.save(file.filename)


        img = keras.preprocessing.image.load_img('static/s1.jpg', target_size=(48, 48), grayscale=True)

        img_array = keras.preprocessing.image.img_to_array(img)
        #plt.imshow(img_array)
        #plt.show()
        img_array = tf.expand_dims(img_array, 0)  # Create a batch
        #print(img_array.shape)
        #emotion_prediction = emotion_model.predict(img_array)
        emotion_prediction = emotion_model(img_array)

        maxindex = int(np.argmax(emotion_prediction))
        print(maxindex)
        emotion_dict = {0: "Angry", 1: "Disgusted", 2: "Fearful", 3: "Happy", 4: "Neutral", 5: "Sad", 6: "Surprised"}

        return render_template('after.html',data = emotion_dict[maxindex])

    else:
        return render_template('after.html')


