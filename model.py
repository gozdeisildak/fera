from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.backend import set_session
import numpy as np
import tensorflow as tf


class FacialExpressionModel(object):

    labels = ["Angry", "Disgust", "Fear",
              "Happy", "Sad", "Surprise", "Neutral"]
    MODEL_PATH = './model/seray.h5'

    def __init__(self):
        global model, graph
        self.sess = tf.Session()
        graph = tf.get_default_graph()
        # IMPORTANT: models have to be loaded AFTER SETTING THE SESSION for keras!
        # Otherwise, their weights will be unavailable in the threads after the session there has been set
        set_session(self.sess)
        # load weights into the new model
        self.loaded_model = load_model(self.MODEL_PATH)

    def predict_emotion(self, img):
        with graph.as_default():
            set_session(self.sess)
            y_preds = self.loaded_model.predict(img)
            self.y_pred = np.argmax(y_preds, axis=1)
            result = FacialExpressionModel.labels[self.y_pred[0]]
        return result
