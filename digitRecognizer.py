from tensorflow import keras
import tensorflow as tf
import pandas as pd
import cv2
import numpy as np
from sklearn.metrics import classification_report

def get_model(path):
    model_temp = keras.models.load_model(path)
    return model_temp

model = get_model("model")

def process_predict(image):
    nparr = np.fromstring(image, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(img,(28,28),interpolation = cv2.INTER_LINEAR)
    img = img.reshape(1,28,28,1)/255
    return predict(img)

def predict(images):
    images = tf.convert_to_tensor(images,dtype=tf.float32)
    pred = model(images).numpy().argmax(axis=1)
    return pred

if __name__=="__main__":
    test = pd.read_csv("data/mnist_test.csv")
    X_test = test.iloc[:,1:].values.reshape(-1, 28,28)/255
    Y_test = keras.utils.to_categorical(test.iloc[:,0].values)
    Y_pred = predict(X_test)
    print(classification_report(Y_test.argmax(axis=1), Y_pred))